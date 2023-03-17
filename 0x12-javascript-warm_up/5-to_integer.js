#!/usr/bin/node
const _args = process.argv.slice(2);
if (!isNaN(Number(_args[0]))) {
  console.log(`My number: ${Number(_args[0])}`);
} else {
  console.log('Not a number');
}
