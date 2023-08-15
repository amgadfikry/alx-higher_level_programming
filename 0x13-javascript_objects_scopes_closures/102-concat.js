#!/usr/bin/node

const argv = process.argv;
const fs = require('fs');
const file1 = fs.readFileSync(argv[2], { encoding: 'utf8', flag: 'r' });
const file2 = fs.readFileSync(argv[3], { encoding: 'utf8', flag: 'r' });
fs.writeFileSync(argv[4], file1 + file2);
