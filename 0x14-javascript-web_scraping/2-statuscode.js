#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, resp) => {
  if (error) {
    console.log(error);
  } else {
    console.log('code: ' + resp.statusCode);
  }
}
);
