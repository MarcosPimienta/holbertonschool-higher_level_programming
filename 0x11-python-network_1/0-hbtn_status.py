#!/usr/bin/python3
"""Fetch status from web"""
from urllib import request
with request.urlopen("https://intranet.hbtn.io/status") as resp:
    data = resp.read()
    html = data.decode()

print("{}\n\t- type: {}\n\t- content: {}\n\t- utf8 content: '{}'"
      .format("Body response:", type(data), data, html))
