# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_CopyFromTrolleyToOrder_Pu.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dstore import values_pb2 as dstore_dot_values__pb2
from dstore.engine import engine_pb2 as dstore_dot_engine_dot_engine__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dstore/engine/procedures/om_CopyFromTrolleyToOrder_Pu.proto',
  package='dstore.engine.om_CopyFromTrolleyToOrder_Pu',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/om_CopyFromTrolleyToOrder_Pu.proto\x12*dstore.engine.om_CopyFromTrolleyToOrder_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xff\x0b\n\nParameters\x12@\n\x1bincorrect_information_exist\x18\x01 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12)\n incorrect_information_exist_null\x18\xe9\x07 \x01(\x08\x12;\n\x16\x61\x64\x64_order_informations\x18\x02 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12$\n\x1b\x61\x64\x64_order_informations_null\x18\xea\x07 \x01(\x08\x12-\n\tunique_id\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xeb\x07 \x01(\x08\x12.\n\tperson_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xec\x07 \x01(\x08\x12\x37\n\x12\x64\x65livery_person_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17\x64\x65livery_person_id_null\x18\xed\x07 \x01(\x08\x12\x35\n\x10shipping_type_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1e\n\x15shipping_type_id_null\x18\xee\x07 \x01(\x08\x12\x34\n\x0fpayment_type_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1d\n\x14payment_type_id_null\x18\xef\x07 \x01(\x08\x12=\n\x16\x64\x65livery_date_and_time\x18\x08 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12$\n\x1b\x64\x65livery_date_and_time_null\x18\xf0\x07 \x01(\x08\x12\x33\n\x0estart_order_id\x18\t \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13start_order_id_null\x18\xf1\x07 \x01(\x08\x12\x41\n\x1cprice_node_characteristic_id\x18\n \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12*\n!price_node_characteristic_id_null\x18\xf2\x07 \x01(\x08\x12\x37\n\x12generated_order_id\x18\x0b \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17generated_order_id_null\x18\xf3\x07 \x01(\x08\x12:\n\x15\x61\x64\x64_order_information\x18\x0c \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12#\n\x1a\x61\x64\x64_order_information_null\x18\xf4\x07 \x01(\x08\x12\x42\n\x1d\x61\x64\x64_order_content_information\x18\r \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12+\n\"add_order_content_information_null\x18\xf5\x07 \x01(\x08\x12>\n\x19get_incorrect_information\x18\x0e \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\'\n\x1eget_incorrect_information_null\x18\xf6\x07 \x01(\x08\x12?\n\x1ause_cash_account_max_value\x18\x0f \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12(\n\x1fuse_cash_account_max_value_null\x18\xf7\x07 \x01(\x08\x12;\n\x16\x61\x62ort_if_items_removed\x18\x10 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12$\n\x1b\x61\x62ort_if_items_removed_null\x18\xf8\x07 \x01(\x08\"\xa9\x03\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row\x12\x37\n\x12generated_order_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x1a\xb9\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x39\n\x13information_type_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x34\n\x0eh_tree_node_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x30\n\nerror_code\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/om_CopyFromTrolleyToOrder_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incorrect_information_exist', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.incorrect_information_exist', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incorrect_information_exist_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.incorrect_information_exist_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_order_informations', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.add_order_informations', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_order_informations_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.add_order_informations_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.unique_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.unique_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.person_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.person_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.delivery_person_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.delivery_person_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.shipping_type_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.shipping_type_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.payment_type_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.payment_type_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_date_and_time', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.delivery_date_and_time', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_date_and_time_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.delivery_date_and_time_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_order_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.start_order_id', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_order_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.start_order_id_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.price_node_characteristic_id', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.price_node_characteristic_id_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generated_order_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.generated_order_id', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generated_order_id_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.generated_order_id_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_order_information', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.add_order_information', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_order_information_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.add_order_information_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_order_content_information', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.add_order_content_information', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_order_content_information_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.add_order_content_information_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_incorrect_information', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.get_incorrect_information', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_incorrect_information_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.get_incorrect_information_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_cash_account_max_value', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.use_cash_account_max_value', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_cash_account_max_value_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.use_cash_account_max_value_null', index=29,
      number=1015, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='abort_if_items_removed', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.abort_if_items_removed', index=30,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='abort_if_items_removed_null', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters.abort_if_items_removed_null', index=31,
      number=1016, type=8, cpp_type=7, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=157,
  serialized_end=1692,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='information_type_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row.information_type_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row.h_tree_node_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row.error_code', index=3,
      number=10003, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1935,
  serialized_end=2120,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generated_order_id', full_name='dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.generated_order_id', index=3,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_ROW, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1695,
  serialized_end=2120,
)

_PARAMETERS.fields_by_name['incorrect_information_exist'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['add_order_informations'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delivery_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delivery_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['start_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['price_node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['generated_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['add_order_information'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['add_order_content_information'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_incorrect_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['use_cash_account_max_value'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['abort_if_items_removed'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['information_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['h_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['error_code'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['generated_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_CopyFromTrolleyToOrder_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_CopyFromTrolleyToOrder_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_CopyFromTrolleyToOrder_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_CopyFromTrolleyToOrder_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_CopyFromTrolleyToOrder_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/om_CopyFromTrolleyToOrder_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
