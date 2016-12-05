# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetUsedVoucherCodes_Ad.proto

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
  name='dstore/engine/procedures/om_GetUsedVoucherCodes_Ad.proto',
  package='dstore.engine.om_GetUsedVoucherCodes_Ad',
  syntax='proto3',
  serialized_pb=_b('\n8dstore/engine/procedures/om_GetUsedVoucherCodes_Ad.proto\x12\'dstore.engine.om_GetUsedVoucherCodes_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xe6\x03\n\nParameters\x12\x38\n\x13visitor_or_order_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12!\n\x18visitor_or_order_id_null\x18\xe9\x07 \x01(\x08\x12\x30\n\x0bis_order_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10is_order_id_null\x18\xea\x07 \x01(\x08\x12\x30\n\x0cvoucher_code\x18\x03 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x1a\n\x11voucher_code_null\x18\xeb\x07 \x01(\x08\x12\x44\n\x1d\x66rom_validation_date_and_time\x18\x04 \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12+\n\"from_validation_date_and_time_null\x18\xec\x07 \x01(\x08\x12\x42\n\x1bto_validation_date_and_time\x18\x05 \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12)\n to_validation_date_and_time_null\x18\xed\x07 \x01(\x08\"\xfb\x03\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x42\n\x03row\x18\x04 \x03(\x0b\x32\x35.dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row\x1a\xaf\x02\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x31\n\x0cvoucher_code\x18\x91N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12/\n\tperson_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x45\n\x1dlast_validation_date_and_time\x18\x93N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12\x39\n\x13visitor_or_order_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x31\n\x0bis_order_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.integerValueBZ\n\x1bio.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/om_GetUsedVoucherCodes_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='visitor_or_order_id', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.visitor_or_order_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visitor_or_order_id_null', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.visitor_or_order_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_order_id', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.is_order_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_order_id_null', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.is_order_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voucher_code', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.voucher_code', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voucher_code_null', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.voucher_code_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_validation_date_and_time', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.from_validation_date_and_time', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_validation_date_and_time_null', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.from_validation_date_and_time_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_validation_date_and_time', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.to_validation_date_and_time', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_validation_date_and_time_null', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters.to_validation_date_and_time_null', index=9,
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
  serialized_start=189,
  serialized_end=675,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voucher_code', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row.voucher_code', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row.person_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_validation_date_and_time', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row.last_validation_date_and_time', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visitor_or_order_id', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row.visitor_or_order_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_order_id', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row.is_order_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
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
  serialized_start=882,
  serialized_end=1185,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetUsedVoucherCodes_Ad.Response.row', index=2,
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
  serialized_start=678,
  serialized_end=1185,
)

_PARAMETERS.fields_by_name['visitor_or_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['is_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['voucher_code'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['from_validation_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['to_validation_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['voucher_code'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['last_validation_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['visitor_or_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['is_order_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetUsedVoucherCodes_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetUsedVoucherCodes_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetUsedVoucherCodes_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetUsedVoucherCodes_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetUsedVoucherCodes_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetUsedVoucherCodes_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/om_GetUsedVoucherCodes_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
