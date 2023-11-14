#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let rect = '';
    for (let x = 0; x < this.width; x++) {
      rect += 'X';
    }
    for (let y = 0; y < this.height; y++) {
      console.log(rect);
    }
  }
  
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
  
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
