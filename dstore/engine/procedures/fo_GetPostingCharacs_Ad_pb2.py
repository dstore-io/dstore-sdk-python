# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_GetPostingCharacs_Ad.proto

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
  name='dstore/engine/procedures/fo_GetPostingCharacs_Ad.proto',
  package='dstore.engine.fo_GetPostingCharacs_Ad',
  syntax='proto3',
  serialized_pb=_b('\n6dstore/engine/procedures/fo_GetPostingCharacs_Ad.proto\x12%dstore.engine.fo_GetPostingCharacs_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xd2\x03\n\nParameters\x12>\n\x19posting_characteristic_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\'\n\x1eposting_characteristic_id_null\x18\xe9\x07 \x01(\x08\x12\x46\n!get_assigned_forums_or_categories\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12/\n&get_assigned_forums_or_categories_null\x18\xea\x07 \x01(\x08\x12\x41\n\x1c\x63haracs_assigned_to_forum_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12*\n!characs_assigned_to_forum_id_null\x18\xeb\x07 \x01(\x08\x12\x44\n\x1f\x63haracs_assigned_to_category_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n$characs_assigned_to_category_id_null\x18\xec\x07 \x01(\x08\"\xd8\t\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12@\n\x03row\x18\x04 \x03(\x0b\x32\x33.dstore.engine.fo_GetPostingCharacs_Ad.Response.Row\x1a\xa6\x08\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12?\n\x1a\x63haracteristic_description\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x33\n\rfield_type_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x19posting_characteristic_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x35\n\x0fprecision_value\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12;\n\x15\x63ommon_characteristic\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x30\n\nmax_length\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x37\n\x11predefined_values\x18\x97N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12>\n\x18\x63heck_posting_visibility\x18\x98N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12+\n\x06\x66ormat\x18\x99N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x10\x62\x61sic_field_type\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12;\n\x16\x66ield_type_description\x18\x9bN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x39\n\x13\x62\x61sic_field_type_id\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x43\n\x1dproperty_modification_allowed\x18\x9dN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12>\n\x18max_number_of_properties\x18\x9eN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12/\n\x08\x66orum_id\x18\xc3\xb8\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x30\n\nforum_name\x18\xc4\xb8\x02 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x38\n\x11\x66orum_category_id\x18\xdb\x86\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12:\n\x14\x63\x61tegory_description\x18\xde\x86\x03 \x01(\x0b\x32\x1a.dstore.values.StringValueBX\n\x1bio.dstore.engine.proceduresZ9gosdk.dstore.de/engine/procedures/fo_GetPostingCharacs_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='posting_characteristic_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.posting_characteristic_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_characteristic_id_null', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.posting_characteristic_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_assigned_forums_or_categories', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.get_assigned_forums_or_categories', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_assigned_forums_or_categories_null', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.get_assigned_forums_or_categories_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characs_assigned_to_forum_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.characs_assigned_to_forum_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characs_assigned_to_forum_id_null', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.characs_assigned_to_forum_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characs_assigned_to_category_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.characs_assigned_to_category_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characs_assigned_to_category_id_null', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Parameters.characs_assigned_to_category_id_null', index=7,
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
  serialized_end=613,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_description', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.characteristic_description', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.field_type_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_characteristic_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.posting_characteristic_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precision_value', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.precision_value', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='common_characteristic', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.common_characteristic', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_length', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.max_length', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predefined_values', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.predefined_values', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_posting_visibility', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.check_posting_visibility', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='format', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.format', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_field_type', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.basic_field_type', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type_description', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.field_type_description', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_field_type_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.basic_field_type_id', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property_modification_allowed', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.property_modification_allowed', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_properties', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.max_number_of_properties', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.forum_id', index=15,
      number=40003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_name', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.forum_name', index=16,
      number=40004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_category_id', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.forum_category_id', index=17,
      number=50011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category_description', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.Row.category_description', index=18,
      number=50014, type=11, cpp_type=10, label=1,
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
  serialized_start=794,
  serialized_end=1856,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_GetPostingCharacs_Ad.Response.row', index=2,
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
  serialized_start=616,
  serialized_end=1856,
)

_PARAMETERS.fields_by_name['posting_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_assigned_forums_or_categories'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['characs_assigned_to_forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['characs_assigned_to_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['characteristic_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['field_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['posting_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['precision_value'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['common_characteristic'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['max_length'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['predefined_values'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['check_posting_visibility'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['format'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['basic_field_type'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['field_type_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['basic_field_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['property_modification_allowed'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['max_number_of_properties'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['forum_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['forum_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['category_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_GetPostingCharacs_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetPostingCharacs_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_GetPostingCharacs_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetPostingCharacs_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_GetPostingCharacs_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetPostingCharacs_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ9gosdk.dstore.de/engine/procedures/fo_GetPostingCharacs_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
