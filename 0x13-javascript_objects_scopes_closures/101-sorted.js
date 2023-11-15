#!/usr/bin/node

const first_dict = require('./101-data').dict;
const second_dict = {};
for (const key in first_dict) {
  second_dict[first_dict[key]] = [];
}
for (const key in first_dict) {
  second_dict[first_dict[key]].push(key);
}
console.log(second_dict);
