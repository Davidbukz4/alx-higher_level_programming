#!/bin/bash
# displays the size of the body of a url response

curl -s "$1" | wc -c
