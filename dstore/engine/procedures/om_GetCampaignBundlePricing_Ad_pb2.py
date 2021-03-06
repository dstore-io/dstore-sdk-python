# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetCampaignBundlePricing_Ad.proto

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
  name='dstore/engine/procedures/om_GetCampaignBundlePricing_Ad.proto',
  package='dstore.engine.om_GetCampaignBundlePricing_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/om_GetCampaignBundlePricing_Ad.proto\x12,dstore.engine.om_GetCampaignBundlePricing_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xfd\x01\n\nParameters\x12\x30\n\x0b\x63\x61mpaign_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10\x63\x61mpaign_id_null\x18\xe9\x07 \x01(\x08\x12/\n\nbenefit_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0f\x62\x65nefit_id_null\x18\xea\x07 \x01(\x08\x12\x36\n\x11get_assigned_sets\x18\x03 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1f\n\x16get_assigned_sets_null\x18\xeb\x07 \x01(\x08\"\xbb\x06\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row\x1a\x82\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x37\n\x11net_based_pricing\x18\x91N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x30\n\nbenefit_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12<\n\x16\x62undle_pricing_type_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x34\n\x0etotal_quantity\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12>\n\x18\x62undle_price_or_discount\x18\x95N \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x38\n\x11item_condition_id\x18\xa2\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0bitem_set_id\x18\xa6\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12/\n\x08quantity\x18\xa7\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12:\n\x13\x64istinct_items_only\x18\xa8\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12@\n\x1aitem_condition_description\x18\xa9\x9c\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12.\n\x07sort_no\x18\xaa\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValueB_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_GetCampaignBundlePricing_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='campaign_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters.campaign_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='campaign_id_null', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters.campaign_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters.benefit_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_id_null', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters.benefit_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_assigned_sets', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters.get_assigned_sets', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_assigned_sets_null', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters.get_assigned_sets_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
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
  serialized_end=414,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='net_based_pricing', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.net_based_pricing', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.benefit_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_pricing_type_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.bundle_pricing_type_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_quantity', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.total_quantity', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_price_or_discount', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.bundle_price_or_discount', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.item_condition_id', index=6,
      number=20002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_set_id', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.item_set_id', index=7,
      number=20006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='quantity', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.quantity', index=8,
      number=20007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='distinct_items_only', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.distinct_items_only', index=9,
      number=20008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_condition_description', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.item_condition_description', index=10,
      number=20009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row.sort_no', index=11,
      number=20010, type=11, cpp_type=10, label=1,
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
  serialized_start=602,
  serialized_end=1244,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetCampaignBundlePricing_Ad.Response.row', index=2,
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
  serialized_start=417,
  serialized_end=1244,
)

_PARAMETERS.fields_by_name['campaign_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['benefit_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_assigned_sets'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['net_based_pricing'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['benefit_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['bundle_pricing_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['total_quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['bundle_price_or_discount'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['item_condition_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['item_set_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['quantity'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['distinct_items_only'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['item_condition_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetCampaignBundlePricing_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetCampaignBundlePricing_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetCampaignBundlePricing_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetCampaignBundlePricing_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetCampaignBundlePricing_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetCampaignBundlePricing_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_GetCampaignBundlePricing_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
