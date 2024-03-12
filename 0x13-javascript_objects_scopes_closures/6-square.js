#!/usr/bin/node
const Square1 = require('./5-square');
class Square extends Square1 {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      for (let x = 0; x < this.height; x++) {
        console.log(c.repeat(this.width));
      }
    }
  }
}
module.exports = Square1;
module.exports = Square;
