#!/bin/bash

# Stop server_4.py using pm2
pm2 stop dash_test_gprc_stream_server_python 

# Remove from pm2 process list
pm2 delete dash_test_gprc_stream_server_python

# Print status
pm2 status
