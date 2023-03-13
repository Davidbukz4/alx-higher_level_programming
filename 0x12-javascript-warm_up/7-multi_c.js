#!/usr/bin/node
let x;
const text = 'C is fun';
const argNum = Number(process.argv[2]);
if (isNaN(argNum)) {
  console.log('Missing number of occurrences');
} else {
  for (x = 0; x < Number.parseInt(argNum); x++) {
    console.log(text);
  }
}
