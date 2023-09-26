#!/usr/bin/node
/* script that prints the title of a Star Wars movie */
const process = require('process');
const request = require('request');

const url = process.argv[2];

request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body).results;
  let num = 0;
  data.forEach((el) => {
    el.characters.forEach((ele) => {
      if (ele.includes('/18')) {
        num++;
      }
    });
  });
  console.log(num);
});
