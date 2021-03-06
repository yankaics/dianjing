# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       club
Date Created:   2015-07-08 15:12
Description:

"""

from django.db import IntegrityError
from django.db.models import Q

from dianjing.exception import GameException
from apps.character.models import Character

from core.club import Club
from core.leaderboard import ClubLeaderBoard

from utils.http import ProtobufResponse
from config import ConfigErrorMessage

from core.signals import game_start_signal

from protomsg.club_pb2 import CreateClubResponse, ClubLeaderBoardResponse


def create(request):
    name = request._proto.name
    flag = request._proto.flag

    session = request._game_session
    account_id = session.account_id
    server_id = session.server_id

    if Character.objects.filter(Q(account_id=account_id) & Q(server_id=server_id)).exists():
        raise GameException(ConfigErrorMessage.get_error_id("CLUB_ALREADY_CREATED"))

    try:
        char = Character.objects.create(
            account_id=account_id,
            server_id=server_id,
            name=name,
        )
    except IntegrityError:
        raise GameException(ConfigErrorMessage.get_error_id("CLUB_NAME_TAKEN"))

    # NOTE: 返回的时候middleware就是根据 request._game_session.char_id
    # 来从 队列里取 消息的。 所以这里得设置
    request._game_session.char_id = char.id
    Club.create(server_id, char.id, name, flag)

    game_start_signal.send(
        sender=None,
        server_id=server_id,
        char_id=char.id,
    )

    club = Club(server_id, char.id, load_staffs=False)
    response = CreateClubResponse()
    response.ret = 0
    response.session = session.serialize()
    response.club.MergeFrom(club.make_protomsg())
    response.create_at = club.create_at
    return ProtobufResponse(response)


def get_leaderboard(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    info = ClubLeaderBoard(server_id, char_id).get_info()

    response = ClubLeaderBoardResponse()
    response.ret = 0
    response.next_update_at = info['next_update_at']
    response.my_level_rank = info['my_level_rank']
    response.my_power_rank = info['my_power_rank']

    for _id, level, power in info['level']:
        obj = Club(server_id, _id, load_staffs=False)

        response_level = response.clubs_by_level.add()
        response_level.MergeFrom(obj.make_protomsg())
        response_level.level = level
        response_level.power = power

    for _id, level, power in info['power']:
        obj = Club(server_id, _id, load_staffs=False)

        response_power = response.clubs_by_power.add()
        response_power.MergeFrom(obj.make_protomsg())
        response_power.level = level
        response_power.power = power

    return ProtobufResponse(response)
