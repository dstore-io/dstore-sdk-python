# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_ModifyMainPostSortCrit_Ad.proto

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
  name='dstore/engine/procedures/fo_ModifyMainPostSortCrit_Ad.proto',
  package='dstore.engine.fo_ModifyMainPostSortCrit_Ad',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/fo_ModifyMainPostSortCrit_Ad.proto\x12*dstore.engine.fo_ModifyMainPostSortCrit_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xa2\x07\n\nParameters\x12-\n\x08\x66orum_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x16\n\rforum_id_null\x18\xe9\x07 \x01(\x08\x12\x38\n\x13sorting_criteria_no\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12!\n\x18sorting_criteria_no_null\x18\xea\x07 \x01(\x08\x12:\n\x15sorting_criteriafirst\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12#\n\x1asorting_criteriafirst_null\x18\xeb\x07 \x01(\x08\x12\x39\n\x14sorting_optionsfirst\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\"\n\x19sorting_optionsfirst_null\x18\xec\x07 \x01(\x08\x12;\n\x16sorting_criteriasecond\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12$\n\x1bsorting_criteriasecond_null\x18\xed\x07 \x01(\x08\x12:\n\x15sorting_optionssecond\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12#\n\x1asorting_optionssecond_null\x18\xee\x07 \x01(\x08\x12:\n\x15sorting_criteriathird\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12#\n\x1asorting_criteriathird_null\x18\xef\x07 \x01(\x08\x12\x39\n\x14sorting_optionsthird\x18\x08 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\"\n\x19sorting_optionsthird_null\x18\xf0\x07 \x01(\x08\x12\x36\n\x11\x61\x63tivate_criteria\x18\t \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1f\n\x16\x61\x63tivate_criteria_null\x18\xf1\x07 \x01(\x08\x12\x34\n\x0f\x64\x65lete_criteria\x18\n \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1d\n\x14\x64\x65lete_criteria_null\x18\xf2\x07 \x01(\x08\"\xcc\x01\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.Row\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/fo_ModifyMainPostSortCrit_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.forum_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.forum_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteria_no', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteria_no_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriafirst', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteriafirst', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriafirst_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteriafirst_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionsfirst', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_optionsfirst', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionsfirst_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_optionsfirst_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriasecond', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteriasecond', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriasecond_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteriasecond_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionssecond', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_optionssecond', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionssecond_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_optionssecond_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriathird', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteriathird', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteriathird_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_criteriathird_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionsthird', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_optionsthird', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_optionsthird_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.sorting_optionsthird_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activate_criteria', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.activate_criteria', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activate_criteria_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.activate_criteria_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_criteria', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.delete_criteria', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_criteria_null', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters.delete_criteria_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
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
  serialized_end=1087,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.Row.row_id', index=0,
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
  serialized_start=1272,
  serialized_end=1294,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.row', index=2,
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
  serialized_start=1090,
  serialized_end=1294,
)

_PARAMETERS.fields_by_name['forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_criteria_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_criteriafirst'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_optionsfirst'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_criteriasecond'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_optionssecond'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_criteriathird'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_optionsthird'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['activate_criteria'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['delete_criteria'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_ModifyMainPostSortCrit_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_ModifyMainPostSortCrit_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_ModifyMainPostSortCrit_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_ModifyMainPostSortCrit_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_ModifyMainPostSortCrit_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/fo_ModifyMainPostSortCrit_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
