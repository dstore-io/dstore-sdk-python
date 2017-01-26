# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/im_GetNodeCharacteristics_Ad.proto

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
  name='dstore/engine/procedures/im_GetNodeCharacteristics_Ad.proto',
  package='dstore.engine.im_GetNodeCharacteristics_Ad',
  syntax='proto3',
  serialized_pb=_b('\n;dstore/engine/procedures/im_GetNodeCharacteristics_Ad.proto\x12*dstore.engine.im_GetNodeCharacteristics_Ad\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xea\x04\n\nParameters\x12\x41\n\x1cinclude_currency_information\x18\x01 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12*\n!include_currency_information_null\x18\xe9\x07 \x01(\x08\x12\x42\n\x1dinclude_currency_informations\x18\x02 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12+\n\"include_currency_informations_null\x18\xea\x07 \x01(\x08\x12=\n\x18only_ids_in_table_one_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12&\n\x1donly_ids_in_table_one_id_null\x18\xeb\x07 \x01(\x08\x12<\n\x17node_charac_category_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12%\n\x1cnode_charac_category_id_null\x18\xec\x07 \x01(\x08\x12/\n\nsort_order\x18\x05 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x18\n\x0fsort_order_null\x18\xed\x07 \x01(\x08\x12=\n\x18get_category_information\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12&\n\x1dget_category_information_null\x18\xee\x07 \x01(\x08\"\xce\t\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12\x45\n\x03row\x18\x04 \x03(\x0b\x32\x38.dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row\x1a\x97\x08\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x30\n\ndeleteable\x18\x91N \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12=\n\x17predecessor_category_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12?\n\x1a\x63haracteristic_description\x18\x93N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x33\n\x0evalue_language\x18\x94N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12\x33\n\rfield_type_id\x18\x95N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12.\n\x08in_netto\x18\x96N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12<\n\x16node_characteristic_id\x18\x97N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07sort_no\x18\x98N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x46\n keep_properties_history_in_hours\x18\x99N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x37\n\x11predefined_values\x18\x9aN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12=\n\x17node_charac_category_id\x18\x9bN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12I\n#has_currency_unit_vals_are_net_vals\x18\x9cN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x36\n\x10\x63\x61tegory_sort_no\x18\x9dN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12-\n\x07unit_id\x18\x9eN \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12/\n\tis_unique\x18\x9fN \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12\x37\n\x11value_language_id\x18\xa0N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x39\n\x14\x63\x61tegory_description\x18\xa1N \x01(\x0b\x32\x1a.dstore.values.StringValue\x12/\n\trecursive\x18\xa2N \x01(\x0b\x32\x1b.dstore.values.BooleanValueB]\n\x1bio.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/im_GetNodeCharacteristics_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='include_currency_information', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.include_currency_information', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_currency_information_null', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.include_currency_information_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_currency_informations', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.include_currency_informations', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='include_currency_informations_null', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.include_currency_informations_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_ids_in_table_one_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.only_ids_in_table_one_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='only_ids_in_table_one_id_null', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.only_ids_in_table_one_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_charac_category_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.node_charac_category_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_charac_category_id_null', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.node_charac_category_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_order', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.sort_order', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_order_null', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.sort_order_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_category_information', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.get_category_information', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_category_information_null', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Parameters.get_category_information_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
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
  serialized_end=775,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleteable', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.deleteable', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predecessor_category_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.predecessor_category_id', index=2,
      number=10002, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='characteristic_description', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.characteristic_description', index=3,
      number=10003, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_language', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.value_language', index=4,
      number=10004, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='field_type_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.field_type_id', index=5,
      number=10005, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='in_netto', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.in_netto', index=6,
      number=10006, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_characteristic_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.node_characteristic_id', index=7,
      number=10007, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sort_no', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.sort_no', index=8,
      number=10008, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='keep_properties_history_in_hours', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.keep_properties_history_in_hours', index=9,
      number=10009, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predefined_values', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.predefined_values', index=10,
      number=10010, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_charac_category_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.node_charac_category_id', index=11,
      number=10011, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='has_currency_unit_vals_are_net_vals', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.has_currency_unit_vals_are_net_vals', index=12,
      number=10012, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category_sort_no', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.category_sort_no', index=13,
      number=10013, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unit_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.unit_id', index=14,
      number=10014, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_unique', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.is_unique', index=15,
      number=10015, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value_language_id', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.value_language_id', index=16,
      number=10016, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='category_description', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.category_description', index=17,
      number=10017, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='recursive', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row.recursive', index=18,
      number=10018, type=11, cpp_type=10, label=1,
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
  serialized_start=961,
  serialized_end=2008,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.im_GetNodeCharacteristics_Ad.Response.row', index=2,
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
  serialized_start=778,
  serialized_end=2008,
)

_PARAMETERS.fields_by_name['include_currency_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['include_currency_informations'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['only_ids_in_table_one_id'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_PARAMETERS.fields_by_name['node_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['sort_order'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['get_category_information'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['deleteable'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['predecessor_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['characteristic_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['value_language'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['field_type_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['in_netto'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['node_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['keep_properties_history_in_hours'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['predefined_values'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['node_charac_category_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['has_currency_unit_vals_are_net_vals'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['category_sort_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['unit_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['is_unique'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['value_language_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['category_description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_RESPONSE_ROW.fields_by_name['recursive'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.im_GetNodeCharacteristics_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.im_GetNodeCharacteristics_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.im_GetNodeCharacteristics_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.im_GetNodeCharacteristics_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.im_GetNodeCharacteristics_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.im_GetNodeCharacteristics_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ>gosdk.dstore.de/engine/procedures/im_GetNodeCharacteristics_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
