#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send a DELETE request to the URL and display the body of the response
response=$(curl -s -X DELETE "$url")

# Display the body of the response
echo "$response"
