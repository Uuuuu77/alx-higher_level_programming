#!/usr/bin/node

const myVar1 = process.argv[2];
const myVar2 = parseInt(myVar1, 10);
if (myVar2) {
  let square = '';
  for (let x = 0; x < myVar2; x++) {
    square += 'X';
  }
  for (let y = 0; y < myVar2; y++) {
    console.log(square);
  }
} else {
  console.log('Missing size');
}
