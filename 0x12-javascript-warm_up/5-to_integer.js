#!/usr/bin/node
// Convertes the first argument into a number
const ag = process.argv;
const i = ag[2];
if (isNaN(i)) {
  console.log('Not a number');
} else {
  console.log('My number:', Number(i));
}
