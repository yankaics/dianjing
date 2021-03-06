# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       functional
Date Created:   2015-08-11 19:00
Description:

"""
import os
import uuid
import hashlib

import arrow

from django.conf import settings


def make_string_id():
    return str(uuid.uuid4())


def make_short_random_string():
    data = os.urandom(6)
    return hashlib.md5(data).hexdigest()[:6]


def make_signed_random_string():
    text = os.urandom(4).encode('hex')

    number = int(text, 16)
    sign = str(number)[:2]
    return '{0}{1}'.format(text, sign)


def check_signed_string(data):
    if len(data) != 10:
        return False

    try:
        text = data[:-2]
        sign = data[8:]
        number = int(text, 16)
        return str(number)[:2] == sign
    except:
        return False


def get_start_time_of_today():
    # 今天的起始时间
    """

    :rtype: arrow.Arrow
    """
    now = arrow.utcnow().to(settings.TIME_ZONE)
    start_day = arrow.Arrow(
        year=now.year,
        month=now.month,
        day=now.day,
        hour=0,
        minute=0,
        second=0,
        microsecond=0,
        tzinfo=now.tzinfo
    )

    return start_day


def make_time_of_today(hour, minute):
    t = get_start_time_of_today()
    t = t.replace(hour=hour)
    t = t.replace(minute=minute)
    return t


def days_passed(timestamp):
    create_at = arrow.get(timestamp).to(settings.TIME_ZONE)
    now = arrow.utcnow().to(settings.TIME_ZONE)
    days = (now.date() - create_at.date()).days
    return days + 1
