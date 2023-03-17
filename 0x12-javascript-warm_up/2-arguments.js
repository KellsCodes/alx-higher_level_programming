#!/usr/bin/node
const _args = process.argv.slice(2);
if (!_args.length)
{
	console.log('No argument');
}
else if (_args.length === 1)
{
	console.log('Argument found');
}
else
{
	console.log('Arguments found');
}

