#!/usr/bin/node
// Reads and prints from a file

const fs = require('fs');
const ag = process.argv;
fs.readFile(ag[2], 'utf8', (err, data) => {
  if (err) {
    console.error(err);
  }
  console.log(data);
});
