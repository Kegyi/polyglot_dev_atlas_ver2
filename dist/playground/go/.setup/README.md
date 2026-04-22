# Go Playground Setup Guide

This folder is a reference hub — not a runnable project itself.
Copy `example_project/` to start a new mini project, then follow the tiers below to grow it.

---

## Folder layout

```text
.setup/
    README.md                   ← you are here
    example_project/            ← copy this to start a new project
        go.mod
        main.go
        internal/
            greeter/
                greeter.go
                greeter_test.go
```

---

## Tier 1 — Single-file scratch pad

Good for quick experiments that fit in one file. No `go.mod` needed for the simplest cases,
but the runner works better with one.

```text
playground/go/my_scratch/
    main.go
```

Minimal `main.go`:

```go
package main

import "fmt"

func main() {
    fmt.Println("hello")
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
go run main.go
go build -o my_scratch.exe main.go
```

Manual test (inside the project folder):

```powershell
# Add a *_test.go file first, then:
go test .
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l go -p my_scratch
go run tools/test_playground.go -l go -p my_scratch
```

Note: tool-based testing requires `*_test.go` files to exist.

When to move up: when you want to split logic into packages, or add tests.

---

## Tier 2 — Module with a single package and tests

Add `go.mod` and keep everything in one package. Tests live next to the code.

```text
playground/go/my_project/
    go.mod
    main.go
    calc.go
    calc_test.go
```

Initialize the module:

```powershell
cd playground/go/my_project
go mod init example.com/my_project
```

Example `calc.go`:

```go
package main

func add(a, b int) int { return a + b }
```

Example `calc_test.go`:

```go
package main

import "testing"

func TestAdd(t *testing.T) {
    if got := add(2, 3); got != 5 {
        t.Fatalf("add(2, 3) = %d, want 5", got)
    }
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
go run .
go build -o my_project.exe .
```

Manual test (inside the project folder):

```powershell
go test ./...
go test -v ./...
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l go -p my_project
go run tools/test_playground.go -l go -p my_project
```

Note: `run_playground` executes the project run command; it does not run tests automatically.

When to move up: when you want to reuse packages across projects or hide internal implementation details.

---

## Tier 3 — Module with internal packages (recommended)

This is the pattern used by `example_project/` and `multi_file/`.
Put reusable logic inside `internal/<pkg>/` — the `internal` path restriction prevents
accidental imports from outside the module.

```text
playground/go/my_project/
    go.mod
    main.go
    internal/
        greeter/
            greeter.go
            greeter_test.go
```

`go.mod`:

```
module playground/my_project

go 1.21
```

`internal/greeter/greeter.go`:

```go
package greeter

import "fmt"

func Greet(name string) string {
    return fmt.Sprintf("Hello, %s!", name)
}
```

`internal/greeter/greeter_test.go` (external test package — tests the public API):

```go
package greeter_test

import (
    "strings"
    "testing"
    "playground/my_project/internal/greeter"
)

func TestGreet_ContainsName(t *testing.T) {
    got := greeter.Greet("Alice")
    if !strings.Contains(got, "Alice") {
        t.Errorf("got %q, want it to contain the name", got)
    }
}
```

`main.go`:

```go
package main

import (
    "fmt"
    "playground/my_project/internal/greeter"
)

func main() {
    fmt.Println(greeter.Greet("world"))
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
go run .
go build -o my_project.exe .
```

Manual test (inside the project folder):

```powershell
go test ./...
go test -v ./...
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l go -p my_project
go run tools/test_playground.go -l go -p my_project
```

---

## Tier 4 — Table-driven tests

When a function has many input/output cases, use a table-driven test to avoid repetition.

```go
package greeter_test

import (
    "strings"
    "testing"
    "playground/my_project/internal/greeter"
)

func TestGreet(t *testing.T) {
    tests := []struct {
        name  string
        input string
        check func(string) bool
    }{
        {"contains name", "Alice", func(s string) bool { return strings.Contains(s, "Alice") }},
        {"starts with Hello", "world", func(s string) bool { return strings.HasPrefix(s, "Hello") }},
        {"empty name non-empty result", "", func(s string) bool { return s != "" }},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            got := greeter.Greet(tt.input)
            if !tt.check(got) {
                t.Errorf("Greet(%q) = %q, check failed", tt.input, got)
            }
        })
    }
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
go run .
go build -o my_project.exe .
```

Manual test (inside the project folder):

```powershell
go test ./...
go test -v ./...
go test -v -run TestGreet/contains_name ./internal/greeter/
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l go -p my_project
go run tools/test_playground.go -l go -p my_project
```

---

## Tier 5 — Advanced: `playground.json` for custom run commands

When the default `go run .` is not enough (different entry point, environment variables,
build tags, etc.), add `playground.json` in the mini project folder.

Example `playground.json`:

```json
{
    "run": ["go", "run", "./cmd/server"],
    "test": ["go", "test", "./...", "-v"]
}
```

See `tools/run_playground.go` and `tools/test_playground.go` for the full list of supported keys.

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
go run ./cmd/server
go build -o server.exe ./cmd/server
```

Manual test (inside the project folder):

```powershell
go test ./...
go test -v ./...
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l go -p my_project
go run tools/test_playground.go -l go -p my_project
```

Note: at this tier, `playground.json` can override both run and test commands.

---

## Quick-start checklist

1. Copy `.setup/example_project/` to `playground/go/<your_name>/`.
2. Update the module name in `go.mod`: `module playground/<your_name>`.
3. Rename the `internal/greeter/` package and update the import path in `main.go`.
4. Replace `greeter.go` with your own logic.
5. Add tests next to the code in `*_test.go` files.
6. Run: `go run tools/run_playground.go -l go -p <your_name>`
7. Test: `go run tools/test_playground.go -l go -p <your_name>`

---

## Testing checklist

- Name tests `TestFunctionName_Scenario` (e.g. `TestGreet_EmptyName`).
- Use `t.Errorf` to report failures without stopping; use `t.Fatalf` only when continuing is meaningless.
- Use `t.Run` and a table for multiple input cases.
- Cover the happy path, at least one boundary (nil/empty slice, zero, max), and one error case.
- Keep tests deterministic — no goroutine timing, no real network calls.
- Use external test packages (`package foo_test`) to test only the public API.
