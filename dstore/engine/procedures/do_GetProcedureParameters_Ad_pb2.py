# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/do_GetProcedureParameters_Ad.proto

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
  name='dstore/engine/procedures/do_GetProcedureParameters_Ad.proto',
  package='dstore.engine.do_GetProcedureParameters_Ad',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/do_GetProcedureParameters_Ad.proto\x12*dstore.engine.do_GetProcedureParameters_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xa9\x02\n\nParameters\x12\x32\n\x0eprocedure_name\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1c\n\x13procedure_name_null\x18\xe9\x07 \x01(\x08\x12\x37\n\x13parameter_name_like\x18\x02 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12!\n\x18parameter_name_like_null\x18\xea\x07 \x01(\x08\x12\x41\n\x1c\x66ilter_rows_with_empty_descr\x18\x03 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12*\n!filter_rows_with_empty_descr_null\x18\xeb\x07 \x01(\x08\"\x92\x07\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.do_GetProcedureParameters_Ad.Response.Row\x1a\xdb\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x39\n\x13is_output_parameter\x18\x91N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x44\n\x1f\x64\x65scription_valid_since_version\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x30\n\x0b\x64\x65scription\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0fprecision_value\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x33\n\x0eparameter_name\x18\x95N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12+\n\x05scale\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07sort_no\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\rdefault_value\x18\x98N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12,\n\x06length\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x17\x64\x65scription_last_edited\x18\x9aN \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x33\n\x0eprocedure_name\x18\x9bN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12@\n\x1bintroduced_indstore_version\x18\x9cN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12.\n\tdata_type\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.StringValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/do_GetProcedureParameters_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='procedure_name', full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters.procedure_name', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procedure_name_null', full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters.procedure_name_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_name_like', full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters.parameter_name_like', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_name_like_null', full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters.parameter_name_like_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_rows_with_empty_descr', full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters.filter_rows_with_empty_descr', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_rows_with_empty_descr_null', full_name='dstore.engine.do_GetProcedureParameters_Ad.Parameters.filter_rows_with_empty_descr_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
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
  serialized_end=454,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_output_parameter', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.is_output_parameter', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_valid_since_version', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.description_valid_since_version', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.description', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision_value', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.precision_value', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_name', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.parameter_name', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scale', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.scale', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.sort_no', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_value', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.default_value', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='length', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.length', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_last_edited', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.description_last_edited', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='procedure_name', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.procedure_name', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='introduced_indstore_version', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.introduced_indstore_version', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_type', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.Row.data_type', index=13,
      number=10013, type=11, cpp_type=10, label=1,
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
  serialized_start=640,
  serialized_end=1371,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.do_GetProcedureParameters_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.do_GetProcedureParameters_Ad.Response.row', index=2,
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
  serialized_start=457,
  serialized_end=1371,
)

_PARAMETERS.fields_by_name['procedure_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['parameter_name_like'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['filter_rows_with_empty_descr'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['is_output_parameter'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['description_valid_since_version'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['precision_value'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['parameter_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['scale'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['default_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['length'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['description_last_edited'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['procedure_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['introduced_indstore_version'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['data_type'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.do_GetProcedureParameters_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.do_GetProcedureParameters_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.do_GetProcedureParameters_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.do_GetProcedureParameters_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.do_GetProcedureParameters_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.do_GetProcedureParameters_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/do_GetProcedureParameters_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
