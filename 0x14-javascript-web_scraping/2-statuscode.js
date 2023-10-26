#!/usr/bin/node

// Require the request module
const request = require('request');

// Get the URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the URL
request(url, async (err, response) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Print the status code of the response
  console.log(`Status code: ${response.statusCode}`);
});
