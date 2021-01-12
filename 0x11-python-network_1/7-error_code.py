#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)."""

import sys
import requests

if __name__ == "__main__":
        url = sys.argv[1]
        response = requests.get(url)
        data = response.text
        if response.status_code < 400:
            print("{}".format(data))
        else:
            print("Error code: {}".format(response.status_code))
