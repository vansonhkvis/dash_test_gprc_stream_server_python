#!/bin/bash

# Change to the directory where server_4.py is located
cd ./

# Start server_6.py using pm2
pm2 start server.py \
  --interpreter=python3 \
  --name dash_test_gprc_stream_server_python

# Print status
pm2 status





