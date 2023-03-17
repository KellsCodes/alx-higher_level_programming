#!/usr/bin/node
const _args = process.argv.slice(2);
if (!_args.length || _args.length === 1) {
	console.log(0);
} else {
	const sortArr = _args.sort((a,b) => b - a);
	console.log(sortArr[1]);
}
