#!/usr/bin/python3
"""sends a request to the URL and displays the requested values"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values).encode('ascii')
    with urllib.request.urlopen(url, data) as response:
        the_page = response.read()
    print(the_page.decode('utf-8'))
