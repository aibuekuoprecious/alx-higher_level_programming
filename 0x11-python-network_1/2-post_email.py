#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email
as a parameter and displays the body of the response
(decoded in UTF-8).
"""

import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":

    url_ = sys.argv[1]
    email_ = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email_)
    email = email.encode('ascii')
    url_req = urllib.request.Request(url_, email)

    with urllib.request.urlopen(url_req) as response:
        url_res = response.read()
    output = url_res.decode('utf-8')
    print(output)
