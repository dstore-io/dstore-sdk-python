# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_CreateSimpleCampItemCond_Ad.proto

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
  name='dstore/engine/procedures/om_CreateSimpleCampItemCond_Ad.proto',
  package='dstore.engine.om_CreateSimpleCampItemCond_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/om_CreateSimpleCampItemCond_Ad.proto\x12,dstore.engine.om_CreateSimpleCampItemCond_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\x80\x13\n\nParameters\x12\x30\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10\x63\x61mpaign_id_null\x18\xe9\x07 \x01(\x08\x12\x39\n\x15\x63ondition_description\x18\x02 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12#\n\x1a\x63ondition_description_null\x18\xea\x07 \x01(\x08\x12\x31\n\x0c\x63ondition_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1a\n\x11\x63ondition_id_null\x18\xeb\x07 \x01(\x08\x12\x36\n\x11item_condition_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1f\n\x16item_condition_id_null\x18\xec\x07 \x01(\x08\x12<\n\x17item_condition_group_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12%\n\x1citem_condition_group_id_null\x18\xed\x07 \x01(\x08\x12;\n\x16item_condition_part_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12$\n\x1bitem_condition_part_id_null\x18\xee\x07 \x01(\x08\x12-\n\tlevel_ids\x18\x07 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0elevel_ids_null\x18\xef\x07 \x01(\x08\x12\x38\n\x14\x64omain_tree_node_ids\x18\x08 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\"\n\x19\x64omain_tree_node_ids_null\x18\xf0\x07 \x01(\x08\x12;\n\x16node_characteristic_id\x18\t \x01(\x0b\x32\x1b.dstore.values.integerValue\x12$\n\x1bnode_characteristic_id_null\x18\xf1\x07 \x01(\x08\x12-\n\toperator1\x18\n \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0eoperator1_null\x18\xf2\x07 \x01(\x08\x12.\n\ncondition1\x18\x0b \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x18\n\x0f\x63ondition1_null\x18\xf3\x07 \x01(\x08\x12-\n\toperator2\x18\x0c \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0eoperator2_null\x18\xf4\x07 \x01(\x08\x12.\n\ncondition2\x18\r \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x18\n\x0f\x63ondition2_null\x18\xf5\x07 \x01(\x08\x12\x32\n\rinherit_depth\x18\x0e \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1b\n\x12inherit_depth_null\x18\xf6\x07 \x01(\x08\x12\x39\n\x14recursive_evaluation\x18\x0f \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\"\n\x19recursive_evaluation_null\x18\xf7\x07 \x01(\x08\x12+\n\x07\x63ountry\x18\x10 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x15\n\x0c\x63ountry_null\x18\xf8\x07 \x01(\x08\x12\x42\n\x1e\x65xtended_condition_description\x18\x11 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12,\n#extended_condition_description_null\x18\xf9\x07 \x01(\x08\x12\x38\n\x13min_number_of_items\x18\x12 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12!\n\x18min_number_of_items_null\x18\xfa\x07 \x01(\x08\x12\x38\n\x13max_number_of_items\x18\x13 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12!\n\x18max_number_of_items_null\x18\xfb\x07 \x01(\x08\x12\x32\n\rfrom_quantity\x18\x14 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1b\n\x12\x66rom_quantity_null\x18\xfc\x07 \x01(\x08\x12\x30\n\x0bto_quantity\x18\x15 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10to_quantity_null\x18\xfd\x07 \x01(\x08\x12:\n\x15\x66rom_item_basic_price\x18\x16 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12#\n\x1a\x66rom_item_basic_price_null\x18\xfe\x07 \x01(\x08\x12\x38\n\x13to_item_basic_price\x18\x17 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12!\n\x18to_item_basic_price_null\x18\xff\x07 \x01(\x08\x12\x39\n\x14\x66rom_basic_price_sum\x18\x18 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\"\n\x19\x66rom_basic_price_sum_null\x18\x80\x08 \x01(\x08\x12\x37\n\x12to_basic_price_sum\x18\x19 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12 \n\x17to_basic_price_sum_null\x18\x81\x08 \x01(\x08\x12G\n\"combine_groups_with_a_n_d_operator\x18\x1a \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x30\n\'combine_groups_with_a_n_d_operator_null\x18\x82\x08 \x01(\x08\x12\x46\n!combine_parts_with_a_n_d_operator\x18\x1b \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12/\n&combine_parts_with_a_n_d_operator_null\x18\x83\x08 \x01(\x08\"\xcc\x03\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.Row\x12\x31\n\x0c\x63ondition_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x36\n\x11item_condition_id\x18\x66 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12<\n\x17item_condition_group_id\x18g \x01(\x0b\x32\x1b.dstore.values.integerValue\x12;\n\x16item_condition_part_id\x18h \x01(\x0b\x32\x1b.dstore.values.integerValue\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_CreateSimpleCampItemCond_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.campaign_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='campaign_id_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.campaign_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_description', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition_description', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_description_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition_description_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_id_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.item_condition_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_id_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.item_condition_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_group_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.item_condition_group_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_group_id_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.item_condition_group_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_part_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.item_condition_part_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_part_id_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.item_condition_part_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_ids', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.level_ids', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_ids_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.level_ids_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_tree_node_ids', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.domain_tree_node_ids', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_tree_node_ids_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.domain_tree_node_ids_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.node_characteristic_id', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.node_characteristic_id_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator1', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.operator1', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator1_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.operator1_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition1', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition1', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition1_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition1_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator2', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.operator2', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator2_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.operator2_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition2', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition2', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition2_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.condition2_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inherit_depth', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.inherit_depth', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inherit_depth_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.inherit_depth_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive_evaluation', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.recursive_evaluation', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive_evaluation_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.recursive_evaluation_null', index=29,
      number=1015, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.country', index=30,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.country_null', index=31,
      number=1016, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extended_condition_description', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.extended_condition_description', index=32,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extended_condition_description_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.extended_condition_description_null', index=33,
      number=1017, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_number_of_items', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.min_number_of_items', index=34,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_number_of_items_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.min_number_of_items_null', index=35,
      number=1018, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_items', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.max_number_of_items', index=36,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_items_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.max_number_of_items_null', index=37,
      number=1019, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_quantity', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.from_quantity', index=38,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_quantity_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.from_quantity_null', index=39,
      number=1020, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_quantity', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.to_quantity', index=40,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_quantity_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.to_quantity_null', index=41,
      number=1021, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_item_basic_price', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.from_item_basic_price', index=42,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_item_basic_price_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.from_item_basic_price_null', index=43,
      number=1022, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_item_basic_price', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.to_item_basic_price', index=44,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_item_basic_price_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.to_item_basic_price_null', index=45,
      number=1023, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_basic_price_sum', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.from_basic_price_sum', index=46,
      number=24, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_basic_price_sum_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.from_basic_price_sum_null', index=47,
      number=1024, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_basic_price_sum', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.to_basic_price_sum', index=48,
      number=25, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_basic_price_sum_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.to_basic_price_sum_null', index=49,
      number=1025, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combine_groups_with_a_n_d_operator', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.combine_groups_with_a_n_d_operator', index=50,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combine_groups_with_a_n_d_operator_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.combine_groups_with_a_n_d_operator_null', index=51,
      number=1026, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combine_parts_with_a_n_d_operator', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.combine_parts_with_a_n_d_operator', index=52,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combine_parts_with_a_n_d_operator_null', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters.combine_parts_with_a_n_d_operator_null', index=53,
      number=1027, type=8, cpp_type=7, label=1,
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
  serialized_end=2631,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.Row.row_id', index=0,
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
  serialized_start=3072,
  serialized_end=3094,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.condition_id', index=3,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.item_condition_id', index=4,
      number=102, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_group_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.item_condition_group_id', index=5,
      number=103, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_part_id', full_name='dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.item_condition_part_id', index=6,
      number=104, type=11, cpp_type=10, label=1,
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
  serialized_start=2634,
  serialized_end=3094,
)

_PARAMETERS.fields_by_name['campaign_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['condition_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['item_condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['item_condition_group_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['item_condition_part_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['level_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['domain_tree_node_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['operator1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['condition1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['operator2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['condition2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['inherit_depth'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['recursive_evaluation'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['country'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['extended_condition_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['min_number_of_items'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['max_number_of_items'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['from_quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['to_quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['from_item_basic_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['to_item_basic_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['from_basic_price_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['to_basic_price_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['combine_groups_with_a_n_d_operator'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['combine_parts_with_a_n_d_operator'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE.fields_by_name['item_condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE.fields_by_name['item_condition_group_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE.fields_by_name['item_condition_part_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_CreateSimpleCampItemCond_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_CreateSimpleCampItemCond_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_CreateSimpleCampItemCond_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_CreateSimpleCampItemCond_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_CreateSimpleCampItemCond_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_CreateSimpleCampItemCond_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_CreateSimpleCampItemCond_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
