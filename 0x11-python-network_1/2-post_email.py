#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)"""

from urllib import request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = parse.urlencode(email)
    data_enc = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        tab = response.read()
        print(tab.decode('utf8'))
