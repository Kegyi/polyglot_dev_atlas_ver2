function sumN(n: number): number {
  return (n * (n + 1)) / 2;
}

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
const n = input.length ? Number(input[0]) : 10;
console.log(sumN(n));
