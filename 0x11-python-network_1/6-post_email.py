#!/usr/bin/python3
"""
A script taht fetches from https://alx-intrabet.hbtn.io/status
using request module
"""

if __name__ == '__main__':
    import requests
    import sys

    params = {"email": sys.argv[2]}
    req = requests.post(sys.argv[1], data=params)
    print(req.text)
