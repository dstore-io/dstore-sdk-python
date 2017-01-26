# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_GetPersonRelationships_Ad.proto

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
  name='dstore/engine/procedures/pm_GetPersonRelationships_Ad.proto',
  package='dstore.engine.pm_GetPersonRelationships_Ad',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/pm_GetPersonRelationships_Ad.proto\x12*dstore.engine.pm_GetPersonRelationships_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xeb\x04\n\nParameters\x12.\n\tperson_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xe9\x07 \x01(\x08\x12\x36\n\x11related_person_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1f\n\x16related_person_id_null\x18\xea\x07 \x01(\x08\x12\x34\n\x0frelationship_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1d\n\x14relationship_id_null\x18\xeb\x07 \x01(\x08\x12\x30\n\tfrom_date\x18\x04 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x17\n\x0e\x66rom_date_null\x18\xec\x07 \x01(\x08\x12.\n\x07to_date\x18\x05 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x15\n\x0cto_date_null\x18\xed\x07 \x01(\x08\x12\x43\n\x1eonly_relations_currently_valid\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12,\n#only_relations_currently_valid_null\x18\xee\x07 \x01(\x08\x12;\n\x16related_person_type_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12$\n\x1brelated_person_type_id_null\x18\xef\x07 \x01(\x08\"\xe9\x05\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.pm_GetPersonRelationships_Ad.Response.Row\x1a\xb2\x04\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x37\n\x11related_person_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12/\n\tperson_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x35\n\x0frelationship_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x46\n person_type_id_of_related_person\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x30\n\x08valid_to\x18\x95N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x32\n\rvalid_to_char\x18\x96N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x32\n\nvalid_from\x18\x97N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12-\n\x07sort_no\x18\x98N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0c\x61\x63\x63\x65ss_level\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x34\n\x0fvalid_from_char\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.StringValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/pm_GetPersonRelationships_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.person_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.person_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.related_person_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.related_person_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.relationship_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.relationship_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.from_date', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.from_date_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.to_date', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.to_date_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_relations_currently_valid', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.only_relations_currently_valid', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_relations_currently_valid_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.only_relations_currently_valid_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_type_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.related_person_type_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_type_id_null', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Parameters.related_person_type_id_null', index=13,
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
  serialized_start=157,
  serialized_end=776,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='related_person_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.related_person_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.person_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relationship_id', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.relationship_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_of_related_person', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.person_type_id_of_related_person', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_to', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.valid_to', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_to_char', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.valid_to_char', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_from', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.valid_from', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.sort_no', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='access_level', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.access_level', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='valid_from_char', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.Row.valid_from_char', index=10,
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
  serialized_start=962,
  serialized_end=1524,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_GetPersonRelationships_Ad.Response.row', index=2,
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
  serialized_start=779,
  serialized_end=1524,
)

_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['related_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['relationship_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['from_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['to_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['only_relations_currently_valid'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['related_person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['related_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['relationship_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['person_type_id_of_related_person'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['valid_to'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['valid_to_char'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['valid_from'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['access_level'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['valid_from_char'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_GetPersonRelationships_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonRelationships_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_GetPersonRelationships_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonRelationships_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_GetPersonRelationships_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonRelationships_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/pm_GetPersonRelationships_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
