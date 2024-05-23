#!/usr/bin/node
const request = require('request');
const API_URL = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

// Function to return a list of promises for each character fetched from the API
function getCharacterNames(characters) {
  return characters.map(character => {
    return new Promise((resolve, reject) => {
      request(character, (error, _, body) => {
        if (error) {
          reject(`Error fetching character: ${error}`);
        } else {
          resolve(JSON.parse(body).name);
        }
      });
    });
  });
}

request(API_URL, (error, _, body) => {
  if (error) {
    console.error(`Error fetching film details: ${error}`);
  } else {
    const targetFilm = JSON.parse(body);
    const namesPromises = getCharacterNames(targetFilm.characters);
    Promise.all(namesPromises)
      .then(names => {
        names.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.error(error);
      });
  }
});

