# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetCampaignItemConGroups_Ad.proto

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
  name='dstore/engine/procedures/om_GetCampaignItemConGroups_Ad.proto',
  package='dstore.engine.om_GetCampaignItemConGroups_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/om_GetCampaignItemConGroups_Ad.proto\x12,dstore.engine.om_GetCampaignItemConGroups_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xc0\x01\n\nParameters\x12\x31\n\x0c\x63ondition_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1a\n\x11\x63ondition_id_null\x18\xe9\x07 \x01(\x08\x12<\n\x17item_condition_group_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12%\n\x1citem_condition_group_id_null\x18\xea\x07 \x01(\x08\"\xbf\x11\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row\x1a\xee\x0f\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12/\n\ncondition1\x18\x91N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12/\n\ncondition2\x18\x92N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12:\n\x14recursive_evaluation\x18\x93N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12=\n\x17to_basic_price_sum_part\x18\x94N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x39\n\x14\x64omain_tree_node_ids\x18\x95N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12<\n\x16node_characteristic_id\x18\x96N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12<\n\x16item_condition_part_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12?\n\x19\x66rom_basic_price_sum_part\x18\x98N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x31\n\x0bto_quantity\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x13max_number_of_items\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12>\n\x18to_item_basic_price_part\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x44\n\x1fitem_condition_part_description\x18\x9cN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12.\n\tlevel_ids\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12=\n\x17item_condition_group_id\x18\x9eN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x43\n\x1e\x65xtended_item_cond_group_descr\x18\x9fN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x33\n\rfrom_quantity\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12;\n\x15\x66rom_item_basic_price\x18\xa1N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x38\n\x12item_group_sort_no\x18\xa2N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12.\n\toperator1\x18\xa3N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12.\n\toperator2\x18\xa4N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12G\n!combine_parts_with_a_n_d_operator\x18\xa5N \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12>\n\x18min_number_of_items_part\x18\xa6N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x37\n\x11item_part_sort_no\x18\xa7N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x42\n\x1d\x65xtended_item_cond_part_descr\x18\xa8N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12>\n\x18max_number_of_items_part\x18\xa9N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12@\n\x1a\x66rom_item_basic_price_part\x18\xaaN \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x39\n\x13min_number_of_items\x18\xabN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12:\n\x14\x66rom_basic_price_sum\x18\xacN \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x38\n\x12to_basic_price_sum\x18\xadN \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x32\n\x0c\x63ondition_id\x18\xaeN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x13to_item_basic_price\x18\xafN \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x36\n\x10to_quantity_part\x18\xb0N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x38\n\x12\x66rom_quantity_part\x18\xb1N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x33\n\rinherit_depth\x18\xb2N \x01(\x0b\x32\x1b.dstore.values.integerValueB_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_GetCampaignItemConGroups_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='condition_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Parameters.condition_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_id_null', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Parameters.condition_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_group_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Parameters.item_condition_group_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_group_id_null', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Parameters.item_condition_group_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
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
  serialized_end=391,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition1', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.condition1', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition2', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.condition2', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive_evaluation', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.recursive_evaluation', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_basic_price_sum_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.to_basic_price_sum_part', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='domain_tree_node_ids', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.domain_tree_node_ids', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.node_characteristic_id', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_part_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.item_condition_part_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_basic_price_sum_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.from_basic_price_sum_part', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_quantity', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.to_quantity', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_items', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.max_number_of_items', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_item_basic_price_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.to_item_basic_price_part', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_part_description', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.item_condition_part_description', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level_ids', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.level_ids', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_group_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.item_condition_group_id', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extended_item_cond_group_descr', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.extended_item_cond_group_descr', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_quantity', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.from_quantity', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_item_basic_price', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.from_item_basic_price', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_group_sort_no', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.item_group_sort_no', index=18,
      number=10018, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator1', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.operator1', index=19,
      number=10019, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operator2', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.operator2', index=20,
      number=10020, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='combine_parts_with_a_n_d_operator', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.combine_parts_with_a_n_d_operator', index=21,
      number=10021, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_number_of_items_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.min_number_of_items_part', index=22,
      number=10022, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_part_sort_no', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.item_part_sort_no', index=23,
      number=10023, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extended_item_cond_part_descr', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.extended_item_cond_part_descr', index=24,
      number=10024, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_items_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.max_number_of_items_part', index=25,
      number=10025, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_item_basic_price_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.from_item_basic_price_part', index=26,
      number=10026, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_number_of_items', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.min_number_of_items', index=27,
      number=10027, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_basic_price_sum', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.from_basic_price_sum', index=28,
      number=10028, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_basic_price_sum', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.to_basic_price_sum', index=29,
      number=10029, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_id', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.condition_id', index=30,
      number=10030, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_item_basic_price', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.to_item_basic_price', index=31,
      number=10031, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_quantity_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.to_quantity_part', index=32,
      number=10032, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_quantity_part', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.from_quantity_part', index=33,
      number=10033, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='inherit_depth', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row.inherit_depth', index=34,
      number=10034, type=11, cpp_type=10, label=1,
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
  serialized_start=603,
  serialized_end=2633,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetCampaignItemConGroups_Ad.Response.row', index=2,
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
  serialized_start=394,
  serialized_end=2633,
)

_PARAMETERS.fields_by_name['condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['item_condition_group_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['condition1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['condition2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['recursive_evaluation'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['to_basic_price_sum_part'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['domain_tree_node_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['item_condition_part_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_basic_price_sum_part'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['to_quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['max_number_of_items'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['to_item_basic_price_part'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['item_condition_part_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['level_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['item_condition_group_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['extended_item_cond_group_descr'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['from_quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_item_basic_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['item_group_sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['operator1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['operator2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['combine_parts_with_a_n_d_operator'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['min_number_of_items_part'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['item_part_sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['extended_item_cond_part_descr'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['max_number_of_items_part'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_item_basic_price_part'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['min_number_of_items'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_basic_price_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['to_basic_price_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['to_item_basic_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['to_quantity_part'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_quantity_part'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['inherit_depth'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetCampaignItemConGroups_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetCampaignItemConGroups_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetCampaignItemConGroups_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetCampaignItemConGroups_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetCampaignItemConGroups_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetCampaignItemConGroups_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_GetCampaignItemConGroups_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
