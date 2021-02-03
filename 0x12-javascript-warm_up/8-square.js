#!/usr/bin/node

const Num = parseInt(process.argv[2]);
if (!Num) {
  console.log('Missing size');
}
for (let i = 0; i < Num; i++) {
  console.log('X'.repeat(Num));
}
