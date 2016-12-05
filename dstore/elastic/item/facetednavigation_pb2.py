# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/elastic/item/facetednavigation.proto

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
  name='dstore/elastic/item/facetednavigation.proto',
  package='dstore.elastic.facetednavigation',
  syntax='proto3',
  serialized_pb=_b('\n+dstore/elastic/item/facetednavigation.proto\x12 dstore.elastic.facetednavigation\x1a\x1c\x64store/elastic/elastic.proto\x1a\x1e\x64store/elastic/item/item.proto\"\xb1\x07\n\x07Request\x12-\n\nbase_query\x18\x01 \x01(\x0b\x32\x19.dstore.elastic.BoolQuery\x12-\n\npost_query\x18\x02 \x01(\x0b\x32\x19.dstore.elastic.BoolQuery\x12>\n\x05\x66\x61\x63\x65t\x18\x03 \x03(\x0b\x32/.dstore.elastic.facetednavigation.Request.Facet\x12I\n\x0brange_facet\x18\x05 \x03(\x0b\x32\x34.dstore.elastic.facetednavigation.Request.RangeFacet\x12N\n\x10\x64\x61te_range_facet\x18\x06 \x03(\x0b\x32\x34.dstore.elastic.facetednavigation.Request.RangeFacet\x12\x1c\n\x14onlyMatchingVariants\x18\x07 \x01(\x08\x12\x0c\n\x04\x66rom\x18\n \x01(\x05\x12\x0c\n\x04size\x18\x0b \x01(\x05\x12\x1d\n\x15include_field_pattern\x18\x0f \x03(\t\x12\x1d\n\x15\x65xclude_field_pattern\x18\x10 \x03(\t\x12\"\n\x04sort\x18\x14 \x03(\x0b\x32\x14.dstore.elastic.Sort\x1a\x46\n\nRangeFacet\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12$\n\x05range\x18\x02 \x03(\x0b\x32\x15.dstore.elastic.Range\x1a\x88\x03\n\x05\x46\x61\x63\x65t\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12R\n\x0csort_no_sort\x18\x02 \x01(\x0b\x32:.dstore.elastic.facetednavigation.Request.Facet.SortNoSortH\x00\x12O\n\nfield_sort\x18\x03 \x01(\x0b\x32\x39.dstore.elastic.facetednavigation.Request.Facet.FieldSortH\x00\x1a<\n\nSortNoSort\x12.\n\nsort_order\x18\x01 \x01(\x0e\x32\x1a.dstore.elastic.Sort.Order\x1a}\n\tFieldSort\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12.\n\nsort_order\x18\x02 \x01(\x0e\x32\x1a.dstore.elastic.Sort.Order\x12,\n\tsort_mode\x18\x03 \x01(\x0e\x32\x19.dstore.elastic.Sort.ModeB\t\n\x07sort_by\"\x90\x01\n\x08Response\x12\x12\n\ntotal_hits\x18\x02 \x01(\x05\x12\'\n\x04item\x18\x03 \x03(\x0b\x32\x19.dstore.elastic.item.Item\x12)\n\x05\x66\x61\x63\x65t\x18\x04 \x03(\x0b\x32\x1a.dstore.elastic.item.Facet\x12\x1c\n\x14\x65lastic_query_string\x18\x05 \x01(\tB\\\n\x16io.dstore.elastic.itemB\x11\x46\x61\x63\x65tedNavigationZ/gosdk.dstore.de/elastic/item/faceted_navigationb\x06proto3')
  ,
  dependencies=[dstore_dot_elastic_dot_elastic__pb2.DESCRIPTOR,dstore_dot_elastic_dot_item_dot_item__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_REQUEST_RANGEFACET = _descriptor.Descriptor(
  name='RangeFacet',
  full_name='dstore.elastic.facetednavigation.Request.RangeFacet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_name', full_name='dstore.elastic.facetednavigation.Request.RangeFacet.field_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range', full_name='dstore.elastic.facetednavigation.Request.RangeFacet.range', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=624,
  serialized_end=694,
)

_REQUEST_FACET_SORTNOSORT = _descriptor.Descriptor(
  name='SortNoSort',
  full_name='dstore.elastic.facetednavigation.Request.Facet.SortNoSort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='dstore.elastic.facetednavigation.Request.Facet.SortNoSort.sort_order', index=0,
      number=1, type=14, cpp_type=8, label=1,
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
  serialized_start=891,
  serialized_end=951,
)

_REQUEST_FACET_FIELDSORT = _descriptor.Descriptor(
  name='FieldSort',
  full_name='dstore.elastic.facetednavigation.Request.Facet.FieldSort',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_name', full_name='dstore.elastic.facetednavigation.Request.Facet.FieldSort.field_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='dstore.elastic.facetednavigation.Request.Facet.FieldSort.sort_order', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_mode', full_name='dstore.elastic.facetednavigation.Request.Facet.FieldSort.sort_mode', index=2,
      number=3, type=14, cpp_type=8, label=1,
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
  serialized_start=953,
  serialized_end=1078,
)

_REQUEST_FACET = _descriptor.Descriptor(
  name='Facet',
  full_name='dstore.elastic.facetednavigation.Request.Facet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='field_name', full_name='dstore.elastic.facetednavigation.Request.Facet.field_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no_sort', full_name='dstore.elastic.facetednavigation.Request.Facet.sort_no_sort', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_sort', full_name='dstore.elastic.facetednavigation.Request.Facet.field_sort', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_FACET_SORTNOSORT, _REQUEST_FACET_FIELDSORT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='sort_by', full_name='dstore.elastic.facetednavigation.Request.Facet.sort_by',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=697,
  serialized_end=1089,
)

_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='dstore.elastic.facetednavigation.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='base_query', full_name='dstore.elastic.facetednavigation.Request.base_query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_query', full_name='dstore.elastic.facetednavigation.Request.post_query', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facet', full_name='dstore.elastic.facetednavigation.Request.facet', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_facet', full_name='dstore.elastic.facetednavigation.Request.range_facet', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_range_facet', full_name='dstore.elastic.facetednavigation.Request.date_range_facet', index=4,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='onlyMatchingVariants', full_name='dstore.elastic.facetednavigation.Request.onlyMatchingVariants', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from', full_name='dstore.elastic.facetednavigation.Request.from', index=6,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='dstore.elastic.facetednavigation.Request.size', index=7,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_field_pattern', full_name='dstore.elastic.facetednavigation.Request.include_field_pattern', index=8,
      number=15, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='exclude_field_pattern', full_name='dstore.elastic.facetednavigation.Request.exclude_field_pattern', index=9,
      number=16, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort', full_name='dstore.elastic.facetednavigation.Request.sort', index=10,
      number=20, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUEST_RANGEFACET, _REQUEST_FACET, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=144,
  serialized_end=1089,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.elastic.facetednavigation.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_hits', full_name='dstore.elastic.facetednavigation.Response.total_hits', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item', full_name='dstore.elastic.facetednavigation.Response.item', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='facet', full_name='dstore.elastic.facetednavigation.Response.facet', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='elastic_query_string', full_name='dstore.elastic.facetednavigation.Response.elastic_query_string', index=3,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=1092,
  serialized_end=1236,
)

_REQUEST_RANGEFACET.fields_by_name['range'].message_type = dstore_dot_elastic_dot_elastic__pb2._RANGE
_REQUEST_RANGEFACET.containing_type = _REQUEST
_REQUEST_FACET_SORTNOSORT.fields_by_name['sort_order'].enum_type = dstore_dot_elastic_dot_elastic__pb2._SORT_ORDER
_REQUEST_FACET_SORTNOSORT.containing_type = _REQUEST_FACET
_REQUEST_FACET_FIELDSORT.fields_by_name['sort_order'].enum_type = dstore_dot_elastic_dot_elastic__pb2._SORT_ORDER
_REQUEST_FACET_FIELDSORT.fields_by_name['sort_mode'].enum_type = dstore_dot_elastic_dot_elastic__pb2._SORT_MODE
_REQUEST_FACET_FIELDSORT.containing_type = _REQUEST_FACET
_REQUEST_FACET.fields_by_name['sort_no_sort'].message_type = _REQUEST_FACET_SORTNOSORT
_REQUEST_FACET.fields_by_name['field_sort'].message_type = _REQUEST_FACET_FIELDSORT
_REQUEST_FACET.containing_type = _REQUEST
_REQUEST_FACET.oneofs_by_name['sort_by'].fields.append(
  _REQUEST_FACET.fields_by_name['sort_no_sort'])
_REQUEST_FACET.fields_by_name['sort_no_sort'].containing_oneof = _REQUEST_FACET.oneofs_by_name['sort_by']
_REQUEST_FACET.oneofs_by_name['sort_by'].fields.append(
  _REQUEST_FACET.fields_by_name['field_sort'])
_REQUEST_FACET.fields_by_name['field_sort'].containing_oneof = _REQUEST_FACET.oneofs_by_name['sort_by']
_REQUEST.fields_by_name['base_query'].message_type = dstore_dot_elastic_dot_elastic__pb2._BOOLQUERY
_REQUEST.fields_by_name['post_query'].message_type = dstore_dot_elastic_dot_elastic__pb2._BOOLQUERY
_REQUEST.fields_by_name['facet'].message_type = _REQUEST_FACET
_REQUEST.fields_by_name['range_facet'].message_type = _REQUEST_RANGEFACET
_REQUEST.fields_by_name['date_range_facet'].message_type = _REQUEST_RANGEFACET
_REQUEST.fields_by_name['sort'].message_type = dstore_dot_elastic_dot_elastic__pb2._SORT
_RESPONSE.fields_by_name['item'].message_type = dstore_dot_elastic_dot_item_dot_item__pb2._ITEM
_RESPONSE.fields_by_name['facet'].message_type = dstore_dot_elastic_dot_item_dot_item__pb2._FACET
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(

  RangeFacet = _reflection.GeneratedProtocolMessageType('RangeFacet', (_message.Message,), dict(
    DESCRIPTOR = _REQUEST_RANGEFACET,
    __module__ = 'dstore.elastic.item.facetednavigation_pb2'
    # @@protoc_insertion_point(class_scope:dstore.elastic.facetednavigation.Request.RangeFacet)
    ))
  ,

  Facet = _reflection.GeneratedProtocolMessageType('Facet', (_message.Message,), dict(

    SortNoSort = _reflection.GeneratedProtocolMessageType('SortNoSort', (_message.Message,), dict(
      DESCRIPTOR = _REQUEST_FACET_SORTNOSORT,
      __module__ = 'dstore.elastic.item.facetednavigation_pb2'
      # @@protoc_insertion_point(class_scope:dstore.elastic.facetednavigation.Request.Facet.SortNoSort)
      ))
    ,

    FieldSort = _reflection.GeneratedProtocolMessageType('FieldSort', (_message.Message,), dict(
      DESCRIPTOR = _REQUEST_FACET_FIELDSORT,
      __module__ = 'dstore.elastic.item.facetednavigation_pb2'
      # @@protoc_insertion_point(class_scope:dstore.elastic.facetednavigation.Request.Facet.FieldSort)
      ))
    ,
    DESCRIPTOR = _REQUEST_FACET,
    __module__ = 'dstore.elastic.item.facetednavigation_pb2'
    # @@protoc_insertion_point(class_scope:dstore.elastic.facetednavigation.Request.Facet)
    ))
  ,
  DESCRIPTOR = _REQUEST,
  __module__ = 'dstore.elastic.item.facetednavigation_pb2'
  # @@protoc_insertion_point(class_scope:dstore.elastic.facetednavigation.Request)
  ))
_sym_db.RegisterMessage(Request)
_sym_db.RegisterMessage(Request.RangeFacet)
_sym_db.RegisterMessage(Request.Facet)
_sym_db.RegisterMessage(Request.Facet.SortNoSort)
_sym_db.RegisterMessage(Request.Facet.FieldSort)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.elastic.item.facetednavigation_pb2'
  # @@protoc_insertion_point(class_scope:dstore.elastic.facetednavigation.Response)
  ))
_sym_db.RegisterMessage(Response)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\026io.dstore.elastic.itemB\021FacetedNavigationZ/gosdk.dstore.de/elastic/item/faceted_navigation'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
