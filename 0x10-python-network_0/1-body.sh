#!/bin/bash
# This bash scripts takes in URL send GET request which displays ist body
curl -sL "$1" -X GET
