#!/usr/bin/node

// Require the request module
const request = require('request');

// Get the API URL from the command line arguments
const url = process.argv[2];

// Make a GET request to the API URL
request(url, async (err, response, body) => {
  // Handle any errors
  if (err) {
    console.log(err);
    return;
  }

  // Parse the JSON response
  const json = JSON.parse(body);

  // Create a map to store the number of completed tasks for each user ID
  const completedTaskCounts = new Map();

  // Iterate over the JSON response and count the number of completed tasks for each user ID
  for (const task of json) {
    if (task.completed) {
      const userId = task.userId;
      let completedTaskCount = completedTaskCounts.get(userId);
      if (completedTaskCount === undefined) {
        completedTaskCount = 0;
      }
      completedTaskCounts.set(userId, completedTaskCount + 1);
    }
  }

  // Print the map
  console.log(completedTaskCounts);
});
