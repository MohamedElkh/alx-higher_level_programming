#!/usr/bin/node
const nm = Math.floor(Number(process.argv[2]));

console.log(isNaN(nm) ? 'Not a number' : `My number: ${nm}`);
