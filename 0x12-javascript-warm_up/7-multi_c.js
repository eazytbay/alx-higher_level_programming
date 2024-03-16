#!/usr/bin/node
const digit = parseInt(process.argv[2]);
if (isNaN(digit)) {
  console.log('Missing number of occurrences');
} else {
  let x = 0;
  while (x < digit) {
    console.log('C is fun');
    x++;
  }
}
