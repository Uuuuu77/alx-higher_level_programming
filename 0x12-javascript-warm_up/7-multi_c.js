#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = parseInt(myVar1, 10);
if (myVar2) {
  for (let x = 0; x < myVar2; x++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
