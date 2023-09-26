#!/usr/bin/node
/* script that display the status code of a GET request */
const request = require('request');
const process = require('process');

request
  .get(process.argv[2])
  .on('response', (response) => {
    console.log(`code: ${response.statusCode}`);
  });
