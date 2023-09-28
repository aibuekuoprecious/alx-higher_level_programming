#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send a request to the URL and display only the status code
curl -s -o /dev/null -w "%{http_code}" "$url"
