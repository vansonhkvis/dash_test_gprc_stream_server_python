# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import todo_pb2 as protos_dot_todo__pb2


class TodoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StreamTodos = channel.unary_stream(
                '/todo.TodoService/StreamTodos',
                request_serializer=protos_dot_todo__pb2.TodoRequest.SerializeToString,
                response_deserializer=protos_dot_todo__pb2.Todo.FromString,
                )


class TodoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StreamTodos(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TodoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StreamTodos': grpc.unary_stream_rpc_method_handler(
                    servicer.StreamTodos,
                    request_deserializer=protos_dot_todo__pb2.TodoRequest.FromString,
                    response_serializer=protos_dot_todo__pb2.Todo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'todo.TodoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TodoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StreamTodos(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/todo.TodoService/StreamTodos',
            protos_dot_todo__pb2.TodoRequest.SerializeToString,
            protos_dot_todo__pb2.Todo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
