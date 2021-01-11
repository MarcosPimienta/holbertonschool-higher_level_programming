#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)."""
import sys
import urllib.parse
from urllib import request

if __name__ == "__main__":
        try:
            with request.urlopen(sys.argv[1]) as resp:
                data = resp.read()
            print("{}".format(data))
        except urllib.error.URLError as e:
            print("Error code: {}".format(e.code))
