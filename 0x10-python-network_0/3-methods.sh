#!/bin/bash
# This is a script that takes in a URL and displays all HTTP methods                            the server will accept.
curl -si -L "$1" -X OPTIONS | grep "Allow" | awk -F ": " '{print $2}'
