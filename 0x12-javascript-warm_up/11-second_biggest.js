#!/usr/bin/node


let zero = 0;
const numList = process.argv.slice(2);
if (numList.length > 1) {
  numList.sort(function (a, b) {
    return a - b;
  });
  zero = numList[numList.length - 2];
}
console.log(zero);
