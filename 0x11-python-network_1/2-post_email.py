#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response
(decoded in utf-8)"""

from urllib import request
from urllib import parse
import sys
url = sys.argv[1]
email = sys.argv[2]

if __name__ == "__main__":
    data = parse.urlencode(email)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        tab = response.read()
        print("Your email is: ".format(tab.decode('utf8')))
