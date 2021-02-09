#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  let n = 0;
  for (i; i <= list.length; i++) {
    if (list[i] === searchElement) {
      n += 1;
    }
  }
  return (n);
};
