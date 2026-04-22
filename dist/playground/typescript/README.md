# TypeScript Playground

Create mini projects as subfolders under this folder.

## Create Your Own Mini Project

Example folder:

```text
playground/typescript/my_project/
  package.json
  tsconfig.json
  src/
    main.ts
    calc.ts
  test/
    calc.test.ts
```

Minimal `package.json` scripts:

```json
{
  "name": "my_project",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "tsx src/main.ts",
    "test": "vitest run",
    "test:watch": "vitest",
    "build": "tsc -p tsconfig.json"
  },
  "devDependencies": {
    "tsx": "^4.19.2",
    "typescript": "^5.6.3",
    "vitest": "^2.1.8"
  }
}
```

Run with the playground runner from repository root:

```powershell
go run tools/run_playground.go -l typescript -p my_project
```

If defaults are not enough, add `playground.json` in the mini project folder.

## Testing Guide (Beginner)

Vitest is a good starting point for TypeScript unit testing.

Example `src/calc.ts`:

```ts
export function add(a: number, b: number): number {
  return a + b;
}
```

Example `test/calc.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { add } from "../src/calc";

describe("add", () => {
  it("returns the sum", () => {
    expect(add(2, 3)).toBe(5);
  });
});
```

Run tests:

```powershell
npm install
npm test
```

Testing checklist:

- Keep source in `src/` and tests in `test/` for clarity.
- Test both happy path and invalid inputs.
- Run `npm run build` to catch type errors early.

## Project Layout

```
multi_file/
  package.json                  # npm project definition (scripts, devDependencies)
  tsconfig.json                 # TypeScript compiler settings
  src/
    main.ts                     # entry point
    stats.ts                    # stats module (sum, average, max)
    stats.test.ts               # vitest unit tests
```

## Runner Behavior

- If `package.json` exists: runs `npm install` (first time only), then `npm run start`.
- Otherwise: looks for `src/main.ts`, `main.ts`, `index.ts`, or `app.ts` and runs directly via `tsx` / `ts-node` / `deno`.

Use `playground.json` for custom build or run commands.

## Manual Build Guidance

```powershell
cd playground/typescript/multi_file

# Install dependencies (first time)
npm install

# Run the program
npm start

# Run tests
npm test

# Type-check and compile to dist/
npm run build
```

