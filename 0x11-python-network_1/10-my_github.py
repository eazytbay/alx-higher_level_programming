#!/usr/bin/python3
'''
This python script Takes your Github credentials (username and password)
and uses the Github API to display your id
'''
import requests as r
from sys import argv


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    fdbk = r.get(url, auth=(argv[1], argv[2]))
    json_fdbk = fdbk.json()
    print(json_fdbk.get('id'))
