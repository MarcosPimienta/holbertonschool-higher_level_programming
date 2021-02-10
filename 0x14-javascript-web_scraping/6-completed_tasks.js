#!/usr/bin/node

const request = require('request');
const args = process.argv;
const dic = {};

request(args[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const bodyJson = JSON.parse(body);
    for (const i of bodyJson) {
      if (i.completed) {
        if (dic[i.userId]) {
          dic[i.userId] += 1;
        } else {
          dic[i.userId] = 1;
        }
      }
    }
  }
  console.log(dic);
});
