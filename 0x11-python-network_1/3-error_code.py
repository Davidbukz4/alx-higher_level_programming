#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL and displays the body
of the response
"""

if __name__ == '__main__':
    import sys
    import urllib.request
    import urllib.error

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as f:
            data = f.read().decode('utf-8')
            print(data)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
