# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetPaymentForShipping_Ad.proto

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
  name='dstore/engine/procedures/om_GetPaymentForShipping_Ad.proto',
  package='dstore.engine.om_GetPaymentForShipping_Ad',
  syntax='proto3',
  serialized_pb=_b('\n:dstore/engine/procedures/om_GetPaymentForShipping_Ad.proto\x12)dstore.engine.om_GetPaymentForShipping_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\x85\x02\n\nParameters\x12\x30\n\x0blanguage_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10language_id_null\x18\xe9\x07 \x01(\x08\x12\x34\n\x0fpayment_type_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1d\n\x14payment_type_id_null\x18\xea\x07 \x01(\x08\x12\x35\n\x10shipping_type_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1e\n\x15shipping_type_id_null\x18\xeb\x07 \x01(\x08\"\xd2\x06\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x44\n\x03row\x18\x04 \x03(\x0b\x32\x37.dstore.engine.om_GetPaymentForShipping_Ad.Response.Row\x1a\x84\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x44\n\x1ftranslated_detailed_description\x18\x91N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12=\n\x18payment_type_description\x18\x92N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12;\n\x16translated_description\x18\x93N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12=\n\x17payment_for_shipping_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12:\n\x15\x64\x65scription_for_admin\x18\x95N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12>\n\x19shipping_type_description\x18\x96N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x36\n\x10shipping_type_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x45\n payment_for_shipping_description\x18\x98N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x35\n\x0fpayment_type_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x14\x64\x65tailed_description\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.stringValueB\\\n\x1bio.dstore.engine.proceduresZ=gosdk.dstore.de/engine/procedures/om_GetPaymentForShipping_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters.language_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id_null', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters.language_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters.payment_type_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id_null', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters.payment_type_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters.shipping_type_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id_null', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Parameters.shipping_type_id_null', index=5,
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
  serialized_start=193,
  serialized_end=454,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translated_detailed_description', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.translated_detailed_description', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_description', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.payment_type_description', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='translated_description', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.translated_description', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.payment_for_shipping_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_for_admin', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.description_for_admin', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_description', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.shipping_type_description', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.shipping_type_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_description', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.payment_for_shipping_description', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.payment_type_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detailed_description', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.Row.detailed_description', index=10,
      number=10010, type=11, cpp_type=10, label=1,
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
  serialized_start=663,
  serialized_end=1307,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetPaymentForShipping_Ad.Response.row', index=2,
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
  serialized_start=457,
  serialized_end=1307,
)

_PARAMETERS.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['translated_detailed_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['payment_type_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['translated_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['payment_for_shipping_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['description_for_admin'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['shipping_type_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['payment_for_shipping_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['detailed_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetPaymentForShipping_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPaymentForShipping_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetPaymentForShipping_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPaymentForShipping_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetPaymentForShipping_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetPaymentForShipping_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ=gosdk.dstore.de/engine/procedures/om_GetPaymentForShipping_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
