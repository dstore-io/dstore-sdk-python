# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetPurchaseOrderQueues_Ad.proto

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
  name='dstore/engine/procedures/om_GetPurchaseOrderQueues_Ad.proto',
  package='dstore.engine.om_GetPurchaseOrderQueues_Ad',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/om_GetPurchaseOrderQueues_Ad.proto\x12*dstore.engine.om_GetPurchaseOrderQueues_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xe3\x04\n\nParameters\x12\x30\n\x0bsupplier_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10supplier_id_null\x18\xe9\x07 \x01(\x08\x12:\n\x13\x66rom_order_deadline\x18\x02 \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12!\n\x18\x66rom_order_deadline_null\x18\xea\x07 \x01(\x08\x12\x38\n\x11to_order_deadline\x18\x03 \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12\x1f\n\x16to_order_deadline_null\x18\xeb\x07 \x01(\x08\x12\x32\n\rorder_type_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1b\n\x12order_type_id_null\x18\xec\x07 \x01(\x08\x12,\n\x07node_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x15\n\x0cnode_id_null\x18\xed\x07 \x01(\x08\x12\x35\n\x10get_summary_only\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1e\n\x15get_summary_only_null\x18\xee\x07 \x01(\x08\x12;\n\x16node_characteristic_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12$\n\x1bnode_characteristic_id_null\x18\xef\x07 \x01(\x08\"\x9d\x11\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row\x1a\xce\x0f\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12G\n\"suppl_charac_val2_restr_by_pattern\x18\x91N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12<\n\x16last_edited_by_user_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x34\n\x0f\x63urrency_symbol\x18\x93N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x44\n\x1clast_edited_at_date_and_time\x18\x94N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12\x31\n\x0bsupplier_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12-\n\x07net_sum\x18\x96N \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x35\n\x10node_description\x18\x97N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x36\n\x0eorder_deadline\x18\x98N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12-\n\x07node_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x32\n\x0ctree_node_id\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x14\x63reated_by_user_name\x18\x9bN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12,\n\x07\x63omment\x18\x9cN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x43\n\x1esupplier_characteristic_value2\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x32\n\ritem_property\x18\x9eN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x43\n\x1esupplier_characteristic_value1\x18\x9fN \x01(\x0b\x32\x1a.dstore.values.stringValue\x12.\n\x08quantity\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12=\n\x18last_edited_by_user_name\x18\xa1N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x31\n\x0b\x63urrency_id\x18\xa2N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12@\n\x18\x63reated_at_date_and_time\x18\xa3N \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12\x38\n\x12\x63reated_by_user_id\x18\xa4N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12;\n\x16order_type_description\x18\xa5N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x34\n\x0eh_tree_node_id\x18\xa6N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x33\n\rorder_type_id\x18\xa7N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12,\n\x07item_no\x18\xa8N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12G\n\"suppl_charac_val1_restr_by_pattern\x18\xa9N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x36\n\x0fnumber_of_items\x18\xa1\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x42\n\x1bnumber_of_expired_deadlines\x18\xa2\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x12min_order_deadline\x18\xa3\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x37\n\x10number_of_queues\x18\xa4\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x12max_order_deadline\x18\xa5\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12:\n\x13number_of_suppliers\x18\xa6\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x34\n\rtotal_net_sum\x18\xb2\xea\x01 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12G\n purchase_price_characteristic_id\x18\xb6\xea\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x35\n\x0etotal_quantity\x18\xbc\xea\x01 \x01(\x0b\x32\x1b.dstore.values.integerValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/om_GetPurchaseOrderQueues_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='supplier_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.supplier_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_id_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.supplier_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_order_deadline', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.from_order_deadline', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_order_deadline_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.from_order_deadline_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_order_deadline', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.to_order_deadline', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_order_deadline_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.to_order_deadline_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_type_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.order_type_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_type_id_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.order_type_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.node_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.node_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_summary_only', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.get_summary_only', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_summary_only_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.get_summary_only_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.node_characteristic_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id_null', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters.node_characteristic_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
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
  serialized_start=195,
  serialized_end=806,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suppl_charac_val2_restr_by_pattern', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.suppl_charac_val2_restr_by_pattern', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_edited_by_user_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.last_edited_by_user_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_symbol', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.currency_symbol', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_edited_at_date_and_time', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.last_edited_at_date_and_time', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.supplier_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net_sum', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.net_sum', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_description', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.node_description', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_deadline', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.order_deadline', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.node_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.tree_node_id', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created_by_user_name', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.created_by_user_name', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comment', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.comment', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_characteristic_value2', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.supplier_characteristic_value2', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_property', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.item_property', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_characteristic_value1', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.supplier_characteristic_value1', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.quantity', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_edited_by_user_name', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.last_edited_by_user_name', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.currency_id', index=18,
      number=10018, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created_at_date_and_time', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.created_at_date_and_time', index=19,
      number=10019, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='created_by_user_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.created_by_user_id', index=20,
      number=10020, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_type_description', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.order_type_description', index=21,
      number=10021, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.h_tree_node_id', index=22,
      number=10022, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='order_type_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.order_type_id', index=23,
      number=10023, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_no', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.item_no', index=24,
      number=10024, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suppl_charac_val1_restr_by_pattern', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.suppl_charac_val1_restr_by_pattern', index=25,
      number=10025, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_items', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.number_of_items', index=26,
      number=20001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_expired_deadlines', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.number_of_expired_deadlines', index=27,
      number=20002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='min_order_deadline', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.min_order_deadline', index=28,
      number=20003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_queues', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.number_of_queues', index=29,
      number=20004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_order_deadline', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.max_order_deadline', index=30,
      number=20005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_suppliers', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.number_of_suppliers', index=31,
      number=20006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_net_sum', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.total_net_sum', index=32,
      number=30002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='purchase_price_characteristic_id', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.purchase_price_characteristic_id', index=33,
      number=30006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_quantity', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row.total_quantity', index=34,
      number=30012, type=11, cpp_type=10, label=1,
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
  serialized_start=1016,
  serialized_end=3014,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.row', index=2,
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
  serialized_start=809,
  serialized_end=3014,
)

_PARAMETERS.fields_by_name['supplier_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['from_order_deadline'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['to_order_deadline'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['order_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_summary_only'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['suppl_charac_val2_restr_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['last_edited_by_user_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['currency_symbol'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['last_edited_at_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['supplier_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['net_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['node_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['order_deadline'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['created_by_user_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['comment'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['supplier_characteristic_value2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['item_property'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['supplier_characteristic_value1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['last_edited_by_user_name'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['currency_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['created_at_date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['created_by_user_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['order_type_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['h_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['order_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['item_no'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['suppl_charac_val1_restr_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['number_of_items'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['number_of_expired_deadlines'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['min_order_deadline'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['number_of_queues'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['max_order_deadline'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['number_of_suppliers'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['total_net_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['purchase_price_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['total_quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetPurchaseOrderQueues_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPurchaseOrderQueues_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetPurchaseOrderQueues_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPurchaseOrderQueues_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetPurchaseOrderQueues_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPurchaseOrderQueues_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/om_GetPurchaseOrderQueues_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)