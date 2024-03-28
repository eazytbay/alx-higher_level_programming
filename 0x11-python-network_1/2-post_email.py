#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the                           passed URL with the email as a parameter, and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.parse as parse
    import urllib.request as request
    from sys import argv
    val = {'email': argv[2]}
    data = parse.urlencode(val).encode('utf-8')
    x = request.Request(argv[1], data)
    with request.urlopen(x) as r:
        print(r.read().decode('utf-8'))
