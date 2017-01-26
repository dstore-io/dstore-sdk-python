# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetPaymentAndShipping_Pu.proto

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
  name='dstore/engine/procedures/om_GetPaymentAndShipping_Pu.proto',
  package='dstore.engine.om_GetPaymentAndShipping_Pu',
  syntax='proto3',
  serialized_pb=_b('\n:dstore/engine/procedures/om_GetPaymentAndShipping_Pu.proto\x12)dstore.engine.om_GetPaymentAndShipping_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xb9\x06\n\nParameters\x12+\n\x06result\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x14\n\x0bresult_null\x18\xe9\x07 \x01(\x08\x12-\n\tunique_id\x18\x02 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xea\x07 \x01(\x08\x12.\n\tperson_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xeb\x07 \x01(\x08\x12\x37\n\x12\x64\x65livery_person_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17\x64\x65livery_person_id_null\x18\xec\x07 \x01(\x08\x12/\n\nbrutto_sum\x18\x05 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x18\n\x0f\x62rutto_sum_null\x18\xed\x07 \x01(\x08\x12.\n\tnetto_sum\x18\x06 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x17\n\x0enetto_sum_null\x18\xee\x07 \x01(\x08\x12<\n\x17payment_for_shipping_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12%\n\x1cpayment_for_shipping_id_null\x18\xef\x07 \x01(\x08\x12+\n\x04\x64\x61te\x18\x08 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x12\n\tdate_null\x18\xf0\x07 \x01(\x08\x12\x41\n\x1cselect_missing_result_reason\x18\t \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12*\n!select_missing_result_reason_null\x18\xf1\x07 \x01(\x08\x12\x34\n\x0f\x63\x61lculate_costs\x18\n \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1d\n\x14\x63\x61lculate_costs_null\x18\xf2\x07 \x01(\x08\"\x96\x07\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x44\n\x03row\x18\x04 \x03(\x0b\x32\x37.dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row\x1a\xe0\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12<\n\x16region_id_payment_type\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12=\n\x17payment_for_shipping_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x36\n\x10shipping_type_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x45\n payment_for_shipping_description\x18\x94N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0fpayment_type_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12=\n\x17region_id_shipping_type\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x19person_charac_category_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x31\n\nerror_code\x18\xa1\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x33\n\x0cpayment_cost\x18\xb1\xea\x01 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12\x34\n\rshipping_cost\x18\xb4\xea\x01 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12;\n\x14shipping_cost_brutto\x18\xb9\xea\x01 \x01(\x0b\x32\x1b.dstore.values.DecimalValue\x12:\n\x13payment_cost_brutto\x18\xba\xea\x01 \x01(\x0b\x32\x1b.dstore.values.DecimalValueB\\\n\x1bio.dstore.engine.proceduresZ=gosdk.dstore.de/engine/procedures/om_GetPaymentAndShipping_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.result', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.result_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.unique_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.unique_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.person_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.person_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.delivery_person_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delivery_person_id_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.delivery_person_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brutto_sum', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.brutto_sum', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='brutto_sum_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.brutto_sum_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='netto_sum', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.netto_sum', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='netto_sum_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.netto_sum_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.payment_for_shipping_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.payment_for_shipping_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.date', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.date_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='select_missing_result_reason', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.select_missing_result_reason', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='select_missing_result_reason_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.select_missing_result_reason_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculate_costs', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.calculate_costs', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='calculate_costs_null', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Parameters.calculate_costs_null', index=19,
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
  serialized_start=155,
  serialized_end=980,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='region_id_payment_type', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.region_id_payment_type', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.payment_for_shipping_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.shipping_type_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_description', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.payment_for_shipping_description', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.payment_type_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='region_id_shipping_type', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.region_id_shipping_type', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.person_charac_category_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_code', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.error_code', index=8,
      number=20001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_cost', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.payment_cost', index=9,
      number=30001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_cost', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.shipping_cost', index=10,
      number=30004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_cost_brutto', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.shipping_cost_brutto', index=11,
      number=30009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_cost_brutto', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row.payment_cost_brutto', index=12,
      number=30010, type=11, cpp_type=10, label=1,
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
  serialized_start=1165,
  serialized_end=1901,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetPaymentAndShipping_Pu.Response.row', index=2,
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
  serialized_start=983,
  serialized_end=1901,
)

_PARAMETERS.fields_by_name['result'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delivery_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['brutto_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['netto_sum'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['payment_for_shipping_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['select_missing_result_reason'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['calculate_costs'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['region_id_payment_type'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['payment_for_shipping_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['payment_for_shipping_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['region_id_shipping_type'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['person_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['error_code'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['payment_cost'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['shipping_cost'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['shipping_cost_brutto'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.fields_by_name['payment_cost_brutto'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetPaymentAndShipping_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPaymentAndShipping_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetPaymentAndShipping_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPaymentAndShipping_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetPaymentAndShipping_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPaymentAndShipping_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ=gosdk.dstore.de/engine/procedures/om_GetPaymentAndShipping_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
