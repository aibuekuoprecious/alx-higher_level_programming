#!/usr/bin/node

const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);

function add(a, b) {
  if (isNaN(a) || isNaN(b)) {
    console.log('NaN');
  } else {
    const c = a + b;
    console.log(c);
  }
}

add(a, b);