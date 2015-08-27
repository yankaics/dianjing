# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: package.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='package.proto',
  package='Dianjing.protocol',
  serialized_pb='\n\rpackage.proto\x12\x11\x44ianjing.protocol\"q\n\x04Item\x12\x34\n\x05items\x18\x01 \x03(\x0b\x32%.Dianjing.protocol.Item.ItemAttribute\x1a\x33\n\rItemAttribute\x12\x13\n\x0bresource_id\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\".\n\x08Resource\x12\x13\n\x0bresource_id\x18\x01 \x02(\t\x12\r\n\x05value\x18\x02 \x02(\x05\"\x97\x01\n\x05Goods\x12.\n\tresources\x18\x01 \x03(\x0b\x32\x1b.Dianjing.protocol.Resource\x12\x35\n\ttrainings\x18\x02 \x03(\x0b\x32\".Dianjing.protocol.Goods.Trainings\x1a\'\n\tTrainings\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x02(\x05\"\xb7\x02\n\x07Package\x12\x0f\n\x07jingong\x18\x01 \x02(\x05\x12\x0f\n\x07qianzhi\x18\x02 \x02(\x05\x12\x0e\n\x06xintai\x18\x03 \x02(\x05\x12\x0f\n\x07\x62\x61obing\x18\x04 \x02(\x05\x12\x10\n\x08\x66\x61ngshou\x18\x05 \x02(\x05\x12\x0f\n\x07yunying\x18\x06 \x02(\x05\x12\r\n\x05yishi\x18\x07 \x02(\x05\x12\x0e\n\x06\x63\x61ozuo\x18\x08 \x02(\x05\x12\x0c\n\x04gold\x18\t \x02(\x05\x12\x0f\n\x07\x64iamond\x18\n \x02(\x05\x12\x11\n\tstaff_exp\x18\x0b \x02(\x05\x12\x13\n\x0b\x63lub_renown\x18\x0c \x02(\x05\x12\x37\n\ttrainings\x18\r \x03(\x0b\x32$.Dianjing.protocol.Package.Trainings\x1a\'\n\tTrainings\x12\n\n\x02id\x18\x01 \x02(\x05\x12\x0e\n\x06\x61mount\x18\x02 \x02(\x05')




_ITEM_ITEMATTRIBUTE = _descriptor.Descriptor(
  name='ItemAttribute',
  full_name='Dianjing.protocol.Item.ItemAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='Dianjing.protocol.Item.ItemAttribute.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dianjing.protocol.Item.ItemAttribute.value', index=1,
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
  extension_ranges=[],
  serialized_start=98,
  serialized_end=149,
)

_ITEM = _descriptor.Descriptor(
  name='Item',
  full_name='Dianjing.protocol.Item',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='Dianjing.protocol.Item.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ITEM_ITEMATTRIBUTE, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=36,
  serialized_end=149,
)


_RESOURCE = _descriptor.Descriptor(
  name='Resource',
  full_name='Dianjing.protocol.Resource',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource_id', full_name='Dianjing.protocol.Resource.resource_id', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dianjing.protocol.Resource.value', index=1,
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
  extension_ranges=[],
  serialized_start=151,
  serialized_end=197,
)


_GOODS_TRAININGS = _descriptor.Descriptor(
  name='Trainings',
  full_name='Dianjing.protocol.Goods.Trainings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Goods.Trainings.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Dianjing.protocol.Goods.Trainings.amount', index=1,
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
  extension_ranges=[],
  serialized_start=312,
  serialized_end=351,
)

_GOODS = _descriptor.Descriptor(
  name='Goods',
  full_name='Dianjing.protocol.Goods',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='Dianjing.protocol.Goods.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainings', full_name='Dianjing.protocol.Goods.trainings', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GOODS_TRAININGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=200,
  serialized_end=351,
)


_PACKAGE_TRAININGS = _descriptor.Descriptor(
  name='Trainings',
  full_name='Dianjing.protocol.Package.Trainings',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.Package.Trainings.id', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Dianjing.protocol.Package.Trainings.amount', index=1,
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
  extension_ranges=[],
  serialized_start=312,
  serialized_end=351,
)

_PACKAGE = _descriptor.Descriptor(
  name='Package',
  full_name='Dianjing.protocol.Package',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='jingong', full_name='Dianjing.protocol.Package.jingong', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qianzhi', full_name='Dianjing.protocol.Package.qianzhi', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xintai', full_name='Dianjing.protocol.Package.xintai', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='baobing', full_name='Dianjing.protocol.Package.baobing', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fangshou', full_name='Dianjing.protocol.Package.fangshou', index=4,
      number=5, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yunying', full_name='Dianjing.protocol.Package.yunying', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='yishi', full_name='Dianjing.protocol.Package.yishi', index=6,
      number=7, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caozuo', full_name='Dianjing.protocol.Package.caozuo', index=7,
      number=8, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gold', full_name='Dianjing.protocol.Package.gold', index=8,
      number=9, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='diamond', full_name='Dianjing.protocol.Package.diamond', index=9,
      number=10, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='staff_exp', full_name='Dianjing.protocol.Package.staff_exp', index=10,
      number=11, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='club_renown', full_name='Dianjing.protocol.Package.club_renown', index=11,
      number=12, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trainings', full_name='Dianjing.protocol.Package.trainings', index=12,
      number=13, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PACKAGE_TRAININGS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=354,
  serialized_end=665,
)

_ITEM_ITEMATTRIBUTE.containing_type = _ITEM;
_ITEM.fields_by_name['items'].message_type = _ITEM_ITEMATTRIBUTE
_GOODS_TRAININGS.containing_type = _GOODS;
_GOODS.fields_by_name['resources'].message_type = _RESOURCE
_GOODS.fields_by_name['trainings'].message_type = _GOODS_TRAININGS
_PACKAGE_TRAININGS.containing_type = _PACKAGE;
_PACKAGE.fields_by_name['trainings'].message_type = _PACKAGE_TRAININGS
DESCRIPTOR.message_types_by_name['Item'] = _ITEM
DESCRIPTOR.message_types_by_name['Resource'] = _RESOURCE
DESCRIPTOR.message_types_by_name['Goods'] = _GOODS
DESCRIPTOR.message_types_by_name['Package'] = _PACKAGE

class Item(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class ItemAttribute(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _ITEM_ITEMATTRIBUTE

    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Item.ItemAttribute)
  DESCRIPTOR = _ITEM

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Item)

class Resource(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESOURCE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Resource)

class Goods(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Trainings(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _GOODS_TRAININGS

    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Goods.Trainings)
  DESCRIPTOR = _GOODS

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Goods)

class Package(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType

  class Trainings(_message.Message):
    __metaclass__ = _reflection.GeneratedProtocolMessageType
    DESCRIPTOR = _PACKAGE_TRAININGS

    # @@protoc_insertion_point(class_scope:Dianjing.protocol.Package.Trainings)
  DESCRIPTOR = _PACKAGE

  # @@protoc_insertion_point(class_scope:Dianjing.protocol.Package)


# @@protoc_insertion_point(module_scope)
