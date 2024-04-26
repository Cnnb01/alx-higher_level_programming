#!/usr/bin/python3
"""a Python script that fetches"""
import requests
import sys

if __name__ == "__main__":
    r = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}

    inp = requests.post(r, data=data)
    print(inp.text)
