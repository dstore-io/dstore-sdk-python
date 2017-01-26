# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_GetEncryptionAlgorithm_Pu.proto

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
  name='dstore/engine/procedures/pm_GetEncryptionAlgorithm_Pu.proto',
  package='dstore.engine.pm_GetEncryptionAlgorithm_Pu',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/pm_GetEncryptionAlgorithm_Pu.proto\x12*dstore.engine.pm_GetEncryptionAlgorithm_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xef\x03\n\nParameters\x12\x33\n\x0eperson_type_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13person_type_id_null\x18\xe9\x07 \x01(\x08\x12\x42\n\x1didentifying_characteristic_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12+\n\"identifying_characteristic_id_null\x18\xea\x07 \x01(\x08\x12\x35\n\x11identifying_value\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1f\n\x16identifying_value_null\x18\xeb\x07 \x01(\x08\x12\x33\n\x0e\x63\x61se_sensitive\x18\x04 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1c\n\x13\x63\x61se_sensitive_null\x18\xec\x07 \x01(\x08\x12\x43\n\x1fget_encr_alg_for_charac_id_list\x18\x05 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n$get_encr_alg_for_charac_id_list_null\x18\xed\x07 \x01(\x08\"\xc8\x02\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.Row\x1a\x91\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12>\n\x18person_characteristic_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x39\n\x14\x65ncryption_algorithm\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/pm_GetEncryptionAlgorithm_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.person_type_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_null', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.person_type_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifying_characteristic_id', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.identifying_characteristic_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifying_characteristic_id_null', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.identifying_characteristic_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifying_value', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.identifying_value', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identifying_value_null', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.identifying_value_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_sensitive', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.case_sensitive', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_sensitive_null', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.case_sensitive_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_encr_alg_for_charac_id_list', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.get_encr_alg_for_charac_id_list', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_encr_alg_for_charac_id_list_null', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters.get_encr_alg_for_charac_id_list_null', index=9,
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
  serialized_end=652,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_characteristic_id', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.Row.person_characteristic_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encryption_algorithm', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.Row.encryption_algorithm', index=2,
      number=10002, type=11, cpp_type=10, label=1,
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
  serialized_start=838,
  serialized_end=983,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.row', index=2,
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
  serialized_start=655,
  serialized_end=983,
)

_PARAMETERS.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['identifying_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['identifying_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['case_sensitive'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['get_encr_alg_for_charac_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['encryption_algorithm'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_GetEncryptionAlgorithm_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetEncryptionAlgorithm_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_GetEncryptionAlgorithm_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_GetEncryptionAlgorithm_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetEncryptionAlgorithm_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/pm_GetEncryptionAlgorithm_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
