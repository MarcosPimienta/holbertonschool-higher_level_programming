#!/usr/bin/python3
"""fetches url"""
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.text

    print("{}\n\t- type: {}\n\t- content: {}"
          .format("Body response:", type(data), data))
