# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_ModifyForumsInCategories_Ad.proto

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
  name='dstore/engine/procedures/fo_ModifyForumsInCategories_Ad.proto',
  package='dstore.engine.fo_ModifyForumsInCategories_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/fo_ModifyForumsInCategories_Ad.proto\x12,dstore.engine.fo_ModifyForumsInCategories_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xec\x02\n\nParameters\x12\x36\n\x11\x66orum_category_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1f\n\x16\x66orum_category_id_null\x18\xe9\x07 \x01(\x08\x12-\n\x08\x66orum_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x16\n\rforum_id_null\x18\xea\x07 \x01(\x08\x12\x31\n\x0cmove_sort_no\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1a\n\x11move_sort_no_null\x18\xeb\x07 \x01(\x08\x12\x42\n\x1dremove_forum_id_from_category\x18\x04 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12+\n\"remove_forum_id_from_category_null\x18\xec\x07 \x01(\x08\"\xe6\x01\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.fo_ModifyForumsInCategories_Ad.Response.Row\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/fo_ModifyForumsInCategories_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forum_category_id', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.forum_category_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_category_id_null', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.forum_category_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.forum_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id_null', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.forum_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_sort_no', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.move_sort_no', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_sort_no_null', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.move_sort_no_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remove_forum_id_from_category', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.remove_forum_id_from_category', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='remove_forum_id_from_category_null', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters.remove_forum_id_from_category_null', index=7,
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
  serialized_start=199,
  serialized_end=563,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Response.Row.row_id', index=0,
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
  serialized_start=774,
  serialized_end=796,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_ModifyForumsInCategories_Ad.Response.row', index=2,
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
  serialized_start=566,
  serialized_end=796,
)

_PARAMETERS.fields_by_name['forum_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['move_sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['remove_forum_id_from_category'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_ModifyForumsInCategories_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_ModifyForumsInCategories_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_ModifyForumsInCategories_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_ModifyForumsInCategories_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_ModifyForumsInCategories_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_ModifyForumsInCategories_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/fo_ModifyForumsInCategories_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)