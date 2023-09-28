#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send a request to the URL and store the response in a variable
response=$(curl -sI "$url")

# Extract the content length from the response headers
content_length=$(echo "$response" | grep -i 'Content-Length' | awk '{print $2}')

# Check if Content-Length header is found
if [ -n "$content_length" ]; then
  echo "$content_length"
else
  echo "Content-Length not found in the response headers"
fi
