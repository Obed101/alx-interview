#!/usr/bin/node
const request = require('request');
movie_id = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${movie_id}`;
request(url, (error, response, body) => {
  if (error) return    // In case the url is unreachable
  if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (chars of body.characters) {
      request(chars, (error, response, body) => {
        if (error) return
        if (response.statusCode === 200) {
          body = JSON.parse(body);
          console.log(body.name);
        }
      });
    }
  }
});
