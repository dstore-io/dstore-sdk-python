# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/co_CreateNewCommunityMember_Pu.proto

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
  name='dstore/engine/procedures/co_CreateNewCommunityMember_Pu.proto',
  package='dstore.engine.co_CreateNewCommunityMember_Pu',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/co_CreateNewCommunityMember_Pu.proto\x12,dstore.engine.co_CreateNewCommunityMember_Pu\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xb6\x08\n\nParameters\x12\x31\n\x0c\x63ommunity_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1a\n\x11\x63ommunity_id_null\x18\xe9\x07 \x01(\x08\x12-\n\tunique_id\x18\x02 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0eunique_id_null\x18\xea\x07 \x01(\x08\x12;\n\x17\x63haracteristic_id_list1\x18\x03 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12%\n\x1c\x63haracteristic_id_list1_null\x18\xeb\x07 \x01(\x08\x12/\n\x0bvalue_list1\x18\x04 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x19\n\x10value_list1_null\x18\xec\x07 \x01(\x08\x12;\n\x17\x63haracteristic_id_list2\x18\x05 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12%\n\x1c\x63haracteristic_id_list2_null\x18\xed\x07 \x01(\x08\x12/\n\x0bvalue_list2\x18\x06 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x19\n\x10value_list2_null\x18\xee\x07 \x01(\x08\x12>\n\x19person_charac_category_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\'\n\x1eperson_charac_category_id_null\x18\xef\x07 \x01(\x08\x12.\n\tperson_id\x18\x08 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x17\n\x0eperson_id_null\x18\xf0\x07 \x01(\x08\x12\x31\n\rerror_id_list\x18\t \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x1b\n\x12\x65rror_id_list_null\x18\xf1\x07 \x01(\x08\x12<\n\x17result_in_error_id_list\x18\n \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12%\n\x1cresult_in_error_id_list_null\x18\xf2\x07 \x01(\x08\x12\x45\n value_ids_for_predefined_characs\x18\x0b \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12.\n%value_ids_for_predefined_characs_null\x18\xf3\x07 \x01(\x08\x12\x34\n\x0f\x63\x61ncel_on_error\x18\x0c \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x1d\n\x14\x63\x61ncel_on_error_null\x18\xf4\x07 \x01(\x08\"\xbd\x03\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.co_CreateNewCommunityMember_Pu.Response.Row\x12.\n\tperson_id\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x31\n\rerror_id_list\x18\x66 \x01(\x0b\x32\x1a.dstore.values.stringValue\x1a\x89\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12>\n\x18person_characteristic_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x31\n\x0bresult_code\x18\x92N \x01(\x0b\x32\x1b.dstore.values.integerValueB_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/co_CreateNewCommunityMember_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='community_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.community_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='community_id_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.community_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.unique_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.unique_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list1', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.characteristic_id_list1', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list1_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.characteristic_id_list1_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_list1', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.value_list1', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_list1_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.value_list1_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list2', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.characteristic_id_list2', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list2_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.characteristic_id_list2_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_list2', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.value_list2', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_list2_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.value_list2_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.person_charac_category_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.person_charac_category_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.person_id', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.person_id_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_id_list', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.error_id_list', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_id_list_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.error_id_list_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_in_error_id_list', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.result_in_error_id_list', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_in_error_id_list_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.result_in_error_id_list_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_ids_for_predefined_characs', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.value_ids_for_predefined_characs', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_ids_for_predefined_characs_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.value_ids_for_predefined_characs_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cancel_on_error', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.cancel_on_error', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cancel_on_error_null', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Parameters.cancel_on_error_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
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
  serialized_end=1277,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_characteristic_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.Row.person_characteristic_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.Row.result_code', index=2,
      number=10002, type=11, cpp_type=10, label=1,
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
  serialized_start=1588,
  serialized_end=1725,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.person_id', index=3,
      number=101, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_id_list', full_name='dstore.engine.co_CreateNewCommunityMember_Pu.Response.error_id_list', index=4,
      number=102, type=11, cpp_type=10, label=1,
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
  serialized_start=1280,
  serialized_end=1725,
)

_PARAMETERS.fields_by_name['community_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['characteristic_id_list1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['value_list1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['characteristic_id_list2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['value_list2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['error_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['result_in_error_id_list'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['value_ids_for_predefined_characs'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['cancel_on_error'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['person_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['result_code'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE.fields_by_name['error_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.co_CreateNewCommunityMember_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.co_CreateNewCommunityMember_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.co_CreateNewCommunityMember_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.co_CreateNewCommunityMember_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.co_CreateNewCommunityMember_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.co_CreateNewCommunityMember_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/co_CreateNewCommunityMember_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)