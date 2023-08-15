#!/usr/bin/node

const square = require('./5-square');

class Square extends square {
  charPrint (c) {
    if (c) {
      this.print(c);
    } else {
      this.print('X');
    }
  }
}

module.exports = Square;
