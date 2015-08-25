# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ladder.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import match_pb2
import package_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ladder.proto',
  package='Dianjing.protocol',
  serialized_pb='\n\x0cladder.proto\x12\x11\x44ianjing.protocol\x1a\x0bmatch.proto\x1a\rpackage.proto\"C\n\nLadderClub\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0c\n\x04name\x18\x02 \x02(\t\x12\x0c\n\x04\x66lag\x18\x03 \x02(\x05\x12\r\n\x05order\x18\x04 \x02(\x05\".\n\tLadderLog\x12\x13\n\x0btemplate_id\x18\x01 \x02(\x05\x12\x0c\n\x04\x61rgs\x18\x02 \x03(\t\"\xb5\x01\n\x0cLadderNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12,\n\x05\x63lubs\x18\x02 \x03(\x0b\x32\x1d.Dianjing.protocol.LadderClub\x12\x16\n\x0eremained_times\x18\x03 \x02(\x05\x12\x10\n\x08my_order\x18\x04 \x02(\x05\x12\x10\n\x08my_score\x18\x05 \x02(\x05\x12*\n\x04logs\x18\x06 \x03(\x0b\x32\x1c.Dianjing.protocol.LadderLog\"\'\n\x14LadderRefreshRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\"5\n\x15LadderRefreshResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"1\n\x12LadderMatchRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"`\n\x13LadderMatchResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12+\n\x05match\x18\x03 \x01(\x0b\x32\x1c.Dianjing.protocol.ClubMatch\"Q\n\x0fLadderStoreItem\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0b\n\x03oid\x18\x02 \x02(\x05\x12%\n\x04item\x18\x03 \x02(\x0b\x32\x17.Dianjing.protocol.Item\"r\n\x11LadderStoreNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x19\n\x11next_refresh_time\x18\x02 \x02(\x03\x12\x31\n\x05items\x18\x03 \x03(\x0b\x32\".Dianjing.protocol.LadderStoreItem\"4\n\x15LadderStoreBuyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\t\"6\n\x16LadderStoreBuyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c')




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
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='Dianjing.protocol.LadderClub.name', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=63,
  serialized_end=130,
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
  extension_ranges=[],
  serialized_start=132,
  serialized_end=178,
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
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=181,
  serialized_end=362,
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
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=364,
  serialized_end=403,
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
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=405,
  serialized_end=458,
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
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.LadderMatchRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=460,
  serialized_end=509,
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
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=511,
  serialized_end=607,
)


_LADDERSTOREITEM = _descriptor.Descriptor(
  name='LadderStoreItem',
  full_name='Dianjing.protocol.LadderStoreItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.LadderStoreItem.id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='oid', full_name='Dianjing.protocol.LadderStoreItem.oid', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='Dianjing.protocol.LadderStoreItem.item', index=2,
      number=3, type=11, cpp_type=10, label=2,
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
  extension_ranges=[],
  serialized_start=609,
  serialized_end=690,
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
      has_default_value=False, default_value="",
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
      name='items', full_name='Dianjing.protocol.LadderStoreNotify.items', index=2,
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
  extension_ranges=[],
  serialized_start=692,
  serialized_end=806,
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
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.LadderStoreBuyRequest.id', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
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
  extension_ranges=[],
  serialized_start=808,
  serialized_end=860,
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
      has_default_value=False, default_value="",
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
  extension_ranges=[],
  serialized_start=862,
  serialized_end=916,
)

_LADDERNOTIFY.fields_by_name['clubs'].message_type = _LADDERCLUB
_LADDERNOTIFY.fields_by_name['logs'].message_type = _LADDERLOG
_LADDERMATCHRESPONSE.fields_by_name['match'].message_type = match_pb2._CLUBMATCH
_LADDERSTOREITEM.fields_by_name['item'].message_type = package_pb2._ITEM
_LADDERSTORENOTIFY.fields_by_name['items'].message_type = _LADDERSTOREITEM
DESCRIPTOR.message_types_by_name['LadderClub'] = _LADDERCLUB
DESCRIPTOR.message_types_by_name['LadderLog'] = _LADDERLOG
DESCRIPTOR.message_types_by_name['LadderNotify'] = _LADDERNOTIFY
DESCRIPTOR.message_types_by_name['LadderRefreshRequest'] = _LADDERREFRESHREQUEST
DESCRIPTOR.message_types_by_name['LadderRefreshResponse'] = _LADDERREFRESHRESPONSE
DESCRIPTOR.message_types_by_name['LadderMatchRequest'] = _LADDERMATCHREQUEST
DESCRIPTOR.message_types_by_name['LadderMatchResponse'] = _LADDERMATCHRESPONSE
DESCRIPTOR.message_types_by_name['LadderStoreItem'] = _LADDERSTOREITEM
DESCRIPTOR.message_types_by_name['LadderStoreNotify'] = _LADDERSTORENOTIFY
DESCRIPTOR.message_types_by_name['LadderStoreBuyRequest'] = _LADDERSTOREBUYREQUEST
DESCRIPTOR.message_types_by_name['LadderStoreBuyResponse'] = _LADDERSTOREBUYRESPONSE

class LadderClub(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERCLUB

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderClub)

class LadderLog(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERLOG

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderLog)

class LadderNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERNOTIFY

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderNotify)

class LadderRefreshRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERREFRESHREQUEST

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderRefreshRequest)

class LadderRefreshResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERREFRESHRESPONSE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderRefreshResponse)

class LadderMatchRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERMATCHREQUEST

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderMatchRequest)

class LadderMatchResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERMATCHRESPONSE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderMatchResponse)

class LadderStoreItem(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERSTOREITEM

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreItem)

class LadderStoreNotify(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERSTORENOTIFY

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreNotify)

class LadderStoreBuyRequest(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERSTOREBUYREQUEST

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreBuyRequest)

class LadderStoreBuyResponse(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _LADDERSTOREBUYRESPONSE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.LadderStoreBuyResponse)


# @@protoc_insertion_point(module_scope)
