
from core.unit import UnitManager

from utils.http import ProtobufResponse

from protomsg.unit_pb2 import UnitLevelUpResponse, UnitStepUpResponse


def level_up(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    uid = request._proto.id

    UnitManager(server_id, char_id).level_up(uid)

    response = UnitLevelUpResponse()
    response.ret = 0

    return ProtobufResponse(response)


def step_up(request):
    server_id = request._game_session.server_id
    char_id = request._game_session.char_id

    uid = request._proto.id

    UnitManager(server_id, char_id).step_up(uid)

    response = UnitStepUpResponse()
    response.ret = 0

    return ProtobufResponse(response)
