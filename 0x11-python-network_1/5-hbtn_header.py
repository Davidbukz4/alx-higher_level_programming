#!/usr/bin/python3
"""
A script taht fetches from https://alx-intrabet.hbtn.io/status
using request module
"""

if __name__ == '__main__':
    import requests
    import sys

    req = requests.get(sys.argv[1])
    print(req.headers['X-Request-Id'])
