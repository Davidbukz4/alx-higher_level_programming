#!/usr/bin/node
// a script that imports a dictionary of occurrences by user id and
// computes a dictionary of user ids by occurrence

const dict = require('./101-data').dict;
// get the unique values from the dict object values
const arr = Array.from(new Set(Object.values(dict)));

const res = {};
let i;
for (i = 0; i < arr.length; i++) {
  res[arr[i]] = [];
}
for (const newKey of Object.keys(res)) {
  for (const oldKey of Object.keys(dict)) {
    if (parseInt(newKey) === dict[oldKey]) {
      res[newKey].push(oldKey);
    }
  }
}
console.log(res);
