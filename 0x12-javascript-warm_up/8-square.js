#!/usr/bin/node
const digit = parseInt(process.argv[2]);
if (isNaN(digit)) {
  console.log('Missing size');
} else {
  let x = 0;
  while (x < digit) {
    let square = '';
    for (let y = 0; y < digit; y++) {
      square += 'X';
    }
    console.log(square);
    x++;
  }
}
