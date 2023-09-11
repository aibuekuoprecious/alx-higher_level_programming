#!/usr/bin/node
if (process.argv.length <= 2) {
  console.log('0');
} else {
  const args = process.argv.slice(2).map(Number);
  const sortedArgs = args.sort();
  const secondLargest = sortedArgs[1]
  console.log(secondLargest)
}
