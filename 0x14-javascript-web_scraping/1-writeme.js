#!/usr/bin/node
/* script that writes a string to a file. */
const fs = require('fs');
const process = require('process');

fs.writeFile(process.argv[2], process.argv[3], (err) => {
  if (err) {
    console.log(err);
  }
});