#!/usr/bin/node
//  prints x times “C is fun”

const ag = process.argv;
let i = 0;
while (ag[i]) {
  i++;
}

const o = Number(ag[2]);

if (i >= 3) {
  for (let k = 0; k < o; k++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
