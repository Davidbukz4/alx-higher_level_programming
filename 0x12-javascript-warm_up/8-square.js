#!/usr/bin/node
let x;
const arg = Number.parseInt(process.argv[2]);
if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (x = 0; x < arg; x++) {
    console.log('X'.repeat(arg));
  }
}
