# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_GetPostingBinaries_Pu.proto

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
  name='dstore/engine/procedures/fo_GetPostingBinaries_Pu.proto',
  package='dstore.engine.fo_GetPostingBinaries_Pu',
  syntax='proto3',
  serialized_pb=_b('\n7dstore/engine/procedures/fo_GetPostingBinaries_Pu.proto\x12&dstore.engine.fo_GetPostingBinaries_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xce\x05\n\nParameters\x12@\n\x1cperson_identification_values\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n!person_identification_values_null\x18\xe9\x07 \x01(\x08\x12\x33\n\x0eperson_type_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13person_type_id_null\x18\xea\x07 \x01(\x08\x12-\n\tunique_id\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xeb\x07 \x01(\x08\x12/\n\nposting_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0fposting_id_null\x18\xec\x07 \x01(\x08\x12,\n\x07sort_no\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x15\n\x0csort_no_null\x18\xed\x07 \x01(\x08\x12\x38\n\x13include_binary_code\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12!\n\x18include_binary_code_null\x18\xee\x07 \x01(\x08\x12=\n\x19posting_binary_identifier\x18\x07 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\'\n\x1eposting_binary_identifier_null\x18\xef\x07 \x01(\x08\x12;\n\x17separator_in_ident_vals\x18\x08 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12%\n\x1cseparator_in_ident_vals_null\x18\xf0\x07 \x01(\x08\"\xc7\x05\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x41\n\x03row\x18\x04 \x03(\x0b\x32\x34.dstore.engine.fo_GetPostingBinaries_Pu.Response.Row\x1a\x94\x04\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x30\n\x0b\x64\x65scription\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\x0c\x63ontent_type\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12>\n\x19posting_binary_identifier\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x08\x66ilename\x18\x94N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0f\x66ilesize_in_k_b\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12H\n#last_modified_at_date_and_time_char\x18\x96N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x07sort_no\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x46\n\x1elast_modified_at_date_and_time\x18\x98N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x30\n\x0b\x62inary_code\x18\xa9\x9c\x01 \x01(\x0b\x32\x19.dstore.values.BytesValueBY\n\x1bio.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/fo_GetPostingBinaries_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_identification_values', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.person_identification_values', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_identification_values_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.person_identification_values_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.person_type_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.person_type_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.unique_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.unique_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_id', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.posting_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_id_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.posting_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.sort_no', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.sort_no_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_binary_code', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.include_binary_code', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_binary_code_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.include_binary_code_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_binary_identifier', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.posting_binary_identifier', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_binary_identifier_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.posting_binary_identifier_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.separator_in_ident_vals', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals_null', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Parameters.separator_in_ident_vals_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
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
  serialized_start=149,
  serialized_end=867,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.description', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content_type', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.content_type', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_binary_identifier', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.posting_binary_identifier', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filename', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.filename', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filesize_in_k_b', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.filesize_in_k_b', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_at_date_and_time_char', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.last_modified_at_date_and_time_char', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.sort_no', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_at_date_and_time', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.last_modified_at_date_and_time', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_code', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.Row.binary_code', index=9,
      number=20009, type=11, cpp_type=10, label=1,
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
  serialized_start=1049,
  serialized_end=1581,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_GetPostingBinaries_Pu.Response.row', index=2,
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
  serialized_start=870,
  serialized_end=1581,
)

_PARAMETERS.fields_by_name['person_identification_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['posting_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['include_binary_code'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['posting_binary_identifier'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['separator_in_ident_vals'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['content_type'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['posting_binary_identifier'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['filename'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['filesize_in_k_b'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['last_modified_at_date_and_time_char'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['last_modified_at_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['binary_code'].message_type = dstore_dot_values__pb2._BYTESVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_GetPostingBinaries_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetPostingBinaries_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_GetPostingBinaries_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetPostingBinaries_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_GetPostingBinaries_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetPostingBinaries_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/fo_GetPostingBinaries_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
