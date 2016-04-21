# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       unit
Date Created:   2016-04-08 14:22
Description:

"""

from dianjing.exception import GameException

from core.abstract import AbstractUnit
from core.mongo import MongoUnit
from core.club import Club
from core.resource import ResourceClassification

from utils.message import MessagePipe

from config import ConfigErrorMessage, ConfigUnitUnLock, ConfigUnitAddition

from protomsg.unit_pb2 import UnitNotify
from protomsg.common_pb2 import ACT_INIT, ACT_UPDATE


class UnitAddition(object):
    __slots__ = [
        'hp_percent', 'attack_percent', 'defense_percent',
        'hit_rate', 'dodge_rate', 'crit_rate', 'toughness_rate', 'crit_multiple',
        'hurt_addition_to_terran', 'hurt_addition_to_protoss', 'hurt_addition_to_zerg',
        'hurt_addition_by_terran', 'hurt_addition_by_protoss', 'hurt_addition_by_zerg',
    ]

    def __init__(self):
        self.hp_percent = 0
        self.attack_percent = 0
        self.defense_percent = 0
        self.hit_rate = 0
        self.dodge_rate = 0
        self.crit_rate = 0
        self.toughness_rate = 0
        self.crit_multiple = 0
        self.hurt_addition_to_terran = 0
        self.hurt_addition_to_protoss = 0
        self.hurt_addition_to_zerg = 0
        self.hurt_addition_by_terran = 0
        self.hurt_addition_by_protoss = 0
        self.hurt_addition_by_zerg = 0

    def add_property(self, attr, value):
        v = getattr(self, attr)
        v += value
        setattr(self, attr, v)


# 用于NPC的
class NPCUnit(AbstractUnit):
    __slots__ = []

    def __init__(self, _id, step, level):
        super(NPCUnit, self).__init__()
        self.id = _id
        self.step = step
        self.level = level
        self.after_init()
        self.calculate()


# 用于玩家的
class Unit(AbstractUnit):
    __slots__ = []

    def __init__(self, server_id, char_id, _id, data):
        super(Unit, self).__init__()
        self.server_id = server_id
        self.char_id = char_id
        self.id = _id
        self.step = data['step']
        self.level = data['level']
        self.after_init()

    def level_up(self):
        if self.level >= self.config.max_level:
            raise GameException(ConfigErrorMessage.get_error_id("UNIT_REACH_MAX_LEVEL"))

        using_items = self.config.levels[self.level].update_item_need
        resource_classified = ResourceClassification.classify(using_items)
        resource_classified.check_exist(self.server_id, self.char_id)
        resource_classified.remove(self.server_id, self.char_id)

        self.level += 1

        MongoUnit.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$inc': {
                'units.{0}.level'.format(self.id): 1
            }}
        )

        # 升级可能会导致其他的unit属性改变（加成）
        # 所以在UnitManage 里统一load一次unit
        # 是否要优化？

    def step_up(self):
        if self.step >= self.config.max_step:
            raise GameException(ConfigErrorMessage.get_error_id("UNIT_REACH_MAX_STEP"))

        if self.level < self.config.steps[self.step].level_limit:
            raise GameException(ConfigErrorMessage.get_error_id("UNIT_LEVEL_NOT_ENOUGH"))

        using_items = self.config.steps[self.step].update_item_need
        resource_classified = ResourceClassification.classify(using_items)
        resource_classified.check_exist(self.server_id, self.char_id)
        resource_classified.remove(self.server_id, self.char_id)

        self.step += 1

        MongoUnit.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$inc': {
                'units.{0}.step'.format(self.id): 1
            }}
        )

    def send_notify(self):
        notify = UnitNotify()
        notify.act = ACT_UPDATE
        notify_unit = notify.units.add()
        notify_unit.MergeFrom(self.make_protomsg())

        MessagePipe(self.char_id).put(msg=notify)


def get_init_units():
    units = []
    for k, v in ConfigUnitUnLock.INSTANCES.items():
        if v.need_club_level == 0 and not v.need_unit_level:
            units.append(k)

    return units


class UnitManager(object):
    __slots__ = ['server_id', 'char_id']

    def __init__(self, server_id, char_id):
        self.server_id = server_id
        self.char_id = char_id

        if not MongoUnit.exist(self.server_id, self.char_id):
            doc = MongoUnit.document()
            doc['_id'] = self.char_id

            init_ids = get_init_units()

            for _id in init_ids:
                unit_doc = MongoUnit.document_unit()
                doc['units'][str(_id)] = unit_doc

            MongoUnit.db(self.server_id).insert_one(doc)

    def unlock_club_level_up_listener(self, club_level):
        pass

    def unlock_unit_level_up_listener(self, unit_id, unit_level):
        pass

    def _unlock(self, _id):
        doc = MongoUnit.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'units': 1}
        )

        if _id in doc['units']:
            # already unlocked
            return

        unlock_conf = ConfigUnitUnLock.get(_id)
        club_lv = Club(self.server_id, self.char_id).level
        if club_lv < unlock_conf.need_club_level:
            raise GameException(ConfigErrorMessage.get_error_id("UNIT_UNLOCK_CLUB_LEVEL_NOT_ENOUGH"))

        for _id, level in unlock_conf.need_unit_level:
            if doc['units'][str(_id)] < level:
                raise GameException(ConfigErrorMessage.get_error_id("UNIT_UNLOCK_UNIT_LEVEL_NOT_ENOUGH"))

        unit_doc = MongoUnit.document_unit()
        MongoUnit.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$set': {'units.{0}'.format(_id): unit_doc}},
        )

        self.send_notify(ids=[_id])

    def is_unit_unlocked(self, _id):
        doc = MongoUnit.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'units.{0}'.format(_id): 1}
        )

        return str(_id) in doc['units']

    def check_unit_unlocked(self, _id):
        if not self.is_unit_unlocked(_id):
            raise GameException(ConfigErrorMessage.get_error_id("UNIT_IS_UNLOCKED"))

    def get_units_data(self):
        doc = MongoUnit.db(self.server_id).find_one(
            {'_id': self.char_id},
            {'units': 1}
        )

        return {int(k): v for k, v in doc['units'].iteritems()}

    def load_units(self):
        units = []
        """:type: list[Unit]"""

        doc = MongoUnit.db(self.server_id).find_one({'_id': self.char_id})
        for _id, _data in doc['units'].iteritems():
            u = Unit(self.server_id, self.char_id, int(_id), _data)
            units.append(u)

        race = {
            1: {'level': 0, 'step': 0},
            2: {'level': 0, 'step': 0},
            3: {'level': 0, 'step': 0},
        }

        for u in units:
            race[u.config.race]['level'] += u.level
            race[u.config.race]['step'] += u.step

        additions = {
            1: UnitAddition(),
            2: UnitAddition(),
            3: UnitAddition(),
        }

        for k, v in additions.iteritems():
            _level_addition = ConfigUnitAddition.get_level_addition(k, race[k]['level'])
            _step_addition = ConfigUnitAddition.get_step_addition(k, race[k]['step'])
            if _level_addition:
                for attr in UnitAddition.__slots__:
                    v.add_property(attr, getattr(_level_addition, attr))

            if _step_addition:
                for attr in UnitAddition.__slots__:
                    v.add_property(attr, getattr(_level_addition, attr))

        for u in units:
            _add = additions[u.config.race]
            for attr in UnitAddition.__slots__:
                setattr(u, attr, getattr(_add, attr))

            u.calculate()
            u.make_cache()

    def get_unit_object(self, _id):
        """

        :param _id:
        :rtype: Unit | None
        """
        unit = Unit.get(self.char_id, _id)
        if unit:
            return unit

        self.load_units()
        return Unit.get(self.char_id, _id)

    def level_up(self, uid):
        unit = self.get_unit_object(uid)
        if not unit:
            raise GameException(ConfigErrorMessage.get_error_id("BAD_MESSAGE"))

        unit.level_up()
        self.after_change(uid)

    def step_up(self, uid):
        unit = self.get_unit_object(uid)
        if not unit:
            raise GameException(ConfigErrorMessage.get_error_id("BAD_MESSAGE"))

        unit.step_up()
        self.after_change(uid)

    def after_change(self, uid):
        self.load_units()
        unit = self.get_unit_object(uid)
        all_units = self.get_units_data()

        all_units_object = [self.get_unit_object(k) for k, _ in all_units.iteritems()]

        changed_unit_ids = []
        for u in all_units_object:
            if u.config.race == unit.config.race:
                u.calculate()
                u.make_cache()
                changed_unit_ids.append(u.id)

        self.send_notify(ids=changed_unit_ids)


    def send_notify(self, ids=None):
        if not ids:
            act = ACT_INIT
            ids = self.get_units_data().keys()
        else:
            act = ACT_UPDATE


        notify = UnitNotify()
        notify.act = act

        for _id in ids:
            notify_unit = notify.units.add()
            unit = self.get_unit_object(_id)
            notify_unit.MergeFrom(unit.make_protomsg())

        MessagePipe(self.char_id).put(msg=notify)