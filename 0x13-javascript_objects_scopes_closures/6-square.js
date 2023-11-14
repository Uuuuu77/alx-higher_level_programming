#!/usr/bin/node

const Square5 = require('./5-square');

module.exports = class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let rect = '';
    if (c === undefined) {
      c = 'X';
    }
    for (let x = 0; x < this.width; x++) {
      rect += c;
    }
    for (let y = 0; y < this.height; y++) {
      console.log(rect);
    }
  }
};
