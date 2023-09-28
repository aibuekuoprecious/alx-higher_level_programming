#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send an OPTIONS request to the URL and display the Allow header
allow_header=$(curl -s -I -X OPTIONS "$url" | grep -i 'Allow')

# Extract and display the allowed HTTP methods from the Allow header
if [ -n "$allow_header" ]; then
  methods=$(echo "$allow_header" | awk -F ': ' '{print $2}')
  echo "$methods"
else
  echo "Could not retrieve the allowed HTTP methods."
fi
