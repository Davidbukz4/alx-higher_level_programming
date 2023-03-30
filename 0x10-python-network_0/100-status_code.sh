#!/bin/bash
# sends a request to a url passed as first arg and displays status code of response
curl -sI "$1" | grep 'HTTP/1.1' | cut -d' ' -f2 | tr -d '\n'
