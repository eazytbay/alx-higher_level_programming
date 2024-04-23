#!/usr/bin/node

const fs = require('fs');
const file = process.argv[2];
const strng = process.argv[3];

fs.writeFile(file, strng, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
}
);
