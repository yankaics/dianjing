# -*- coding: utf-8 -*-
"""
Author:         Wang Chao <yueyoum@gmail.com>
Filename:       party
Date Created:   2016-09-19 16:01
Description:

"""
import json

from django.http import JsonResponse

from core.party import Party


def create(request):
    data = json.loads(request.body)
    print "API party create got {0}".format(data)

    server_id = data['server_id']
    char_id = data['char_id']
    party_level = data['party_level']

    p = Party(server_id, char_id)
    response = p.create(party_level)

    return JsonResponse(response)


def start(request):
    data = json.loads(request.body)
    print "API party start got {0}".format(data)


    server_id = data['server_id']
    char_id = data['char_id']
    member_ids = data['member_ids']

    p = Party(server_id, char_id)
    response = p.start(member_ids)

    return JsonResponse(response)


def buy(request):
    data = json.loads(request.body)
    print "API party buy got {0}".format(data)


    server_id = data['server_id']
    char_id = data['char_id']
    party_level = data['party_level']
    buy_id = data['buy_id']
    member_ids = data['member_ids']

    p = Party(server_id, char_id)
    response = p.buy_item(party_level, buy_id, member_ids)

    return JsonResponse(response)

def end(request):
    data = json.loads(request.body)
    print "API party end got {0}".format(data)

    server_id = data['server_id']
    char_id = data['char_id']
    party_level = data['party_level']
    member_ids = data['member_ids']

    p = Party(server_id, char_id)
    response = p.end(party_level, member_ids)

    return JsonResponse(response)
