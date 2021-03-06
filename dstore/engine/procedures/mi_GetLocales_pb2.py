# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/mi_GetLocales.proto

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
  name='dstore/engine/procedures/mi_GetLocales.proto',
  package='dstore.engine.mi_GetLocales',
  syntax='proto3',
  serialized_pb=_b('\n,dstore/engine/procedures/mi_GetLocales.proto\x12\x1b\x64store.engine.mi_GetLocales\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\x8b\x02\n\nParameters\x12/\n\ncountry_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0f\x63ountry_id_null\x18\xe9\x07 \x01(\x08\x12\x30\n\x0blanguage_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10language_id_null\x18\xea\x07 \x01(\x08\x12=\n\x18get_names_in_language_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12&\n\x1dget_names_in_language_id_null\x18\xeb\x07 \x01(\x08\"\xb6\x06\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x36\n\x03row\x18\x04 \x03(\x0b\x32).dstore.engine.mi_GetLocales.Response.Row\x1a\x8e\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x30\n\ncountry_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x38\n\x13\x63ountry_description\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x34\n\x0flanguage_symbol\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12/\n\tlocale_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x44\n\x1f\x63ountry_descr_in_given_language\x18\x95N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x08language\x18\x96N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12@\n\x1blanguage_in_locale_language\x18\x97N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12?\n\x1alanguage_in_given_language\x18\x98N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\x0c\x63ountry_code\x18\x99N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x45\n country_descr_in_locale_language\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\x0blanguage_id\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.IntegerValueBN\n\x1bio.dstore.engine.proceduresZ/gosdk.dstore.de/engine/procedures/mi_GetLocalesb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.mi_GetLocales.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='country_id', full_name='dstore.engine.mi_GetLocales.Parameters.country_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_id_null', full_name='dstore.engine.mi_GetLocales.Parameters.country_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.mi_GetLocales.Parameters.language_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id_null', full_name='dstore.engine.mi_GetLocales.Parameters.language_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_names_in_language_id', full_name='dstore.engine.mi_GetLocales.Parameters.get_names_in_language_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_names_in_language_id_null', full_name='dstore.engine.mi_GetLocales.Parameters.get_names_in_language_id_null', index=5,
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
  serialized_start=127,
  serialized_end=394,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.mi_GetLocales.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.mi_GetLocales.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_id', full_name='dstore.engine.mi_GetLocales.Response.Row.country_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_description', full_name='dstore.engine.mi_GetLocales.Response.Row.country_description', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_symbol', full_name='dstore.engine.mi_GetLocales.Response.Row.language_symbol', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='locale_id', full_name='dstore.engine.mi_GetLocales.Response.Row.locale_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_descr_in_given_language', full_name='dstore.engine.mi_GetLocales.Response.Row.country_descr_in_given_language', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language', full_name='dstore.engine.mi_GetLocales.Response.Row.language', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_in_locale_language', full_name='dstore.engine.mi_GetLocales.Response.Row.language_in_locale_language', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_in_given_language', full_name='dstore.engine.mi_GetLocales.Response.Row.language_in_given_language', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='dstore.engine.mi_GetLocales.Response.Row.country_code', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_descr_in_locale_language', full_name='dstore.engine.mi_GetLocales.Response.Row.country_descr_in_locale_language', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.mi_GetLocales.Response.Row.language_id', index=11,
      number=10011, type=11, cpp_type=10, label=1,
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
  serialized_start=565,
  serialized_end=1219,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.mi_GetLocales.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.mi_GetLocales.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.mi_GetLocales.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.mi_GetLocales.Response.row', index=2,
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
  serialized_start=397,
  serialized_end=1219,
)

_PARAMETERS.fields_by_name['country_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_names_in_language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['country_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['country_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['language_symbol'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['locale_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['country_descr_in_given_language'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['language'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['language_in_locale_language'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['language_in_given_language'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['country_code'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['country_descr_in_locale_language'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.mi_GetLocales_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.mi_GetLocales.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.mi_GetLocales_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.mi_GetLocales.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.mi_GetLocales_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.mi_GetLocales.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ/gosdk.dstore.de/engine/procedures/mi_GetLocales'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
