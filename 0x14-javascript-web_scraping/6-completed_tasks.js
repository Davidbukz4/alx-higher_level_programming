#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const userTask = {};
    for (const x in data) {
      const todo = data[x];
      if (todo.completed === true) {
        if (userTask[todo.userId] === undefined) {
          userTask[todo.userId] = 1;
        } else {
          userTask[todo.userId]++;
        }
      }
    }
    console.log(userTask);
  }
});
