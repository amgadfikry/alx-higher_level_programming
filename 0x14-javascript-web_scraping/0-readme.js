#!/usr/bin/node
/* script that reads and prints the content of a file */
const process = require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }
  console.log(data.toString());
});
