#!/usr/bin/node
// a function that returns the reversed version of a list

exports.esrever = function (list) {
  const newList = [];
  let i;
  for (i = 0; i < list.length; i++) {
    newList[i] = list[list.length - i - 1];
  }
  return (newList);
};
