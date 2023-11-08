
import grpc
from concurrent import futures
import time

import random


from protos import todo_pb2
from protos import todo_pb2_grpc

class TodoService(todo_pb2_grpc.TodoServiceServicer):
    def StreamTodos(self, request, context):
        # Simulate streaming ToDo items
        todos = [
            todo_pb2.Todo(id='1', text='Buy groceries', completed=False),
            todo_pb2.Todo(id='2', text='Walk the dog', completed=True),
            todo_pb2.Todo(id='3', text='Do laundry', completed=False),
        ]


        # Randomly select 3 ToDo items from the list
        selected_todos = random.sample(todos, k=3)

        # Yield each selected ToDo item
        for todo in selected_todos:
            yield todo


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    todo_pb2_grpc.add_TodoServiceServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('gRPC server started on port 50051')
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()

