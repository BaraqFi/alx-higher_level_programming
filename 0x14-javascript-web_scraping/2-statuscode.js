#!/usr/bin/node
// Dis[lays the status code

const request = require('request');
const ag = process.argv;

request.get(ag[2]).on('response', (response) => {
  console.log('code: ' + response.statusCode);
});
