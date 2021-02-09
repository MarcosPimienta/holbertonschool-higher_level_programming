#!/usr/bin/node

let i = 0;
exports.logMe = function (item) {
  function prnt (item) {
    console.log(i + ': ' + item);
    i++;
  }
  return (prnt(item));
};
