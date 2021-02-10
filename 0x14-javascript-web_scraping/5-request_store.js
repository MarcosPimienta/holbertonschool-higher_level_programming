#!/usr/bin/node

const request = require('request');
const args = process.argv;
const emptydic = {};

request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const bodyJson = JSON.parse(body);
    for (const i of bodyJson) {
      if (i.completed) {
        if (emptydic[i.userId]) {
          emptydic[i.userId] += 1;
        } else {
          emptydic[i.userId] = 1;
        }
      }
    }
  }
  console.log(emptydic);
});
