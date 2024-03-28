#!/usr/bin/python3
"""
This python scripts takes in a URL, sends a request to the URL &\ 
displays the body of the response
"""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
