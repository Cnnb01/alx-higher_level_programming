#!/usr/bin/python3
"""using urllib to fetch https://alx-intranet.hbtn.io/status"""

from urllib import request

if __name__ == "__main__":

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        tab = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(tab)))
        print("\t- content: {}".format(tab))
        print("\t- utf8 content: {}".format(tab.decode('utf8')))
