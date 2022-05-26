#!/usr/bin/node
const request = require('request');
movie_id = process.argv[2];

const char_list = [];
const url = `https://swapi-api.hbtn.io/api/films/${movie_id}`;
request(url, (error, response, body) => {
  if (error) return console.log('Cannot connect');
  if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (chars of body.characters) {
      item = function () {
        request(chars, (error, _, res) => {
          if (error) return console.log('Cannot get actors name');
          actor =  JSON.parse(res).name;
          console.log(actor)
        });
      };
      char_list.push(item());
    }
  }
});
