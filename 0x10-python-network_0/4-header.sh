#!/bin/bash
# sends a GET request to a url passed as first arg with a header variable
curl -sH "X-School-User-Id: 98" "$1"
