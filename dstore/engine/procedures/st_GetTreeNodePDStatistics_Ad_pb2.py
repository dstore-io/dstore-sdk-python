# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/st_GetTreeNodePDStatistics_Ad.proto

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
  name='dstore/engine/procedures/st_GetTreeNodePDStatistics_Ad.proto',
  package='dstore.engine.st_GetTreeNodePDStatistics_Ad',
  syntax='proto3',
  serialized_pb=_b('\n<dstore/engine/procedures/st_GetTreeNodePDStatistics_Ad.proto\x12+dstore.engine.st_GetTreeNodePDStatistics_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xb3\x03\n\nParameters\x12\x30\n\tfrom_date\x18\x01 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x17\n\x0e\x66rom_date_null\x18\xe9\x07 \x01(\x08\x12.\n\x07to_date\x18\x02 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x15\n\x0cto_date_null\x18\xea\x07 \x01(\x08\x12@\n\x1c\x62\x61sic_characteristic_numbers\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n!basic_characteristic_numbers_null\x18\xeb\x07 \x01(\x08\x12\x33\n\x0fh_tree_node_ids\x18\x04 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1d\n\x14h_tree_node_ids_null\x18\xec\x07 \x01(\x08\x12\x33\n\x0esummarize_days\x18\x05 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1c\n\x13summarize_days_null\x18\xed\x07 \x01(\x08\"\xdc\x03\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x46\n\x03row\x18\x04 \x03(\x0b\x32\x39.dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row\x1a\xa4\x02\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x31\n\x0btotal_value\x18\x91N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x34\n\x0eh_tree_node_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0c\x64irect_value\x18\x93N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12,\n\x04\x64\x61te\x18\x94N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x41\n\x1b\x62\x61sic_characteristic_number\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValueB^\n\x1bio.dstore.engine.proceduresZ?gosdk.dstore.de/engine/procedures/st_GetTreeNodePDStatistics_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_date', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.from_date', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date_null', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.from_date_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.to_date', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date_null', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.to_date_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_numbers', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.basic_characteristic_numbers', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_numbers_null', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.basic_characteristic_numbers_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_ids', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.h_tree_node_ids', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_ids_null', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.h_tree_node_ids_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summarize_days', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.summarize_days', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='summarize_days_null', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters.summarize_days_null', index=9,
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
  serialized_start=159,
  serialized_end=594,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_value', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row.total_value', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_id', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row.h_tree_node_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direct_value', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row.direct_value', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row.date', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_number', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row.basic_characteristic_number', index=5,
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
  serialized_start=781,
  serialized_end=1073,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.row', index=2,
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
  serialized_start=597,
  serialized_end=1073,
)

_PARAMETERS.fields_by_name['from_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['to_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['basic_characteristic_numbers'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['h_tree_node_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['summarize_days'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['total_value'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['h_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['direct_value'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['basic_characteristic_number'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.st_GetTreeNodePDStatistics_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.st_GetTreeNodePDStatistics_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.st_GetTreeNodePDStatistics_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.st_GetTreeNodePDStatistics_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.st_GetTreeNodePDStatistics_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.st_GetTreeNodePDStatistics_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ?gosdk.dstore.de/engine/procedures/st_GetTreeNodePDStatistics_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
