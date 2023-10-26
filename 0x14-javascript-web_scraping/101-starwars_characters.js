#!/usr/bin/node

// Require the request module
const request = require('request');

// Get the episode number from the command line arguments
const episodeNumber = process.argv[2];

// Construct the API URL
const url = `https://swapi-api.hbtn.io/api/films/${episodeNumber}/`;

// Make a GET request to the API URL
request(url, async (err, response, body) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Get the array of character URLs in the correct order
  const characterUrls = movieData.characters.sort((a, b) => a - b);

  // Print the characters in the correct order
  for (const characterUrl of characterUrls) {
    const characterData = await request(characterUrl);
    console.log(characterData.name);
  }
});
