#!/usr/bin/node

const myVar = process.argv.length;
if (myVar < 4) {
  console.log(0);
} else {
  let array = [];
  for (let x = 2; x < process.argv.length; x++) {
    array.push(parseInt(process.argv[x]));
    array = array.sort(function (a, b) {
      return a - b;
    });
  }
  console.log(array[array.length - 2]);
}
