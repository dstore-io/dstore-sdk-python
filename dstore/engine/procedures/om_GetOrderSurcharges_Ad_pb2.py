# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetOrderSurcharges_Ad.proto

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
  name='dstore/engine/procedures/om_GetOrderSurcharges_Ad.proto',
  package='dstore.engine.om_GetOrderSurcharges_Ad',
  syntax='proto3',
  serialized_pb=_b('\n7dstore/engine/procedures/om_GetOrderSurcharges_Ad.proto\x12&dstore.engine.om_GetOrderSurcharges_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xa6\x01\n\nParameters\x12-\n\x08order_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x16\n\rorder_id_null\x18\xe9\x07 \x01(\x08\x12\x33\n\x0esplit_by_taxes\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13split_by_taxes_null\x18\xea\x07 \x01(\x08\"\x89\t\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x41\n\x03row\x18\x04 \x03(\x0b\x32\x34.dstore.engine.om_GetOrderSurcharges_Ad.Response.Row\x1a\xd6\x07\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12>\n\x18original_surcharge_value\x18\x91N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12<\n\x16orig_surch_val_unit_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x1aorig_surch_val_unit_symbol\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x38\n\x12\x61pplied_on_net_sum\x18\x94N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x36\n\x10taxes_multiplier\x18\x95N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12<\n\x16\x61\x62solute_net_surcharge\x18\x96N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x31\n\x0bposition_no\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12:\n\x14\x61pplied_on_gross_sum\x18\x98N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x31\n\x0b\x63urrency_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x34\n\x0f\x63urrency_symbol\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12@\n\x1aorig_surch_val_is_absolute\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12>\n\x18\x61\x62solute_gross_surcharge\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x39\n\x14\x63\x61tegory_description\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12?\n\x1asurcharge_type_description\x18\x9eN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x37\n\x11surcharge_type_id\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12@\n\x1asurcharge_type_category_id\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.IntegerValueBY\n\x1bio.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_GetOrderSurcharges_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetOrderSurcharges_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='order_id', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Parameters.order_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_id_null', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Parameters.order_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='split_by_taxes', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Parameters.split_by_taxes', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='split_by_taxes_null', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Parameters.split_by_taxes_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
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
  serialized_start=149,
  serialized_end=315,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='original_surcharge_value', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.original_surcharge_value', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orig_surch_val_unit_id', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.orig_surch_val_unit_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orig_surch_val_unit_symbol', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.orig_surch_val_unit_symbol', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_on_net_sum', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.applied_on_net_sum', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='taxes_multiplier', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.taxes_multiplier', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_net_surcharge', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.absolute_net_surcharge', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='position_no', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.position_no', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='applied_on_gross_sum', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.applied_on_gross_sum', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.currency_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_symbol', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.currency_symbol', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orig_surch_val_is_absolute', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.orig_surch_val_is_absolute', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_gross_surcharge', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.absolute_gross_surcharge', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category_description', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.category_description', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_type_description', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.surcharge_type_description', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_type_id', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.surcharge_type_id', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_type_category_id', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.Row.surcharge_type_category_id', index=16,
      number=10016, type=11, cpp_type=10, label=1,
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
  serialized_start=497,
  serialized_end=1479,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetOrderSurcharges_Ad.Response.row', index=2,
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
  serialized_start=318,
  serialized_end=1479,
)

_PARAMETERS.fields_by_name['order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['split_by_taxes'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['original_surcharge_value'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['orig_surch_val_unit_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['orig_surch_val_unit_symbol'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['applied_on_net_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['taxes_multiplier'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_net_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['position_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['applied_on_gross_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['currency_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['currency_symbol'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['orig_surch_val_is_absolute'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['absolute_gross_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['category_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['surcharge_type_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['surcharge_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['surcharge_type_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetOrderSurcharges_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetOrderSurcharges_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetOrderSurcharges_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetOrderSurcharges_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetOrderSurcharges_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetOrderSurcharges_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_GetOrderSurcharges_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
