#!/usr/bin/python3
"""
What's my status?
"""
if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as f:
        print('Body response:')
        data = f.read()
        print('\t - type: {}'.format(type(data)))
        print('\t - content: {}'.format(data))
        print('\t - utf8 content: {}'.format(data.decode('utf-8')))
