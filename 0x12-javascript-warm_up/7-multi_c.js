#!/usr/bin/node

const lim = parseInt(process.argv[2]);
if (!lim) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < lim; i++) {
  console.log('C is fun');
}
