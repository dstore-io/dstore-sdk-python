# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/values.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dstore/values.proto',
  package='dstore.values',
  syntax='proto3',
  serialized_pb=_b('\n\x13\x64store/values.proto\x12\rdstore.values\x1a\x1fgoogle/protobuf/timestamp.proto\"\x1d\n\x0cintegerValue\x12\r\n\x05value\x18\x01 \x01(\x05\"\x1c\n\x0bstringValue\x12\r\n\x05value\x18\x01 \x01(\t\"\x1b\n\nbytesValue\x12\r\n\x05value\x18\x01 \x01(\x0c\"\x1c\n\x0b\x64oubleValue\x12\r\n\x05value\x18\x01 \x01(\x01\"\x1d\n\x0c\x62ooleanValue\x12\r\n\x05value\x18\x01 \x01(\x08\"\x1d\n\x0c\x64\x65\x63imalValue\x12\r\n\x05value\x18\x01 \x01(\t\";\n\x0etimestampValue\x12)\n\x05value\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"\x1a\n\tlongValue\x12\r\n\x05value\x18\x01 \x01(\x03\"\xb5\x03\n\x05Value\x12\x34\n\rinteger_value\x18\n \x01(\x0b\x32\x1b.dstore.values.integerValueH\x00\x12\x32\n\x0cstring_value\x18\x0b \x01(\x0b\x32\x1a.dstore.values.stringValueH\x00\x12/\n\nbyte_value\x18\x0c \x01(\x0b\x32\x19.dstore.values.bytesValueH\x00\x12\x32\n\x0c\x64ouble_value\x18\r \x01(\x0b\x32\x1a.dstore.values.doubleValueH\x00\x12\x34\n\rboolean_value\x18\x0e \x01(\x0b\x32\x1b.dstore.values.booleanValueH\x00\x12\x34\n\rdecimal_value\x18\x0f \x01(\x0b\x32\x1b.dstore.values.decimalValueH\x00\x12\x38\n\x0ftimestamp_value\x18\x10 \x01(\x0b\x32\x1d.dstore.values.timestampValueH\x00\x12.\n\nlong_value\x18\x11 \x01(\x0b\x32\x18.dstore.values.longValueH\x00\x42\x07\n\x05valueB#\n\tio.dstoreZ\x16gosdk.dstore.de/valuesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INTEGERVALUE = _descriptor.Descriptor(
  name='integerValue',
  full_name='dstore.values.integerValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.integerValue.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=71,
  serialized_end=100,
)


_STRINGVALUE = _descriptor.Descriptor(
  name='stringValue',
  full_name='dstore.values.stringValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.stringValue.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=102,
  serialized_end=130,
)


_BYTESVALUE = _descriptor.Descriptor(
  name='bytesValue',
  full_name='dstore.values.bytesValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.bytesValue.value', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=132,
  serialized_end=159,
)


_DOUBLEVALUE = _descriptor.Descriptor(
  name='doubleValue',
  full_name='dstore.values.doubleValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.doubleValue.value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=161,
  serialized_end=189,
)


_BOOLEANVALUE = _descriptor.Descriptor(
  name='booleanValue',
  full_name='dstore.values.booleanValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.booleanValue.value', index=0,
      number=1, type=8, cpp_type=7, label=1,
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
  serialized_start=191,
  serialized_end=220,
)


_DECIMALVALUE = _descriptor.Descriptor(
  name='decimalValue',
  full_name='dstore.values.decimalValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.decimalValue.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=222,
  serialized_end=251,
)


_TIMESTAMPVALUE = _descriptor.Descriptor(
  name='timestampValue',
  full_name='dstore.values.timestampValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.timestampValue.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=253,
  serialized_end=312,
)


_LONGVALUE = _descriptor.Descriptor(
  name='longValue',
  full_name='dstore.values.longValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='dstore.values.longValue.value', index=0,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=314,
  serialized_end=340,
)


_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='dstore.values.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='integer_value', full_name='dstore.values.Value.integer_value', index=0,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='dstore.values.Value.string_value', index=1,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='byte_value', full_name='dstore.values.Value.byte_value', index=2,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='dstore.values.Value.double_value', index=3,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='dstore.values.Value.boolean_value', index=4,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decimal_value', full_name='dstore.values.Value.decimal_value', index=5,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_value', full_name='dstore.values.Value.timestamp_value', index=6,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long_value', full_name='dstore.values.Value.long_value', index=7,
      number=17, type=11, cpp_type=10, label=1,
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
    _descriptor.OneofDescriptor(
      name='value', full_name='dstore.values.Value.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=343,
  serialized_end=780,
)

_TIMESTAMPVALUE.fields_by_name['value'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_VALUE.fields_by_name['integer_value'].message_type = _INTEGERVALUE
_VALUE.fields_by_name['string_value'].message_type = _STRINGVALUE
_VALUE.fields_by_name['byte_value'].message_type = _BYTESVALUE
_VALUE.fields_by_name['double_value'].message_type = _DOUBLEVALUE
_VALUE.fields_by_name['boolean_value'].message_type = _BOOLEANVALUE
_VALUE.fields_by_name['decimal_value'].message_type = _DECIMALVALUE
_VALUE.fields_by_name['timestamp_value'].message_type = _TIMESTAMPVALUE
_VALUE.fields_by_name['long_value'].message_type = _LONGVALUE
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['integer_value'])
_VALUE.fields_by_name['integer_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['string_value'])
_VALUE.fields_by_name['string_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['byte_value'])
_VALUE.fields_by_name['byte_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['double_value'])
_VALUE.fields_by_name['double_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['boolean_value'])
_VALUE.fields_by_name['boolean_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['decimal_value'])
_VALUE.fields_by_name['decimal_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['timestamp_value'])
_VALUE.fields_by_name['timestamp_value'].containing_oneof = _VALUE.oneofs_by_name['value']
_VALUE.oneofs_by_name['value'].fields.append(
  _VALUE.fields_by_name['long_value'])
_VALUE.fields_by_name['long_value'].containing_oneof = _VALUE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['integerValue'] = _INTEGERVALUE
DESCRIPTOR.message_types_by_name['stringValue'] = _STRINGVALUE
DESCRIPTOR.message_types_by_name['bytesValue'] = _BYTESVALUE
DESCRIPTOR.message_types_by_name['doubleValue'] = _DOUBLEVALUE
DESCRIPTOR.message_types_by_name['booleanValue'] = _BOOLEANVALUE
DESCRIPTOR.message_types_by_name['decimalValue'] = _DECIMALVALUE
DESCRIPTOR.message_types_by_name['timestampValue'] = _TIMESTAMPVALUE
DESCRIPTOR.message_types_by_name['longValue'] = _LONGVALUE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE

integerValue = _reflection.GeneratedProtocolMessageType('integerValue', (_message.Message,), dict(
  DESCRIPTOR = _INTEGERVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.integerValue)
  ))
_sym_db.RegisterMessage(integerValue)

stringValue = _reflection.GeneratedProtocolMessageType('stringValue', (_message.Message,), dict(
  DESCRIPTOR = _STRINGVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.stringValue)
  ))
_sym_db.RegisterMessage(stringValue)

bytesValue = _reflection.GeneratedProtocolMessageType('bytesValue', (_message.Message,), dict(
  DESCRIPTOR = _BYTESVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.bytesValue)
  ))
_sym_db.RegisterMessage(bytesValue)

doubleValue = _reflection.GeneratedProtocolMessageType('doubleValue', (_message.Message,), dict(
  DESCRIPTOR = _DOUBLEVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.doubleValue)
  ))
_sym_db.RegisterMessage(doubleValue)

booleanValue = _reflection.GeneratedProtocolMessageType('booleanValue', (_message.Message,), dict(
  DESCRIPTOR = _BOOLEANVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.booleanValue)
  ))
_sym_db.RegisterMessage(booleanValue)

decimalValue = _reflection.GeneratedProtocolMessageType('decimalValue', (_message.Message,), dict(
  DESCRIPTOR = _DECIMALVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.decimalValue)
  ))
_sym_db.RegisterMessage(decimalValue)

timestampValue = _reflection.GeneratedProtocolMessageType('timestampValue', (_message.Message,), dict(
  DESCRIPTOR = _TIMESTAMPVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.timestampValue)
  ))
_sym_db.RegisterMessage(timestampValue)

longValue = _reflection.GeneratedProtocolMessageType('longValue', (_message.Message,), dict(
  DESCRIPTOR = _LONGVALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.longValue)
  ))
_sym_db.RegisterMessage(longValue)

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'dstore.values_pb2'
  # @@protoc_insertion_point(class_scope:dstore.values.Value)
  ))
_sym_db.RegisterMessage(Value)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\tio.dstoreZ\026gosdk.dstore.de/values'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities
# @@protoc_insertion_point(module_scope)