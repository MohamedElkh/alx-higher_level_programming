#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let a = 0; a < this.height; a++) {
      let st = '';

      for (let i = 0; i < this.width; i++) {
        st += 'X';
      }
      console.log(st);
    }
  }

  rotate () {
    const ax = this.width;
    this.width = this.height;
    this.height = ax;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
