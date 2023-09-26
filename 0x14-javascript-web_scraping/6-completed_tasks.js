#!/usr/bin/node
/* script that computes the number of tasks completed by user id */
const request = require('request');
const process = require('process');

request.get(process.argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  const obj = {};
  data.forEach((el) => {
    if (el.completed) {
      if (el.userId in obj) {
        obj[el.userId]++;
      } else {
        obj[el.userId] = 1;
      }
    }
  });
  console.log(obj);
});
