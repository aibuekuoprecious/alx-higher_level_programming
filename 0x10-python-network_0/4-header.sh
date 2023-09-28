#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Use curl to send a GET request to the URL with the X-School-User-Id header set to 98
response=$(curl -s -H "X-School-User-Id: 98" "$url")

# Display the body of the response
echo "$response"
