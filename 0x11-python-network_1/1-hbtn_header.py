#!/usr/bin/python3
"""a Python script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id variable found
in the header of the response"""

from urllib import request
import sys
url = sys.argv[1]

if __name__ == "__main__":
    with request.urlopen(url) as response:
        print(dict(response.headers).get("X-Request-Id"))
