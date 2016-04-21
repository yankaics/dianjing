# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: formation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='formation.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x66ormation.proto\x12\x11\x44ianjing.protocol\x1a\x0c\x63ommon.proto\"\x8d\x01\n\rFormationSlot\x12\x0f\n\x07slot_id\x18\x01 \x02(\x05\x12\x36\n\x06status\x18\x02 \x02(\x0e\x32&.Dianjing.protocol.FormationSlotStatus\x12\x10\n\x08position\x18\x03 \x01(\x05\x12\x10\n\x08staff_id\x18\x04 \x01(\t\x12\x0f\n\x07unit_id\x18\x05 \x01(\x05\"\x7f\n\x0f\x46ormationNotify\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12&\n\x03\x61\x63t\x18\x02 \x02(\x0e\x32\x19.Dianjing.protocol.Action\x12\x33\n\tformation\x18\x03 \x03(\x0b\x32 .Dianjing.protocol.FormationSlot\"N\n\x18\x46ormationSetStaffRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\x05\x12\x10\n\x08staff_id\x18\x03 \x02(\t\"9\n\x19\x46ormationSetStaffResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"L\n\x17\x46ormationSetUnitRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\x05\x12\x0f\n\x07unit_id\x18\x03 \x02(\x05\"8\n\x18\x46ormationSetUnitResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c\"N\n\x18\x46ormationMoveSlotRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\x0f\n\x07slot_id\x18\x02 \x02(\x05\x12\x10\n\x08to_index\x18\x03 \x02(\x05\"9\n\x19\x46ormationMoveSlotResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c*d\n\x13\x46ormationSlotStatus\x12\x1b\n\x17\x46ORMATION_SLOT_NOT_OPEN\x10\x00\x12\x18\n\x14\x46ORMATION_SLOT_EMPTY\x10\x01\x12\x16\n\x12\x46ORMATION_SLOT_USE\x10\x02')
  ,
  dependencies=[common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FORMATIONSLOTSTATUS = _descriptor.EnumDescriptor(
  name='FormationSlotStatus',
  full_name='Dianjing.protocol.FormationSlotStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORMATION_SLOT_NOT_OPEN', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMATION_SLOT_EMPTY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMATION_SLOT_USE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=739,
  serialized_end=839,
)
_sym_db.RegisterEnumDescriptor(_FORMATIONSLOTSTATUS)

FormationSlotStatus = enum_type_wrapper.EnumTypeWrapper(_FORMATIONSLOTSTATUS)
FORMATION_SLOT_NOT_OPEN = 0
FORMATION_SLOT_EMPTY = 1
FORMATION_SLOT_USE = 2



_FORMATIONSLOT = _descriptor.Descriptor(
  name='FormationSlot',
  full_name='Dianjing.protocol.FormationSlot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationSlot.slot_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='Dianjing.protocol.FormationSlot.status', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position', full_name='Dianjing.protocol.FormationSlot.position', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.FormationSlot.staff_id', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='Dianjing.protocol.FormationSlot.unit_id', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=53,
  serialized_end=194,
)


_FORMATIONNOTIFY = _descriptor.Descriptor(
  name='FormationNotify',
  full_name='Dianjing.protocol.FormationNotify',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationNotify.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='act', full_name='Dianjing.protocol.FormationNotify.act', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='formation', full_name='Dianjing.protocol.FormationNotify.formation', index=2,
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
  serialized_start=196,
  serialized_end=323,
)


_FORMATIONSETSTAFFREQUEST = _descriptor.Descriptor(
  name='FormationSetStaffRequest',
  full_name='Dianjing.protocol.FormationSetStaffRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetStaffRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationSetStaffRequest.slot_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_id', full_name='Dianjing.protocol.FormationSetStaffRequest.staff_id', index=2,
      number=3, type=9, cpp_type=9, label=2,
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
  serialized_start=325,
  serialized_end=403,
)


_FORMATIONSETSTAFFRESPONSE = _descriptor.Descriptor(
  name='FormationSetStaffResponse',
  full_name='Dianjing.protocol.FormationSetStaffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationSetStaffResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetStaffResponse.session', index=1,
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
  serialized_start=405,
  serialized_end=462,
)


_FORMATIONSETUNITREQUEST = _descriptor.Descriptor(
  name='FormationSetUnitRequest',
  full_name='Dianjing.protocol.FormationSetUnitRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetUnitRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationSetUnitRequest.slot_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='Dianjing.protocol.FormationSetUnitRequest.unit_id', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=464,
  serialized_end=540,
)


_FORMATIONSETUNITRESPONSE = _descriptor.Descriptor(
  name='FormationSetUnitResponse',
  full_name='Dianjing.protocol.FormationSetUnitResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationSetUnitResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationSetUnitResponse.session', index=1,
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
  serialized_start=542,
  serialized_end=598,
)


_FORMATIONMOVESLOTREQUEST = _descriptor.Descriptor(
  name='FormationMoveSlotRequest',
  full_name='Dianjing.protocol.FormationMoveSlotRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationMoveSlotRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='slot_id', full_name='Dianjing.protocol.FormationMoveSlotRequest.slot_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_index', full_name='Dianjing.protocol.FormationMoveSlotRequest.to_index', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=600,
  serialized_end=678,
)


_FORMATIONMOVESLOTRESPONSE = _descriptor.Descriptor(
  name='FormationMoveSlotResponse',
  full_name='Dianjing.protocol.FormationMoveSlotResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.FormationMoveSlotResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.FormationMoveSlotResponse.session', index=1,
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
  serialized_start=680,
  serialized_end=737,
)

_FORMATIONSLOT.fields_by_name['status'].enum_type = _FORMATIONSLOTSTATUS
_FORMATIONNOTIFY.fields_by_name['act'].enum_type = common__pb2._ACTION
_FORMATIONNOTIFY.fields_by_name['formation'].message_type = _FORMATIONSLOT
DESCRIPTOR.message_types_by_name['FormationSlot'] = _FORMATIONSLOT
DESCRIPTOR.message_types_by_name['FormationNotify'] = _FORMATIONNOTIFY
DESCRIPTOR.message_types_by_name['FormationSetStaffRequest'] = _FORMATIONSETSTAFFREQUEST
DESCRIPTOR.message_types_by_name['FormationSetStaffResponse'] = _FORMATIONSETSTAFFRESPONSE
DESCRIPTOR.message_types_by_name['FormationSetUnitRequest'] = _FORMATIONSETUNITREQUEST
DESCRIPTOR.message_types_by_name['FormationSetUnitResponse'] = _FORMATIONSETUNITRESPONSE
DESCRIPTOR.message_types_by_name['FormationMoveSlotRequest'] = _FORMATIONMOVESLOTREQUEST
DESCRIPTOR.message_types_by_name['FormationMoveSlotResponse'] = _FORMATIONMOVESLOTRESPONSE
DESCRIPTOR.enum_types_by_name['FormationSlotStatus'] = _FORMATIONSLOTSTATUS

FormationSlot = _reflection.GeneratedProtocolMessageType('FormationSlot', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSLOT,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSlot)
  ))
_sym_db.RegisterMessage(FormationSlot)

FormationNotify = _reflection.GeneratedProtocolMessageType('FormationNotify', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONNOTIFY,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationNotify)
  ))
_sym_db.RegisterMessage(FormationNotify)

FormationSetStaffRequest = _reflection.GeneratedProtocolMessageType('FormationSetStaffRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETSTAFFREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetStaffRequest)
  ))
_sym_db.RegisterMessage(FormationSetStaffRequest)

FormationSetStaffResponse = _reflection.GeneratedProtocolMessageType('FormationSetStaffResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETSTAFFRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetStaffResponse)
  ))
_sym_db.RegisterMessage(FormationSetStaffResponse)

FormationSetUnitRequest = _reflection.GeneratedProtocolMessageType('FormationSetUnitRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETUNITREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetUnitRequest)
  ))
_sym_db.RegisterMessage(FormationSetUnitRequest)

FormationSetUnitResponse = _reflection.GeneratedProtocolMessageType('FormationSetUnitResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONSETUNITRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationSetUnitResponse)
  ))
_sym_db.RegisterMessage(FormationSetUnitResponse)

FormationMoveSlotRequest = _reflection.GeneratedProtocolMessageType('FormationMoveSlotRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONMOVESLOTREQUEST,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationMoveSlotRequest)
  ))
_sym_db.RegisterMessage(FormationMoveSlotRequest)

FormationMoveSlotResponse = _reflection.GeneratedProtocolMessageType('FormationMoveSlotResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORMATIONMOVESLOTRESPONSE,
  __module__ = 'formation_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.FormationMoveSlotResponse)
  ))
_sym_db.RegisterMessage(FormationMoveSlotResponse)


# @@protoc_insertion_point(module_scope)