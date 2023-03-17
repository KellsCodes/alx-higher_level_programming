#!/usr/bin/node
const _arg = process.argv.slice(2);
if (isNaN(Number(_arg[0]))) {
	console.log('Missing number of occurrences');
} else {
	let i = 0;
	while (i < Number(_arg[0])) {
		console.log('C is fun');
		i++;
	}
}
