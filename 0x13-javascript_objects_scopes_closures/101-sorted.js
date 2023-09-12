#!/usr/bin/node

const dict = require('./101-data').dict;

const tolist = Object.entries(dict);
const vl = Object.values(dict);
const vluni = [...new Set(vl)];
const newd = {};

for (const x in vluni) {
  const nlist = [];
  for (const a in tolist) {
    if (tolist[a][1] === vluni[x]) {
      nlist.unshift(tolist[a][0]);
    }
  }
  newd[vluni[x]] = nlist;
}

console.log(newd);
