#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const prse = JSON.parse(body);
    let n = 0;
    const res = prse.results;
    for (let i = 0; i < res.length; i++) {
      // console.log(prse.results[i].characters[15]);
      for (const j of res[i].characters) {
        if (j.includes('18')) {
          n += 1;
        }
      }
    }
    console.log(n);
  }
});
