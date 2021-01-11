#!/usr/bin/python3
"""Fetch status from web"""
from urllib import request
resp = request.urlopen("https://intranet.hbtn.io/status")
data = resp.read()
code = resp.code
html = data.decode("UTF-8")
print("- type: {}".format(type(data)))
if code == 200:
    print("- content: b'{}'".format("OK"))
if type(html) == str:
    print("- utf8 content:'{}'".format("OK"))
