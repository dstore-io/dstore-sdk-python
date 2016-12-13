# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_GetAllowedOrderStates.proto

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
  name='dstore/engine/procedures/om_GetAllowedOrderStates.proto',
  package='dstore.engine.om_GetAllowedOrderStates',
  syntax='proto3',
  serialized_pb=_b('\n7dstore/engine/procedures/om_GetAllowedOrderStates.proto\x12&dstore.engine.om_GetAllowedOrderStates\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xc1\x03\n\nParameters\x12\x38\n\x13\x66rom_order_state_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12!\n\x18\x66rom_order_state_id_null\x18\xe9\x07 \x01(\x08\x12\x36\n\x11to_order_state_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1f\n\x16to_order_state_id_null\x18\xea\x07 \x01(\x08\x12<\n\x17payment_for_shipping_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12%\n\x1cpayment_for_shipping_id_null\x18\xeb\x07 \x01(\x08\x12\x30\n\x0blanguage_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10language_id_null\x18\xec\x07 \x01(\x08\x12\x30\n\x0bonly_active\x18\x05 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x19\n\x10only_active_null\x18\xed\x07 \x01(\x08\"\xb0\x06\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x41\n\x03row\x18\x04 \x03(\x0b\x32\x34.dstore.engine.om_GetAllowedOrderStates.Response.Row\x1a\xe5\x04\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12:\n\x15to_public_description\x18\x91N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x37\n\x11to_order_state_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12=\n\x17payment_for_shipping_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x39\n\x13\x66rom_order_state_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12<\n\x17\x66rom_public_description\x18\x95N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x36\n\x10shipping_type_id\x18\x96N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x33\n\x0eto_order_state\x18\x97N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x45\n payment_for_shipping_description\x18\x98N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x35\n\x0fpayment_type_id\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x35\n\x10\x66rom_order_state\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.stringValueBY\n\x1bio.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_GetAllowedOrderStatesb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_GetAllowedOrderStates.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='from_order_state_id', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.from_order_state_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_order_state_id_null', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.from_order_state_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_order_state_id', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.to_order_state_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_order_state_id_null', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.to_order_state_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.payment_for_shipping_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id_null', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.payment_for_shipping_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.language_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id_null', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.language_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_active', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.only_active', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_active_null', full_name='dstore.engine.om_GetAllowedOrderStates.Parameters.only_active_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
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
  serialized_end=636,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_public_description', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.to_public_description', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_order_state_id', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.to_order_state_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_id', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.payment_for_shipping_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_order_state_id', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.from_order_state_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_public_description', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.from_public_description', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shipping_type_id', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.shipping_type_id', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_order_state', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.to_order_state', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_for_shipping_description', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.payment_for_shipping_description', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payment_type_id', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.payment_type_id', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_order_state', full_name='dstore.engine.om_GetAllowedOrderStates.Response.Row.from_order_state', index=10,
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
  serialized_start=842,
  serialized_end=1455,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_GetAllowedOrderStates.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_GetAllowedOrderStates.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_GetAllowedOrderStates.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_GetAllowedOrderStates.Response.row', index=2,
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
  serialized_start=639,
  serialized_end=1455,
)

_PARAMETERS.fields_by_name['from_order_state_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['to_order_state_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['payment_for_shipping_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['only_active'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['to_public_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['to_order_state_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['payment_for_shipping_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_order_state_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_public_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['shipping_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['to_order_state'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['payment_for_shipping_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['payment_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['from_order_state'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_GetAllowedOrderStates_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetAllowedOrderStates.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_GetAllowedOrderStates_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_GetAllowedOrderStates.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_GetAllowedOrderStates_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_GetAllowedOrderStates.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_GetAllowedOrderStates'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)