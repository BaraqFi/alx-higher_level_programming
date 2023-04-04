#!/usr/bin/node
// Every haracter in a movie
const request = require('request');
const ag = process.argv;

request('https://swapi-api.alx-tools.com/api/films/' + ag[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const person = JSON.parse(body).characters;
  person.forEach((character) => {
    request(character, (error, response, body) => {
      if (!error) {
        const being = JSON.parse(body).name;
        console.log(being);
      }
    });
  });
});
