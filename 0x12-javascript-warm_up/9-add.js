#!/usr/bin/node
const arg = process.argv;
const arg1 = Number.parseInt(arg[2]);
const arg2 = Number.parseInt(arg[3]);

function add (a, b) {
  return (a + b);
}
console.log(add(arg1, arg2));
