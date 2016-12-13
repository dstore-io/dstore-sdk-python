# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dstore/engine/engine.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from dstore.engine import procedure_pb2 as dstore_dot_engine_dot_procedure__pb2
from dstore import values_pb2 as dstore_dot_values__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dstore/engine/engine.proto',
  package='dstore.engine',
  syntax='proto3',
  serialized_pb=_b('\n\x1a\x64store/engine/engine.proto\x12\rdstore.engine\x1a\x1d\x64store/engine/procedure.proto\x1a\x13\x64store/values.proto2\xce\x02\n\x06\x45ngine\x12U\n\rexecProcedure\x12\x1d.dstore.engine.procedure.Call\x1a!.dstore.engine.procedure.Response\"\x00\x30\x01\x12S\n\texecBatch\x12\x1d.dstore.engine.procedure.Call\x1a!.dstore.engine.procedure.Response\"\x00(\x01\x30\x01\x12J\n\x0e\x63reateUniqueID\x12\x1a.dstore.values.stringValue\x1a\x1a.dstore.values.stringValue\"\x00\x12L\n\x0fisValidUniqueID\x12\x1a.dstore.values.stringValue\x1a\x1b.dstore.values.booleanValue\"\x00\x42*\n\x10io.dstore.engineZ\x16gosdk.dstore.de/engineb\x06proto3')
  ,
  dependencies=[dstore_dot_engine_dot_procedure__pb2.DESCRIPTOR,dstore_dot_values__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)





DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\020io.dstore.engineZ\026gosdk.dstore.de/engine'))
import grpc
from grpc.beta import implementations as beta_implementations
from grpc.beta import interfaces as beta_interfaces
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities


class EngineStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.execProcedure = channel.unary_stream(
        '/dstore.engine.Engine/execProcedure',
        request_serializer=dstore_dot_engine_dot_procedure__pb2.Call.SerializeToString,
        response_deserializer=dstore_dot_engine_dot_procedure__pb2.Response.FromString,
        )
    self.execBatch = channel.stream_stream(
        '/dstore.engine.Engine/execBatch',
        request_serializer=dstore_dot_engine_dot_procedure__pb2.Call.SerializeToString,
        response_deserializer=dstore_dot_engine_dot_procedure__pb2.Response.FromString,
        )
    self.createUniqueID = channel.unary_unary(
        '/dstore.engine.Engine/createUniqueID',
        request_serializer=dstore_dot_values__pb2.stringValue.SerializeToString,
        response_deserializer=dstore_dot_values__pb2.stringValue.FromString,
        )
    self.isValidUniqueID = channel.unary_unary(
        '/dstore.engine.Engine/isValidUniqueID',
        request_serializer=dstore_dot_values__pb2.stringValue.SerializeToString,
        response_deserializer=dstore_dot_values__pb2.booleanValue.FromString,
        )


class EngineServicer(object):

  def execProcedure(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def execBatch(self, request_iterator, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def createUniqueID(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def isValidUniqueID(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EngineServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'execProcedure': grpc.unary_stream_rpc_method_handler(
          servicer.execProcedure,
          request_deserializer=dstore_dot_engine_dot_procedure__pb2.Call.FromString,
          response_serializer=dstore_dot_engine_dot_procedure__pb2.Response.SerializeToString,
      ),
      'execBatch': grpc.stream_stream_rpc_method_handler(
          servicer.execBatch,
          request_deserializer=dstore_dot_engine_dot_procedure__pb2.Call.FromString,
          response_serializer=dstore_dot_engine_dot_procedure__pb2.Response.SerializeToString,
      ),
      'createUniqueID': grpc.unary_unary_rpc_method_handler(
          servicer.createUniqueID,
          request_deserializer=dstore_dot_values__pb2.stringValue.FromString,
          response_serializer=dstore_dot_values__pb2.stringValue.SerializeToString,
      ),
      'isValidUniqueID': grpc.unary_unary_rpc_method_handler(
          servicer.isValidUniqueID,
          request_deserializer=dstore_dot_values__pb2.stringValue.FromString,
          response_serializer=dstore_dot_values__pb2.booleanValue.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'dstore.engine.Engine', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class BetaEngineServicer(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def execProcedure(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def execBatch(self, request_iterator, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def createUniqueID(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
  def isValidUniqueID(self, request, context):
    context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


class BetaEngineStub(object):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This class was generated
  only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
  def execProcedure(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  def execBatch(self, request_iterator, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  def createUniqueID(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  createUniqueID.future = None
  def isValidUniqueID(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
    raise NotImplementedError()
  isValidUniqueID.future = None


def beta_create_Engine_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_deserializers = {
    ('dstore.engine.Engine', 'createUniqueID'): dstore_dot_values__pb2.stringValue.FromString,
    ('dstore.engine.Engine', 'execBatch'): dstore_dot_engine_dot_procedure__pb2.Call.FromString,
    ('dstore.engine.Engine', 'execProcedure'): dstore_dot_engine_dot_procedure__pb2.Call.FromString,
    ('dstore.engine.Engine', 'isValidUniqueID'): dstore_dot_values__pb2.stringValue.FromString,
  }
  response_serializers = {
    ('dstore.engine.Engine', 'createUniqueID'): dstore_dot_values__pb2.stringValue.SerializeToString,
    ('dstore.engine.Engine', 'execBatch'): dstore_dot_engine_dot_procedure__pb2.Response.SerializeToString,
    ('dstore.engine.Engine', 'execProcedure'): dstore_dot_engine_dot_procedure__pb2.Response.SerializeToString,
    ('dstore.engine.Engine', 'isValidUniqueID'): dstore_dot_values__pb2.booleanValue.SerializeToString,
  }
  method_implementations = {
    ('dstore.engine.Engine', 'createUniqueID'): face_utilities.unary_unary_inline(servicer.createUniqueID),
    ('dstore.engine.Engine', 'execBatch'): face_utilities.stream_stream_inline(servicer.execBatch),
    ('dstore.engine.Engine', 'execProcedure'): face_utilities.unary_stream_inline(servicer.execProcedure),
    ('dstore.engine.Engine', 'isValidUniqueID'): face_utilities.unary_unary_inline(servicer.isValidUniqueID),
  }
  server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
  return beta_implementations.server(method_implementations, options=server_options)


def beta_create_Engine_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
  """The Beta API is deprecated for 0.15.0 and later.

  It is recommended to use the GA API (classes and functions in this
  file not marked beta) for all further purposes. This function was
  generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
  request_serializers = {
    ('dstore.engine.Engine', 'createUniqueID'): dstore_dot_values__pb2.stringValue.SerializeToString,
    ('dstore.engine.Engine', 'execBatch'): dstore_dot_engine_dot_procedure__pb2.Call.SerializeToString,
    ('dstore.engine.Engine', 'execProcedure'): dstore_dot_engine_dot_procedure__pb2.Call.SerializeToString,
    ('dstore.engine.Engine', 'isValidUniqueID'): dstore_dot_values__pb2.stringValue.SerializeToString,
  }
  response_deserializers = {
    ('dstore.engine.Engine', 'createUniqueID'): dstore_dot_values__pb2.stringValue.FromString,
    ('dstore.engine.Engine', 'execBatch'): dstore_dot_engine_dot_procedure__pb2.Response.FromString,
    ('dstore.engine.Engine', 'execProcedure'): dstore_dot_engine_dot_procedure__pb2.Response.FromString,
    ('dstore.engine.Engine', 'isValidUniqueID'): dstore_dot_values__pb2.booleanValue.FromString,
  }
  cardinalities = {
    'createUniqueID': cardinality.Cardinality.UNARY_UNARY,
    'execBatch': cardinality.Cardinality.STREAM_STREAM,
    'execProcedure': cardinality.Cardinality.UNARY_STREAM,
    'isValidUniqueID': cardinality.Cardinality.UNARY_UNARY,
  }
  stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
  return beta_implementations.dynamic_stub(channel, 'dstore.engine.Engine', cardinalities, options=stub_options)
# @@protoc_insertion_point(module_scope)
