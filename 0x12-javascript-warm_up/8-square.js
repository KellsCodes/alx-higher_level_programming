#!/usr/bin/node
const _args = process.argv.slice(2);
if (isNaN(Number(_args[0]))) {
	console.log('Missing size');
} else {
	let i = 0, j = 0;
	while (i < Number(_args[0])) {
		let chars = '';
		while (j < Number(_args[0])) {
			chars += 'x';
			j++;
		}
		console.log(chars);
		j = 0;
		i++;
	}
}
