#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send a GET request to the URL and store the response in a variable
response=$(curl -s -o /dev/null -w "%{http_code}" "$url")

# Check if the response status code is 200 (OK)
if [ "$response" -eq 200 ]; then
  # If the status code is 200, retrieve and display the response body
  curl -s "$url"
else
  echo "Response status code is not 200 (OK)"
fi
