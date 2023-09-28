#!/bin/bash

# Check if the URL argument is provided
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Store the URL in a variable
url="$1"

# Define the parameters for the POST request
email="test@gmail.com"
subject="I will always be here for PLD"

# Use curl to send a POST request to the URL with the specified parameters
response=$(curl -s -X POST -d "email=$email" -d "subject=$subject" "$url")

# Display the body of the response
echo "$response"
