# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetPurchasePrices_Ad.proto

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
  name='dstore/engine/procedures/om_GetPurchasePrices_Ad.proto',
  package='dstore.engine.om_GetPurchasePrices_Ad',
  syntax='proto3',
  serialized_pb=_b('\n6dstore/engine/procedures/om_GetPurchasePrices_Ad.proto\x12%dstore.engine.om_GetPurchasePrices_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xae\x04\n\nParameters\x12\x39\n\x14tree_node_or_node_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\"\n\x19tree_node_or_node_id_null\x18\xe9\x07 \x01(\x08\x12\x34\n\x0fis_tree_node_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1d\n\x14is_tree_node_id_null\x18\xea\x07 \x01(\x08\x12-\n\x08quantity\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x16\n\rquantity_null\x18\xeb\x07 \x01(\x08\x12\x30\n\x0bsupplier_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10supplier_id_null\x18\xec\x07 \x01(\x08\x12\x46\n\x1f\x64\x61te_for_property_determination\x18\x05 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12-\n$date_for_property_determination_null\x18\xed\x07 \x01(\x08\x12;\n\x16node_characteristic_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12$\n\x1bnode_characteristic_id_null\x18\xee\x07 \x01(\x08\"\xcf\x08\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12@\n\x03row\x18\x04 \x03(\x0b\x32\x33.dstore.engine.om_GetPurchasePrices_Ad.Response.Row\x1a\x9d\x07\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12G\n\"suppl_charac_val2_restr_by_pattern\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x32\n\ritem_property\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x43\n\x1esupplier_characteristic_value2\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0ftotal_net_price\x18\x94N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12.\n\x08quantity\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x43\n\x1esupplier_characteristic_value1\x18\x96N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\x0b\x63urrency_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x34\n\x0f\x63urrency_symbol\x18\x98N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\x0bsupplier_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x35\n\x10node_description\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x34\n\x0eunit_net_price\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x34\n\x0eh_tree_node_id\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12,\n\x07item_no\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x07node_id\x18\x9eN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0ctree_node_id\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12G\n\"suppl_charac_val1_restr_by_pattern\x18\xa0N \x01(\x0b\x32\x1a.dstore.values.StringValueBX\n\x1bio.dstore.engine.proceduresZ9gosdk.dstore.de/engine/procedures/om_GetPurchasePrices_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_node_or_node_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.tree_node_or_node_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_or_node_id_null', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.tree_node_or_node_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_tree_node_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.is_tree_node_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_tree_node_id_null', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.is_tree_node_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.quantity', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity_null', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.quantity_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.supplier_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_id_null', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.supplier_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_for_property_determination', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.date_for_property_determination', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_for_property_determination_null', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.date_for_property_determination_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.node_characteristic_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id_null', full_name='dstore.engine.om_GetPurchasePrices_Ad.Parameters.node_characteristic_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
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
  serialized_start=147,
  serialized_end=705,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suppl_charac_val2_restr_by_pattern', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.suppl_charac_val2_restr_by_pattern', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_property', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.item_property', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_characteristic_value2', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.supplier_characteristic_value2', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_net_price', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.total_net_price', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.quantity', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_characteristic_value1', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.supplier_characteristic_value1', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.currency_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currency_symbol', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.currency_symbol', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplier_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.supplier_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_description', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.node_description', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_net_price', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.unit_net_price', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='h_tree_node_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.h_tree_node_id', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_no', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.item_no', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.node_id', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.tree_node_id', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='suppl_charac_val1_restr_by_pattern', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.Row.suppl_charac_val1_restr_by_pattern', index=16,
      number=10016, type=11, cpp_type=10, label=1,
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
  serialized_start=886,
  serialized_end=1811,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetPurchasePrices_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetPurchasePrices_Ad.Response.row', index=2,
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
  serialized_start=708,
  serialized_end=1811,
)

_PARAMETERS.fields_by_name['tree_node_or_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['is_tree_node_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['supplier_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['date_for_property_determination'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['suppl_charac_val2_restr_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['item_property'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['supplier_characteristic_value2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['total_net_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['supplier_characteristic_value1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['currency_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['currency_symbol'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['supplier_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['node_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['unit_net_price'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['h_tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['item_no'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['suppl_charac_val1_restr_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetPurchasePrices_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPurchasePrices_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetPurchasePrices_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPurchasePrices_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetPurchasePrices_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPurchasePrices_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ9gosdk.dstore.de/engine/procedures/om_GetPurchasePrices_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
