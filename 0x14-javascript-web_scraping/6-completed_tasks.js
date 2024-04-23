#!/usr/bin/node
const request = require('request');
request(process.argv[2], (error, resp, body) => {
  if (!error) {
    const pends = JSON.parse(body);
    const completedTask = {};
    pends.forEach((pend) => {
      if (pend.completed && completedTask[pend.userId] === undefined) {
        completedTask[pend.userId] = 1;
      } else if (pend.completed) {
        completedTask[pend.userId] += 1;
      }
    });
    console.log(completedTask);
  }
}
);
