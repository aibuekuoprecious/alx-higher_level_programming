#!/usr/bin/node

// Require the request module
const request = require('request');

// Get the episode number from the command line arguments
const episodeNumber = process.argv[2];

// Construct the API URL
const url = 'https://swapi-api.hbtn.io/api/films/' + episodeNumber + '/';

// Make a GET request to the API URL
request(url, async (err, response, body) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Get the array of character URLs
  const characterUrls = movieData.characters;

  // Make a GET request to each character URL and print the character name
  for (const characterUrl of characterUrls) {
    await request(characterUrl, async (err, response, body) => {
      if (err) {
        console.log(err);
        return;
      }

      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  }
});
