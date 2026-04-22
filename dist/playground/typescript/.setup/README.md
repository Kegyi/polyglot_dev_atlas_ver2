# TypeScript Playground Setup Guide

This folder is a reference hub — not a runnable project itself.
Copy `example_project/` to start a new mini project, then follow the tiers below to grow it.

---

## Folder layout

```text
.setup/
    README.md                   ← you are here
    example_project/            ← copy this to start a new project
        package.json
        tsconfig.json
        src/
            main.ts
            greeting.ts
        test/
            greeting.test.ts
```

---

## Tier 1 — Single-file scratch pad

Good for quick experiments that fit in one file. No dependencies needed initially.

```text
playground/typescript/my_scratch/
    main.ts
```

Minimal `main.ts`:

```ts
function greet(name: string): string {
  return `Hello, ${name}`;
}

console.log(greet("world"));
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
npx tsx main.ts
```

Manual test (inside the project folder):

```powershell
# Add a test file (main.test.ts), then install vitest and run:
npm install --save-dev vitest
npx vitest run
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l typescript -p my_scratch
go run tools/test_playground.go -l typescript -p my_scratch
```

Note: tool-based testing requires a `package.json` with vitest configured.

When to move up: when the file exceeds ~100 lines, or you want to reuse logic across files.

---

## Tier 2 — Simple npm project with basic testing

Add `package.json` and `tsconfig.json` to enable TypeScript compilation and testing.

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

Minimal `package.json`:

```json
{
  "name": "my_project",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "tsx src/main.ts",
    "build": "tsc",
    "test": "vitest run"
  },
  "devDependencies": {
    "typescript": "^5.6.3",
    "tsx": "^4.19.2",
    "vitest": "^2.1.8"
  }
}
```

Minimal `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "test"]
}
```

Example `src/calc.ts`:

```ts
export function add(a: number, b: number): number {
  return a + b;
}
```

Example `test/calc.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { add } from "../src/calc.js";

describe("add", () => {
  it("returns the sum", () => {
    expect(add(2, 3)).toBe(5);
  });
});
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
npm install
npm start
npm run build
```

Manual test (inside the project folder):

```powershell
npm test
npm test -- --reporter=verbose
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l typescript -p my_project
go run tools/test_playground.go -l typescript -p my_project
```

Note: `vitest run` runs all `*.test.ts` files automatically; `npm test` is a convenient alias.

When to move up: when you need stricter type checking or want to organize code into modules.

---

## Tier 3 — Multi-file project with strict TypeScript (recommended)

Use the `src/` + `test/` layout with strict TypeScript compiler options.
This is the pattern used by `example_project/` and `multi_file/`.

```text
playground/typescript/my_project/
    package.json
    tsconfig.json
    src/
        main.ts
        greeting.ts
    test/
        greeting.test.ts
```

`package.json`:

```json
{
  "name": "my_project",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "start": "tsx src/main.ts",
    "build": "tsc",
    "test": "vitest run",
    "test:watch": "vitest"
  },
  "devDependencies": {
    "typescript": "^5.6.3",
    "tsx": "^4.19.2",
    "vitest": "^2.1.8"
  }
}
```

`tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Bundler",
    "outDir": "dist",
    "rootDir": "src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "lib": ["ES2022"]
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "test"]
}
```

Example `src/greeting.ts`:

```ts
export function greet(name: string): string {
  if (name === "") {
    return "Hello";
  }
  return `Hello, ${name}`;
}
```

Example `test/greeting.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { greet } from "../src/greeting.js";

describe("greet", () => {
  it("returns greeting with name", () => {
    expect(greet("Alice")).toBe("Hello, Alice");
  });

  it("returns plain hello for empty string", () => {
    expect(greet("")).toBe("Hello");
  });
});
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
npm install
npm start
npm run build
```

Manual test (inside the project folder):

```powershell
npm test
npm test -- --reporter=verbose
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l typescript -p my_project
go run tools/test_playground.go -l typescript -p my_project
```

Note: strict TypeScript (`"strict": true`) catches type errors at compile time, avoiding failures at runtime.

When to move up: when you want advanced test patterns or parameterized test scenarios.

---

## Tier 4 — Better test quality with advanced patterns

Use parameterized tests (`test.each`) and test fixtures for comprehensive coverage.

Example `test/greeting.test.ts`:

```ts
import { describe, expect, it } from "vitest";
import { greet } from "../src/greeting.js";

describe("greet", () => {
  it.each([
    ["Alice", "Hello, Alice"],
    ["", "Hello"],
    ["world", "Hello, world"],
    ["Bob Smith", "Hello, Bob Smith"],
  ])('greet("%s") returns "%s"', (input, expected) => {
    expect(greet(input)).toBe(expected);
  });
});
```

Or using descriptive test data with `describe.each`:

```ts
import { describe, expect, it } from "vitest";
import { greet } from "../src/greeting.js";

const testCases = [
  { input: "Alice", expected: "Hello, Alice", description: "with name" },
  { input: "", expected: "Hello", description: "empty string" },
  { input: "world", expected: "Hello, world", description: "with world" },
];

describe("greet", () => {
  testCases.forEach(({ input, expected, description }) => {
    it(`returns greeting ${description}`, () => {
      expect(greet(input)).toBe(expected);
    });
  });
});
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
npm install
npm start
npm run build
```

Manual test (inside the project folder):

```powershell
npm test
npm test -- --reporter=verbose
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l typescript -p my_project
go run tools/test_playground.go -l typescript -p my_project
```

Note: Vitest's `it.each()` and `describe.each()` reduce test duplication and improve readability for parameterized tests.

When to move up: when you need custom build commands or environment-specific configurations.

---

## Tier 5 — Custom playground.json configuration

Override default build/run/test commands with a `playground.json` file in your project folder.

Example `playground.json`:

```json
{
  "build": ["npm", "run", "build"],
  "run": ["npm", "start"],
  "test": ["npm", "test", "--", "--reporter=verbose"],
  "workDir": ".",
  "env": {}
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
npm install
npm run build
npm start
npm test
```

Tool run/test (from repository root):

Uses the commands specified in `playground.json`:

```powershell
go run tools/run_playground.go -l typescript -p my_project
go run tools/test_playground.go -l typescript -p my_project
```

Note: `playground.json` is optional. Use it to customize build settings, environment variables, or test reporters.

When to move up: your project is mature enough to warrant custom build logic or distributed testing.

---

## Testing Checklist

- ✓ Use clear test names that describe behavior (`returns greeting with name`).
- ✓ Keep pure logic in small functions to simplify testing.
- ✓ Add edge-case tests (empty strings, boundary values, special characters).
- ✓ Use `expect()` assertions with `.toBe()`, `.toEqual()`, `.toContain()` matchers.
- ✓ Consider `it.each()` for parameterized tests to reduce duplication.
- ✓ Run tests frequently with `npm test` or the tool runner.
- ✓ Run `npm run build` to catch type errors before deployment.

---

## Quick-start Checklist

- [ ] Copy `example_project/` to `playground/typescript/my_first_try/`
- [ ] Run: `go run tools/run_playground.go -l typescript -p my_first_try` (from repo root)
- [ ] Test: `go run tools/test_playground.go -l typescript -p my_first_try` (from repo root)
- [ ] Modify `src/greeting.ts` with your logic
- [ ] Add new test cases to `test/greeting.test.ts`
- [ ] Run `npm run build` to check for type errors
- [ ] Re-run tests to validate changes
