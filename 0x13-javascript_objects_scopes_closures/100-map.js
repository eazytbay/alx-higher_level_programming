#!/usr/bin/node
// script that imports an array and computes a new array

const array = require('./100-data').list;

console.log(array);
let dis = 0;
const customList = array.map(function (x) {
  return (x * dis++);
});
console.log(customList);
