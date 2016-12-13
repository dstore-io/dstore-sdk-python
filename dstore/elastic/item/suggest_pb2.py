# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/elastic/item/suggest.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dstore.elastic import elastic_pb2 as dstore_dot_elastic_dot_elastic__pb2
from dstore.elastic.item import item_pb2 as dstore_dot_elastic_dot_item_dot_item__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dstore/elastic/item/suggest.proto',
  package='dstore.elastic.suggest',
  syntax='proto3',
  serialized_pb=_b('\n!dstore/elastic/item/suggest.proto\x12\x16\x64store.elastic.suggest\x1a\x1c\x64store/elastic/elastic.proto\x1a\x1e\x64store/elastic/item/item.proto\"\xad\x01\n\x07Request\x12\r\n\x05input\x18\x01 \x01(\t\x12\x12\n\nfield_name\x18\x02 \x03(\t\x12-\n\nbase_query\x18\x03 \x01(\x0b\x32\x19.dstore.elastic.BoolQuery\x12\x11\n\tmax_items\x18\x05 \x01(\x05\x12\x14\n\x0cmax_suggests\x18\x06 \x01(\x05\x12\r\n\x05\x66uzzy\x18\x07 \x01(\x08\x12\x18\n\x10use_and_operator\x18\x08 \x01(\x08\"\xdb\x01\n\x08Response\x12?\n\nsuggestion\x18\x02 \x03(\x0b\x32+.dstore.elastic.suggest.Response.Suggestion\x12\x30\n\rmatching_item\x18\x03 \x03(\x0b\x32\x19.dstore.elastic.item.Item\x12\x1c\n\x14\x65lastic_query_string\x18\x05 \x01(\t\x1a>\n\nSuggestion\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12\r\n\x05\x63ount\x18\x02 \x01(\x05\x12\r\n\x05value\x18\x03 \x01(\tBG\n\x16io.dstore.elastic.itemB\x07SuggestZ$gosdk.dstore.de/elastic/item/suggestb\x06proto3')
  ,
  dependencies=[dstore_dot_elastic_dot_elastic__pb2.DESCRIPTOR,dstore_dot_elastic_dot_item_dot_item__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='dstore.elastic.suggest.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='input', full_name='dstore.elastic.suggest.Request.input', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_name', full_name='dstore.elastic.suggest.Request.field_name', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_query', full_name='dstore.elastic.suggest.Request.base_query', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_items', full_name='dstore.elastic.suggest.Request.max_items', index=3,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_suggests', full_name='dstore.elastic.suggest.Request.max_suggests', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fuzzy', full_name='dstore.elastic.suggest.Request.fuzzy', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_and_operator', full_name='dstore.elastic.suggest.Request.use_and_operator', index=6,
      number=8, type=8, cpp_type=7, label=1,
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
  serialized_start=124,
  serialized_end=297,
)


_RESPONSE_SUGGESTION = _descriptor.Descriptor(
  name='Suggestion',
  full_name='dstore.elastic.suggest.Response.Suggestion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_name', full_name='dstore.elastic.suggest.Response.Suggestion.field_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='dstore.elastic.suggest.Response.Suggestion.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.elastic.suggest.Response.Suggestion.value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=457,
  serialized_end=519,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.elastic.suggest.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='suggestion', full_name='dstore.elastic.suggest.Response.suggestion', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='matching_item', full_name='dstore.elastic.suggest.Response.matching_item', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elastic_query_string', full_name='dstore.elastic.suggest.Response.elastic_query_string', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSE_SUGGESTION, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=519,
)

_REQUEST.fields_by_name['base_query'].message_type = dstore_dot_elastic_dot_elastic__pb2._BOOLQUERY
_RESPONSE_SUGGESTION.containing_type = _RESPONSE
_RESPONSE.fields_by_name['suggestion'].message_type = _RESPONSE_SUGGESTION
_RESPONSE.fields_by_name['matching_item'].message_type = dstore_dot_elastic_dot_item_dot_item__pb2._ITEM
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'dstore.elastic.item.suggest_pb2'
  # @@protoc_insertion_point(class_scope:dstore.elastic.suggest.Request)
  ))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Suggestion = _reflection.GeneratedProtocolMessageType('Suggestion', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_SUGGESTION,
    __module__ = 'dstore.elastic.item.suggest_pb2'
    # @@protoc_insertion_point(class_scope:dstore.elastic.suggest.Response.Suggestion)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.elastic.item.suggest_pb2'
  # @@protoc_insertion_point(class_scope:dstore.elastic.suggest.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Suggestion)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026io.dstore.elastic.itemB\007SuggestZ$gosdk.dstore.de/elastic/item/suggest'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
