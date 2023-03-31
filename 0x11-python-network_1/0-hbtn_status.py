#!/usr/bin/python3
"""
What's my status?
"""
if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as f:
        print('Body response:')
        data = f.read()
        print('\t- type: {}'.format(type(data)))
        print('\t- content: {}'.format(data))
        print('\t- utf8 content: {}'.format(data.decode('utf-8')))
