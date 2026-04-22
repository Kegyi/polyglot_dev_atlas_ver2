# Go Playground

Create mini projects as subfolders under this folder.

## Create Your Own Mini Project

Example folder:

```text
playground/go/my_project/
  go.mod
  main.go
  internal/
    calc/
      calc.go
      calc_test.go
```

Create and initialize from the mini project folder:

```powershell
go mod init example.com/my_project
```

Minimal `main.go`:

```go
package main

import "fmt"

func main() {
    fmt.Println("hello from my_project")
}
```

Run with the playground runner from repository root:

```powershell
go run tools/run_playground.go -l go -p my_project
```

Run tests with the playground test runner from repository root:

```powershell
go run tools/test_playground.go -l go -p my_project
```

Or run tests with Go's testing tool:

```powershell
go test ./...
go test -v ./...
```

Note: `run_playground` runs the project command; it does not execute tests automatically.

If defaults are not enough, add `playground.json` in the mini project folder.

## Testing Guide (Beginner)

Go testing is built in. Create files ending with `_test.go` and write `TestXxx` functions.

Example `internal/calc/calc.go`:

```go
package calc

func Add(a, b int) int { return a + b }
```

Example `internal/calc/calc_test.go`:

```go
package calc

import "testing"

func TestAdd(t *testing.T) {
    got := Add(2, 3)
    want := 5
    if got != want {
        t.Fatalf("Add(2, 3) = %d, want %d", got, want)
    }
}
```

Run tests:

```powershell
go run tools/test_playground.go -l go -p my_project
go test ./...
go test -v ./...
```

Testing checklist:

- Use table-driven tests when you have many input/output cases.
- Keep tests in the same package as the code at first.
- Add one test per bug fix to prevent regressions.

## Project Layout

```
multi_file/
  go.mod                          # module definition (required for real projects)
  main.go                         # package main — entry point
  internal/
    stats/
      stats.go                    # stats package (Sum, Average, Max)
      stats_test.go               # unit tests
```

## Runner Behavior

- If `go.mod` exists: runs `go run .` from the project directory.
- Otherwise: falls back to compiling all non-test `.go` files directly.

## Test Runner Behavior

- `tools/test_playground.go` runs project tests using language defaults.
- For Go projects, it runs `go test ./...` from the project directory.

Use `playground.json` for custom build or run commands.

## Manual Build Guidance

```powershell
cd playground/go/multi_file

# Run the program
go run .

# Build a binary
go build -o multi_file.exe .

# Run all tests
go test ./...

# Run tests with verbose output
go test -v ./...
```

