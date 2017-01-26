# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_SearchPostings_Pu.proto

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
  name='dstore/engine/procedures/fo_SearchPostings_Pu.proto',
  package='dstore.engine.fo_SearchPostings_Pu',
  syntax='proto3',
  serialized_pb=_b('\n3dstore/engine/procedures/fo_SearchPostings_Pu.proto\x12\"dstore.engine.fo_SearchPostings_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xc6\r\n\nParameters\x12@\n\x1cperson_identification_values\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n!person_identification_values_null\x18\xe9\x07 \x01(\x08\x12\x33\n\x0eperson_type_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13person_type_id_null\x18\xea\x07 \x01(\x08\x12-\n\tunique_id\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xeb\x07 \x01(\x08\x12-\n\x08\x66orum_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x16\n\rforum_id_null\x18\xec\x07 \x01(\x08\x12>\n\x19search_with_like_operator\x18\x05 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\'\n\x1esearch_with_like_operator_null\x18\xed\x07 \x01(\x08\x12;\n\x16include_posting_bodies\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12$\n\x1binclude_posting_bodies_null\x18\xee\x07 \x01(\x08\x12.\n\trow_count\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x17\n\x0erow_count_null\x18\xef\x07 \x01(\x08\x12=\n\x18include_additional_infos\x18\x08 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12&\n\x1dinclude_additional_infos_null\x18\xf0\x07 \x01(\x08\x12\x30\n\tfrom_date\x18\t \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x17\n\x0e\x66rom_date_null\x18\xf1\x07 \x01(\x08\x12.\n\x07to_date\x18\n \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12\x15\n\x0cto_date_null\x18\xf2\x07 \x01(\x08\x12/\n\nvisibility\x18\x0b \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0fvisibility_null\x18\xf3\x07 \x01(\x08\x12\x42\n\x1dget_own_not_approved_postings\x18\x0c \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12+\n\"get_own_not_approved_postings_null\x18\xf4\x07 \x01(\x08\x12\x37\n\x12output_into_one_id\x18\r \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17output_into_one_id_null\x18\xf5\x07 \x01(\x08\x12\x42\n\x1eposting_characteristic_id_list\x18\x0e \x01(\x0b\x32\x1a.dstore.values.StringValue\x12,\n#posting_characteristic_id_list_null\x18\xf6\x07 \x01(\x08\x12\x32\n\x0e\x63ondition_list\x18\x0f \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x1c\n\x13\x63ondition_list_null\x18\xf7\x07 \x01(\x08\x12<\n\x18\x66ilter_by_person_id_list\x18\x10 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12&\n\x1d\x66ilter_by_person_id_list_null\x18\xf8\x07 \x01(\x08\x12+\n\x07\x63ountry\x18\x11 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x15\n\x0c\x63ountry_null\x18\xf9\x07 \x01(\x08\x12\x43\n\x1esearch_only_postings_in_one_id\x18\x12 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12,\n#search_only_postings_in_one_id_null\x18\xfa\x07 \x01(\x08\x12;\n\x17separator_in_ident_vals\x18\x13 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12%\n\x1cseparator_in_ident_vals_null\x18\xfb\x07 \x01(\x08\"\x92\x07\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12=\n\x03row\x18\x04 \x03(\x0b\x32\x30.dstore.engine.fo_SearchPostings_Pu.Response.Row\x1a\xe3\x05\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12/\n\nsmall_body\x18\x91N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x35\n\x10\x65_mail_of_author\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x30\n\nposting_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x36\n\x10\x61uthor_person_id\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x35\n\x0fmain_posting_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07visible\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x39\n\x13reply_to_posting_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12+\n\x06\x61uthor\x18\x98N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x31\n\tpost_date\x18\x99N \x01(\x0b\x32\x1d.dstore.values.TimestampValue\x12)\n\x04\x62ody\x18\x9aN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12,\n\x07subject\x18\x9bN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x33\n\x0c\x61lready_read\x18\xa1\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x33\n\x0chas_binaries\x18\xa9\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x35\n\x0ehas_successors\x18\xac\x9c\x01 \x01(\x0b\x32\x1b.dstore.values.BooleanValueBU\n\x1bio.dstore.engine.proceduresZ6gosdk.dstore.de/engine/procedures/fo_SearchPostings_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_SearchPostings_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_identification_values', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.person_identification_values', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_identification_values_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.person_identification_values_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.person_type_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.person_type_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.unique_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.unique_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.forum_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.forum_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_with_like_operator', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.search_with_like_operator', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_with_like_operator_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.search_with_like_operator_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_posting_bodies', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.include_posting_bodies', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_posting_bodies_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.include_posting_bodies_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row_count', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.row_count', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row_count_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.row_count_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_additional_infos', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.include_additional_infos', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_additional_infos_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.include_additional_infos_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.from_date', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_date_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.from_date_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.to_date', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='to_date_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.to_date_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.visibility', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visibility_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.visibility_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_own_not_approved_postings', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.get_own_not_approved_postings', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_own_not_approved_postings_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.get_own_not_approved_postings_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_one_id', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.output_into_one_id', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_one_id_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.output_into_one_id_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_characteristic_id_list', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.posting_characteristic_id_list', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_characteristic_id_list_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.posting_characteristic_id_list_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_list', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.condition_list', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_list_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.condition_list_null', index=29,
      number=1015, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_person_id_list', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.filter_by_person_id_list', index=30,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_person_id_list_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.filter_by_person_id_list_null', index=31,
      number=1016, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.country', index=32,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.country_null', index=33,
      number=1017, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_only_postings_in_one_id', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.search_only_postings_in_one_id', index=34,
      number=18, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='search_only_postings_in_one_id_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.search_only_postings_in_one_id_null', index=35,
      number=1018, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.separator_in_ident_vals', index=36,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals_null', full_name='dstore.engine.fo_SearchPostings_Pu.Parameters.separator_in_ident_vals_null', index=37,
      number=1019, type=8, cpp_type=7, label=1,
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
  serialized_start=141,
  serialized_end=1875,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_body', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.small_body', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='e_mail_of_author', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.e_mail_of_author', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_id', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.posting_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_person_id', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.author_person_id', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='main_posting_id', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.main_posting_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.visible', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reply_to_posting_id', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.reply_to_posting_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.author', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_date', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.post_date', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.body', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.subject', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='already_read', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.already_read', index=12,
      number=20001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_binaries', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.has_binaries', index=13,
      number=20009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_successors', full_name='dstore.engine.fo_SearchPostings_Pu.Response.Row.has_successors', index=14,
      number=20012, type=11, cpp_type=10, label=1,
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
  serialized_start=2053,
  serialized_end=2792,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_SearchPostings_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_SearchPostings_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_SearchPostings_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_SearchPostings_Pu.Response.row', index=2,
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
  serialized_start=1878,
  serialized_end=2792,
)

_PARAMETERS.fields_by_name['person_identification_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['search_with_like_operator'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['include_posting_bodies'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['row_count'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['include_additional_infos'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['from_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['to_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_PARAMETERS.fields_by_name['visibility'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_own_not_approved_postings'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['output_into_one_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['posting_characteristic_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['condition_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['filter_by_person_id_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['country'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['search_only_postings_in_one_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['separator_in_ident_vals'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['small_body'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['e_mail_of_author'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['posting_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['author_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['main_posting_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['visible'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['reply_to_posting_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['author'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['post_date'].message_type = dstore_dot_values__pb2._TIMESTAMPVALUE
_RESPONSE_ROW.fields_by_name['body'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['subject'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['already_read'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['has_binaries'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['has_successors'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_SearchPostings_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_SearchPostings_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_SearchPostings_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_SearchPostings_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_SearchPostings_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_SearchPostings_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ6gosdk.dstore.de/engine/procedures/fo_SearchPostings_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
