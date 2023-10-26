#!/usr/bin/node

// Require the request module
const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request(apiUrl, async (err, response, body) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Parse the JSON response
  const results = JSON.parse(body).results;

  // Count the number of movies where Wedge Antilles is present
  let count = 0;
  for (const result of results) {
    const characters = result.characters;
    if (characters.includes('https://swapi.dev/api/people/18/')) {
      count++;
    }
  }

  // Print the count
  console.log(count);
});
