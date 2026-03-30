const nums = [1, 2, 3, 4, 5, 6, 7, 8];
const result = nums
  .filter(n => n % 2 === 0)
  .map(n => n * n)
  .reduce((a, b) => a + b, 0);

console.log(`Sum of squares of even numbers: ${result}`);
function processStream(items: number[], processor: (n: number) => number) {
  return items.map(processor);
}

const data = [1, 2, 3, 4, 5];
const doubled = processStream(data, (n) => n * 2);
console.log(doubled);
