# Playground

This folder is a multi-language scratch area for small, multi-file experiments.

Structure:

- cpp/
- go/
- scala/
- python/
- typescript/

Each language folder contains mini projects as subdirectories.

Note: C++ mini projects are CMake-first when a CMakeLists.txt is present.

## Quick Start Guides By Language

Use these language-specific guides to create a new mini project and add beginner-level tests:

- [C++ mini project + testing guide](./cpp/README.md)
- [Go mini project + testing guide](./go/README.md)
- [Python mini project + testing guide](./python/README.md)
- [Scala mini project + testing guide](./scala/README.md)
- [TypeScript mini project + testing guide](./typescript/README.md)

Example:

playground/
  cpp/
    linkage_demo/
      CMakeLists.txt
      main.cpp
      greeter.cpp
      greeter.h

## Runner

Use 	ools/run_playground.go to build and run mini projects.
Use 	ools/test_playground.go to run mini project tests.

Build the runner binary:

`powershell
go build -o tools/run_playground.exe tools/run_playground.go
`

Run projects directly with Go:

`powershell
# List all projects
go run tools/run_playground.go -pl
go run tools/run_playground.go -pl -l cpp

# Run a specific project
go run tools/run_playground.go -l cpp -p linkage_demo
go run tools/run_playground.go -l go -p my_project
go run tools/run_playground.go -l scala -p example_project
go run tools/run_playground.go -l typescript -p example_project

# Run all projects of a language
go run tools/run_playground.go -l python -a
`

Run tests directly with Go:

`powershell
# List all projects with tests
go run tools/test_playground.go -pl
go run tools/test_playground.go -pl -l scala

# Run tests for a specific project
go run tools/test_playground.go -l cpp -p threadpool
go run tools/test_playground.go -l go -p my_project
go run tools/test_playground.go -l scala -p example_project
go run tools/test_playground.go -l typescript -p example_project

# Run all tests for a language
go run tools/test_playground.go -l python -a
`

Supported language values:

- cpp, cpp17, cpp20, c++, c++17, c++20
- go
- scala
- python
- typescript, ts
- all (for list or batch modes)

## Optional project config

You can put a playground.json file inside a mini project when defaults are not enough.

Example:

`json
{
  "workDir": ".",
  "env": {
    "MY_FLAG": "1"
  },
  "build": ["cmake", "-S", ".", "-B", "build"],
  "run": ["cmake", "--build", "build"]
}
`

Rules:

- uild and un are command arrays: first item is executable, rest are args.
- workDir is relative to the mini project folder.
- env adds environment variables for both commands.
- If no playground.json exists, language-specific defaults are used.