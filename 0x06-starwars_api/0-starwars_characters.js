#!/usr/bin/env node
const request = require('request');
movie_id = process.argv[2];

const char_list = [];
const url = `https://swapi-api.hbtn.io/api/films/${movie_id}`;
request(url, (error, response, body) => {
  if (error) return console.log('Cannot connect'); // In case it is unreachable
  if (response.statusCode === 200) {
    body = JSON.parse(body);
    for (chars of body.characters) {
      item = function () {
        request(chars, (error, _, res) => {
          if (error) return console.log('error fetching name');
          cha =  JSON.parse(res).name;
          console.log(cha)
        });
      };
      char_list.push(item());
    }
    // for (char of char_list) {
    //   console.log(char)
    // }
  }
});
