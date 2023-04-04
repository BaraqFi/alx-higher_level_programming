#!/usr/bin/node
// Writes to a file from the command line

const fs = require('fs');
const ag = process.argv;
fs.writeFile(ag[2], ag[3], (err) => {
  if (err) {
    console.error(err);
  }
});
