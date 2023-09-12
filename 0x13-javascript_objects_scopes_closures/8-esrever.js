#!/usr/bin/node

exports.esrever = function (list) {
  let le = list.length - 1;
  let x = 0;

  while ((le - x) > 0) {
    const ax = list[le];

    list[le] = list[x];
    list[x] = ax;

    x++;
    le--;
  }
  return list;
};
