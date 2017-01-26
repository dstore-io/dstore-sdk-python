# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/st_GetDSS_Index_Trend_Ad.proto

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
  name='dstore/engine/procedures/st_GetDSS_Index_Trend_Ad.proto',
  package='dstore.engine.st_GetDSS_Index_Trend_Ad',
  syntax='proto3',
  serialized_pb=_b('\n7dstore/engine/procedures/st_GetDSS_Index_Trend_Ad.proto\x12&dstore.engine.st_GetDSS_Index_Trend_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xe0\n\n\nParameters\x12\x38\n\x13\x64omain_tree_node_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12!\n\x18\x64omain_tree_node_id_null\x18\xe9\x07 \x01(\x08\x12/\n\nintervalls\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0fintervalls_null\x18\xea\x07 \x01(\x08\x12:\n\x15minutes_per_intervall\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12#\n\x1aminutes_per_intervall_null\x18\xeb\x07 \x01(\x08\x12<\n\x17group_by_nodes_on_level\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12%\n\x1cgroup_by_nodes_on_level_null\x18\xec\x07 \x01(\x08\x12\x30\n\x0bis_level_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x19\n\x10is_level_id_null\x18\xed\x07 \x01(\x08\x12\x44\n\x1fgroup_by_node_characteristic_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n$group_by_node_characteristic_id_null\x18\xee\x07 \x01(\x08\x12:\n\x15only_values_in_one_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12#\n\x1aonly_values_in_one_id_null\x18\xef\x07 \x01(\x08\x12\x44\n\x1fids_in_one_id_are_tree_node_ids\x18\x08 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12-\n$ids_in_one_id_are_tree_node_ids_null\x18\xf0\x07 \x01(\x08\x12\x31\n\x0cweight_views\x18\t \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x1a\n\x11weight_views_null\x18\xf1\x07 \x01(\x08\x12;\n\x16weight_buying_interest\x18\n \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12$\n\x1bweight_buying_interest_null\x18\xf2\x07 \x01(\x08\x12\x31\n\x0cweight_order\x18\x0b \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x1a\n\x11weight_order_null\x18\xf3\x07 \x01(\x08\x12>\n\x19include_deactivated_nodes\x18\x0c \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\'\n\x1einclude_deactivated_nodes_null\x18\xf4\x07 \x01(\x08\x12G\n\"include_nodes_without_tree_node_id\x18\r \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x30\n\'include_nodes_without_tree_node_id_null\x18\xf5\x07 \x01(\x08\x12>\n\x19order_result_by_intervall\x18\x0e \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\'\n\x1eorder_result_by_intervall_null\x18\xf6\x07 \x01(\x08\"\xe7\x04\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x41\n\x03row\x18\x04 \x03(\x0b\x32\x34.dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row\x1a\xb4\x03\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x37\n\x0fintervall_start\x18\x91N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12,\n\x06orders\x18\x92N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x31\n\x0bv_b_o_index\x18\x93N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x31\n\x0btrend_of_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12+\n\x05views\x18\x95N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x39\n\x14trend_of_description\x18\x96N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12/\n\tintervall\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x36\n\x10\x62uying_interests\x18\x98N \x01(\x0b\x32\x1b.dstore.values.DecimalValueBY\n\x1bio.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/st_GetDSS_Index_Trend_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain_tree_node_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.domain_tree_node_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_tree_node_id_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.domain_tree_node_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intervalls', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.intervalls', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intervalls_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.intervalls_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minutes_per_intervall', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.minutes_per_intervall', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='minutes_per_intervall_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.minutes_per_intervall_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_by_nodes_on_level', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.group_by_nodes_on_level', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_by_nodes_on_level_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.group_by_nodes_on_level_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_level_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.is_level_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_level_id_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.is_level_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_by_node_characteristic_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.group_by_node_characteristic_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_by_node_characteristic_id_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.group_by_node_characteristic_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_values_in_one_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.only_values_in_one_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_values_in_one_id_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.only_values_in_one_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids_in_one_id_are_tree_node_ids', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.ids_in_one_id_are_tree_node_ids', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ids_in_one_id_are_tree_node_ids_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.ids_in_one_id_are_tree_node_ids_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_views', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.weight_views', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_views_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.weight_views_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_buying_interest', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.weight_buying_interest', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_buying_interest_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.weight_buying_interest_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_order', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.weight_order', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_order_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.weight_order_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_deactivated_nodes', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.include_deactivated_nodes', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_deactivated_nodes_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.include_deactivated_nodes_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_nodes_without_tree_node_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.include_nodes_without_tree_node_id', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_nodes_without_tree_node_id_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.include_nodes_without_tree_node_id_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_result_by_intervall', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.order_result_by_intervall', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_result_by_intervall_null', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters.order_result_by_intervall_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
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
  serialized_end=1525,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intervall_start', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.intervall_start', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='orders', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.orders', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_b_o_index', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.v_b_o_index', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trend_of_id', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.trend_of_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='views', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.views', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trend_of_description', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.trend_of_description', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='intervall', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.intervall', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='buying_interests', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row.buying_interests', index=8,
      number=10008, type=11, cpp_type=10, label=1,
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
  serialized_start=1707,
  serialized_end=2143,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.st_GetDSS_Index_Trend_Ad.Response.row', index=2,
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
  serialized_start=1528,
  serialized_end=2143,
)

_PARAMETERS.fields_by_name['domain_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['intervalls'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['minutes_per_intervall'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['group_by_nodes_on_level'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['is_level_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['group_by_node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['only_values_in_one_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['ids_in_one_id_are_tree_node_ids'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['weight_views'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['weight_buying_interest'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['weight_order'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['include_deactivated_nodes'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['include_nodes_without_tree_node_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['order_result_by_intervall'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['intervall_start'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['orders'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['v_b_o_index'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['trend_of_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['views'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['trend_of_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['intervall'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['buying_interests'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.st_GetDSS_Index_Trend_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.st_GetDSS_Index_Trend_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.st_GetDSS_Index_Trend_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.st_GetDSS_Index_Trend_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.st_GetDSS_Index_Trend_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.st_GetDSS_Index_Trend_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/st_GetDSS_Index_Trend_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
