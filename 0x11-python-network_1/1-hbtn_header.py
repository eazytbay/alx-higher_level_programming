#!/usr/bin/python3
"""
This scripts takes in a URL, sends a request to the URL and                                    displays the value of the X-Request-Id variable                                                 found in the header of the response
"""
if __name__ == "__main__":
    import urllib.request as request
    from sys import argv
    x = request.Request(argv[1])
    with request.urlopen(x) as r:
        print(r.headers.get('X-Request-Id'))
