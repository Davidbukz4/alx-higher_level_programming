#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
myObject.value = 89; // myObject['value'] will also work
console.log(myObject);
