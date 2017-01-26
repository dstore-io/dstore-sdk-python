# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/pm_ModifyPersonData_Pu.proto

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
  name='dstore/engine/procedures/pm_ModifyPersonData_Pu.proto',
  package='dstore.engine.pm_ModifyPersonData_Pu',
  syntax='proto3',
  serialized_pb=_b('\n5dstore/engine/procedures/pm_ModifyPersonData_Pu.proto\x12$dstore.engine.pm_ModifyPersonData_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xdd\x0b\n\nParameters\x12:\n\x16\x63haracteristic_id_list\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12$\n\x1b\x63haracteristic_id_list_null\x18\xe9\x07 \x01(\x08\x12.\n\nvalue_list\x18\x02 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x18\n\x0fvalue_list_null\x18\xea\x07 \x01(\x08\x12\x39\n\x15identification_values\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12#\n\x1aidentification_values_null\x18\xeb\x07 \x01(\x08\x12\x31\n\rerror_id_list\x18\x04 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1b\n\x12\x65rror_id_list_null\x18\xec\x07 \x01(\x08\x12.\n\tperson_id\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0eperson_id_null\x18\xed\x07 \x01(\x08\x12\x33\n\x0eperson_type_id\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13person_type_id_null\x18\xee\x07 \x01(\x08\x12<\n\x17person_grant_access_ids\x18\x07 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12%\n\x1cperson_grant_access_ids_null\x18\xef\x07 \x01(\x08\x12>\n\x19person_charac_category_id\x18\x08 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\'\n\x1eperson_charac_category_id_null\x18\xf0\x07 \x01(\x08\x12>\n\x19\x64\x65lete_charac_category_id\x18\t \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\'\n\x1e\x64\x65lete_charac_category_id_null\x18\xf1\x07 \x01(\x08\x12<\n\x17result_in_error_id_list\x18\n \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12%\n\x1cresult_in_error_id_list_null\x18\xf2\x07 \x01(\x08\x12\x45\n value_ids_for_predefined_characs\x18\x0b \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12.\n%value_ids_for_predefined_characs_null\x18\xf3\x07 \x01(\x08\x12:\n\x15\x63hange_all_or_nothing\x18\x0c \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12#\n\x1a\x63hange_all_or_nothing_null\x18\xf4\x07 \x01(\x08\x12\x33\n\x0e\x63\x61se_sensitive\x18\r \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x1c\n\x13\x63\x61se_sensitive_null\x18\xf5\x07 \x01(\x08\x12+\n\x07\x63ountry\x18\x0e \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x15\n\x0c\x63ountry_null\x18\xf6\x07 \x01(\x08\x12;\n\x17separator_in_value_list\x18\x0f \x01(\x0b\x32\x1a.dstore.values.StringValue\x12%\n\x1cseparator_in_value_list_null\x18\xf7\x07 \x01(\x08\x12>\n\x1aseparator_for_ident_values\x18\x10 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12(\n\x1fseparator_for_ident_values_null\x18\xf8\x07 \x01(\x08\"\xed\x02\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12?\n\x03row\x18\x04 \x03(\x0b\x32\x32.dstore.engine.pm_ModifyPersonData_Pu.Response.Row\x12\x31\n\rerror_id_list\x18\x65 \x01(\x0b\x32\x1a.dstore.values.StringValue\x1a\x89\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12>\n\x18person_characteristic_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x31\n\x0bresult_code\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValueBW\n\x1bio.dstore.engine.proceduresZ8gosdk.dstore.de/engine/procedures/pm_ModifyPersonData_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='characteristic_id_list', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.characteristic_id_list', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_id_list_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.characteristic_id_list_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_list', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.value_list', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_list_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.value_list_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identification_values', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.identification_values', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='identification_values_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.identification_values_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_id_list', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.error_id_list', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_id_list_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.error_id_list_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_id', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_id_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_id_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_type_id', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_type_id_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_grant_access_ids', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_grant_access_ids', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_grant_access_ids_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_grant_access_ids_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_charac_category_id', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_charac_category_id_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.person_charac_category_id_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_charac_category_id', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.delete_charac_category_id', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_charac_category_id_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.delete_charac_category_id_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_in_error_id_list', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.result_in_error_id_list', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_in_error_id_list_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.result_in_error_id_list_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_ids_for_predefined_characs', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.value_ids_for_predefined_characs', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_ids_for_predefined_characs_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.value_ids_for_predefined_characs_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_all_or_nothing', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.change_all_or_nothing', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='change_all_or_nothing_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.change_all_or_nothing_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_sensitive', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.case_sensitive', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='case_sensitive_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.case_sensitive_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.country', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.country_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_value_list', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.separator_in_value_list', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_value_list_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.separator_in_value_list_null', index=29,
      number=1015, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_for_ident_values', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.separator_for_ident_values', index=30,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_for_ident_values_null', full_name='dstore.engine.pm_ModifyPersonData_Pu.Parameters.separator_for_ident_values_null', index=31,
      number=1016, type=8, cpp_type=7, label=1,
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
  serialized_start=145,
  serialized_end=1646,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_characteristic_id', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.Row.person_characteristic_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result_code', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.Row.result_code', index=2,
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
  serialized_start=1877,
  serialized_end=2014,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.pm_ModifyPersonData_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_id_list', full_name='dstore.engine.pm_ModifyPersonData_Pu.Response.error_id_list', index=3,
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
  serialized_start=1649,
  serialized_end=2014,
)

_PARAMETERS.fields_by_name['characteristic_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['value_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['identification_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['error_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['person_grant_access_ids'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['person_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delete_charac_category_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['result_in_error_id_list'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['value_ids_for_predefined_characs'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['change_all_or_nothing'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['case_sensitive'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['country'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['separator_in_value_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['separator_for_ident_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['person_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['result_code'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['error_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.pm_ModifyPersonData_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_ModifyPersonData_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.pm_ModifyPersonData_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.pm_ModifyPersonData_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.pm_ModifyPersonData_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.pm_ModifyPersonData_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ8gosdk.dstore.de/engine/procedures/pm_ModifyPersonData_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
