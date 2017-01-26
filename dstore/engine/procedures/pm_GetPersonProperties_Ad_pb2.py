# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_GetPersonProperties_Ad.proto

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
  name='dstore/engine/procedures/pm_GetPersonProperties_Ad.proto',
  package='dstore.engine.pm_GetPersonProperties_Ad',
  syntax='proto3',
  serialized_pb=_b('\n8dstore/engine/procedures/pm_GetPersonProperties_Ad.proto\x12\'dstore.engine.pm_GetPersonProperties_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\x83\n\n\nParameters\x12.\n\tperson_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xe9\x07 \x01(\x08\x12\x30\n\x0blanguage_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x19\n\x10language_id_null\x18\xea\x07 \x01(\x08\x12:\n\x16\x63haracteristic_id_list\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12$\n\x1b\x63haracteristic_id_list_null\x18\xeb\x07 \x01(\x08\x12/\n\x0b\x64\x61te_format\x18\x04 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x19\n\x10\x64\x61te_format_null\x18\xec\x07 \x01(\x08\x12>\n\x19person_charac_category_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\'\n\x1eperson_charac_category_id_null\x18\xed\x07 \x01(\x08\x12\x43\n\x1einclude_creation_date_and_time\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12,\n#include_creation_date_and_time_null\x18\xee\x07 \x01(\x08\x12\x46\n!include_person_charac_category_id\x18\x07 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12/\n&include_person_charac_category_id_null\x18\xef\x07 \x01(\x08\x12\x34\n\rdate_and_time\x18\x08 \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x1b\n\x12\x64\x61te_and_time_null\x18\xf0\x07 \x01(\x08\x12:\n\x15get_actual_properties\x18\t \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12#\n\x1aget_actual_properties_null\x18\xf1\x07 \x01(\x08\x12<\n\x17get_person_type_id_only\x18\n \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12%\n\x1cget_person_type_id_only_null\x18\xf2\x07 \x01(\x08\x12\x44\n\x1fignore_bad_person_ids_in_one_id\x18\x0b \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12-\n$ignore_bad_person_ids_in_one_id_null\x18\xf3\x07 \x01(\x08\x12\x46\n!only_rows_for_existing_properties\x18\x0c \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12/\n&only_rows_for_existing_properties_null\x18\xf4\x07 \x01(\x08\x12\x35\n\x10get_details_info\x18\r \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1e\n\x15get_details_info_null\x18\xf5\x07 \x01(\x08\"\xbb\x0b\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x42\n\x03row\x18\x04 \x03(\x0b\x32\x35.dstore.engine.pm_GetPersonProperties_Ad.Response.Row\x1a\x87\n\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12@\n\x1bvalue_restricted_by_pattern\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0f\x61\x63tual_value_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x1a\x63haracteristic_description\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x33\n\rfield_type_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x33\n\rdetails_exist\x18\x95N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x37\n\x11\x63haracteristic_id\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\x08value_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12,\n\x06modify\x18\x98N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07sort_no\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x30\n\nmax_length\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12>\n\x18required_charac_category\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x37\n\x11predefined_values\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12?\n\x19person_charac_category_id\x18\x9dN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x44\n\x1fread_access_restriction_pattern\x18\x9eN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12/\n\tperson_id\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\x08required\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x31\n\x0c\x61\x63tual_value\x18\xa1N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n\x05value\x18\xa2N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12-\n\x07visible\x18\xa3N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x33\n\x0blast_edited\x18\xa4N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x39\n\x14\x63\x61tegory_description\x18\xa5N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12=\n\x17person_type_description\x18\xa1\x9c\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x0eperson_type_id\x18\xa3\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValueBZ\n\x1bio.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/pm_GetPersonProperties_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.person_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.person_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.language_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='language_id_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.language_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.characteristic_id_list', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.characteristic_id_list_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_format', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.date_format', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_format_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.date_format_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.person_charac_category_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.person_charac_category_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_creation_date_and_time', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.include_creation_date_and_time', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_creation_date_and_time_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.include_creation_date_and_time_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_person_charac_category_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.include_person_charac_category_id', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_person_charac_category_id_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.include_person_charac_category_id_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_and_time', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.date_and_time', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='date_and_time_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.date_and_time_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_actual_properties', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.get_actual_properties', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_actual_properties_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.get_actual_properties_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_person_type_id_only', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.get_person_type_id_only', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_person_type_id_only_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.get_person_type_id_only_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_bad_person_ids_in_one_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.ignore_bad_person_ids_in_one_id', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ignore_bad_person_ids_in_one_id_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.ignore_bad_person_ids_in_one_id_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_rows_for_existing_properties', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.only_rows_for_existing_properties', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_rows_for_existing_properties_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.only_rows_for_existing_properties_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_details_info', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.get_details_info', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_details_info_null', full_name='dstore.engine.pm_GetPersonProperties_Ad.Parameters.get_details_info_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
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
  serialized_start=151,
  serialized_end=1434,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_restricted_by_pattern', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.value_restricted_by_pattern', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actual_value_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.actual_value_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_description', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.characteristic_description', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.field_type_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='details_exist', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.details_exist', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.characteristic_id', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.value_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='modify', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.modify', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.sort_no', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_length', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.max_length', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required_charac_category', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.required_charac_category', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predefined_values', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.predefined_values', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.person_charac_category_id', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_access_restriction_pattern', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.read_access_restriction_pattern', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.person_id', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='required', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.required', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actual_value', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.actual_value', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.value', index=18,
      number=10018, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.visible', index=19,
      number=10019, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_edited', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.last_edited', index=20,
      number=10020, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category_description', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.category_description', index=21,
      number=10021, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_description', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.person_type_description', index=22,
      number=20001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.Row.person_type_id', index=23,
      number=20003, type=11, cpp_type=10, label=1,
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
  serialized_start=1617,
  serialized_end=2904,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_GetPersonProperties_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_GetPersonProperties_Ad.Response.row', index=2,
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
  serialized_start=1437,
  serialized_end=2904,
)

_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['characteristic_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['date_format'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['include_creation_date_and_time'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['include_person_charac_category_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['date_and_time'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['get_actual_properties'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['get_person_type_id_only'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['ignore_bad_person_ids_in_one_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['only_rows_for_existing_properties'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['get_details_info'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['value_restricted_by_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['actual_value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['characteristic_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['field_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['details_exist'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['modify'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['max_length'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['required_charac_category'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['predefined_values'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['person_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['read_access_restriction_pattern'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['required'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['actual_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['visible'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['last_edited'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['category_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_type_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_GetPersonProperties_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonProperties_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_GetPersonProperties_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonProperties_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_GetPersonProperties_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_GetPersonProperties_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ;gosdk.dstore.de/engine/procedures/pm_GetPersonProperties_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
