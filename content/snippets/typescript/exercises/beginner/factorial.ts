function factorial(n: number): number {
  let r = 1;
  for (let i = 2; i <= n; i++) r *= i;
  return r;
}

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
const n = input.length ? Number(input[0]) : 5;
console.log(factorial(n));
