#!/usr/bin/node
// prints the factorial

function factorialize (n) {
  return n === 0 || isNaN(n) ? 1 : n * factorialize(n - 1);
}
const ag = process.argv;
const i = Number(ag[2]);
console.log(factorialize(i));
