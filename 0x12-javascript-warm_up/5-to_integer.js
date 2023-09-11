#!/usr/bin/node

const firstArg = parseInt(process.argv[2])
const notAnInt = isNaN(firstArg);
if (notAnInt) {
  console.log('Not a number');
} else {
  console.log('My number:', firstArg );
}
