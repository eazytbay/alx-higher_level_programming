#!/usr/bin/node
const arr = process.argv.slice(2);
if (arr.length > 2) {
  const secBiggest = arr.sort(function (a, b) { return a - b; })[arr.length - 2];
  console.log(secBiggest);
} else {
  console.log(0);
}
