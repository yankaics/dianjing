# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vip.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import package_pb2 as package__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vip.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\tvip.proto\x12\x11\x44ianjing.protocol\x1a\rpackage.proto\"H\n\tVIPNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03vip\x18\x02 \x02(\x05\x12\x0b\n\x03\x65xp\x18\x03 \x02(\x05\x12\x10\n\x08rewarded\x18\x04 \x03(\x05\"3\n\x13VIPBuyRewardRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0b\n\x03vip\x18\x02 \x02(\x05\"[\n\x14VIPBuyRewardResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\x12%\n\x04\x64rop\x18\x03 \x01(\x0b\x32\x17.Dianjing.protocol.Drop')
  ,
  dependencies=[package__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VIPNOTIFY = _descriptor.Descriptor(
  name='VIPNotify',
  full_name='Dianjing.protocol.VIPNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.VIPNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip', full_name='Dianjing.protocol.VIPNotify.vip', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exp', full_name='Dianjing.protocol.VIPNotify.exp', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rewarded', full_name='Dianjing.protocol.VIPNotify.rewarded', index=3,
      number=4, type=5, cpp_type=1, label=3,
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
  serialized_start=47,
  serialized_end=119,
)


_VIPBUYREWARDREQUEST = _descriptor.Descriptor(
  name='VIPBuyRewardRequest',
  full_name='Dianjing.protocol.VIPBuyRewardRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.VIPBuyRewardRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='vip', full_name='Dianjing.protocol.VIPBuyRewardRequest.vip', index=1,
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
  serialized_start=121,
  serialized_end=172,
)


_VIPBUYREWARDRESPONSE = _descriptor.Descriptor(
  name='VIPBuyRewardResponse',
  full_name='Dianjing.protocol.VIPBuyRewardResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.VIPBuyRewardResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.VIPBuyRewardResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drop', full_name='Dianjing.protocol.VIPBuyRewardResponse.drop', index=2,
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
  serialized_start=174,
  serialized_end=265,
)

_VIPBUYREWARDRESPONSE.fields_by_name['drop'].message_type = package__pb2._DROP
DESCRIPTOR.message_types_by_name['VIPNotify'] = _VIPNOTIFY
DESCRIPTOR.message_types_by_name['VIPBuyRewardRequest'] = _VIPBUYREWARDREQUEST
DESCRIPTOR.message_types_by_name['VIPBuyRewardResponse'] = _VIPBUYREWARDRESPONSE

VIPNotify = _reflection.GeneratedProtocolMessageType('VIPNotify', (_message.Message,), dict(
  DESCRIPTOR = _VIPNOTIFY,
  __module__ = 'vip_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.VIPNotify)
  ))
_sym_db.RegisterMessage(VIPNotify)

VIPBuyRewardRequest = _reflection.GeneratedProtocolMessageType('VIPBuyRewardRequest', (_message.Message,), dict(
  DESCRIPTOR = _VIPBUYREWARDREQUEST,
  __module__ = 'vip_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.VIPBuyRewardRequest)
  ))
_sym_db.RegisterMessage(VIPBuyRewardRequest)

VIPBuyRewardResponse = _reflection.GeneratedProtocolMessageType('VIPBuyRewardResponse', (_message.Message,), dict(
  DESCRIPTOR = _VIPBUYREWARDRESPONSE,
  __module__ = 'vip_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.VIPBuyRewardResponse)
  ))
_sym_db.RegisterMessage(VIPBuyRewardResponse)


# @@protoc_insertion_point(module_scope)
