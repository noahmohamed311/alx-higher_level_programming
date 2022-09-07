#!/usr/bin/node
const Rectangle = require('./4-rectangle');

/**
 * represents a square class
 */
class Square extends Rectangle {
  /**
  * instantiates objects
  * @param {Number} size of the width and height
  */
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
