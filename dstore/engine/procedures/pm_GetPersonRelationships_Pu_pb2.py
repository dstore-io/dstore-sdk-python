# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_GetPersonRelationships_Pu.proto

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
  name='dstore/engine/procedures/pm_GetPersonRelationships_Pu.proto',
  package='dstore.engine.pm_GetPersonRelationships_Pu',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/pm_GetPersonRelationships_Pu.proto\x12*dstore.engine.pm_GetPersonRelationships_Pu\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xa1\x05\n\nParameters\x12@\n\x1cperson_identification_values\x18\x01 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12*\n!person_identification_values_null\x18\xe9\x07 \x01(\x08\x12\x33\n\x0eperson_type_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1c\n\x13person_type_id_null\x18\xea\x07 \x01(\x08\x12-\n\tunique_id\x18\x03 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0eunique_id_null\x18\xeb\x07 \x01(\x08\x12;\n\x16related_person_type_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12$\n\x1brelated_person_type_id_null\x18\xec\x07 \x01(\x08\x12\x34\n\x0frelationship_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1d\n\x14relationship_id_null\x18\xed\x07 \x01(\x08\x12\x41\n\x1doutput_characteristic_id_list\x18\x06 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12+\n\"output_characteristic_id_list_null\x18\xee\x07 \x01(\x08\x12;\n\x17separator_in_ident_vals\x18\x07 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12%\n\x1cseparator_in_ident_vals_null\x18\xef\x07 \x01(\x08\"\xc2\x07\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.pm_GetPersonRelationships_Pu.Response.Row\x1a\xf3\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x37\n\x11output_charac_id3\x18\x91N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x41\n\x1cvalue1_restricted_by_pattern\x18\x92N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x37\n\x11related_person_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x41\n\x1cvalue2_restricted_by_pattern\x18\x94N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12+\n\x06value3\x18\x95N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12+\n\x06value1\x18\x96N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12+\n\x06value2\x18\x97N \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x32\n\x0c\x61\x63\x63\x65ss_level\x18\x98N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x37\n\x11output_charac_id1\x18\x99N \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x37\n\x11output_charac_id2\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12<\n\x16related_person_type_id\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x35\n\x0frelationship_id\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x41\n\x1cvalue3_restricted_by_pattern\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.stringValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/pm_GetPersonRelationships_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_identification_values', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.person_identification_values', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_identification_values_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.person_identification_values_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.person_type_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.person_type_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.unique_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.unique_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_type_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.related_person_type_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_type_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.related_person_type_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.relationship_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.relationship_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_characteristic_id_list', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.output_characteristic_id_list', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_characteristic_id_list_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.output_characteristic_id_list_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.separator_in_ident_vals', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals_null', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Parameters.separator_in_ident_vals_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
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
  serialized_start=195,
  serialized_end=868,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_charac_id3', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.output_charac_id3', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value1_restricted_by_pattern', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.value1_restricted_by_pattern', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.related_person_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value2_restricted_by_pattern', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.value2_restricted_by_pattern', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value3', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.value3', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value1', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.value1', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value2', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.value2', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access_level', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.access_level', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_charac_id1', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.output_charac_id1', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_charac_id2', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.output_charac_id2', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_type_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.related_person_type_id', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship_id', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.relationship_id', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value3_restricted_by_pattern', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.Row.value3_restricted_by_pattern', index=13,
      number=10013, type=11, cpp_type=10, label=1,
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
  serialized_start=1078,
  serialized_end=1833,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_GetPersonRelationships_Pu.Response.row', index=2,
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
  serialized_start=871,
  serialized_end=1833,
)

_PARAMETERS.fields_by_name['person_identification_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['related_person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['relationship_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['output_characteristic_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['separator_in_ident_vals'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['output_charac_id3'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value1_restricted_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['related_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value2_restricted_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value3'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value1'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value2'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['access_level'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['output_charac_id1'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['output_charac_id2'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['related_person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['relationship_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value3_restricted_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_GetPersonRelationships_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonRelationships_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_GetPersonRelationships_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonRelationships_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_GetPersonRelationships_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonRelationships_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/pm_GetPersonRelationships_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
