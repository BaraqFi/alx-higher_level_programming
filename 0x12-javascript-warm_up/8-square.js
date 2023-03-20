#!/usr/bin/node
// prints a square

const ag = process.argv;
const n = Number(ag[2]);
if (isNaN(n)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n; j++) {
      process.stdout.write('X');
    }
    console.log('');
  }
}
