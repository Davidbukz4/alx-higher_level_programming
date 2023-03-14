#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the
// rectangle using the character c
// If c is undefined, use the character X

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

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
