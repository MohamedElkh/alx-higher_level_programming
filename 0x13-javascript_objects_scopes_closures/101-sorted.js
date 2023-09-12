#!/usr/bin/node

const dict = require('./101-data.js').dict;
let newd = {};

for (let x in dict) {
  if (newd[dict[x]] === undefined) {
    newd[dict[x]] = [x];
  } else {
    newd[dict[x]].push(x);
  }
}

console.log(newd);
