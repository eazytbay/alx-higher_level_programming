#!/usr/bin/python3
"""
This python scripts takes in a letter and sends a POST request to http://0.0.0.0:5000/          search_user with the letter as a parameter
"""
if __name__ == '__main__':
    import requests
    from sys import argv
    if len(argv) == 2:
        y = argv[1]
    else:
        y = ""
    x = requests.post('http://0.0.0.0:5000/search_user', data={'y': y})
    try:
        x_dict = x.json()
        id = x_dict.get('id')
        name = x_dict.get('name')
        if len(x_dict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(x_dict.get('id'), x_dict.get('name')))
    except:
        print("Not a valid JSON")
