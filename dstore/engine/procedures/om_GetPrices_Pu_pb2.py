# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetPrices_Pu.proto

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
  name='dstore/engine/procedures/om_GetPrices_Pu.proto',
  package='dstore.engine.om_GetPrices_Pu',
  syntax='proto3',
  serialized_pb=_b('\n.dstore/engine/procedures/om_GetPrices_Pu.proto\x12\x1d\x64store.engine.om_GetPrices_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xea\x08\n\nParameters\x12,\n\x08node_ids\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x16\n\rnode_ids_null\x18\xe9\x07 \x01(\x08\x12.\n\nquantities\x18\x02 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x18\n\x0fquantities_null\x18\xea\x07 \x01(\x08\x12.\n\tperson_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xeb\x07 \x01(\x08\x12\x30\n\x0b\x63urrency_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10\x63urrency_id_null\x18\xec\x07 \x01(\x08\x12\x34\n\x0fis_tree_node_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1d\n\x14is_tree_node_id_null\x18\xed\x07 \x01(\x08\x12\x41\n\x1cprice_node_characteristic_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12*\n!price_node_characteristic_id_null\x18\xee\x07 \x01(\x08\x12\x30\n\x0b\x63ompute_sum\x18\x07 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x19\n\x10\x63ompute_sum_null\x18\xef\x07 \x01(\x08\x12-\n\tunique_id\x18\x08 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xf0\x07 \x01(\x08\x12>\n\x19get_additional_price_info\x18\t \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\'\n\x1eget_additional_price_info_null\x18\xf1\x07 \x01(\x08\x12\x37\n\x12\x64\x65livery_person_id\x18\n \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17\x64\x65livery_person_id_null\x18\xf2\x07 \x01(\x08\x12\x41\n\x1cget_price_per_single_node_id\x18\x0b \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12*\n!get_price_per_single_node_id_null\x18\xf3\x07 \x01(\x08\x12\x34\n\x0fpayment_type_id\x18\x0c \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1d\n\x14payment_type_id_null\x18\xf4\x07 \x01(\x08\x12\x35\n\x10shipping_type_id\x18\r \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1e\n\x15shipping_type_id_null\x18\xf5\x07 \x01(\x08\"\xc9\x12\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x38\n\x03row\x18\x04 \x03(\x0b\x32+.dstore.engine.om_GetPrices_Pu.Response.Row\x1a\x9f\x11\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x37\n\x11total_netto_price\x18\x91N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x46\n precise_abs_unit_gross_surcharge\x18\x92N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x42\n\x1cprice_node_characteristic_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x43\n\x1d\x61\x62solute_unit_netto_surcharge\x18\x94N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x36\n\x10unit_gross_price\x18\x95N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x42\n\x1c\x61\x62solute_total_net_surcharge\x18\x96N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x44\n\x1e\x61\x62solute_total_gross_surcharge\x18\x97N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x37\n\x11unit_brutto_price\x18\x98N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12>\n\x18precise_unit_gross_price\x18\x99N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x34\n\x0eunit_net_price\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x38\n\x12total_brutto_price\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x44\n\x1eprecise_abs_unit_net_surcharge\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x35\n\x10surcharge_reason\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x07node_id\x18\x9eN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0ctree_node_id\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x44\n\x1e\x61\x62solute_total_netto_surcharge\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x38\n\x12relative_surcharge\x18\xa1N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x45\n\x1f\x61\x62solute_total_brutto_surcharge\x18\xa2N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x44\n\x1fsurcharge_generated_by_camp_ids\x18\xa3N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12?\n\x19precise_total_gross_price\x18\xa4N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x36\n\x10unit_netto_price\x18\xa5N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x36\n\x10taxes_multiplier\x18\xa6N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12G\n!precise_abs_total_gross_surcharge\x18\xa7N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x45\n\x1fprecise_abs_total_net_surcharge\x18\xa8N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x35\n\x0ftotal_net_price\x18\xa9N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12.\n\x08quantity\x18\xaaN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12I\n$quantity_per_bundle_item_set_id_list\x18\xabN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0fsurcharge_value\x18\xacN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x41\n\x1b\x61\x62solute_unit_net_surcharge\x18\xadN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x44\n\x1e\x61\x62solute_unit_brutto_surcharge\x18\xaeN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x43\n\x1d\x61\x62solute_unit_gross_surcharge\x18\xafN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12=\n\x17precise_total_net_price\x18\xb0N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x37\n\x11surcharge_type_id\x18\xb1N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12<\n\x16precise_unit_net_price\x18\xb2N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x37\n\x11total_gross_price\x18\xb3N \x01(\x0b\x32\x1b.dstore.values.DecimalValueBP\n\x1bio.dstore.engine.proceduresZ1gosdk.dstore.de/engine/procedures/om_GetPrices_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetPrices_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_ids', full_name='dstore.engine.om_GetPrices_Pu.Parameters.node_ids', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_ids_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.node_ids_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantities', full_name='dstore.engine.om_GetPrices_Pu.Parameters.quantities', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantities_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.quantities_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.person_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.person_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.currency_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.currency_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_tree_node_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.is_tree_node_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_tree_node_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.is_tree_node_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.price_node_characteristic_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.price_node_characteristic_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compute_sum', full_name='dstore.engine.om_GetPrices_Pu.Parameters.compute_sum', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='compute_sum_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.compute_sum_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.unique_id', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.unique_id_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_additional_price_info', full_name='dstore.engine.om_GetPrices_Pu.Parameters.get_additional_price_info', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_additional_price_info_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.get_additional_price_info_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.delivery_person_id', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.delivery_person_id_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_price_per_single_node_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.get_price_per_single_node_id', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_price_per_single_node_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.get_price_per_single_node_id_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.payment_type_id', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.payment_type_id_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_GetPrices_Pu.Parameters.shipping_type_id', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id_null', full_name='dstore.engine.om_GetPrices_Pu.Parameters.shipping_type_id_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
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
  serialized_start=131,
  serialized_end=1261,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetPrices_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_netto_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.total_netto_price', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_abs_unit_gross_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_abs_unit_gross_surcharge', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.price_node_characteristic_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_unit_netto_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_unit_netto_surcharge', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_gross_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.unit_gross_price', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_total_net_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_total_net_surcharge', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_total_gross_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_total_gross_surcharge', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_brutto_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.unit_brutto_price', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_unit_gross_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_unit_gross_price', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_net_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.unit_net_price', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_brutto_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.total_brutto_price', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_abs_unit_net_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_abs_unit_net_surcharge', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_reason', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.surcharge_reason', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.node_id', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.tree_node_id', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_total_netto_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_total_netto_surcharge', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.relative_surcharge', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_total_brutto_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_total_brutto_surcharge', index=18,
      number=10018, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_generated_by_camp_ids', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.surcharge_generated_by_camp_ids', index=19,
      number=10019, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_total_gross_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_total_gross_price', index=20,
      number=10020, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_netto_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.unit_netto_price', index=21,
      number=10021, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='taxes_multiplier', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.taxes_multiplier', index=22,
      number=10022, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_abs_total_gross_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_abs_total_gross_surcharge', index=23,
      number=10023, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_abs_total_net_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_abs_total_net_surcharge', index=24,
      number=10024, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_net_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.total_net_price', index=25,
      number=10025, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.quantity', index=26,
      number=10026, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity_per_bundle_item_set_id_list', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.quantity_per_bundle_item_set_id_list', index=27,
      number=10027, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_value', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.surcharge_value', index=28,
      number=10028, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_unit_net_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_unit_net_surcharge', index=29,
      number=10029, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_unit_brutto_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_unit_brutto_surcharge', index=30,
      number=10030, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_unit_gross_surcharge', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.absolute_unit_gross_surcharge', index=31,
      number=10031, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_total_net_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_total_net_price', index=32,
      number=10032, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_type_id', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.surcharge_type_id', index=33,
      number=10033, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='precise_unit_net_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.precise_unit_net_price', index=34,
      number=10034, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_gross_price', full_name='dstore.engine.om_GetPrices_Pu.Response.Row.total_gross_price', index=35,
      number=10035, type=11, cpp_type=10, label=1,
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
  serialized_start=1434,
  serialized_end=3641,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetPrices_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetPrices_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetPrices_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetPrices_Pu.Response.row', index=2,
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
  serialized_start=1264,
  serialized_end=3641,
)

_PARAMETERS.fields_by_name['node_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['quantities'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['currency_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['is_tree_node_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['price_node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['compute_sum'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['get_additional_price_info'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['delivery_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_price_per_single_node_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['total_netto_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['precise_abs_unit_gross_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['price_node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['absolute_unit_netto_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['unit_gross_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_total_net_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_total_gross_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['unit_brutto_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['precise_unit_gross_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['unit_net_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['total_brutto_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['precise_abs_unit_net_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['surcharge_reason'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['absolute_total_netto_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['relative_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_total_brutto_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['surcharge_generated_by_camp_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['precise_total_gross_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['unit_netto_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['taxes_multiplier'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['precise_abs_total_gross_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['precise_abs_total_net_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['total_net_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['quantity_per_bundle_item_set_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['surcharge_value'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_unit_net_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_unit_brutto_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_unit_gross_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['precise_total_net_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['surcharge_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['precise_unit_net_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['total_gross_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetPrices_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPrices_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetPrices_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPrices_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetPrices_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPrices_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ1gosdk.dstore.de/engine/procedures/om_GetPrices_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
