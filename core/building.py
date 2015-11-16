# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       building
Date Created:   2015-07-21 00:33
Description:

"""
import arrow

from dianjing.exception import GameException

from core.mongo import MongoBuilding
from core.club import Club
from core.resource import Resource
from core.signals import building_level_up_done_signal, building_level_up_start_signal
from config import ConfigBuilding, ConfigErrorMessage

from utils.api import Timerd
from utils.message import MessagePipe

from protomsg.building_pb2 import BuildingNotify
from protomsg.common_pb2 import ACT_UPDATE, ACT_INIT


class BuildingManager(object):
    def __init__(self, server_id, char_id):
        self.server_id = server_id
        self.char_id = char_id

        doc = MongoBuilding.db(server_id).find_one({'_id': self.char_id})
        if not doc:
            doc = MongoBuilding.document()
            doc['_id'] = self.char_id
            building_doc = MongoBuilding.document_building()
            doc['buildings'] = {str(i): building_doc for i in ConfigBuilding.INSTANCES.keys()}
            MongoBuilding.db(server_id).insert_one(doc)
        else:
            updater = {}
            for i in ConfigBuilding.INSTANCES.keys():
                if str(i) not in doc['buildings']:
                    updater['buildings.{0}.level'.format(i)] = 1
                    updater['buildings.{0}.end_at'.format(i)] = 0

            if updater:
                MongoBuilding.db(server_id).update_one(
                    {'_id': self.char_id},
                    {'$set': updater}
                )

    def current_level(self, building_id):
        doc = MongoBuilding.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'buildings.{0}.level'.format(building_id): 1}
        )

        return doc['buildings'].get(str(building_id), {}).get('level', 1)

    def level_up(self, building_id):
        config = ConfigBuilding.get(building_id)
        if not config:
            raise GameException(ConfigErrorMessage.get_error_id("BUILDING_NOT_EXIST"))

        if not config.max_levels:
            raise GameException(ConfigErrorMessage.get_error_id("BUILDING_CAN_NOT_LEVEL_UP"))

        doc = MongoBuilding.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'buildings.{0}'.format(building_id): 1}
        )

        current_level = doc['buildings'][str(building_id)]['level']
        if current_level >= config.max_levels:
            raise GameException(ConfigErrorMessage.get_error_id("BUILDING_ALREADY_MAX_LEVEL"))

        end_at = doc['buildings'][str(building_id)]['end_at']
        if end_at:
            raise GameException(ConfigErrorMessage.get_error_id("BUILDING_IN_UPGRADING"))

        if config.level_up_condition_type == 1:
            if Club(self.server_id, self.char_id).level < config.get_level(current_level).up_condition_value:
                raise GameException(ConfigErrorMessage.get_error_id("CLUB_LEVEL_NOT_ENOUGH"))
        else:
            if BuildingClubCenter(self.server_id, self.char_id).current_level() < config.get_level(current_level).up_condition_value:
                raise GameException(ConfigErrorMessage.get_error_id("BUILDING_CLUB_CENTER_LEVEL_NOT_ENOUGH"))

        check = {
            "gold": -config.get_level(current_level).up_need_gold,
            "message": u"Building {0} level up to {1}".format(building_id, current_level + 1)
        }

        with Resource(self.server_id, self.char_id).check(**check):
            end_at = arrow.utcnow().timestamp + config.get_level(current_level).up_need_minutes * 60
            # register to timerd
            data = {
                'sid': self.server_id,
                'cid': self.char_id,
                'building_id': building_id
            }

            key = Timerd.register(end_at, '/api/timerd/building/', data)

            MongoBuilding.db(self.server_id).update_one(
                {'_id': self.char_id},
                {'$set': {
                    'buildings.{0}.end_at'.format(building_id): end_at,
                    'buildings.{0}.key'.format(building_id): key
                }}
            )

        self.send_notify(building_ids=[building_id])

        building_level_up_start_signal.send(
            sender=None,
            server_id=self.server_id,
            char_id=self.char_id,
            building_id=building_id
        )



    def levelup_callback(self, building_id):
        # 定时任务回调
        doc = MongoBuilding.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'buildings.{0}'.format(building_id): 1}
        )

        end_at = doc['buildings'][str(building_id)]['end_at']
        if end_at > arrow.utcnow().timestamp:
            # not finish
            return end_at

        new_level = doc['buildings'][str(building_id)]['level'] + 1
        data = {
            'level': new_level,
            'end_at': 0,
            'key': ''
        }

        MongoBuilding.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$set': {
                'buildings.{0}'.format(building_id): data
            }}
        )

        self.send_notify(building_ids=[building_id])

        building_level_up_done_signal.send(
            sender=None,
            server_id=self.server_id,
            char_id=self.char_id,
            building_id=building_id
        )

        return 0

    def send_notify(self, building_ids=None):
        if building_ids:
            projection = {'buildings.{0}'.format(i): 1 for i in building_ids}
            act = ACT_UPDATE
        else:
            projection = {'buildings': 1}
            act = ACT_INIT

        doc = MongoBuilding.db(self.server_id).find_one({'_id': self.char_id}, projection)
        notify = BuildingNotify()
        notify.act = act

        for b in ConfigBuilding.all_values():
            if building_ids and b.id not in building_ids:
                continue

            notify_building = notify.buildings.add()
            notify_building.id = b.id
            notify_building.level = doc['buildings'][str(b.id)]['level']
            notify_building.end_at = doc['buildings'][str(b.id)]['end_at']

        MessagePipe(self.char_id).put(msg=notify)


class BaseBuilding(object):
    BUILDING_ID = 0

    def __init__(self, server_id, char_id):
        self.bm = BuildingManager(server_id, char_id)

    def current_level(self):
        return self.bm.current_level(self.BUILDING_ID)

    def level_up(self):
        return self.bm.level_up(self.BUILDING_ID)


# 俱乐部总部
class BuildingClubCenter(BaseBuilding):
    BUILDING_ID = 1

# 培训中心
class BuildingTrainingCenter(BaseBuilding):
    BUILDING_ID = 2


# 人才市场
class BuildingStaffCenter(BaseBuilding):
    BUILDING_ID = 3


# 精彩活动
class BuildingTaskCenter(BaseBuilding):
    BUILDING_ID = 4


# 电竞赛场
class BuildingLeagueCenter(BaseBuilding):
    BUILDING_ID = 5


# 赞助商事务所
class BuildingSponsorCenter(BaseBuilding):
    BUILDING_ID = 6


# 商务部
class BuildingBusinessCenter(BaseBuilding):
    BUILDING_ID = 7
