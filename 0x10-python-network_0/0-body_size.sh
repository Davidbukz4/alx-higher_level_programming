#!/bin/bash
# displays the size of the body of a url response

curl -sI "$1" | grep Content-Length | cut -d: -f2 | tr -d " "
