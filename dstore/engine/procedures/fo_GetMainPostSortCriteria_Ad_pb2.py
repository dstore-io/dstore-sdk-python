# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_GetMainPostSortCriteria_Ad.proto

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
  name='dstore/engine/procedures/fo_GetMainPostSortCriteria_Ad.proto',
  package='dstore.engine.fo_GetMainPostSortCriteria_Ad',
  syntax='proto3',
  serialized_pb=_b('\n<dstore/engine/procedures/fo_GetMainPostSortCriteria_Ad.proto\x12+dstore.engine.fo_GetMainPostSortCriteria_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xb0\x01\n\nParameters\x12-\n\x08\x66orum_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x16\n\rforum_id_null\x18\xe9\x07 \x01(\x08\x12\x38\n\x13sorting_criteria_no\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12!\n\x18sorting_criteria_no_null\x18\xea\x07 \x01(\x08\"\xce\x06\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x46\n\x03row\x18\x04 \x03(\x0b\x32\x39.dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row\x1a\xfe\x04\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x44\n\x1clast_edited_at_date_and_time\x18\x91N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12:\n\x14sorting_optionsfirst\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12G\n\x1flast_activated_at_date_and_time\x18\x93N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12;\n\x15sorting_criteriafirst\x18\x94N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12/\n\tis_active\x18\x95N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x13sorting_criteria_no\x18\x96N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12;\n\x15sorting_criteriathird\x18\x97N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12;\n\x15sorting_optionssecond\x18\x98N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12:\n\x14sorting_optionsthird\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12<\n\x16sorting_criteriasecond\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.integerValueB^\n\x1bio.dstore.engine.proceduresZ?gosdk.dstore.de/engine/procedures/fo_GetMainPostSortCriteria_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Parameters.forum_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id_null', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Parameters.forum_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Parameters.sorting_criteria_no', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no_null', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Parameters.sorting_criteria_no_null', index=3,
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
  serialized_start=197,
  serialized_end=373,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_edited_at_date_and_time', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.last_edited_at_date_and_time', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionsfirst', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_optionsfirst', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_activated_at_date_and_time', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.last_activated_at_date_and_time', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriafirst', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_criteriafirst', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_active', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.is_active', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_criteria_no', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriathird', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_criteriathird', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionssecond', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_optionssecond', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionsthird', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_optionsthird', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriasecond', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row.sorting_criteriasecond', index=10,
      number=10010, type=11, cpp_type=10, label=1,
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
  serialized_start=584,
  serialized_end=1222,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.row', index=2,
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
  serialized_start=376,
  serialized_end=1222,
)

_PARAMETERS.fields_by_name['forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_criteria_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['last_edited_at_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['sorting_optionsfirst'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['last_activated_at_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['sorting_criteriafirst'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['is_active'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sorting_criteria_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sorting_criteriathird'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sorting_optionssecond'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sorting_optionsthird'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sorting_criteriasecond'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_GetMainPostSortCriteria_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetMainPostSortCriteria_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_GetMainPostSortCriteria_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetMainPostSortCriteria_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_GetMainPostSortCriteria_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetMainPostSortCriteria_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ?gosdk.dstore.de/engine/procedures/fo_GetMainPostSortCriteria_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)