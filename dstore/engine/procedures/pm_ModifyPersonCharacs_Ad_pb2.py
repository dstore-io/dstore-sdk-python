# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_ModifyPersonCharacs_Ad.proto

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
  name='dstore/engine/procedures/pm_ModifyPersonCharacs_Ad.proto',
  package='dstore.engine.pm_ModifyPersonCharacs_Ad',
  syntax='proto3',
  serialized_pb=_b('\n8dstore/engine/procedures/pm_ModifyPersonCharacs_Ad.proto\x12\'dstore.engine.pm_ModifyPersonCharacs_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xa5\x07\n\nParameters\x12=\n\x18person_characteristic_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12&\n\x1dperson_characteristic_id_null\x18\xe9\x07 \x01(\x08\x12>\n\x1a\x63haracteristic_description\x18\x02 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12(\n\x1f\x63haracteristic_description_null\x18\xea\x07 \x01(\x08\x12\x32\n\rfield_type_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1b\n\x12\x66ield_type_id_null\x18\xeb\x07 \x01(\x08\x12,\n\x07sort_no\x18\x04 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x15\n\x0csort_no_null\x18\xec\x07 \x01(\x08\x12-\n\x08required\x18\x05 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x16\n\rrequired_null\x18\xed\x07 \x01(\x08\x12,\n\x07visible\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x15\n\x0cvisible_null\x18\xee\x07 \x01(\x08\x12+\n\x06modify\x18\x07 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x14\n\x0bmodify_null\x18\xef\x07 \x01(\x08\x12\x36\n\x11predefined_values\x18\x08 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x1f\n\x16predefined_values_null\x18\xf0\x07 \x01(\x08\x12.\n\tis_unique\x18\t \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x17\n\x0eis_unique_null\x18\xf1\x07 \x01(\x08\x12:\n\x15\x64\x65lete_characteristic\x18\n \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12#\n\x1a\x64\x65lete_characteristic_null\x18\xf2\x07 \x01(\x08\x12\x39\n\x15\x64\x65scription_for_admin\x18\x0b \x01(\x0b\x32\x1a.dstore.values.stringValue\x12#\n\x1a\x64\x65scription_for_admin_null\x18\xf3\x07 \x01(\x08\"\xe1\x01\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x42\n\x03row\x18\x04 \x03(\x0b\x32\x35.dstore.engine.pm_ModifyPersonCharacs_Ad.Response.Row\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42Z\n\x1bio.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/pm_ModifyPersonCharacs_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_characteristic_id', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.person_characteristic_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_characteristic_id_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.person_characteristic_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_description', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.characteristic_description', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_description_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.characteristic_description_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type_id', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.field_type_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type_id_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.field_type_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.sort_no', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.sort_no_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.required', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.required_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.visible', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.visible_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modify', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.modify', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modify_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.modify_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predefined_values', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.predefined_values', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predefined_values_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.predefined_values_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_unique', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.is_unique', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_unique_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.is_unique_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_characteristic', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.delete_characteristic', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_characteristic_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.delete_characteristic_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_for_admin', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.description_for_admin', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_for_admin_null', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters.description_for_admin_null', index=21,
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
  serialized_start=189,
  serialized_end=1122,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Response.Row.row_id', index=0,
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
  serialized_start=1328,
  serialized_end=1350,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_ModifyPersonCharacs_Ad.Response.row', index=2,
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
  serialized_start=1125,
  serialized_end=1350,
)

_PARAMETERS.fields_by_name['person_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['characteristic_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['field_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['required'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['visible'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['modify'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['predefined_values'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['is_unique'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['delete_characteristic'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['description_for_admin'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_ModifyPersonCharacs_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_ModifyPersonCharacs_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_ModifyPersonCharacs_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_ModifyPersonCharacs_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_ModifyPersonCharacs_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_ModifyPersonCharacs_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/pm_ModifyPersonCharacs_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
