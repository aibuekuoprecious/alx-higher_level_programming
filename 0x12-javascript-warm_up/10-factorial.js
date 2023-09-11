#!/usr/bin/node

const arg = parseInt(process.argv[2]);
function factorial (i) {
  if (i < 0) {
    return (-1);
  } else if (i === 0 || isNaN(i)) {
    return (1);
  } else {
    return (i * factorial(i - 1));
  }
}

console.log(factorial(arg));
