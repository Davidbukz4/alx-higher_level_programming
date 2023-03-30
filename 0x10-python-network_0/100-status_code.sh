#!/bin/bash
# sends a request to a url passed as first arg and displays status code of response
curl -so /dev/null -w "%{http_code}" "$1"
