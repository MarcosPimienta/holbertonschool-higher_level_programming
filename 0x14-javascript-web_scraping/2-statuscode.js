#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response) {
    if (process.argv[2] === undefined){
        console.error('error:', error);
    }
  console.log('code:', response.statusCode);
});
