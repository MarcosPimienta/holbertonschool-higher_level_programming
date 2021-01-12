#!/usr/bin/python3
"""displays the body of the response (decoded in utf-8)."""

import sys
import requests

if __name__ == "__main__":

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    response = requests.post(url, data)
    jsonRes = response.json()
    if type(jsonRes) is not dict:
        print("Not a valid JSON")
    elif len(jsonRes) == 0:
        print("No result")
    else:
        jstring = jsonRes.get('[id]')
        print(jstring, jsonRes['name'], sep=' ')
