# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shop.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='shop.proto',
  package='Dianjing.protocol',
  syntax='proto2',
  serialized_pb=b'\n\nshop.proto\x12\x11\x44ianjing.protocol\"A\n\x12ItemShopBuyRequest\x12\x0f\n\x07session\x18\x01 \x02(\x0c\x12\n\n\x02id\x18\x02 \x02(\x05\x12\x0e\n\x06\x61mount\x18\x03 \x02(\x05\"3\n\x13ItemShopBuyResponse\x12\x0b\n\x03ret\x18\x01 \x02(\x05\x12\x0f\n\x07session\x18\x02 \x02(\x0c'
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ITEMSHOPBUYREQUEST = _descriptor.Descriptor(
  name='ItemShopBuyRequest',
  full_name='Dianjing.protocol.ItemShopBuyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ItemShopBuyRequest.session', index=0,
      number=1, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Dianjing.protocol.ItemShopBuyRequest.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='amount', full_name='Dianjing.protocol.ItemShopBuyRequest.amount', index=2,
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
  serialized_start=33,
  serialized_end=98,
)


_ITEMSHOPBUYRESPONSE = _descriptor.Descriptor(
  name='ItemShopBuyResponse',
  full_name='Dianjing.protocol.ItemShopBuyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='Dianjing.protocol.ItemShopBuyResponse.ret', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='Dianjing.protocol.ItemShopBuyResponse.session', index=1,
      number=2, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=b"",
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
  serialized_start=100,
  serialized_end=151,
)

DESCRIPTOR.message_types_by_name['ItemShopBuyRequest'] = _ITEMSHOPBUYREQUEST
DESCRIPTOR.message_types_by_name['ItemShopBuyResponse'] = _ITEMSHOPBUYRESPONSE

ItemShopBuyRequest = _reflection.GeneratedProtocolMessageType('ItemShopBuyRequest', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSHOPBUYREQUEST,
  __module__ = 'shop_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ItemShopBuyRequest)
  ))
_sym_db.RegisterMessage(ItemShopBuyRequest)

ItemShopBuyResponse = _reflection.GeneratedProtocolMessageType('ItemShopBuyResponse', (_message.Message,), dict(
  DESCRIPTOR = _ITEMSHOPBUYRESPONSE,
  __module__ = 'shop_pb2'
  # @@protoc_insertion_point(class_scope:Dianjing.protocol.ItemShopBuyResponse)
  ))
_sym_db.RegisterMessage(ItemShopBuyResponse)


# @@protoc_insertion_point(module_scope)
