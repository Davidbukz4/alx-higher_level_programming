#!/bin/bash
# sends a post request to a url passed as arg
curl -s "$1" -X POST -d email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD
