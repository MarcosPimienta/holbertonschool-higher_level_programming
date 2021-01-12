#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)."""

import sys
import requests

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    usr = sys.argv[1]
    pswd = sys.argv[2]
    response = requests.get(url, auth=(usr, pswd))
    jsonRes = response.json()
    print(jsonRes.get('id'))
