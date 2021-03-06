# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/mi_SearchSourceCode_Ad.proto

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
  name='dstore/engine/procedures/mi_SearchSourceCode_Ad.proto',
  package='dstore.engine.mi_SearchSourceCode_Ad',
  syntax='proto3',
  serialized_pb=_b('\n5dstore/engine/procedures/mi_SearchSourceCode_Ad.proto\x12$dstore.engine.mi_SearchSourceCode_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xd7\x05\n\nParameters\x12\x32\n\x0esearch_pattern\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1c\n\x13search_pattern_null\x18\xe9\x07 \x01(\x08\x12\x33\n\x0e\x63\x61se_sensitive\x18\x02 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1c\n\x13\x63\x61se_sensitive_null\x18\xea\x07 \x01(\x08\x12\x42\n\x1d\x64o_not_search_in_comment_part\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12+\n\"do_not_search_in_comment_part_null\x18\xeb\x07 \x01(\x08\x12@\n\x1csearch_only_this_object_name\x18\x04 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n!search_only_this_object_name_null\x18\xec\x07 \x01(\x08\x12;\n\x17search_only_object_type\x18\x05 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12%\n\x1csearch_only_object_type_null\x18\xed\x07 \x01(\x08\x12\x43\n\x1eget_distinct_object_names_only\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12,\n#get_distinct_object_names_only_null\x18\xee\x07 \x01(\x08\x12\x41\n\x1dsearch_objects_with_name_like\x18\x07 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12+\n\"search_objects_with_name_like_null\x18\xef\x07 \x01(\x08\"\x93\x03\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12?\n\x03row\x18\x04 \x03(\x0b\x32\x32.dstore.engine.mi_SearchSourceCode_Ad.Response.Row\x1a\xe2\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x30\n\x0bobject_type\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x36\n\x10\x63ode_line_number\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\tcode_line\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x30\n\x0bobject_name\x18\x94N \x01(\x0b\x32\x1a.dstore.values.StringValueBW\n\x1bio.dstore.engine.proceduresZ8gosdk.dstore.de/engine/procedures/mi_SearchSourceCode_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='search_pattern', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_pattern', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_pattern_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_pattern_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_sensitive', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.case_sensitive', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_sensitive_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.case_sensitive_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='do_not_search_in_comment_part', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.do_not_search_in_comment_part', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='do_not_search_in_comment_part_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.do_not_search_in_comment_part_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_only_this_object_name', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_only_this_object_name', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_only_this_object_name_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_only_this_object_name_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_only_object_type', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_only_object_type', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_only_object_type_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_only_object_type_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_distinct_object_names_only', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.get_distinct_object_names_only', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_distinct_object_names_only_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.get_distinct_object_names_only_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_objects_with_name_like', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_objects_with_name_like', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_objects_with_name_like_null', full_name='dstore.engine.mi_SearchSourceCode_Ad.Parameters.search_objects_with_name_like_null', index=13,
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
  serialized_start=145,
  serialized_end=872,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_type', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.Row.object_type', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code_line_number', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.Row.code_line_number', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code_line', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.Row.code_line', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_name', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.Row.object_name', index=4,
      number=10004, type=11, cpp_type=10, label=1,
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
  serialized_start=1052,
  serialized_end=1278,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.mi_SearchSourceCode_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.mi_SearchSourceCode_Ad.Response.row', index=2,
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
  serialized_start=875,
  serialized_end=1278,
)

_PARAMETERS.fields_by_name['search_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['case_sensitive'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['do_not_search_in_comment_part'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['search_only_this_object_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['search_only_object_type'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['get_distinct_object_names_only'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['search_objects_with_name_like'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['object_type'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['code_line_number'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['code_line'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['object_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.mi_SearchSourceCode_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.mi_SearchSourceCode_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.mi_SearchSourceCode_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.mi_SearchSourceCode_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.mi_SearchSourceCode_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.mi_SearchSourceCode_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ8gosdk.dstore.de/engine/procedures/mi_SearchSourceCode_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
