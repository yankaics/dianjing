# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       game
Date Created:   2015-04-30 15:23
Description:

"""

import arrow
from django.dispatch import receiver

from core.signals import game_start_signal
from core.character import Character
from core.club import Club
from core.staff import StaffRecruit, StaffManger
from core.skill import SkillManager
from core.training import TrainingExp, TrainingProperty, TrainingBroadcast, TrainingShop, TrainingSponsor
from core.bag import BagTrainingSkill, BagItem
from core.challenge import Challenge
from core.building import BuildingManager
from core.league import League
from core.friend import FriendManager
from core.mail import MailManager
from core.task import TaskManager, RandomEvent
from core.chat import Chat
from core.notification import Notification
from core.ladder import Ladder, LadderStore
from core.statistics import FinanceStatistics
from core.sponsor import SponsorManager
from core.activity import ActivityCategory
from core.activity.login_reward import ActivityLoginReward
from core.activity.signin import SignIn
from core.active_value import ActiveValue

from utils.message import MessagePipe
from protomsg.common_pb2 import UTCNotify


@receiver(game_start_signal, dispatch_uid='signals.game.game_start_handler')
def game_start_handler(server_id, char_id, **kwargs):
    MessagePipe(char_id).clean()

    msg = UTCNotify()
    msg.timestamp = arrow.utcnow().timestamp
    MessagePipe(char_id).put(msg=msg)

    c = Character(server_id, char_id)
    c.set_login()
    c.send_notify()

    club = Club(server_id, char_id)
    club.send_notify()
    club.send_staff_slots_notify()

    StaffRecruit(server_id, char_id).send_notify()
    StaffManger(server_id, char_id).send_notify()
    SkillManager(server_id, char_id).send_notify()

    TrainingExp(server_id, char_id).send_notify()
    TrainingProperty(server_id, char_id).send_notify()
    TrainingBroadcast(server_id, char_id).send_notify()
    TrainingShop(server_id, char_id).send_notify()
    TrainingSponsor(server_id, char_id).send_notify()

    BagTrainingSkill(server_id, char_id).send_notify()
    BagItem(server_id, char_id).send_notify()

    Challenge(server_id, char_id).send_notify()
    BuildingManager(server_id, char_id).send_notify()
    League(server_id, char_id).send_notify()
    FriendManager(server_id, char_id).send_notify()
    MailManager(server_id, char_id).send_notify()
    TaskManager(server_id, char_id).send_notify()
    RandomEvent(server_id, char_id).send_notify()

    Chat(server_id, char_id).send_notify()

    Notification(server_id, char_id).send_notify()

    Ladder(server_id, char_id).send_notify()
    LadderStore(server_id, char_id).send_notify()

    FinanceStatistics(server_id, char_id).send_notify()
    SponsorManager(server_id, char_id).send_notify()

    ActivityCategory(server_id, char_id).send_notify()
    ActivityLoginReward(server_id, char_id).send_notify()
    SignIn(server_id, char_id).send_notify()

    av = ActiveValue(server_id, char_id)
    av.send_function_notify()
    av.send_value_notify()
