# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       operation_log
Date Created:   2016-07-07 15-27
Description:

"""
import arrow

from utils.functional import make_string_id

from core.mongo import MongoOperationLog


KEEP_DAYS = 3

class OperationLog(object):
    __slots__ = ['server_id', 'char_id',  'start_at']
    def __init__(self, server_id, char_id):
        self.server_id = server_id
        self.char_id = char_id

        self.start_at = arrow.utcnow()

    @classmethod
    def clean(cls, server_id):
        limit = arrow.utcnow().replace(days=-KEEP_DAYS)
        MongoOperationLog.db(server_id).delete_many({'timestamp': {'$lte': limit.timestamp}})

    @classmethod
    def get_recent_action_char_ids(cls, server_id, recent_minutes=15, keep_order=False):
        limit = arrow.utcnow().replace(minutes=-recent_minutes)

        if keep_order:
            char_ids = []
            docs = MongoOperationLog.db(server_id).find(
                        {'timestamp': {'$gte': limit.timestamp}},
                        {'char_id': 1}
                    ).sort('timestamp', -1)

            for doc in docs:
                if doc['char_id'] not in char_ids:
                    char_ids.append(doc['char_id'])
        else:
            char_ids = MongoOperationLog.db(server_id).distinct(
                'char_id',
                {'timestamp': {'$gte': limit.timestamp}}
            )

        return char_ids

    def record(self, action, ret):
        start_at = self.start_at.timestamp + self.start_at.microsecond / 1000

        now = arrow.utcnow()
        end_at = now.timestamp + now.microsecond / 1000

        cost = end_at - start_at

        doc = MongoOperationLog.document()
        doc['_id'] = make_string_id()
        doc['char_id'] = self.char_id
        doc['action'] = action
        doc['ret'] = ret
        doc['timestamp'] = self.start_at.timestamp
        doc['cost_millisecond'] = cost

        MongoOperationLog.db(self.server_id).insert_one(doc)