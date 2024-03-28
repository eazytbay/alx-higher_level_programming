#!/usr/bin/python3
"""
This is a python script that fetches https://alx-intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests
    x = requests.get('https://alx-intranet.hbtn.io/status')
    text = x.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
