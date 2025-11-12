#!/usr/bin/node
const x = process.argv[2];
if (parseInt(x)) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < x.length; i++) {
  console.log(x);
}
