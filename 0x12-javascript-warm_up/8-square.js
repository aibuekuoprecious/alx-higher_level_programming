#!/usr/bin/node
const size = parseInt(process.argv[2]);
const notAnInt = isNaN(size);
if (notAnInt || size <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
