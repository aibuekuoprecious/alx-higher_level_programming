#!/bin/bash
# Use curl to make a POST request to the specified URL with a special header
curl -s -X PUT -H "Origin: HolbertonSchool" -d "user_id=98" "http://0.0.0.0:5000/catch_me"
