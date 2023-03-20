#!/usr/bin/node
// prints the addition of 2 integers

function add (a, b) {
  return a + b;
}

const ag = process.argv;
const i = Number(ag[2]);
const k = Number(ag[3]);

console.log(add(i, k));
