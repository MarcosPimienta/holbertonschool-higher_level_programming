#!/usr/bin/python3
"""sends a request to the URL and displays the requested values"""
import sys
from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as resp:
        data = resp.info()
    print("{}".format(data['X-Request-Id']))
