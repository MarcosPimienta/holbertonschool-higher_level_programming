#!/usr/bin/node

const fs = require('fs');
const path = process.argv[2];
const file = process.argv[3];

const request = require('request')
request(path, function (
  error,
  response,
  body
) {
    fs.writeFile(file, body, 'utf-8', (err) => {
        if (err) { console.log(err); }
      });
    console.log(body)
});

