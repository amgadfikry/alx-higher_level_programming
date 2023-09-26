#!/usr/bin/node
/* script that prints all characters of a Star Wars movi */
const request = require('request');
const process = require('process');

const url = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  data.characters.forEach((el) => {
    request(el, (error, response, dt) => {
      if (error) {
        console.log(error);
        return;
      }
      const chara = JSON.parse(dt).name;
      console.log(chara);
    });
  });
});
