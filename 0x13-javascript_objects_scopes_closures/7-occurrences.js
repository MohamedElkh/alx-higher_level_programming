#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.reduce((num, curr) => curr === searchElement ? num + 1 : num, 0);
};
