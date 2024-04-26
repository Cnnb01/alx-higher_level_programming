#!/usr/bin/python3
"""a Python script that takes in a URL"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(url) as response:
            tab = response.read().decode('utf8')
            print (tab)
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
