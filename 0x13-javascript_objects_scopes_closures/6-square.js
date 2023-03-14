#!/usr/bin/node
// Create an instance method called charPrint(c) that prints the
// rectangle using the character c
// If c is undefined, use the character X

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let i;
    if (c === undefined) {
      for (i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width));
      }
    } else {
      for (i = 0; i < this.height; i++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
