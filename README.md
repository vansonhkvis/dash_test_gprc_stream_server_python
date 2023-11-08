
### Install
```shell
# python3.7+
python3 -m pip install -r requirements.txt

# python<3.7
python3 -m pip install -r requirements_py35.txt

```

### Rebuild protos
```shell

python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. ./protos/todo.proto

```

### Deploy (pm2)
```shell
# start
./deployforever.sh

# stop
./deploystop.sh

```

