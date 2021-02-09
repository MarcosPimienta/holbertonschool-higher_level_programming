#!/usr/bin/node

const SquareX = require('./5-square');

class Square extends SquareX {
  charPrint (C) {
    if (C == null) {
      C = 'X';
    }
    let i = 0;
    for (i; i < this.height; i++) {
      console.log(C.repeat(this.width));
    }
  }
}

module.exports = Square;
