#!/usr/bin/node

// Require the request module
const request = require('request');

// Get the episode number from the command line arguments
const id = process.argv[2];

// Construct the API URL
const apiUrl = 'https://swapi-api.hbtn.io/api/films/' + id + '/';

// Make a GET request to the API URL
request(apiUrl, async (err, response, body) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Print the title of the movie
  console.log(movieData.title);
});
