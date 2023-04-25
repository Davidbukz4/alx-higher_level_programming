#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const x in films) {
      const filmCharacters = films[x].characters;
      for (const prop in filmCharacters) {
        if (filmCharacters[prop].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
