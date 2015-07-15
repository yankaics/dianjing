# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: match.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import club_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='match.proto',
  package='Dianjing.protocol',
  serialized_pb='\n\x0bmatch.proto\x12\x11\x44ianjing.protocol\x1a\nclub.proto\"\xde\x01\n\x05Round\x12\x13\n\x0bround_index\x18\x01 \x02(\x05\x12\x31\n\tstaff_one\x18\x02 \x02(\x0b\x32\x1e.Dianjing.protocol.Round.Staff\x12\x31\n\tstaff_two\x18\x03 \x02(\x0b\x32\x1e.Dianjing.protocol.Round.Staff\x1aZ\n\x05Staff\x12\x0f\n\x07unit_id\x18\x01 \x02(\x05\x12\x10\n\x08unit_des\x18\x02 \x02(\x05\x12\x17\n\x0f\x61\x64vantage_begin\x18\x03 \x02(\x05\x12\x15\n\radvantage_end\x18\x04 \x02(\x05\"t\n\x05Match\x12\x14\n\x0cstaff_one_id\x18\x01 \x02(\x05\x12\x14\n\x0cstaff_two_id\x18\x02 \x02(\x05\x12(\n\x06rounds\x18\x03 \x03(\x0b\x32\x18.Dianjing.protocol.Round\x12\x15\n\rstaff_one_win\x18\x04 \x02(\x08\"\xa0\x01\n\tClubMatch\x12)\n\x08\x63lub_one\x18\x01 \x02(\x0b\x32\x17.Dianjing.protocol.Club\x12)\n\x08\x63lub_two\x18\x02 \x02(\x0b\x32\x17.Dianjing.protocol.Club\x12\'\n\x05match\x18\x03 \x03(\x0b\x32\x18.Dianjing.protocol.Match\x12\x14\n\x0c\x63lub_one_win\x18\x04 \x02(\x08')




_ROUND_STAFF = _descriptor.Descriptor(
  name='Staff',
  full_name='Dianjing.protocol.Round.Staff',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='Dianjing.protocol.Round.Staff.unit_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_des', full_name='Dianjing.protocol.Round.Staff.unit_des', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='advantage_begin', full_name='Dianjing.protocol.Round.Staff.advantage_begin', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='advantage_end', full_name='Dianjing.protocol.Round.Staff.advantage_end', index=3,
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
  serialized_start=179,
  serialized_end=269,
)

_ROUND = _descriptor.Descriptor(
  name='Round',
  full_name='Dianjing.protocol.Round',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='round_index', full_name='Dianjing.protocol.Round.round_index', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_one', full_name='Dianjing.protocol.Round.staff_one', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_two', full_name='Dianjing.protocol.Round.staff_two', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ROUND_STAFF, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=47,
  serialized_end=269,
)


_MATCH = _descriptor.Descriptor(
  name='Match',
  full_name='Dianjing.protocol.Match',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='staff_one_id', full_name='Dianjing.protocol.Match.staff_one_id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_two_id', full_name='Dianjing.protocol.Match.staff_two_id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rounds', full_name='Dianjing.protocol.Match.rounds', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_one_win', full_name='Dianjing.protocol.Match.staff_one_win', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=271,
  serialized_end=387,
)


_CLUBMATCH = _descriptor.Descriptor(
  name='ClubMatch',
  full_name='Dianjing.protocol.ClubMatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='club_one', full_name='Dianjing.protocol.ClubMatch.club_one', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_two', full_name='Dianjing.protocol.ClubMatch.club_two', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match', full_name='Dianjing.protocol.ClubMatch.match', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_one_win', full_name='Dianjing.protocol.ClubMatch.club_one_win', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_start=390,
  serialized_end=550,
)

_ROUND_STAFF.containing_type = _ROUND;
_ROUND.fields_by_name['staff_one'].message_type = _ROUND_STAFF
_ROUND.fields_by_name['staff_two'].message_type = _ROUND_STAFF
_MATCH.fields_by_name['rounds'].message_type = _ROUND
_CLUBMATCH.fields_by_name['club_one'].message_type = club_pb2._CLUB
_CLUBMATCH.fields_by_name['club_two'].message_type = club_pb2._CLUB
_CLUBMATCH.fields_by_name['match'].message_type = _MATCH
DESCRIPTOR.message_types_by_name['Round'] = _ROUND
DESCRIPTOR.message_types_by_name['Match'] = _MATCH
DESCRIPTOR.message_types_by_name['ClubMatch'] = _CLUBMATCH

class Round(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Staff(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ROUND_STAFF

    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Round.Staff)
  DESCRIPTOR = _ROUND

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Round)

class Match(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _MATCH

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Match)

class ClubMatch(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CLUBMATCH

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ClubMatch)


# @@protoc_insertion_point(module_scope)
