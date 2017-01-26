# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/im_GetDirectSuccessors_Pu.proto

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
  name='dstore/engine/procedures/im_GetDirectSuccessors_Pu.proto',
  package='dstore.engine.im_GetDirectSuccessors_Pu',
  syntax='proto3',
  serialized_pb=_b('\n8dstore/engine/procedures/im_GetDirectSuccessors_Pu.proto\x12\'dstore.engine.im_GetDirectSuccessors_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xa1\x0c\n\nParameters\x12\x31\n\x0ctree_node_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1a\n\x11tree_node_id_null\x18\xe9\x07 \x01(\x08\x12\x30\n\x0blanguage_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10language_id_null\x18\xea\x07 \x01(\x08\x12?\n\x1agroup_by_characteristic_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12(\n\x1fgroup_by_characteristic_id_null\x18\xeb\x07 \x01(\x08\x12\x43\n\x1e\x62inary_characteristic_value_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12,\n#binary_characteristic_value_id_null\x18\xec\x07 \x01(\x08\x12@\n\x1b\x66ilter_by_characteristic_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12)\n filter_by_characteristic_id_null\x18\xed\x07 \x01(\x08\x12:\n\x16\x66ilter_by_charac_value\x18\x06 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12$\n\x1b\x66ilter_by_charac_value_null\x18\xee\x07 \x01(\x08\x12\x37\n\x12output_into_one_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17output_into_one_id_null\x18\xef\x07 \x01(\x08\x12<\n\x17negate_filter_by_params\x18\x08 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12%\n\x1cnegate_filter_by_params_null\x18\xf0\x07 \x01(\x08\x12\x42\n\x1esort_by_characteristic_id_list\x18\t \x01(\x0b\x32\x1a.dstore.values.StringValue\x12,\n#sort_by_characteristic_id_list_null\x18\xf1\x07 \x01(\x08\x12\x34\n\x10sort_option_list\x18\n \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1e\n\x15sort_option_list_null\x18\xf2\x07 \x01(\x08\x12=\n\x19inherit_depth_option_list\x18\x0b \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\'\n\x1einherit_depth_option_list_null\x18\xf3\x07 \x01(\x08\x12\x44\n recursive_evaluation_option_list\x18\x0c \x01(\x0b\x32\x1a.dstore.values.StringValue\x12.\n%recursive_evaluation_option_list_null\x18\xf4\x07 \x01(\x08\x12\x43\n\x1eget_values_for_sort_by_characs\x18\r \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12,\n#get_values_for_sort_by_characs_null\x18\xf5\x07 \x01(\x08\x12\x34\n\x0f\x66rom_row_number\x18\x0e \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1d\n\x14\x66rom_row_number_null\x18\xf6\x07 \x01(\x08\x12\x38\n\x13max_number_of_nodes\x18\x0f \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12!\n\x18max_number_of_nodes_null\x18\xf7\x07 \x01(\x08\x12*\n\x05\x63ount\x18\x10 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x13\n\ncount_null\x18\xf8\x07 \x01(\x08\"\xc0\x06\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x42\n\x03row\x18\x04 \x03(\x0b\x32\x35.dstore.engine.im_GetDirectSuccessors_Pu.Response.Row\x12*\n\x05\x63ount\x18\x65 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x1a\xe0\x04\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x35\n\x10node_description\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12+\n\x06value2\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12+\n\x06value3\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12+\n\x06value1\x18\x94N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x34\n\x0e\x62inary_code_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07node_id\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0ctree_node_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07sort_no\x18\x98N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\x08level_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12+\n\x05value\x18\xa5\x9c\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x34\n\rvalue_sort_no\x18\xa6\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12/\n\x08value_id\x18\xa7\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValueBZ\n\x1bio.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/im_GetDirectSuccessors_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.tree_node_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.tree_node_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.language_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.language_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_by_characteristic_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.group_by_characteristic_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_by_characteristic_id_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.group_by_characteristic_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_characteristic_value_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.binary_characteristic_value_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_characteristic_value_id_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.binary_characteristic_value_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_characteristic_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.filter_by_characteristic_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_characteristic_id_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.filter_by_characteristic_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_charac_value', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.filter_by_charac_value', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_charac_value_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.filter_by_charac_value_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_one_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.output_into_one_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_one_id_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.output_into_one_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negate_filter_by_params', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.negate_filter_by_params', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negate_filter_by_params_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.negate_filter_by_params_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_by_characteristic_id_list', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.sort_by_characteristic_id_list', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_by_characteristic_id_list_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.sort_by_characteristic_id_list_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_option_list', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.sort_option_list', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_option_list_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.sort_option_list_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inherit_depth_option_list', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.inherit_depth_option_list', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inherit_depth_option_list_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.inherit_depth_option_list_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive_evaluation_option_list', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.recursive_evaluation_option_list', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive_evaluation_option_list_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.recursive_evaluation_option_list_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_values_for_sort_by_characs', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.get_values_for_sort_by_characs', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_values_for_sort_by_characs_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.get_values_for_sort_by_characs_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_row_number', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.from_row_number', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_row_number_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.from_row_number_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_nodes', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.max_number_of_nodes', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_nodes_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.max_number_of_nodes_null', index=29,
      number=1015, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.count', index=30,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count_null', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Parameters.count_null', index=31,
      number=1016, type=8, cpp_type=7, label=1,
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
  serialized_start=151,
  serialized_end=1720,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_description', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.node_description', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value2', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.value2', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value3', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.value3', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value1', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.value1', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_code_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.binary_code_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.node_id', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.tree_node_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.sort_no', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.level_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.value', index=10,
      number=20005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_sort_no', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.value_sort_no', index=11,
      number=20006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_id', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.Row.value_id', index=12,
      number=20007, type=11, cpp_type=10, label=1,
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
  serialized_start=1947,
  serialized_end=2555,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='count', full_name='dstore.engine.im_GetDirectSuccessors_Pu.Response.count', index=3,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1723,
  serialized_end=2555,
)

_PARAMETERS.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['group_by_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['binary_characteristic_value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['filter_by_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['filter_by_charac_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['output_into_one_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['negate_filter_by_params'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['sort_by_characteristic_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['sort_option_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['inherit_depth_option_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['recursive_evaluation_option_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['get_values_for_sort_by_characs'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['from_row_number'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['max_number_of_nodes'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['count'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['node_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value3'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['binary_code_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['level_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value_sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['count'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.im_GetDirectSuccessors_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.im_GetDirectSuccessors_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.im_GetDirectSuccessors_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.im_GetDirectSuccessors_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.im_GetDirectSuccessors_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.im_GetDirectSuccessors_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/im_GetDirectSuccessors_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
