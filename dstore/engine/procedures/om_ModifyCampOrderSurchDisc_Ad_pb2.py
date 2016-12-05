# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_ModifyCampOrderSurchDisc_Ad.proto

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
  name='dstore/engine/procedures/om_ModifyCampOrderSurchDisc_Ad.proto',
  package='dstore.engine.om_ModifyCampOrderSurchDisc_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/om_ModifyCampOrderSurchDisc_Ad.proto\x12,dstore.engine.om_ModifyCampOrderSurchDisc_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xd3\x03\n\nParameters\x12/\n\nbenefit_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x18\n\x0f\x62\x65nefit_id_null\x18\xe9\x07 \x01(\x08\x12?\n\x1a\x61pply_to_surcharge_type_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12(\n\x1f\x61pply_to_surcharge_type_id_null\x18\xea\x07 \x01(\x08\x12?\n\x1a\x64iscount_surcharge_type_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12(\n\x1f\x64iscount_surcharge_type_id_null\x18\xeb\x07 \x01(\x08\x12\x33\n\x0e\x64iscount_value\x18\x04 \x01(\x0b\x32\x1b.dstore.values.decimalValue\x12\x1c\n\x13\x64iscount_value_null\x18\xec\x07 \x01(\x08\x12\x33\n\x0e\x64\x65lete_benefit\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1c\n\x13\x64\x65lete_benefit_null\x18\xed\x07 \x01(\x08\"\x97\x02\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.Row\x12/\n\nbenefit_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_ModifyCampOrderSurchDisc_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='benefit_id', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.benefit_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_id_null', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.benefit_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply_to_surcharge_type_id', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.apply_to_surcharge_type_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='apply_to_surcharge_type_id_null', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.apply_to_surcharge_type_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='discount_surcharge_type_id', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.discount_surcharge_type_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='discount_surcharge_type_id_null', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.discount_surcharge_type_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='discount_value', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.discount_value', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='discount_value_null', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.discount_value_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_benefit', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.delete_benefit', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_benefit_null', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters.delete_benefit_null', index=9,
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
  serialized_start=199,
  serialized_end=666,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.Row.row_id', index=0,
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
  serialized_start=926,
  serialized_end=948,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_id', full_name='dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.benefit_id', index=3,
      number=101, type=11, cpp_type=10, label=1,
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
  serialized_start=669,
  serialized_end=948,
)

_PARAMETERS.fields_by_name['benefit_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['apply_to_surcharge_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['discount_surcharge_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['discount_value'].message_type = dstore_dot_values__pb2._DECIMALVALUE
_PARAMETERS.fields_by_name['delete_benefit'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['benefit_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_ModifyCampOrderSurchDisc_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_ModifyCampOrderSurchDisc_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_ModifyCampOrderSurchDisc_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_ModifyCampOrderSurchDisc_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/om_ModifyCampOrderSurchDisc_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
