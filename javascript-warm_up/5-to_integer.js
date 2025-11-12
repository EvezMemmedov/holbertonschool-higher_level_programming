#!/usr/bin/node
const argv = process.argv[2];
const number = parsenInt(argv);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
