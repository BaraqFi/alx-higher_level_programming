#!/usr/bin/node
// Stroes a webpage contents in a file

const request = require('request');
const fs = require('fs');
const ag = process.argv;

request(ag[2]).pipe(fs.createWriteStream(ag[3]));
