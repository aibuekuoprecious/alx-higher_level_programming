#!/usr/bin/node
const x = parseInt(process.argv[2])
const notAnInt = isNaN(x);
if (notAnInt || x <= 0) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < x) {
    console.log('C is fun');
    i++;
  }
}