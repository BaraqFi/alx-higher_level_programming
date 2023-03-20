#!/usr/bin/node
// Prints only the first argument
const ag = process.argv;
let i = 0;
while (ag[i]) {
  i++;
}
if (i >= 3) {
  const tx = ag[2];
  console.log(tx);
} else {
  console.log('No argument');
}
