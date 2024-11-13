#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];

request.get(`https://swapi-api.alx-tools.com/api/films/${filmId}`, (err, res, body) => {
  if (err) {
    console.err(err, res.statusCode);
  } else {
    const characters = JSON.parse(body).characters;
    function fetchCharacters (i) {
      if (i < characters.length) {
        request.get(characters[i], (err, res, body) => {
          if (err) {
            console.error(err, res.statusCode);
          } else {
            console.log(JSON.parse(body).name);
            fetchCharacters(i + 1);
          }
        });
      }
    }
    fetchCharacters(0);
  }
});
