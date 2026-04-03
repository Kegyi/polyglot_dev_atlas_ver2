const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
let idx = 0;
let n = input.length ? Number(input[idx++]) : 5;
const arr = [];
for (let i = 0; i < n; i++) arr.push(input.length > idx ? Number(input[idx++]) : i+1);
console.log(Math.max(...arr));
