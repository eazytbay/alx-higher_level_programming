#!/usr/bin/node
const dict = require('./101-data.js').dict;
const customDict = {};
for (const key in dict) {
  if (customDict[dict[key]] === undefined) {
    customDict[dict[key]] = [key];
  } else {
    customDict[dict[key]].push(key);
  }
}
console.log(customDict);
