#!/usr/bin/node
// Takes movie Id as argument and returns 
// returns all character's names to the console
// in specific order

const request = require('request');
const movie_id = process.argv[2];
const char_list = [];
const url = `https://swapi-api.hbtn.io/api/films/${movie_id}`;

request(url, async function(error, _, body) {
  if (error) return `Unable to connect`;
  body = JSON.parse(body);

  for (chars of body.characters) {

    item = new Promise(function (resolve) {
      request(chars, (error, _, res) => {
        if (error) return `Cannot get Actor's name`;
        resolve(JSON.parse(res).name);
      });
    });
    char_list.push(item);
  }
  const actors = await Promise.all(char_list);
  // finally printing the character names
  for (const actor of actors) {
    console.log(actor);
  }
});
