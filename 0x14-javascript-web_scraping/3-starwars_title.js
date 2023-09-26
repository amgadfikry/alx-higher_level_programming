#!/usr/bin/node
/* script that prints the title of a Star Wars movie */
const process = require('process');
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (parseError) {
    console.error(parseError);
  }
});
