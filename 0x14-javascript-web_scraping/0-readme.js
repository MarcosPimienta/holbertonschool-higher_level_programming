#!/usr/bin/node

const rd = require('fs');

rd.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(data);
});
