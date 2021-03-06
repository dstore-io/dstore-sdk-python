# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/co_GetMemberInformation_Pu.proto

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
  name='dstore/engine/procedures/co_GetMemberInformation_Pu.proto',
  package='dstore.engine.co_GetMemberInformation_Pu',
  syntax='proto3',
  serialized_pb=_b('\n9dstore/engine/procedures/co_GetMemberInformation_Pu.proto\x12(dstore.engine.co_GetMemberInformation_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xb8\x06\n\nParameters\x12-\n\tunique_id\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xe9\x07 \x01(\x08\x12@\n\x1cperson_identification_values\x18\x02 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n!person_identification_values_null\x18\xea\x07 \x01(\x08\x12\x31\n\x0c\x63ommunity_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1a\n\x11\x63ommunity_id_null\x18\xeb\x07 \x01(\x08\x12\x45\n get_info_for_community_member_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n%get_info_for_community_member_id_null\x18\xec\x07 \x01(\x08\x12:\n\x16\x63haracteristic_id_list\x18\x05 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12$\n\x1b\x63haracteristic_id_list_null\x18\xed\x07 \x01(\x08\x12\x32\n\rsorted_result\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1b\n\x12sorted_result_null\x18\xee\x07 \x01(\x08\x12/\n\x0b\x64\x61te_format\x18\x07 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x19\n\x10\x64\x61te_format_null\x18\xef\x07 \x01(\x08\x12\x30\n\x0bget_details\x18\x08 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x19\n\x10get_details_null\x18\xf0\x07 \x01(\x08\x12;\n\x17separator_in_ident_vals\x18\t \x01(\x0b\x32\x1a.dstore.values.StringValue\x12%\n\x1cseparator_in_ident_vals_null\x18\xf1\x07 \x01(\x08\"\x92\x04\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x43\n\x03row\x18\x04 \x03(\x0b\x32\x36.dstore.engine.co_GetMemberInformation_Pu.Response.Row\x1a\xdd\x02\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12@\n\x1bvalue_restricted_by_pattern\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12?\n\x1a\x63haracteristic_description\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n\x05value\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x37\n\x11\x63haracteristic_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\x08value_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07\x64\x65tails\x18\xa1\x9c\x01 \x01(\x0b\x32\x1a.dstore.values.StringValueB[\n\x1bio.dstore.engine.proceduresZ<gosdk.dstore.de/engine/procedures/co_GetMemberInformation_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.unique_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.unique_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_identification_values', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.person_identification_values', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_identification_values_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.person_identification_values_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='community_id', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.community_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='community_id_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.community_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_info_for_community_member_id', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.get_info_for_community_member_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_info_for_community_member_id_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.get_info_for_community_member_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.characteristic_id_list', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.characteristic_id_list_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorted_result', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.sorted_result', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorted_result_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.sorted_result_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_format', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.date_format', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_format_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.date_format_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_details', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.get_details', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_details_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.get_details_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.separator_in_ident_vals', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals_null', full_name='dstore.engine.co_GetMemberInformation_Pu.Parameters.separator_in_ident_vals_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
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
  serialized_start=153,
  serialized_end=977,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_restricted_by_pattern', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.value_restricted_by_pattern', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_description', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.characteristic_description', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.value', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.characteristic_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_id', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.value_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='details', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.Row.details', index=6,
      number=20001, type=11, cpp_type=10, label=1,
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
  serialized_start=1161,
  serialized_end=1510,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.co_GetMemberInformation_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.co_GetMemberInformation_Pu.Response.row', index=2,
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
  serialized_start=980,
  serialized_end=1510,
)

_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_identification_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['community_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_info_for_community_member_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['characteristic_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['sorted_result'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['date_format'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['get_details'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['separator_in_ident_vals'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value_restricted_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['characteristic_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['details'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.co_GetMemberInformation_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.co_GetMemberInformation_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.co_GetMemberInformation_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.co_GetMemberInformation_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.co_GetMemberInformation_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.co_GetMemberInformation_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ<gosdk.dstore.de/engine/procedures/co_GetMemberInformation_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
