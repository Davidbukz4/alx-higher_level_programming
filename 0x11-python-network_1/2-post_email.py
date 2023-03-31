#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a post request to the
passed URL with the email as parameter and displays the body of the response
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.parse

    data = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(data).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as f:
        body = f.read().decode('utf-8')
        print(body)
