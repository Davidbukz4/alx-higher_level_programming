#!/bin/bash
# displays all methods the http server will accept
curl -sI "$1" | grep Allow | cut -d: -f2 | cut -c 2-
