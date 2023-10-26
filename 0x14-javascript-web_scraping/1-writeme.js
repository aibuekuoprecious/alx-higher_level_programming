#!/usr/bin/node

// Require the file system module
const fs = require('fs');

// Get the file name and text to write from the command line arguments
const filename = process.argv[2];
const text = process.argv[3];

// Write the text to the file
fs.writeFile(filename, text, 'utf8', async (err) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Print a success message
  console.log(`Successfully wrote text to file ${filename}`);
});
