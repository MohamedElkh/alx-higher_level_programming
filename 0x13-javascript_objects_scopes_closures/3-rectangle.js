#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {

      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let x = 0; x < this.height; x++) {
      let st = '';

      for (let a = 0; a < this.width; a++) {
        st += 'X';
      }

      console.log(st);
    }
  }
}


module.exports = Rectangle;
