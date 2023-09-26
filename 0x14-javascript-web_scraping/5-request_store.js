#!/usr/bin/node
/* Write a script that gets the contents of a webpage and stores it in a file */
const request = require('request');
const fs = require('fs');
const process = require('process');

const path = process.argv[3];
const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = body;
  fs.writeFile(path, data, (err) => {
    if (err) {
      console.log(err);
    }
  });
});
