import * as readline from "readline";
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
rl.question("Enter a number: ", (input) => {
  const n = parseInt(input);
  console.log(n % 2 === 0 ? `${n} is even` : `${n} is odd`);
  rl.close();
});
import * as readline from "readline";

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
rl.question("Enter a number: ", (input) => {
  const n = parseInt(input);
  console.log(n % 2 === 0 ? `${n} is even` : `${n} is odd`);
  rl.close();
});
