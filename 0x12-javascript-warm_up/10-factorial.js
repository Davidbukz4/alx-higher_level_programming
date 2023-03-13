#!/usr/bin/node
const arg = Number.parseInt(process.argv[2]);

function recursion (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (num * recursion(num - 1));
}

const res = recursion(arg);
console.log(res);
