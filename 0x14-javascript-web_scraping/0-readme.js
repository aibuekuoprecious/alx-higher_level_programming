#!/usr/bin/node

// Require the file system module
const fs = require('fs');

// Get the file name from the command line arguments
const filename = process.argv[2];

// Read the file contents
fs.readFile(filename, 'utf8', async (err, data) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Print the file contents
  console.log(data.toString());
});
