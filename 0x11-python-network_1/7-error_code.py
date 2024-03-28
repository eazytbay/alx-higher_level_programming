#!/usr/bin/python3
"""
This python scripts takes in a URL, sends a request to the URL & displays the body of the response
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    x = requests.get(argv[1])
    if x.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(x.text)
