#!/usr/bin/node
// A script that concatenates 2 files

const fs = require('fs');

const data1 = fs.readFileSync(process.argv[2], { encoding: 'utf8', flag: 'r' });
const data2 = fs.readFileSync(process.argv[3], { encoding: 'utf8', flag: 'r' });
const res = data1 + data2;
fs.writeFileSync(process.argv[4], res);
