#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL & displays 
the body of the response
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as f:
            res = f.read().decode('utf-8')
        print(res)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
