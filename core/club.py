# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       club
Date Created:   2015-07-03 15:09
Description:

"""

import itertools

from core.mongo import MongoCharacter
from core.abstract import AbstractClub
from core.staff import Staff
from core.signals import match_staffs_set_done_signal, club_level_up_signal
from core.staff import StaffManger
from core.qianban import QianBanContainer

from dianjing.exception import GameException

from utils.message import MessagePipe

from config import (
    ConfigClubLevel,
    ConfigPolicy,
    ConfigErrorMessage
)

from protomsg.club_pb2 import ClubNotify


def club_level_up_need_renown(level):
    return ConfigClubLevel.get(level).renown


class Club(AbstractClub):
    def __init__(self, server_id, char_id):
        super(Club, self).__init__()

        self.server_id = server_id
        self.char_id = char_id
        self.load_data()

    def load_data(self):
        doc = MongoCharacter.db(self.server_id).find_one({'_id': self.char_id}, {'club': 1, 'name': 1})

        club = doc['club']
        staffs = StaffManger(self.server_id, self.char_id).get_all_staffs()

        self.id = self.char_id  # 玩家ID
        self.name = club['name']  # 俱乐部名
        self.manager_name = doc['name']  # 角色名
        self.flag = club['flag']  # 俱乐部旗帜
        self.level = club['level']  # 俱乐部等级
        self.renown = club['renown']  # 俱乐部声望
        self.vip = club['vip']  # vip等级
        self.gold = club['gold']  # 游戏币
        # FIXME
        self.diamond = int(club['diamond'])  # 钻石
        self.policy = club.get('policy', 1)  # 战术

        self.match_staffs = club.get('match_staffs', [])  # 出战员工
        self.tibu_staffs = club.get('tibu_staffs', [])  # 替补员工

        for k, v in staffs.iteritems():
            self.staffs[int(k)] = Staff(self.server_id, self.char_id, int(k), v)

        qc = QianBanContainer(self.all_match_staffs())
        for i in itertools.chain(self.match_staffs, self.tibu_staffs):
            if i == 0:
                continue

            qc.affect(self.staffs[i])

    def is_staff_in_match(self, staff_id):
        return staff_id in self.match_staffs or staff_id in self.tibu_staffs

    def all_match_staffs(self):
        # 所有上阵员工
        staffs = []
        staffs.extend([i for i in self.match_staffs if i != 0])
        staffs.extend([i for i in self.tibu_staffs if i != 0])

        return staffs

    def set_policy(self, policy):
        if not ConfigPolicy.get(policy):
            raise GameException(ConfigErrorMessage.get_error_id('POLICY_NOT_EXIST'))

        MongoCharacter.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$set': {'club.policy': policy}}
        )

        self.policy = policy
        self.send_notify()

    def set_match_staffs(self, staff_ids):
        if len(staff_ids) != 10:
            raise GameException(ConfigErrorMessage.get_error_id("BAD_MESSAGE"))

        if not StaffManger(self.server_id, self.char_id).has_staff([i for i in staff_ids if i != 0]):
            raise GameException(ConfigErrorMessage.get_error_id('STAFF_NOT_EXIST'))

        match_staffs = staff_ids[:5]
        tibu_staffs = staff_ids[5:]

        MongoCharacter.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$set': {
                'club.match_staffs': match_staffs,
                'club.tibu_staffs': tibu_staffs
            }}
        )

        if all([i != 0 for i in match_staffs]):
            # set done
            match_staffs_set_done_signal.send(
                sender=None,
                server_id=self.server_id,
                char_id=self.char_id,
                match_staffs=match_staffs
            )

        self.load_data()
        self.send_notify()

    def update(self, **kwargs):
        renown = kwargs.get('renown', 0)
        gold = kwargs.get('gold', 0)
        diamond = kwargs.get('diamond', 0)

        self.gold += gold
        self.diamond += diamond
        self.renown += renown

        # update
        level_changed = False
        while True:
            need_renown = club_level_up_need_renown(self.level)
            next_level_id = ConfigClubLevel.get(self.level).next_level_id
            if not next_level_id:
                if self.renown >= need_renown:
                    self.renown = need_renown - 1
                break

            if self.renown < need_renown:
                break

            self.renown -= need_renown
            self.level += 1
            level_changed = True

        MongoCharacter.db(self.server_id).update_one(
            {'_id': self.char_id},
            {'$set': {
                'club.level': self.level,
                'club.renown': self.renown,
                'club.gold': self.gold,
                'club.diamond': self.diamond,
            }}
        )

        if level_changed:
            club_level_up_signal.send(
                sender=None,
                server_id=self.server_id,
                char_id=self.char_id,
                new_level=self.level
            )

        self.send_notify()

    def send_notify(self):
        msg = self.make_protomsg()
        notify = ClubNotify()
        notify.club.MergeFrom(msg)
        MessagePipe(self.char_id).put(notify)
