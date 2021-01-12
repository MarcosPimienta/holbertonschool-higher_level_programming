#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)."""

import sys
import requests

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        response = requests.get(url)
        data = response.text
        print("{}".format(data))
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.code))
