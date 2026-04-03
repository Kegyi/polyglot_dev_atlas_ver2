function isPrime(n: number): boolean {
  if (n < 2) return false;
  if (n % 2 === 0) return n === 2;
  for (let i = 3; i * i <= n; i += 2) if (n % i === 0) return false;
  return true;
}

const fs = require('fs');
const input = fs.readFileSync(0, 'utf8').trim().split(/\s+/);
const n = input.length ? Number(input[0]) : 97;
console.log(isPrime(n));
