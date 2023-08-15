#!/usr/bin/node

const dict = require('./101-data.js').dict;

const values = [...new Set(Object.values(dict).sort())];
const obj = {};
values.forEach(el => { obj[el] = []; });
for (const key in dict) {
  const val = dict[key];
  obj[val].push(key);
}
console.log(obj);
