#!/bin/bash

# Check if both URL and JSON file arguments are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <URL> <JSON_FILE>"
  exit 1
fi

# Store the URL and JSON file in variables
url="$1"
json_file="$2"

# Check if the JSON file is valid JSON
if ! jq . "$json_file" &>/dev/null; then
  echo "Not a valid JSON"
  exit 1
fi

# Use curl to send a JSON POST request with the contents of the file as the body
response=$(curl -s -H "Content-Type: application/json" -d "@$json_file" "$url")

# Display the body of the response
echo "$response"
