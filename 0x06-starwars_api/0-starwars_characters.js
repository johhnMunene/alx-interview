#!/usr/bin/node
const request = require('request');
const API_URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

// a function to return a list of promises for each character fetched from the api
function getCharacterNames (characters) {
  const names = characters.map((character) => {
    return new Promise((resolve, reject) => {
      request(character, (error, _, body) => {
        if (error) reject(Error('something went wrong'));
        else resolve(JSON.parse(body).name);
      });
    });
  });
  return names;
}

request(API_URL, (error, _, body) => {
  if (error) console.log(`error: ${error}`);
  else {
    const targetFilm = JSON.parse(body);
    const namesPromises = getCharacterNames(targetFilm.characters);
    Promise.all(namesPromises).then((result) => {
      result.forEach((element) => {
        console.log(element);
      });
    });
  }
});
