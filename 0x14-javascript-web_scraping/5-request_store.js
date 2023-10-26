#!/usr/bin/node

// Require the request and file system modules
const request = require('request');
const fs = require('fs');

// Get the URL and filename from the command line arguments
const url = process.argv[2];
const filename = process.argv[3];

// Make a GET request to the URL
request(url, async (err, response, body) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Write the body of the response to the file
  await fs.promises.writeFile(filename, body);

  // Print a success message
  console.log(`Successfully wrote webpage contents to file ${filename}`);
});
