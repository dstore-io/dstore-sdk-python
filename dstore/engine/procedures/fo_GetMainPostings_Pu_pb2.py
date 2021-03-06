# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/fo_GetMainPostings_Pu.proto

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
  name='dstore/engine/procedures/fo_GetMainPostings_Pu.proto',
  package='dstore.engine.fo_GetMainPostings_Pu',
  syntax='proto3',
  serialized_pb=_b('\n4dstore/engine/procedures/fo_GetMainPostings_Pu.proto\x12#dstore.engine.fo_GetMainPostings_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xfc\n\n\nParameters\x12@\n\x1cperson_identification_values\x18\x01 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12*\n!person_identification_values_null\x18\xe9\x07 \x01(\x08\x12\x33\n\x0eperson_type_id\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1c\n\x13person_type_id_null\x18\xea\x07 \x01(\x08\x12-\n\tunique_id\x18\x03 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x17\n\x0eunique_id_null\x18\xeb\x07 \x01(\x08\x12-\n\x08\x66orum_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x16\n\rforum_id_null\x18\xec\x07 \x01(\x08\x12\x32\n\rsort_criteria\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1b\n\x12sort_criteria_null\x18\xed\x07 \x01(\x08\x12\x36\n\x11\x66rom_main_posting\x18\x06 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1f\n\x16\x66rom_main_posting_null\x18\xee\x07 \x01(\x08\x12:\n\x15max_number_of_threads\x18\x07 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12#\n\x1amax_number_of_threads_null\x18\xef\x07 \x01(\x08\x12;\n\x16include_posting_bodies\x18\x08 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12$\n\x1binclude_posting_bodies_null\x18\xf0\x07 \x01(\x08\x12/\n\nvisibility\x18\t \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0fvisibility_null\x18\xf1\x07 \x01(\x08\x12\x43\n\x1eshow_post_date_of_main_posting\x18\n \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12,\n#show_post_date_of_main_posting_null\x18\xf2\x07 \x01(\x08\x12\x42\n\x1dget_own_not_approved_postings\x18\x0b \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12+\n\"get_own_not_approved_postings_null\x18\xf3\x07 \x01(\x08\x12\x37\n\x12output_into_one_id\x18\x0c \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12 \n\x17output_into_one_id_null\x18\xf4\x07 \x01(\x08\x12\x38\n\x13sorting_criteria_no\x18\r \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12!\n\x18sorting_criteria_no_null\x18\xf5\x07 \x01(\x08\x12=\n\x18reverse_order_of_sorting\x18\x0e \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12&\n\x1dreverse_order_of_sorting_null\x18\xf6\x07 \x01(\x08\x12;\n\x17separator_in_ident_vals\x18\x0f \x01(\x0b\x32\x1a.dstore.values.StringValue\x12%\n\x1cseparator_in_ident_vals_null\x18\xf7\x07 \x01(\x08\"\x9d\x08\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12>\n\x03row\x18\x04 \x03(\x0b\x32\x31.dstore.engine.fo_GetMainPostings_Pu.Response.Row\x1a\xed\x06\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x32\n\x0c\x61lready_read\x18\x91N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12/\n\nsmall_body\x18\x92N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x30\n\nposting_id\x18\x93N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x42\n\x1cposting_id_of_latest_posting\x18\x94N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12,\n\x07subject\x18\x95N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x38\n\x12postings_in_thread\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x35\n\x10\x65_mail_of_author\x18\x97N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x36\n\x10\x61uthor_person_id\x18\x98N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07visible\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0chas_binaries\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12+\n\x06\x61uthor\x18\x9bN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12;\n\x16main_posting_post_date\x18\x9cN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12=\n\x18latest_posting_post_date\x18\x9dN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12.\n\tpost_date\x18\x9eN \x01(\x0b\x32\x1a.dstore.values.StringValue\x12<\n\x16new_postings_in_thread\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12)\n\x04\x62ody\x18\xa0N \x01(\x0b\x32\x1a.dstore.values.StringValueBV\n\x1bio.dstore.engine.proceduresZ7gosdk.dstore.de/engine/procedures/fo_GetMainPostings_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='person_identification_values', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.person_identification_values', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_identification_values_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.person_identification_values_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.person_type_id', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='person_type_id_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.person_type_id_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.unique_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unique_id_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.unique_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.forum_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forum_id_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.forum_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_criteria', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.sort_criteria', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_criteria_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.sort_criteria_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_main_posting', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.from_main_posting', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_main_posting_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.from_main_posting_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_threads', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.max_number_of_threads', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_number_of_threads_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.max_number_of_threads_null', index=13,
      number=1007, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_posting_bodies', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.include_posting_bodies', index=14,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_posting_bodies_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.include_posting_bodies_null', index=15,
      number=1008, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.visibility', index=16,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visibility_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.visibility_null', index=17,
      number=1009, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='show_post_date_of_main_posting', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.show_post_date_of_main_posting', index=18,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='show_post_date_of_main_posting_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.show_post_date_of_main_posting_null', index=19,
      number=1010, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_own_not_approved_postings', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.get_own_not_approved_postings', index=20,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_own_not_approved_postings_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.get_own_not_approved_postings_null', index=21,
      number=1011, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_one_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.output_into_one_id', index=22,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='output_into_one_id_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.output_into_one_id_null', index=23,
      number=1012, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.sorting_criteria_no', index=24,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sorting_criteria_no_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.sorting_criteria_no_null', index=25,
      number=1013, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_order_of_sorting', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.reverse_order_of_sorting', index=26,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reverse_order_of_sorting_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.reverse_order_of_sorting_null', index=27,
      number=1014, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.separator_in_ident_vals', index=28,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='separator_in_ident_vals_null', full_name='dstore.engine.fo_GetMainPostings_Pu.Parameters.separator_in_ident_vals_null', index=29,
      number=1015, type=8, cpp_type=7, label=1,
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
  serialized_start=143,
  serialized_end=1547,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='already_read', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.already_read', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='small_body', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.small_body', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.posting_id', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='posting_id_of_latest_posting', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.posting_id_of_latest_posting', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subject', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.subject', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='postings_in_thread', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.postings_in_thread', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='e_mail_of_author', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.e_mail_of_author', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author_person_id', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.author_person_id', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visible', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.visible', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_binaries', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.has_binaries', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='author', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.author', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='main_posting_post_date', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.main_posting_post_date', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latest_posting_post_date', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.latest_posting_post_date', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='post_date', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.post_date', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='new_postings_in_thread', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.new_postings_in_thread', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='body', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.Row.body', index=16,
      number=10016, type=11, cpp_type=10, label=1,
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
  serialized_start=1726,
  serialized_end=2603,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.fo_GetMainPostings_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.fo_GetMainPostings_Pu.Response.row', index=2,
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
  serialized_start=1550,
  serialized_end=2603,
)

_PARAMETERS.fields_by_name['person_identification_values'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['person_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['unique_id'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['forum_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sort_criteria'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['from_main_posting'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['max_number_of_threads'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['include_posting_bodies'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['visibility'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['show_post_date_of_main_posting'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['get_own_not_approved_postings'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['output_into_one_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sorting_criteria_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['reverse_order_of_sorting'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['separator_in_ident_vals'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['already_read'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['small_body'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['posting_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['posting_id_of_latest_posting'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['subject'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['postings_in_thread'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['e_mail_of_author'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['author_person_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['visible'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['has_binaries'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['author'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['main_posting_post_date'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['latest_posting_post_date'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['post_date'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['new_postings_in_thread'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['body'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.fo_GetMainPostings_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetMainPostings_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.fo_GetMainPostings_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetMainPostings_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.fo_GetMainPostings_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.fo_GetMainPostings_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ7gosdk.dstore.de/engine/procedures/fo_GetMainPostings_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
