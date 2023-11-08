
import grpc
from protos import todo_pb2
from protos import todo_pb2_grpc

def receive_todo_stream():
    channel = grpc.insecure_channel('localhost:50051')
    stub = todo_pb2_grpc.TodoServiceStub(channel)
    request = todo_pb2.TodoRequest(filter='')

    try:
        response_stream = stub.StreamTodos(request)
        for todo in response_stream:
            print(f"Received ToDo: ID={todo.id}, Text={todo.text}, Completed={todo.completed}")
    except grpc.RpcError as e:
        print(f"Error occurred: {e}")

if __name__ == '__main__':
    receive_todo_stream()

