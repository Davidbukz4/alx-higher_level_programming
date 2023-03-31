#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as parameter
"""

if __name__ == '__main__':
    import sys
    import requests
    ch = "" if not sys.argv[1] else sys.argv[1]
    param = {"q": ch}
    req = requests.post('http://0.0.0.0:5000/search_user', data=param)

    try:
        r = req.json()
        if r == {}:
            print("No result")
        else:
            print('[{}] {}'.format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
