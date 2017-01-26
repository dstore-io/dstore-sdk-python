# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/st_GetDirectSuccessors_Tree_Ad.proto

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
  name='dstore/engine/procedures/st_GetDirectSuccessors_Tree_Ad.proto',
  package='dstore.engine.st_GetDirectSuccessors_Tree_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/st_GetDirectSuccessors_Tree_Ad.proto\x12,dstore.engine.st_GetDirectSuccessors_Tree_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xcf\x08\n\nParameters\x12\x33\n\x0eh_tree_node_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13h_tree_node_id_null\x18\xe9\x07 \x01(\x08\x12\x30\n\tfrom_date\x18\x02 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x17\n\x0e\x66rom_date_null\x18\xea\x07 \x01(\x08\x12.\n\x07to_date\x18\x03 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x15\n\x0cto_date_null\x18\xeb\x07 \x01(\x08\x12=\n\x18\x62\x61sic_characteristic_no1\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12&\n\x1d\x62\x61sic_characteristic_no1_null\x18\xec\x07 \x01(\x08\x12\x44\n\x1fweight_basic_characteristic_no1\x18\x05 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12-\n$weight_basic_characteristic_no1_null\x18\xed\x07 \x01(\x08\x12=\n\x18\x62\x61sic_characteristic_no2\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12&\n\x1d\x62\x61sic_characteristic_no2_null\x18\xee\x07 \x01(\x08\x12\x44\n\x1fweight_basic_characteristic_no2\x18\x07 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12-\n$weight_basic_characteristic_no2_null\x18\xef\x07 \x01(\x08\x12=\n\x18\x62\x61sic_characteristic_no3\x18\x08 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12&\n\x1d\x62\x61sic_characteristic_no3_null\x18\xf0\x07 \x01(\x08\x12\x44\n\x1fweight_basic_characteristic_no3\x18\t \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12-\n$weight_basic_characteristic_no3_null\x18\xf1\x07 \x01(\x08\x12@\n\x1bsource_table_for_statistics\x18\n \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12)\n source_table_for_statistics_null\x18\xf2\x07 \x01(\x08\x12\x38\n\x13\x64isplay_only_active\x18\x0b \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12!\n\x18\x64isplay_only_active_null\x18\xf3\x07 \x01(\x08\"\x86\x0c\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row\x1a\xcd\n\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x30\n\ntree_level\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x31\n\x0bpredecessor\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\x08level_no\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x45\n\x1frelative_value_basic_charac_no3\x18\x94N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x45\n\x1frelative_value_basic_charac_no2\x18\x95N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x45\n\x1frelative_value_basic_charac_no1\x18\x96N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x37\n\x11total_value_index\x18\x97N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12:\n\x14relative_value_index\x18\x98N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x35\n\x10node_description\x18\x99N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12,\n\x06\x61\x63tive\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x36\n\x10has_next_sibling\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x42\n\x1ctotal_value_basic_charac_no1\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x34\n\x0eh_tree_node_id\x18\x9dN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x42\n\x1ctotal_value_basic_charac_no2\x18\x9eN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x42\n\x1ctotal_value_basic_charac_no3\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12H\n\"max_relative_value_per_predecessor\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x32\n\x0ctree_node_id\x18\xa1N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07node_id\x18\xa2N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12G\n!max_relative_value_index_per_pred\x18\xa3N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12.\n\tfrom_date\x18\xa4N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12,\n\x07to_date\x18\xa5N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x34\n\x0ehas_successors\x18\xa6N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12-\n\x07\x64\x65leted\x18\xa7N \x01(\x0b\x32\x1b.dstore.values.BooleanValueB_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/st_GetDirectSuccessors_Tree_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='h_tree_node_id', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.h_tree_node_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_id_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.h_tree_node_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.from_date', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.from_date_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.to_date', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.to_date_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_no1', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.basic_characteristic_no1', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_no1_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.basic_characteristic_no1_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_basic_characteristic_no1', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.weight_basic_characteristic_no1', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_basic_characteristic_no1_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.weight_basic_characteristic_no1_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_no2', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.basic_characteristic_no2', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_no2_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.basic_characteristic_no2_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_basic_characteristic_no2', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.weight_basic_characteristic_no2', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_basic_characteristic_no2_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.weight_basic_characteristic_no2_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_no3', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.basic_characteristic_no3', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='basic_characteristic_no3_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.basic_characteristic_no3_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_basic_characteristic_no3', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.weight_basic_characteristic_no3', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_basic_characteristic_no3_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.weight_basic_characteristic_no3_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_table_for_statistics', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.source_table_for_statistics', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_table_for_statistics_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.source_table_for_statistics_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_only_active', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.display_only_active', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='display_only_active_null', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters.display_only_active_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
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
  serialized_start=161,
  serialized_end=1264,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_level', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.tree_level', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predecessor', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.predecessor', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_no', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.level_no', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_value_basic_charac_no3', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.relative_value_basic_charac_no3', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_value_basic_charac_no2', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.relative_value_basic_charac_no2', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_value_basic_charac_no1', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.relative_value_basic_charac_no1', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_value_index', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.total_value_index', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_value_index', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.relative_value_index', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_description', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.node_description', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.active', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_next_sibling', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.has_next_sibling', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_value_basic_charac_no1', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.total_value_basic_charac_no1', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_id', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.h_tree_node_id', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_value_basic_charac_no2', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.total_value_basic_charac_no2', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_value_basic_charac_no3', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.total_value_basic_charac_no3', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_relative_value_per_predecessor', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.max_relative_value_per_predecessor', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.tree_node_id', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.node_id', index=18,
      number=10018, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_relative_value_index_per_pred', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.max_relative_value_index_per_pred', index=19,
      number=10019, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.from_date', index=20,
      number=10020, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.to_date', index=21,
      number=10021, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_successors', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.has_successors', index=22,
      number=10022, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row.deleted', index=23,
      number=10023, type=11, cpp_type=10, label=1,
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
  serialized_start=1452,
  serialized_end=2809,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.row', index=2,
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
  serialized_start=1267,
  serialized_end=2809,
)

_PARAMETERS.fields_by_name['h_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['from_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['to_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['basic_characteristic_no1'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['weight_basic_characteristic_no1'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['basic_characteristic_no2'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['weight_basic_characteristic_no2'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['basic_characteristic_no3'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['weight_basic_characteristic_no3'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['source_table_for_statistics'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['display_only_active'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['tree_level'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['predecessor'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['level_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['relative_value_basic_charac_no3'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['relative_value_basic_charac_no2'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['relative_value_basic_charac_no1'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['total_value_index'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['relative_value_index'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['node_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['active'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['has_next_sibling'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['total_value_basic_charac_no1'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['h_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['total_value_basic_charac_no2'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['total_value_basic_charac_no3'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['max_relative_value_per_predecessor'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['max_relative_value_index_per_pred'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['from_date'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['to_date'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['has_successors'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['deleted'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.st_GetDirectSuccessors_Tree_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.st_GetDirectSuccessors_Tree_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.st_GetDirectSuccessors_Tree_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.st_GetDirectSuccessors_Tree_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.st_GetDirectSuccessors_Tree_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/st_GetDirectSuccessors_Tree_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
