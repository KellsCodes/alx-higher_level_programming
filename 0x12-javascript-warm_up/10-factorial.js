#!/usr/bin/node
const _args = process.argv.slice(2);
function factorial (num) {
  if (!num || num <= 0) return 1;
  return factorial(num - 1) * num;
}

console.log(factorial(_args[0]));
