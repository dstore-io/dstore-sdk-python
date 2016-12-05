# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/om_ModifyVoucherTypes_Ad.proto

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
  name='dstore/engine/procedures/om_ModifyVoucherTypes_Ad.proto',
  package='dstore.engine.om_ModifyVoucherTypes_Ad',
  syntax='proto3',
  serialized_pb=_b('\n7dstore/engine/procedures/om_ModifyVoucherTypes_Ad.proto\x12&dstore.engine.om_ModifyVoucherTypes_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xd9\x07\n\nParameters\x12\x34\n\x0fvoucher_type_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1d\n\x14voucher_type_id_null\x18\xe9\x07 \x01(\x08\x12/\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x19\n\x10\x64\x65scription_null\x18\xea\x07 \x01(\x08\x12:\n\x15v_code_origin_type_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12#\n\x1av_code_origin_type_id_null\x18\xeb\x07 \x01(\x08\x12\x36\n\x12generation_pattern\x18\x04 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12 \n\x17generation_pattern_null\x18\xec\x07 \x01(\x08\x12\x34\n\x0f\x62\x65nefit_type_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1d\n\x14\x62\x65nefit_type_id_null\x18\xed\x07 \x01(\x08\x12\x35\n\x10valid_for_x_days\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1e\n\x15valid_for_x_days_null\x18\xee\x07 \x01(\x08\x12:\n\x13\x64\x65\x66\x61ult_valid_until\x18\x07 \x01(\x0b\x32\x1d.dstore.values.timestampValue\x12!\n\x18\x64\x65\x66\x61ult_valid_until_null\x18\xef\x07 \x01(\x08\x12\x30\n\x0b\x63ode_status\x18\x08 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x19\n\x10\x63ode_status_null\x18\xf0\x07 \x01(\x08\x12\x33\n\x0ex_times_usable\x18\t \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1c\n\x13x_times_usable_null\x18\xf1\x07 \x01(\x08\x12>\n\x19x_times_usable_per_person\x18\n \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\'\n\x1ex_times_usable_per_person_null\x18\xf2\x07 \x01(\x08\x12\x38\n\x13\x64\x65lete_voucher_type\x18\x0b \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12!\n\x18\x64\x65lete_voucher_type_null\x18\xf3\x07 \x01(\x08\"\x96\x02\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x41\n\x03row\x18\x04 \x03(\x0b\x32\x34.dstore.engine.om_ModifyVoucherTypes_Ad.Response.Row\x12\x34\n\x0fvoucher_type_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42Y\n\x1bio.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_ModifyVoucherTypes_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='voucher_type_id', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.voucher_type_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voucher_type_id_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.voucher_type_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.description', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.description_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_code_origin_type_id', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.v_code_origin_type_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_code_origin_type_id_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.v_code_origin_type_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generation_pattern', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.generation_pattern', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generation_pattern_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.generation_pattern_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_type_id', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.benefit_type_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='benefit_type_id_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.benefit_type_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_for_x_days', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.valid_for_x_days', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_for_x_days_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.valid_for_x_days_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_valid_until', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.default_valid_until', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_valid_until_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.default_valid_until_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code_status', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.code_status', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='code_status_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.code_status_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_times_usable', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.x_times_usable', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_times_usable_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.x_times_usable_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_times_usable_per_person', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.x_times_usable_per_person', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x_times_usable_per_person_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.x_times_usable_per_person_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_voucher_type', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.delete_voucher_type', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_voucher_type_null', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Parameters.delete_voucher_type_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
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
  serialized_end=1172,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response.Row.row_id', index=0,
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
  serialized_start=1431,
  serialized_end=1453,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='voucher_type_id', full_name='dstore.engine.om_ModifyVoucherTypes_Ad.Response.voucher_type_id', index=3,
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
  serialized_start=1175,
  serialized_end=1453,
)

_PARAMETERS.fields_by_name['voucher_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['v_code_origin_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['generation_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['benefit_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['valid_for_x_days'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['default_valid_until'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['code_status'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['x_times_usable'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['x_times_usable_per_person'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delete_voucher_type'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['voucher_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.om_ModifyVoucherTypes_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_ModifyVoucherTypes_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.om_ModifyVoucherTypes_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.om_ModifyVoucherTypes_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.om_ModifyVoucherTypes_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.om_ModifyVoucherTypes_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ:gosdk.dstore.de/engine/procedures/om_ModifyVoucherTypes_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
