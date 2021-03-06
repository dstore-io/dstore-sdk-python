# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/im_GetRandomProduct_Pu.proto

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
  name='dstore/engine/procedures/im_GetRandomProduct_Pu.proto',
  package='dstore.engine.im_GetRandomProduct_Pu',
  syntax='proto3',
  serialized_pb=_b('\n5dstore/engine/procedures/im_GetRandomProduct_Pu.proto\x12$dstore.engine.im_GetRandomProduct_Pu\x1a\x13\x64store/values.proto\x1a\x1a\x64store/engine/engine.proto\"\xeb\x04\n\nParameters\x12\x31\n\x0ctree_node_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x1a\n\x11tree_node_id_null\x18\xe9\x07 \x01(\x08\x12>\n\x19number_of_random_products\x18\x02 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\'\n\x1enumber_of_random_products_null\x18\xea\x07 \x01(\x08\x12\x43\n\x1e\x62inary_characteristic_value_id\x18\x03 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12,\n#binary_characteristic_value_id_null\x18\xeb\x07 \x01(\x08\x12@\n\x1b\x66ilter_by_characteristic_id\x18\x04 \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12)\n filter_by_characteristic_id_null\x18\xec\x07 \x01(\x08\x12:\n\x16\x66ilter_by_charac_value\x18\x05 \x01(\x0b\x32\x1a.dstore.values.StringValue\x12$\n\x1b\x66ilter_by_charac_value_null\x18\xed\x07 \x01(\x08\x12<\n\x17negate_filter_by_params\x18\x06 \x01(\x0b\x32\x1b.dstore.values.BooleanValue\x12%\n\x1cnegate_filter_by_params_null\x18\xee\x07 \x01(\x08\"\xb1\x02\n\x08Response\x12\x38\n\x10meta_information\x18\x02 \x03(\x0b\x32\x1e.dstore.engine.MetaInformation\x12\'\n\x07message\x18\x03 \x03(\x0b\x32\x16.dstore.engine.Message\x12?\n\x03row\x18\x04 \x03(\x0b\x32\x32.dstore.engine.im_GetRandomProduct_Pu.Response.Row\x1a\x80\x01\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x12\x34\n\x0e\x62inary_code_id\x18\x91N \x01(\x0b\x32\x1b.dstore.values.IntegerValue\x12\x32\n\x0ctree_node_id\x18\x92N \x01(\x0b\x32\x1b.dstore.values.IntegerValueBW\n\x1bio.dstore.engine.proceduresZ8gosdk.dstore.de/engine/procedures/im_GetRandomProduct_Pub\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_engine__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.tree_node_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id_null', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.tree_node_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_random_products', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.number_of_random_products', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_of_random_products_null', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.number_of_random_products_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_characteristic_value_id', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.binary_characteristic_value_id', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_characteristic_value_id_null', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.binary_characteristic_value_id_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_characteristic_id', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.filter_by_characteristic_id', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_characteristic_id_null', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.filter_by_characteristic_id_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_charac_value', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.filter_by_charac_value', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_by_charac_value_null', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.filter_by_charac_value_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negate_filter_by_params', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.negate_filter_by_params', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='negate_filter_by_params_null', full_name='dstore.engine.im_GetRandomProduct_Pu.Parameters.negate_filter_by_params_null', index=11,
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
  serialized_start=145,
  serialized_end=764,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.im_GetRandomProduct_Pu.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.im_GetRandomProduct_Pu.Response.Row.row_id', index=0,
      number=10000, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binary_code_id', full_name='dstore.engine.im_GetRandomProduct_Pu.Response.Row.binary_code_id', index=1,
      number=10001, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tree_node_id', full_name='dstore.engine.im_GetRandomProduct_Pu.Response.Row.tree_node_id', index=2,
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
  serialized_start=944,
  serialized_end=1072,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.im_GetRandomProduct_Pu.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.im_GetRandomProduct_Pu.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.im_GetRandomProduct_Pu.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.im_GetRandomProduct_Pu.Response.row', index=2,
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
  serialized_start=767,
  serialized_end=1072,
)

_PARAMETERS.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['number_of_random_products'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['binary_characteristic_value_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['filter_by_characteristic_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['filter_by_charac_value'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['negate_filter_by_params'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.fields_by_name['binary_code_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.fields_by_name['tree_node_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_engine__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_engine__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.im_GetRandomProduct_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.im_GetRandomProduct_Pu.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.im_GetRandomProduct_Pu_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.im_GetRandomProduct_Pu.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.im_GetRandomProduct_Pu_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.im_GetRandomProduct_Pu.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ8gosdk.dstore.de/engine/procedures/im_GetRandomProduct_Pu'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)
