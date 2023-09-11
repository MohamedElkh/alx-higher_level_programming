#!/usr/bin/node

function fact (num) {
  return num === 0 || isNaN(num) ? 1 : num * fact(num - 1);
}

console.log(fact(Number(process.argv[2])));
