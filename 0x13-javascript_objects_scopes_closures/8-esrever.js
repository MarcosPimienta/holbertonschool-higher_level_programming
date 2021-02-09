#!/usr/bin/node

exports.esrever = function (list) {
  const l = [];
  let i = list.length - 1;
  for (i; i >= 0; i--) {
    l.push(list[i]);
  }
  return (l);
};
