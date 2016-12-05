# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/ac_InsertAction_Ad.proto

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
  name='dstore/engine/procedures/ac_InsertAction_Ad.proto',
  package='dstore.engine.ac_InsertAction_Ad',
  syntax='proto3',
  serialized_pb=_b('\n1dstore/engine/procedures/ac_InsertAction_Ad.proto\x12 dstore.engine.ac_InsertAction_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xf3\x04\n\nParameters\x12/\n\ncommand_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x18\n\x0f\x63ommand_id_null\x18\xe9\x07 \x01(\x08\x12+\n\x06status\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x14\n\x0bstatus_null\x18\xea\x07 \x01(\x08\x12\x33\n\x0fparameter_names\x18\x03 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x1d\n\x14parameter_names_null\x18\xeb\x07 \x01(\x08\x12\x34\n\x10parameter_values\x18\x04 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x1e\n\x15parameter_values_null\x18\xec\x07 \x01(\x08\x12\x32\n\rnew_action_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1b\n\x12new_action_id_null\x18\xed\x07 \x01(\x08\x12=\n\x19separator_in_param_values\x18\x06 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\'\n\x1eseparator_in_param_values_null\x18\xee\x07 \x01(\x08\x12\x44\n sep_in_any_values_other_than_l_f\x18\x07 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12.\n%sep_in_any_values_other_than_l_f_null\x18\xef\x07 \x01(\x08\"\x8e\x02\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12;\n\x03row\x18\x04 \x03(\x0b\x32..dstore.engine.ac_InsertAction_Ad.Response.Row\x12\x32\n\rnew_action_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42S\n\x1bio.dstore.engine.proceduresZ4gosdk.dstore.de/engine/procedures/ac_InsertAction_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.ac_InsertAction_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_id', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.command_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='command_id_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.command_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.status', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.status_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_names', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.parameter_names', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_names_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.parameter_names_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_values', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.parameter_values', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parameter_values_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.parameter_values_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_action_id', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.new_action_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_action_id_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.new_action_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_param_values', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.separator_in_param_values', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_param_values_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.separator_in_param_values_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sep_in_any_values_other_than_l_f', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.sep_in_any_values_other_than_l_f', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sep_in_any_values_other_than_l_f_null', full_name='dstore.engine.ac_InsertAction_Ad.Parameters.sep_in_any_values_other_than_l_f_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
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
  serialized_start=175,
  serialized_end=802,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.ac_InsertAction_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.ac_InsertAction_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1053,
  serialized_end=1075,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.ac_InsertAction_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.ac_InsertAction_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.ac_InsertAction_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.ac_InsertAction_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_action_id', full_name='dstore.engine.ac_InsertAction_Ad.Response.new_action_id', index=3,
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
  serialized_start=805,
  serialized_end=1075,
)

_PARAMETERS.fields_by_name['command_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['status'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['parameter_names'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['parameter_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['new_action_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['separator_in_param_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['sep_in_any_values_other_than_l_f'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['new_action_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.ac_InsertAction_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.ac_InsertAction_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.ac_InsertAction_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.ac_InsertAction_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.ac_InsertAction_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.ac_InsertAction_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ4gosdk.dstore.de/engine/procedures/ac_InsertAction_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
