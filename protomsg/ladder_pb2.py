# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ladder.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import match_pb2 as match__pb2
import package_pb2 as package__pb2
import training_match_pb2 as training__match__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ladder.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\x0cladder.proto\x12\x11\x44ianjing.protocol\x1a\x0bmatch.proto\x1a\rpackage.proto\x1a\x14training_match.proto\"a\n\nLadderClub\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04\x66lag\x18\x03 \x02(\x05\x12\r\n\x05order\x18\x04 \x02(\x05\x12\r\n\x05power\x18\x05 \x02(\x05\x12\r\n\x05score\x18\x06 \x02(\x05\".\n\tLadderLog\x12\x13\n\x0btemplate_id\x18\x01 \x02(\x05\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\"\xb5\x01\n\x0cLadderNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12,\n\x05\x63lubs\x18\x02 \x03(\x0b\x32\x1d.Dianjing.protocol.LadderClub\x12\x16\n\x0eremained_times\x18\x03 \x02(\x05\x12\x10\n\x08my_order\x18\x04 \x02(\x05\x12\x10\n\x08my_score\x18\x05 \x02(\x05\x12*\n\x04logs\x18\x06 \x03(\x0b\x32\x1c.Dianjing.protocol.LadderLog\"\'\n\x14LadderRefreshRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"5\n\x15LadderRefreshResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"1\n\x12LadderMatchRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"`\n\x13LadderMatchResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12+\n\x05match\x18\x03 \x01(\x0b\x32\x1c.Dianjing.protocol.ClubMatch\"\x8e\x01\n\x18LadderMatchReportRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\r\n\x05video\x18\x02 \x02(\x0c\x12\x0b\n\x03key\x18\x03 \x02(\t\x12\x10\n\x08win_club\x18\x04 \x02(\t\x12\x33\n\x06result\x18\x05 \x03(\x0b\x32#.Dianjing.protocol.StaffMatchResult\"`\n\x19LadderMatchReportResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop\"L\n\x11LadderStoreNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x19\n\x11next_refresh_time\x18\x02 \x02(\x03\x12\x0b\n\x03ids\x18\x03 \x03(\x05\"4\n\x15LadderStoreBuyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\"6\n\x16LadderStoreBuyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\",\n\x19LadderStoreRefreshRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\":\n\x1aLadderStoreRefreshResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"+\n\x18LadderLeaderBoardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"g\n\x19LadderLeaderBoardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12,\n\x05\x63lubs\x18\x03 \x03(\x0b\x32\x1d.Dianjing.protocol.LadderClub')
  ,
  dependencies=[match__pb2.DESCRIPTOR,package__pb2.DESCRIPTOR,training__match__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_LADDERCLUB = _descriptor.Descriptor(
  name='LadderClub',
  full_name='Dianjing.protocol.LadderClub',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.LadderClub.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.LadderClub.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='flag', full_name='Dianjing.protocol.LadderClub.flag', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order', full_name='Dianjing.protocol.LadderClub.order', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='power', full_name='Dianjing.protocol.LadderClub.power', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='score', full_name='Dianjing.protocol.LadderClub.score', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=85,
  serialized_end=182,
)


_LADDERLOG = _descriptor.Descriptor(
  name='LadderLog',
  full_name='Dianjing.protocol.LadderLog',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='template_id', full_name='Dianjing.protocol.LadderLog.template_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='args', full_name='Dianjing.protocol.LadderLog.args', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=230,
)


_LADDERNOTIFY = _descriptor.Descriptor(
  name='LadderNotify',
  full_name='Dianjing.protocol.LadderNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clubs', full_name='Dianjing.protocol.LadderNotify.clubs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remained_times', full_name='Dianjing.protocol.LadderNotify.remained_times', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_order', full_name='Dianjing.protocol.LadderNotify.my_order', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='my_score', full_name='Dianjing.protocol.LadderNotify.my_score', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='logs', full_name='Dianjing.protocol.LadderNotify.logs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=233,
  serialized_end=414,
)


_LADDERREFRESHREQUEST = _descriptor.Descriptor(
  name='LadderRefreshRequest',
  full_name='Dianjing.protocol.LadderRefreshRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderRefreshRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=416,
  serialized_end=455,
)


_LADDERREFRESHRESPONSE = _descriptor.Descriptor(
  name='LadderRefreshResponse',
  full_name='Dianjing.protocol.LadderRefreshResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.LadderRefreshResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderRefreshResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=457,
  serialized_end=510,
)


_LADDERMATCHREQUEST = _descriptor.Descriptor(
  name='LadderMatchRequest',
  full_name='Dianjing.protocol.LadderMatchRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderMatchRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.LadderMatchRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=512,
  serialized_end=561,
)


_LADDERMATCHRESPONSE = _descriptor.Descriptor(
  name='LadderMatchResponse',
  full_name='Dianjing.protocol.LadderMatchResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.LadderMatchResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderMatchResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='Dianjing.protocol.LadderMatchResponse.match', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=563,
  serialized_end=659,
)


_LADDERMATCHREPORTREQUEST = _descriptor.Descriptor(
  name='LadderMatchReportRequest',
  full_name='Dianjing.protocol.LadderMatchReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderMatchReportRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='video', full_name='Dianjing.protocol.LadderMatchReportRequest.video', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='key', full_name='Dianjing.protocol.LadderMatchReportRequest.key', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='win_club', full_name='Dianjing.protocol.LadderMatchReportRequest.win_club', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='Dianjing.protocol.LadderMatchReportRequest.result', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=662,
  serialized_end=804,
)


_LADDERMATCHREPORTRESPONSE = _descriptor.Descriptor(
  name='LadderMatchReportResponse',
  full_name='Dianjing.protocol.LadderMatchReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.LadderMatchReportResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderMatchReportResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.LadderMatchReportResponse.drop', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=806,
  serialized_end=902,
)


_LADDERSTORENOTIFY = _descriptor.Descriptor(
  name='LadderStoreNotify',
  full_name='Dianjing.protocol.LadderStoreNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderStoreNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_refresh_time', full_name='Dianjing.protocol.LadderStoreNotify.next_refresh_time', index=1,
      number=2, type=3, cpp_type=2, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids', full_name='Dianjing.protocol.LadderStoreNotify.ids', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=904,
  serialized_end=980,
)


_LADDERSTOREBUYREQUEST = _descriptor.Descriptor(
  name='LadderStoreBuyRequest',
  full_name='Dianjing.protocol.LadderStoreBuyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderStoreBuyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.LadderStoreBuyRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=982,
  serialized_end=1034,
)


_LADDERSTOREBUYRESPONSE = _descriptor.Descriptor(
  name='LadderStoreBuyResponse',
  full_name='Dianjing.protocol.LadderStoreBuyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.LadderStoreBuyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderStoreBuyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1036,
  serialized_end=1090,
)


_LADDERSTOREREFRESHREQUEST = _descriptor.Descriptor(
  name='LadderStoreRefreshRequest',
  full_name='Dianjing.protocol.LadderStoreRefreshRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderStoreRefreshRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1092,
  serialized_end=1136,
)


_LADDERSTOREREFRESHRESPONSE = _descriptor.Descriptor(
  name='LadderStoreRefreshResponse',
  full_name='Dianjing.protocol.LadderStoreRefreshResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.LadderStoreRefreshResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderStoreRefreshResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1138,
  serialized_end=1196,
)


_LADDERLEADERBOARDREQUEST = _descriptor.Descriptor(
  name='LadderLeaderBoardRequest',
  full_name='Dianjing.protocol.LadderLeaderBoardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderLeaderBoardRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1198,
  serialized_end=1241,
)


_LADDERLEADERBOARDRESPONSE = _descriptor.Descriptor(
  name='LadderLeaderBoardResponse',
  full_name='Dianjing.protocol.LadderLeaderBoardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.LadderLeaderBoardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.LadderLeaderBoardResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='clubs', full_name='Dianjing.protocol.LadderLeaderBoardResponse.clubs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1243,
  serialized_end=1346,
)

_LADDERNOTIFY.fields_by_name['clubs'].message_type = _LADDERCLUB
_LADDERNOTIFY.fields_by_name['logs'].message_type = _LADDERLOG
_LADDERMATCHRESPONSE.fields_by_name['match'].message_type = match__pb2._CLUBMATCH
_LADDERMATCHREPORTREQUEST.fields_by_name['result'].message_type = training__match__pb2._STAFFMATCHRESULT
_LADDERMATCHREPORTRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
_LADDERLEADERBOARDRESPONSE.fields_by_name['clubs'].message_type = _LADDERCLUB
DESCRIPTOR.message_types_by_name['LadderClub'] = _LADDERCLUB
DESCRIPTOR.message_types_by_name['LadderLog'] = _LADDERLOG
DESCRIPTOR.message_types_by_name['LadderNotify'] = _LADDERNOTIFY
DESCRIPTOR.message_types_by_name['LadderRefreshRequest'] = _LADDERREFRESHREQUEST
DESCRIPTOR.message_types_by_name['LadderRefreshResponse'] = _LADDERREFRESHRESPONSE
DESCRIPTOR.message_types_by_name['LadderMatchRequest'] = _LADDERMATCHREQUEST
DESCRIPTOR.message_types_by_name['LadderMatchResponse'] = _LADDERMATCHRESPONSE
DESCRIPTOR.message_types_by_name['LadderMatchReportRequest'] = _LADDERMATCHREPORTREQUEST
DESCRIPTOR.message_types_by_name['LadderMatchReportResponse'] = _LADDERMATCHREPORTRESPONSE
DESCRIPTOR.message_types_by_name['LadderStoreNotify'] = _LADDERSTORENOTIFY
DESCRIPTOR.message_types_by_name['LadderStoreBuyRequest'] = _LADDERSTOREBUYREQUEST
DESCRIPTOR.message_types_by_name['LadderStoreBuyResponse'] = _LADDERSTOREBUYRESPONSE
DESCRIPTOR.message_types_by_name['LadderStoreRefreshRequest'] = _LADDERSTOREREFRESHREQUEST
DESCRIPTOR.message_types_by_name['LadderStoreRefreshResponse'] = _LADDERSTOREREFRESHRESPONSE
DESCRIPTOR.message_types_by_name['LadderLeaderBoardRequest'] = _LADDERLEADERBOARDREQUEST
DESCRIPTOR.message_types_by_name['LadderLeaderBoardResponse'] = _LADDERLEADERBOARDRESPONSE

LadderClub = _reflection.GeneratedProtocolMessageType('LadderClub', (_message.Message,), dict(
  DESCRIPTOR = _LADDERCLUB,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderClub)
  ))
_sym_db.RegisterMessage(LadderClub)

LadderLog = _reflection.GeneratedProtocolMessageType('LadderLog', (_message.Message,), dict(
  DESCRIPTOR = _LADDERLOG,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderLog)
  ))
_sym_db.RegisterMessage(LadderLog)

LadderNotify = _reflection.GeneratedProtocolMessageType('LadderNotify', (_message.Message,), dict(
  DESCRIPTOR = _LADDERNOTIFY,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderNotify)
  ))
_sym_db.RegisterMessage(LadderNotify)

LadderRefreshRequest = _reflection.GeneratedProtocolMessageType('LadderRefreshRequest', (_message.Message,), dict(
  DESCRIPTOR = _LADDERREFRESHREQUEST,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderRefreshRequest)
  ))
_sym_db.RegisterMessage(LadderRefreshRequest)

LadderRefreshResponse = _reflection.GeneratedProtocolMessageType('LadderRefreshResponse', (_message.Message,), dict(
  DESCRIPTOR = _LADDERREFRESHRESPONSE,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderRefreshResponse)
  ))
_sym_db.RegisterMessage(LadderRefreshResponse)

LadderMatchRequest = _reflection.GeneratedProtocolMessageType('LadderMatchRequest', (_message.Message,), dict(
  DESCRIPTOR = _LADDERMATCHREQUEST,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderMatchRequest)
  ))
_sym_db.RegisterMessage(LadderMatchRequest)

LadderMatchResponse = _reflection.GeneratedProtocolMessageType('LadderMatchResponse', (_message.Message,), dict(
  DESCRIPTOR = _LADDERMATCHRESPONSE,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderMatchResponse)
  ))
_sym_db.RegisterMessage(LadderMatchResponse)

LadderMatchReportRequest = _reflection.GeneratedProtocolMessageType('LadderMatchReportRequest', (_message.Message,), dict(
  DESCRIPTOR = _LADDERMATCHREPORTREQUEST,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderMatchReportRequest)
  ))
_sym_db.RegisterMessage(LadderMatchReportRequest)

LadderMatchReportResponse = _reflection.GeneratedProtocolMessageType('LadderMatchReportResponse', (_message.Message,), dict(
  DESCRIPTOR = _LADDERMATCHREPORTRESPONSE,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderMatchReportResponse)
  ))
_sym_db.RegisterMessage(LadderMatchReportResponse)

LadderStoreNotify = _reflection.GeneratedProtocolMessageType('LadderStoreNotify', (_message.Message,), dict(
  DESCRIPTOR = _LADDERSTORENOTIFY,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreNotify)
  ))
_sym_db.RegisterMessage(LadderStoreNotify)

LadderStoreBuyRequest = _reflection.GeneratedProtocolMessageType('LadderStoreBuyRequest', (_message.Message,), dict(
  DESCRIPTOR = _LADDERSTOREBUYREQUEST,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreBuyRequest)
  ))
_sym_db.RegisterMessage(LadderStoreBuyRequest)

LadderStoreBuyResponse = _reflection.GeneratedProtocolMessageType('LadderStoreBuyResponse', (_message.Message,), dict(
  DESCRIPTOR = _LADDERSTOREBUYRESPONSE,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreBuyResponse)
  ))
_sym_db.RegisterMessage(LadderStoreBuyResponse)

LadderStoreRefreshRequest = _reflection.GeneratedProtocolMessageType('LadderStoreRefreshRequest', (_message.Message,), dict(
  DESCRIPTOR = _LADDERSTOREREFRESHREQUEST,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreRefreshRequest)
  ))
_sym_db.RegisterMessage(LadderStoreRefreshRequest)

LadderStoreRefreshResponse = _reflection.GeneratedProtocolMessageType('LadderStoreRefreshResponse', (_message.Message,), dict(
  DESCRIPTOR = _LADDERSTOREREFRESHRESPONSE,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreRefreshResponse)
  ))
_sym_db.RegisterMessage(LadderStoreRefreshResponse)

LadderLeaderBoardRequest = _reflection.GeneratedProtocolMessageType('LadderLeaderBoardRequest', (_message.Message,), dict(
  DESCRIPTOR = _LADDERLEADERBOARDREQUEST,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderLeaderBoardRequest)
  ))
_sym_db.RegisterMessage(LadderLeaderBoardRequest)

LadderLeaderBoardResponse = _reflection.GeneratedProtocolMessageType('LadderLeaderBoardResponse', (_message.Message,), dict(
  DESCRIPTOR = _LADDERLEADERBOARDRESPONSE,
  __module__ = 'ladder_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderLeaderBoardResponse)
  ))
_sym_db.RegisterMessage(LadderLeaderBoardResponse)


# @@protoc_insertion_point(module_scope)
