#!/usr/bin/node

const list = require('./100-data.js').list;

const arr = list.map((el, index) => el * index);

console.log(list);
console.log(arr);
