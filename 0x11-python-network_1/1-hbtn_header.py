#!/usr/bin/python3
"""
This script sends a request to a URL and displays
the value of the X-Request-Id variable found in
the header of the response.
"""

import sys
import urllib.request

if __name__ == '__main__':

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        url_res = response.info()
        print(url_res['X-Request-Id'])