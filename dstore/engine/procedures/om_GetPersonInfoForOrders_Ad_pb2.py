# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetPersonInfoForOrders_Ad.proto

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
  name='dstore/engine/procedures/om_GetPersonInfoForOrders_Ad.proto',
  package='dstore.engine.om_GetPersonInfoForOrders_Ad',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/om_GetPersonInfoForOrders_Ad.proto\x12*dstore.engine.om_GetPersonInfoForOrders_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xa0\x03\n\nParameters\x12-\n\x08order_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x16\n\rorder_id_null\x18\xe9\x07 \x01(\x08\x12\x30\n\x0blanguage_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10language_id_null\x18\xea\x07 \x01(\x08\x12\x34\n\rdate_and_time\x18\x03 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x1b\n\x12\x64\x61te_and_time_null\x18\xeb\x07 \x01(\x08\x12:\n\x15get_actual_properties\x18\x04 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12#\n\x1aget_actual_properties_null\x18\xec\x07 \x01(\x08\x12/\n\x0b\x64\x61te_format\x18\x05 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x19\n\x10\x64\x61te_format_null\x18\xed\x07 \x01(\x08\"\xb7\x05\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row\x1a\x80\x04\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12@\n\x1bvalue_restricted_by_pattern\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x30\n\x0b\x64\x65scription\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12/\n\tperson_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x1ainvoice_or_delivery_adress\x18\x94N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\x0c\x61\x63tual_value\x18\x95N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12>\n\x18person_characteristic_id\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12*\n\x05value\x18\x97N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x07sort_no\x18\x98N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x34\n\x0eperson_type_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/om_GetPersonInfoForOrders_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.order_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id_null', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.order_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.language_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id_null', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.language_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_and_time', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.date_and_time', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_and_time_null', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.date_and_time_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_actual_properties', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.get_actual_properties', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_actual_properties_null', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.get_actual_properties_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_format', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.date_format', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_format_null', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters.date_format_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
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
  serialized_end=573,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_restricted_by_pattern', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.value_restricted_by_pattern', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.description', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.person_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='invoice_or_delivery_adress', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.invoice_or_delivery_adress', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actual_value', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.actual_value', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_characteristic_id', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.person_characteristic_id', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.value', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.sort_no', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row.person_type_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
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
  serialized_start=759,
  serialized_end=1271,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetPersonInfoForOrders_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=576,
  serialized_end=1271,
)

_PARAMETERS.fields_by_name['order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['get_actual_properties'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['date_format'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value_restricted_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['invoice_or_delivery_adress'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['actual_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetPersonInfoForOrders_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPersonInfoForOrders_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetPersonInfoForOrders_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPersonInfoForOrders_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetPersonInfoForOrders_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPersonInfoForOrders_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/om_GetPersonInfoForOrders_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
