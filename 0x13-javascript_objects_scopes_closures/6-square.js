#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the
// rectangle using the character c
// If c is undefined, use the character X

const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c = 'X') {
    let i;
    let rowString = '';
    for (i = 0; i < this.width; i++) {
      rowString += c;
    }
    for (i = 0; i < this.height; i++) {
      console.log(rowString);
    }
  }
}

module.exports = Square;
