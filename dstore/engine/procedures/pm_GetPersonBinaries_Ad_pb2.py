# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_GetPersonBinaries_Ad.proto

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
  name='dstore/engine/procedures/pm_GetPersonBinaries_Ad.proto',
  package='dstore.engine.pm_GetPersonBinaries_Ad',
  syntax='proto3',
  serialized_pb=_b('\n6dstore/engine/procedures/pm_GetPersonBinaries_Ad.proto\x12%dstore.engine.pm_GetPersonBinaries_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xd9\x02\n\nParameters\x12.\n\tperson_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xe9\x07 \x01(\x08\x12\x38\n\x13include_binary_code\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12!\n\x18include_binary_code_null\x18\xea\x07 \x01(\x08\x12=\n\x18\x62inary_characteristic_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12&\n\x1d\x62inary_characteristic_id_null\x18\xeb\x07 \x01(\x08\x12)\n\x05value\x18\x04 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x13\n\nvalue_null\x18\xec\x07 \x01(\x08\"\xcd\x03\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12@\n\x03row\x18\x04 \x03(\x0b\x32\x33.dstore.engine.pm_GetPersonBinaries_Ad.Response.Row\x1a\x9b\x02\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12/\n\tperson_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x37\n\x12\x62inary_description\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x34\n\x0e\x62inary_code_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0ethumbnail_code\x18\x94N \x01(\x0b\x32\x19.dstore.values.BytesValue\x12/\n\x0b\x62inary_code\x18\x95N \x01(\x0b\x32\x19.dstore.values.BytesValueBX\n\x1bio.dstore.engine.proceduresZ9gosdk.dstore.de/engine/procedures/pm_GetPersonBinaries_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.person_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.person_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_binary_code', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.include_binary_code', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_binary_code_null', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.include_binary_code_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_characteristic_id', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.binary_characteristic_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_characteristic_id_null', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.binary_characteristic_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.value', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_null', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Parameters.value_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
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
  serialized_start=147,
  serialized_end=492,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row.person_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_description', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row.binary_description', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_code_id', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row.binary_code_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thumbnail_code', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row.thumbnail_code', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_code', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.Row.binary_code', index=5,
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
  serialized_start=673,
  serialized_end=956,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_GetPersonBinaries_Ad.Response.row', index=2,
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
  serialized_start=495,
  serialized_end=956,
)

_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['include_binary_code'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['binary_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['binary_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['binary_code_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['thumbnail_code'].message_type = dstore_dot_values__pb2._BYTESVALUE
_RESPONSE_ROW.fields_by_name['binary_code'].message_type = dstore_dot_values__pb2._BYTESVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_GetPersonBinaries_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonBinaries_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_GetPersonBinaries_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonBinaries_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_GetPersonBinaries_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonBinaries_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ9gosdk.dstore.de/engine/procedures/pm_GetPersonBinaries_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
