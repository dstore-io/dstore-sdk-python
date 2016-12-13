# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/procedures/mi_ModifyTRITriggerWorkflow_Ad.proto

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
  name='dstore/engine/procedures/mi_ModifyTRITriggerWorkflow_Ad.proto',
  package='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad',
  syntax='proto3',
  serialized_pb=_b('\n=dstore/engine/procedures/mi_ModifyTRITriggerWorkflow_Ad.proto\x12,dstore.engine.mi_ModifyTRITriggerWorkflow_Ad\x1a\x13\x64store/values.proto\x1a\x1b\x64store/engine/message.proto\x1a#dstore/engine/metainformation.proto\"\xb8\x04\n\nParameters\x12/\n\ntrigger_id\x18\x01 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x18\n\x0ftrigger_id_null\x18\xe9\x07 \x01(\x08\x12\x31\n\x0cwork_step_no\x18\x02 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1a\n\x11work_step_no_null\x18\xea\x07 \x01(\x08\x12\x32\n\x0eiteration_list\x18\x03 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x1c\n\x13iteration_list_null\x18\xeb\x07 \x01(\x08\x12-\n\twork_step\x18\x04 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x17\n\x0ework_step_null\x18\xec\x07 \x01(\x08\x12/\n\x0b\x64\x65scription\x18\x05 \x01(\x0b\x32\x1a.dstore.values.stringValue\x12\x19\n\x10\x64\x65scription_null\x18\xed\x07 \x01(\x08\x12\x34\n\x0f\x63\x61ncel_on_error\x18\x06 \x01(\x0b\x32\x1b.dstore.values.integerValue\x12\x1d\n\x14\x63\x61ncel_on_error_null\x18\xee\x07 \x01(\x08\x12\x35\n\x10\x64\x65lete_work_step\x18\x07 \x01(\x0b\x32\x1b.dstore.values.booleanValue\x12\x1e\n\x15\x64\x65lete_work_step_null\x18\xef\x07 \x01(\x08\"\x99\x02\n\x08Response\x12H\n\x10meta_information\x18\x02 \x03(\x0b\x32..dstore.engine.metainformation.MetaInformation\x12/\n\x07message\x18\x03 \x03(\x0b\x32\x1e.dstore.engine.message.Message\x12G\n\x03row\x18\x04 \x03(\x0b\x32:.dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.Row\x12\x31\n\x0cwork_step_no\x18\x65 \x01(\x0b\x32\x1b.dstore.values.integerValue\x1a\x16\n\x03Row\x12\x0f\n\x06row_id\x18\x90N \x01(\x05\x42_\n\x1bio.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/mi_ModifyTRITriggerWorkflow_Adb\x06proto3')
  ,
  dependencies=[dstore_dot_values__pb2.DESCRIPTOR,dstore_dot_engine_dot_message__pb2.DESCRIPTOR,dstore_dot_engine_dot_metainformation__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_PARAMETERS = _descriptor.Descriptor(
  name='Parameters',
  full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='trigger_id', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.trigger_id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='trigger_id_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.trigger_id_null', index=1,
      number=1001, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='work_step_no', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.work_step_no', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='work_step_no_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.work_step_no_null', index=3,
      number=1002, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration_list', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.iteration_list', index=4,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iteration_list_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.iteration_list_null', index=5,
      number=1003, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='work_step', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.work_step', index=6,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='work_step_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.work_step_null', index=7,
      number=1004, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.description', index=8,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.description_null', index=9,
      number=1005, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cancel_on_error', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.cancel_on_error', index=10,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cancel_on_error_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.cancel_on_error_null', index=11,
      number=1006, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_work_step', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.delete_work_step', index=12,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='delete_work_step_null', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters.delete_work_step_null', index=13,
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
  serialized_start=199,
  serialized_end=767,
)


_RESPONSE_ROW = _descriptor.Descriptor(
  name='Row',
  full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.Row',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_id', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.Row.row_id', index=0,
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
  serialized_start=1029,
  serialized_end=1051,
)

_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='meta_information', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.meta_information', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='message', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.message', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='row', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.row', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='work_step_no', full_name='dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.work_step_no', index=3,
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
  serialized_start=770,
  serialized_end=1051,
)

_PARAMETERS.fields_by_name['trigger_id'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['work_step_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['iteration_list'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['work_step'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['description'].message_type = dstore_dot_values__pb2._STRINGVALUE
_PARAMETERS.fields_by_name['cancel_on_error'].message_type = dstore_dot_values__pb2._INTEGERVALUE
_PARAMETERS.fields_by_name['delete_work_step'].message_type = dstore_dot_values__pb2._BOOLEANVALUE
_RESPONSE_ROW.containing_type = _RESPONSE
_RESPONSE.fields_by_name['meta_information'].message_type = dstore_dot_engine_dot_metainformation__pb2._METAINFORMATION
_RESPONSE.fields_by_name['message'].message_type = dstore_dot_engine_dot_message__pb2._MESSAGE
_RESPONSE.fields_by_name['row'].message_type = _RESPONSE_ROW
_RESPONSE.fields_by_name['work_step_no'].message_type = dstore_dot_values__pb2._INTEGERVALUE
DESCRIPTOR.message_types_by_name['Parameters'] = _PARAMETERS
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Parameters = _reflection.GeneratedProtocolMessageType('Parameters', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETERS,
  __module__ = 'dstore.engine.procedures.mi_ModifyTRITriggerWorkflow_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Parameters)
  ))
_sym_db.RegisterMessage(Parameters)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(

  Row = _reflection.GeneratedProtocolMessageType('Row', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSE_ROW,
    __module__ = 'dstore.engine.procedures.mi_ModifyTRITriggerWorkflow_Ad_pb2'
    # @@protoc_insertion_point(class_scope:dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response.Row)
    ))
  ,
  DESCRIPTOR = _RESPONSE,
  __module__ = 'dstore.engine.procedures.mi_ModifyTRITriggerWorkflow_Ad_pb2'
  # @@protoc_insertion_point(class_scope:dstore.engine.mi_ModifyTRITriggerWorkflow_Ad.Response)
  ))
_sym_db.RegisterMessage(Response)
_sym_db.RegisterMessage(Response.Row)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033io.dstore.engine.proceduresZ@gosdk.dstore.de/engine/procedures/mi_ModifyTRITriggerWorkflow_Ad'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)