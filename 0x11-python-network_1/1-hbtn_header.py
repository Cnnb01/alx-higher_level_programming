#!/usr/bin/python3
"""a Python script that takes in a URL"""

from urllib import request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
