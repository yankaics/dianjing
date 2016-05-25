# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       resource
Date Created:   2015-07-21 10:17
Description:

"""

from config import ConfigItemNew

from protomsg.package_pb2 import Drop as MsgDrop

MONEY = {
    30000: 'diamond',  # 钻石
    30001: 'gold',  # 金币
    30002: 'renown',  # 声望
    30003: 'crystal',  # 水晶
    30004: 'gas',  # 气矿
}

_MONEY_REVERSE = {v: k for k, v in MONEY.iteritems()}

TALENT_ITEM_ID = 30006
VIP_EXP_ITEM_ID = 30010
CLUB_EXP_ITEM_ID = 30011

# 领地建筑产出ID
TERRITORY_PRODUCT_BUILDING_TABLE = {
    30012: 101,
    30013: 102,
    30014: 103,
}


def item_id_to_money_text(_id):
    return MONEY[_id]


def money_text_to_item_id(text):
    return _MONEY_REVERSE[text]


def filter_money(items):
    # items: [(id, amount), (id, amount)...]
    """

    :rtype: dict[string, int]
    """
    money = {}
    for _id, _amount in items:
        name = MONEY.get(_id, None)
        if not name:
            continue

        if name in money:
            money[name] += _amount
        else:
            money[name] = _amount

    return money


def filter_bag_item(items):
    """

    :rtype: list
    """
    return [(_id, _amount) for _id, _amount in items if _id not in MONEY]


class ResourceClassification(object):
    __slots__ = ['money', 'bag', 'staff', 'talent_point', 'club_exp', 'territory_product',
                 'vip_exp',
                 ]

    def __init__(self):
        self.money = []
        self.bag = []
        self.staff = []
        self.talent_point = 0
        # club_exp 并不会 check_exist 和 remove
        self.club_exp = 0
        # 领地资源
        self.territory_product = []
        # vip exp
        self.vip_exp = 0

    @classmethod
    def classify(cls, items):
        # type: (list) -> ResourceClassification
        # items: [(id, amount)...]
        money = {}
        bag = {}
        staff = {}
        talent_point = 0
        club_exp = 0
        territory_product = {}
        vip_exp = 0

        for _id, _amount in items:
            if _id == TALENT_ITEM_ID:
                talent_point += _amount
                continue

            if _id == CLUB_EXP_ITEM_ID:
                club_exp += _amount
                continue

            if _id == VIP_EXP_ITEM_ID:
                vip_exp += _amount
                continue

            if _id in TERRITORY_PRODUCT_BUILDING_TABLE:
                if _id in territory_product:
                    territory_product[_id] += _amount
                else:
                    territory_product[_id] = _amount

                continue

            # NOTE: 上面先处理特殊ID，下面再根据类型处理

            tp = ConfigItemNew.get(_id).tp
            if tp == 3:
                if _id in money:
                    money[_id] += _amount
                else:
                    money[_id] = _amount
            elif tp == 6:
                if _id in staff:
                    staff[_id] += _amount
                else:
                    staff[_id] = _amount
            else:
                if _id in bag:
                    bag[_id] += _amount
                else:
                    bag[_id] = _amount

        obj = cls()
        obj.money = money.items()
        obj.bag = bag.items()
        obj.staff = staff.items()
        obj.talent_point = talent_point
        obj.club_exp = club_exp
        obj.vip_exp = vip_exp
        obj.territory_product = territory_product.items()

        return obj

    def money_as_text_dict(self):
        # type: () -> dict[str, int]
        res = {}
        for _id, _amount in self.money:
            res[item_id_to_money_text(_id)] = _amount

        return res

    def check_exist(self, server_id, char_id):
        from core.club import Club
        from core.bag import Bag
        from core.staff import StaffManger
        from core.talent import TalentManager
        from core.territory import Territory

        money_text = self.money_as_text_dict()
        Club(server_id, char_id).check_money(**money_text)
        Bag(server_id, char_id).check_items(self.bag)
        StaffManger(server_id, char_id).check_original_staff_is_initial_state(self.staff)
        TalentManager(server_id, char_id).check_talent_points(self.talent_point)
        Territory(server_id, char_id).check_product(self.territory_product)

    def remove(self, server_id, char_id):
        from core.club import Club
        from core.bag import Bag
        from core.staff import StaffManger
        from core.talent import TalentManager
        from core.territory import Territory

        money_text = self.money_as_text_dict()
        money_text = {k: -v for k, v in money_text.iteritems()}
        Club(server_id, char_id).update(**money_text)

        bag = Bag(server_id, char_id)
        for _id, _amount in self.bag:
            bag.remove_by_item_id(_id, _amount)

        sm = StaffManger(server_id, char_id)
        for _id, _amount in self.staff:
            for _ in range(_amount):
                sm.remove_initial_state_staff(_id)

        TalentManager(server_id, char_id).deduct_talent_points(self.talent_point)
        Territory(server_id, char_id).check_product(self.territory_product)

    def add(self, server_id, char_id):
        from core.club import Club
        from core.bag import Bag
        from core.staff import StaffManger
        from core.talent import TalentManager
        from core.territory import Territory
        from core.vip import VIP

        club_property = self.money_as_text_dict()
        if self.club_exp:
            club_property['exp'] = self.club_exp
        Club(server_id, char_id).update(**club_property)

        if self.vip_exp:
            VIP(server_id, char_id).add_exp(self.vip_exp)

        bag = Bag(server_id, char_id)
        for _id, _amount in self.bag:
            bag.add(_id, amount=_amount)

        sm = StaffManger(server_id, char_id)
        for _id, _amount in self.staff:
            for _ in range(_amount):
                sm.add(_id)

        TalentManager(server_id, char_id).add_talent_points(self.talent_point)
        if self.territory_product:
            Territory(server_id, char_id).add_product(self.territory_product)

    def make_protomsg(self):
        msg = MsgDrop()
        for _id, _amount in self.money:
            msg_item = msg.items.add()
            msg_item.id = _id
            msg_item.amount = _amount

        for _id, _amount in self.bag:
            msg_item = msg.items.add()
            msg_item.id = _id
            msg_item.amount = _amount

        for _id, _amount in self.staff:
            msg_item = msg.items.add()
            msg_item.id = _id
            msg_item.amount = _amount

        if self.talent_point:
            msg_item = msg.items.add()
            msg_item.id = TALENT_ITEM_ID
            msg_item.amount = self.talent_point

        if self.club_exp:
            msg_item = msg.items.add()
            msg_item.id = CLUB_EXP_ITEM_ID
            msg_item.amount = self.club_exp

        if self.vip_exp:
            msg_item = msg.items.add()
            msg_item.id = VIP_EXP_ITEM_ID
            msg_item.amount = self.vip_exp

        for _id, _amount in self.territory_product:
            msg_item = msg.items.add()
            msg_item.id = _id
            msg_item.amount = _amount

        return msg
