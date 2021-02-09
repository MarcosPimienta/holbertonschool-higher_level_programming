#!/usr/bin/node

const rd = require('fs');

rd.readFile(process.argv[2], 'utf-8', function (err, data) {
  if (data === undefined) {
    console.log(err);
  }
  console.log(data);
});
