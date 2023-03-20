#!/usr/bin/node
// Checks if there were arguments given on command line
const ag = process.argv;
let i = 0;
while (ag[i]) {
  i++;
}
i -= 2;
if (i === 0) {
  console.log('No argument');
} else if (i === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
