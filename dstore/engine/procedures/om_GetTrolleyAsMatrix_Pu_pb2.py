# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetTrolleyAsMatrix_Pu.proto

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
  name='dstore/engine/procedures/om_GetTrolleyAsMatrix_Pu.proto',
  package='dstore.engine.om_GetTrolleyAsMatrix_Pu',
  syntax='proto3',
  serialized_pb=_b('\n7dstore/engine/procedures/om_GetTrolleyAsMatrix_Pu.proto\x12&dstore.engine.om_GetTrolleyAsMatrix_Pu\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xb3\x07\n\nParameters\x12-\n\tunique_id\x18\x01 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0eunique_id_null\x18\xe9\x07 \x01(\x08\x12.\n\tperson_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x17\n\x0eperson_id_null\x18\xea\x07 \x01(\x08\x12\x35\n\x10\x63\x61lculate_prices\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1e\n\x15\x63\x61lculate_prices_null\x18\xeb\x07 \x01(\x08\x12\x37\n\x12\x63heck_availability\x18\x04 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12 \n\x17\x63heck_availability_null\x18\xec\x07 \x01(\x08\x12\x41\n\x1cprice_node_characteristic_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12*\n!price_node_characteristic_id_null\x18\xed\x07 \x01(\x08\x12\x45\n repair_entries_with_same_node_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12.\n%repair_entries_with_same_node_id_null\x18\xee\x07 \x01(\x08\x12\x37\n\x12\x64\x65livery_person_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12 \n\x17\x64\x65livery_person_id_null\x18\xef\x07 \x01(\x08\x12\x45\n output_into_trolley_surch_interf\x18\x08 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12.\n%output_into_trolley_surch_interf_null\x18\xf0\x07 \x01(\x08\x12\x34\n\x0fpayment_type_id\x18\t \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1d\n\x14payment_type_id_null\x18\xf1\x07 \x01(\x08\x12\x35\n\x10shipping_type_id\x18\n \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1e\n\x15shipping_type_id_null\x18\xf2\x07 \x01(\x08\"\xad\n\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x41\n\x03row\x18\x04 \x03(\x0b\x32\x34.dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row\x1a\xe2\x08\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12:\n\x14variant_tree_node_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12:\n\x14product_tree_node_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x42\n\x1cprice_node_characteristic_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x44\n\x1fsurcharge_generated_by_camp_ids\x18\x94N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x35\n\x10y_axis_value_ids\x18\x95N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12;\n\x13input_date_and_time\x18\x96N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12\x36\n\x10unit_netto_price\x18\x97N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x43\n\x1d\x61\x62solute_unit_netto_surcharge\x18\x98N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12.\n\x08quantity\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x30\n\x0bunit_symbol\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12-\n\x07removed\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x37\n\x11unit_brutto_price\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x32\n\ry_axis_values\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x35\n\x10surcharge_reason\x18\x9eN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x31\n\x0cx_axis_value\x18\x9fN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x44\n\x1e\x61\x62solute_unit_brutto_surcharge\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x38\n\x13product_description\x18\xa1N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x35\n\x0fx_axis_value_id\x18\xa2N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x38\n\x12relative_surcharge\x18\xa3N \x01(\x0b\x32\x1b.dstore.values.decimalValueBY\n\x1bio.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_GetTrolleyAsMatrix_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.unique_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.unique_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.person_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.person_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculate_prices', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.calculate_prices', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculate_prices_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.calculate_prices_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_availability', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.check_availability', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='check_availability_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.check_availability_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.price_node_characteristic_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.price_node_characteristic_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repair_entries_with_same_node_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.repair_entries_with_same_node_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repair_entries_with_same_node_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.repair_entries_with_same_node_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.delivery_person_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.delivery_person_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_trolley_surch_interf', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.output_into_trolley_surch_interf', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_trolley_surch_interf_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.output_into_trolley_surch_interf_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.payment_type_id', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.payment_type_id_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.shipping_type_id', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id_null', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters.shipping_type_id_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
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
  serialized_start=187,
  serialized_end=1134,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='variant_tree_node_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.variant_tree_node_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_tree_node_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.product_tree_node_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='price_node_characteristic_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.price_node_characteristic_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_generated_by_camp_ids', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.surcharge_generated_by_camp_ids', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_axis_value_ids', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.y_axis_value_ids', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_date_and_time', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.input_date_and_time', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_netto_price', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.unit_netto_price', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_unit_netto_surcharge', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.absolute_unit_netto_surcharge', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.quantity', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_symbol', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.unit_symbol', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='removed', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.removed', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_brutto_price', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.unit_brutto_price', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y_axis_values', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.y_axis_values', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='surcharge_reason', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.surcharge_reason', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_axis_value', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.x_axis_value', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='absolute_unit_brutto_surcharge', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.absolute_unit_brutto_surcharge', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='product_description', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.product_description', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_axis_value_id', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.x_axis_value_id', index=18,
      number=10018, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relative_surcharge', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row.relative_surcharge', index=19,
      number=10019, type=11, cpp_type=10, label=1,
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
  serialized_start=1340,
  serialized_end=2462,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.row', index=2,
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
  serialized_start=1137,
  serialized_end=2462,
)

_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['calculate_prices'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['check_availability'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['price_node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['repair_entries_with_same_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delivery_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['output_into_trolley_surch_interf'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['variant_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['product_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['price_node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['surcharge_generated_by_camp_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['y_axis_value_ids'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['input_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['unit_netto_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['absolute_unit_netto_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['unit_symbol'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['removed'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['unit_brutto_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['y_axis_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['surcharge_reason'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['x_axis_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['absolute_unit_brutto_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['product_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['x_axis_value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['relative_surcharge'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetTrolleyAsMatrix_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetTrolleyAsMatrix_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetTrolleyAsMatrix_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetTrolleyAsMatrix_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetTrolleyAsMatrix_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetTrolleyAsMatrix_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_GetTrolleyAsMatrix_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
