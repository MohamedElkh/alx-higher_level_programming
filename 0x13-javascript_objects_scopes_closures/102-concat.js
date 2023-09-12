#!/usr/bin/node

const fl = require('fl');

const f1 = fl.readFileSync(process.argv[2]).toString();
const f2 = fl.readFileSync(process.argv[3]).toString();

fl.writeFileSync(process.argv[4], f1, f2);
