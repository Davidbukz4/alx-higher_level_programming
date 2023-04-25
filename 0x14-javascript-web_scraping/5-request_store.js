#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const filename = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, 'utf-8', () => {});
  }
});
