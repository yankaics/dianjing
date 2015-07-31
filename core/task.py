# -*- coding:utf-8 -*-

__author__ = 'hikaly'


from dianjing.exception import GameException


from core.db import get_mongo_db
from core.mongo import Document
from core.resource import Resource

from config.task import ConfigTask
from config import ConfigErrorMessage

from utils.message import MessagePipe

from protomsg.task_pb2 import TaskNotify
from protomsg.common_pb2 import ACT_INIT, ACT_UPDATE

TASK_STATUS_UNRECEIVED = 0
TASK_STATUS_DOING = 1
TASK_STATUS_FINISH = 2
TASK_STATUS_END = 3

class TaskRefresh(object):
    def __init__(self, server_id):
        self.server = server_id
        self.mongo = get_mongo_db(server_id)
        data = self.mongo.common.find_one({'_id': 'task'}, {'tasks': 1})
        if not data:
            doc = {
                '_id': 'task',
                'tasks': [],
            }
            self.mongo.common.insert_one(doc)


    def task_refresh(self):
        pass




class TaskManage(object):
    def __init__(self, server_id, char_id):
        self.server_id = server_id
        self.char_id = char_id
        self.mongo = get_mongo_db(self.server_id)

        doc = self.mongo.task.find_one({'_id': self.char_id}, {'_id': 1})
        if not doc:
            doc = Document.get("task")
            doc['_id'] = self.char_id
            self.mongo.task.insert_one(doc)


    def receive(self, task_id):
        task = ConfigTask.get(task_id)
        if not task:
            raise GameException(ConfigErrorMessage.get_error_id('TASK_NOT_EXIST'))

        char = self.mongo.character.find_one({'_id': self.char_id}, {'club.level': 1})
        if char['club']['level'] < task.level:
            raise GameException(ConfigErrorMessage.get_error_id('CLUB_LEVEL_NOT_ENOUGH'))

        task = self.mongo.task.find_one(
            {'_id': self.char_id},
            {'tasks.{0}'.format(task_id): 1}
        )

        if str(task_id) in task['tasks']:
            raise GameException(ConfigErrorMessage.get_error_id("TASK_ALREADY_DOING"))


        doc = Document.get("task.embedded")
        doc['status'] = TASK_STATUS_DOING

        self.mongo.task.update_one(
            {'_id': self.char_id},
            {'$set': {'tasks.{0}'.format(task_id): doc}}
        )
        self.send_notify(ACT_UPDATE, [task_id])


    def get_reward(self, task_id):

        # TODO check task finish
        task = self.mongo.task.find_one({'_id': self.char_id}, {'tasks.{0}'.format(task_id): 1})

        this_task = task['tasks'].get(str(task_id), None)
        if not this_task:
            raise GameException(ConfigErrorMessage.get_error_id("TASK_NOT_EXIST"))

        if this_task['status'] == TASK_STATUS_DOING:
            raise GameException(ConfigErrorMessage.get_error_id("TASK_NOT_DONE"))

        if this_task['status'] == TASK_STATUS_END:
            raise GameException(ConfigErrorMessage.get_error_id("TASK_ALREADY_GET_REWARD"))

        config = ConfigTask.get(task_id)

        Resource(self.server_id, self.char_id).add_from_package_id(config.package)
        self.mongo.task.update_one(
            {'_id': self.char_id},
            {'$set': {'tasks.{0}.status'.format(task_id): TASK_STATUS_END}}
        )

        self.send_notify(ACT_UPDATE, [task_id])


    def send_notify(self, act=ACT_INIT, task_ids=None):
        if not task_ids:
            projection = {'tasks': 1}
        else:
            projection = {'tasks.{0}'.format(i): 1 for i in task_ids}

        data = self.mongo.task.find_one({'_id': self.char_id}, projection)
        tasks = data.get('tasks', {})

        notify = TaskNotify()
        notify.act = act
        for k, v in tasks.iteritems():
            s = notify.tasks.add()
            s.id = int(k)
            s.num = v['num']
            s.status = v['status']

        MessagePipe(self.char_id).put(msg=notify)


    def update(self, **kwargs):
        task_id = kwargs.get('task_id', 0)
        num = kwargs.get('num', 0)

        task = self.mongo.task.find_one({'_id': self.char_id}, {'tasks.{0}'.format(task_id): 1})
        if str(task_id) not in task['tasks']:
            # 没有接此任务
            return

        num += task['tasks'][str(task_id)]['num']

        updater = {'tasks.{0}.num'.format(task_id): num}

        config = ConfigTask.get(task_id)
        if num >= config.num:
            updater['tasks.{0}.status'.format(task_id)] = TASK_STATUS_FINISH

        self.mongo.task.update_one(
            {'_id': self.char_id},
            {'$set': updater}
        )

        self.send_notify(ACT_UPDATE, [task_id])


    def clear(self):
        # TODO clear task data
        self.mongo.task.delete_one({'_id': self.char_id})

    def refresh(self):
        pass




