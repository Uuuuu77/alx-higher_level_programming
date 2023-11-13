#!/usr/bin/node

exports.callMeMoby = function (y, theFunction) {
  for (let x = 0; x < y; x++) {
    theFunction();
  }
};
