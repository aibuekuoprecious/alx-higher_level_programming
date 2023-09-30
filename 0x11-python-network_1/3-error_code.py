#!/usr/bin/python3
"""
This script sends a request to a URL, displays the body of
the response (decoded in UTF-8), and handles HTTPError
exceptions to print the HTTP status code.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":

    url = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(url) as response:
            url_res = response.read()
            print(url_res.decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
