#!/usr/bin/node

const sz = Math.floor(Number(process.argv[2]));

if (isNaN(sz)) {
  console.log('Missing size');
} else {
  for (let d = 0; d < sz; d++) {
    let rw = '';

    for (let a = 0; a < sz; a++) rw += 'X';
    console.log(rw);
  }
}
