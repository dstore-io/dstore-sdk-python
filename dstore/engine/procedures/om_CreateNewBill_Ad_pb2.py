# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_CreateNewBill_Ad.proto

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
from dstore.engine import message_pb2 as dstore_dot_engine_dot_message__pb2
from dstore.engine import metainformation_pb2 as dstore_dot_engine_dot_metainformation__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dstore/engine/procedures/om_CreateNewBill_Ad.proto',
  package='dstore.engine.om_CreateNewBill_Ad',
  syntax='proto3',
  serialized_pb=_b('\n2dstore/engine/procedures/om_CreateNewBill_Ad.proto\x12!dstore.engine.om_CreateNewBill_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xa6\t\n\nParameters\x12\x41\n\x1cincorrect_information_exists\x18\x01 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12*\n!incorrect_information_exists_null\x18\xe9\x07 \x01(\x08\x12+\n\x06result\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x14\n\x0bresult_null\x18\xea\x07 \x01(\x08\x12-\n\x08order_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x16\n\rorder_id_null\x18\xeb\x07 \x01(\x08\x12\x38\n\x13recipient_person_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12!\n\x18recipient_person_id_null\x18\xec\x07 \x01(\x08\x12\x35\n\x10\x64rawer_person_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1e\n\x15\x64rawer_person_id_null\x18\xed\x07 \x01(\x08\x12\x30\n\x0b\x63urrency_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10\x63urrency_id_null\x18\xee\x07 \x01(\x08\x12\x36\n\x11generated_bill_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1f\n\x16generated_bill_id_null\x18\xef\x07 \x01(\x08\x12\x39\n\x14\x61\x64\x64_bill_information\x18\x08 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\"\n\x19\x61\x64\x64_bill_information_null\x18\xf0\x07 \x01(\x08\x12\x41\n\x1c\x61\x64\x64_bill_content_information\x18\t \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12*\n!add_bill_content_information_null\x18\xf1\x07 \x01(\x08\x12\x37\n\x12other_bill_content\x18\n \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12 \n\x17other_bill_content_null\x18\xf2\x07 \x01(\x08\x12\x42\n\x1d\x61\x64\x64_other_content_information\x18\x0b \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12+\n\"add_other_content_information_null\x18\xf3\x07 \x01(\x08\x12>\n\x19get_incorrect_information\x18\x0c \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\'\n\x1eget_incorrect_information_null\x18\xf4\x07 \x01(\x08\x12+\n\x07\x63ountry\x18\r \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x15\n\x0c\x63ountry_null\x18\xf5\x07 \x01(\x08\"\xe5\x03\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12<\n\x03row\x18\x04 \x03(\x0b\x32/.dstore.engine.om_CreateNewBill_Ad.Response.Row\x12\x36\n\x11generated_bill_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x1a\xe7\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12.\n\x08table_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x13information_type_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x32\n\x0ctable_key_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x30\n\nerror_code\x18\x94N \x01(\x0b\x32\x1b.dstore.values.integerValueBT\n\x1bio.dstore.engine.proceduresZ5gosdk.dstore.de/engine/procedures/om_CreateNewBill_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_CreateNewBill_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incorrect_information_exists', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.incorrect_information_exists', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='incorrect_information_exists_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.incorrect_information_exists_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.result', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.result_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.order_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.order_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recipient_person_id', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.recipient_person_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recipient_person_id_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.recipient_person_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drawer_person_id', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.drawer_person_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='drawer_person_id_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.drawer_person_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.currency_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.currency_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generated_bill_id', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.generated_bill_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generated_bill_id_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.generated_bill_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_bill_information', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.add_bill_information', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_bill_information_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.add_bill_information_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_bill_content_information', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.add_bill_content_information', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_bill_content_information_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.add_bill_content_information_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_bill_content', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.other_bill_content', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_bill_content_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.other_bill_content_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_other_content_information', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.add_other_content_information', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_other_content_information_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.add_other_content_information_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_incorrect_information', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.get_incorrect_information', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_incorrect_information_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.get_incorrect_information_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.country', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_null', full_name='dstore.engine.om_CreateNewBill_Ad.Parameters.country_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
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
  serialized_start=177,
  serialized_end=1367,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_CreateNewBill_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_CreateNewBill_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_id', full_name='dstore.engine.om_CreateNewBill_Ad.Response.Row.table_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='information_type_id', full_name='dstore.engine.om_CreateNewBill_Ad.Response.Row.information_type_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='table_key_id', full_name='dstore.engine.om_CreateNewBill_Ad.Response.Row.table_key_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='dstore.engine.om_CreateNewBill_Ad.Response.Row.error_code', index=4,
      number=10004, type=11, cpp_type=10, label=1,
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
  serialized_start=1624,
  serialized_end=1855,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_CreateNewBill_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_CreateNewBill_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_CreateNewBill_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_CreateNewBill_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generated_bill_id', full_name='dstore.engine.om_CreateNewBill_Ad.Response.generated_bill_id', index=3,
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
  serialized_start=1370,
  serialized_end=1855,
)

_PARAMETERS.fields_by_name['incorrect_information_exists'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['result'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['recipient_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['drawer_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['currency_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['generated_bill_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['add_bill_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['add_bill_content_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['other_bill_content'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['add_other_content_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['get_incorrect_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['country'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['table_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['information_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['table_key_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['error_code'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['generated_bill_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_CreateNewBill_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_CreateNewBill_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_CreateNewBill_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_CreateNewBill_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_CreateNewBill_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_CreateNewBill_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ5gosdk.dstore.de/engine/procedures/om_CreateNewBill_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
