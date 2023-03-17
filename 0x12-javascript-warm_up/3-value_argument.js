#!/usr/bin/node
const _arg = process.argv.slice(2);
if (!_arg[0]) {
  console.log('No argument');
} else {
  console.log(_arg[0]);
}
