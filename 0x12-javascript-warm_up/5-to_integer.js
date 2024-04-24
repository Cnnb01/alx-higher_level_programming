#!/usr/bin/node

const process = require('process');
const argus = process.argv;
const val = parseInt(argus[2]);
if (!isNaN(val)) {
  console.log('My nummber: ' + val);
} else {
  console.log('Not a number');
}
