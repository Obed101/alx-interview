#!/usr/bin/node
// Takes movie Id as argument and returns
// returns all character's names to the console
// in specific order

const request = require('request');
const movieId = process.argv[2];
const charList = [];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request(url, async function (error, _, body) {
  if (error) return 'Unable to connect';
  body = JSON.parse(body);

  for (const chars of body.characters) {
    const item = new Promise(function (resolve) {
      request(chars, (error, _, res) => {
        if (error) return 'Cannot get Actors name';
        resolve(JSON.parse(res).name);
      });
    });
    charList.push(item);
  }
  const actors = await Promise.all(charList);
  // finally printing the character names
  for (const actor of actors) {
    console.log(actor);
  }
});
