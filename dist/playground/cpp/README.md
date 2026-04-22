# C++ Playground

Create mini projects as subfolders under this folder.

## Create Your Own Mini Project

Example folder:

```text
playground/cpp/my_project/
	CMakeLists.txt
	src/
		main.cpp
		math_utils.cpp
		math_utils.h
	tests/
		math_utils_tests.cpp
```

Minimal `CMakeLists.txt` starter:

```cmake
cmake_minimum_required(VERSION 3.20)
project(my_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(my_project
	src/main.cpp
	src/math_utils.cpp
)

# Simple test executable without external test frameworks.
add_executable(my_project_tests
	tests/math_utils_tests.cpp
	src/math_utils.cpp
)

enable_testing()
add_test(NAME my_project_tests COMMAND my_project_tests)
```

Run with the playground runner from repository root:

```powershell
go run tools/run_playground.go -l cpp -p my_project
```

Run tests with the playground test runner from repository root:

```powershell
go run tools/test_playground.go -l cpp -p my_project
```

If your project needs custom commands or flags, add `playground.json` in the mini project folder.

## Testing Guide (Beginner)

Start with tiny, focused tests. For each function, add at least one passing case and one edge case.

Example `tests/math_utils_tests.cpp`:

```cpp
#include <cassert>
#include "../src/math_utils.h"

int main() {
		assert(add(2, 3) == 5);
		assert(add(-1, 1) == 0);
		return 0;
}
```

Run tests with CTest:

```powershell
cmake -S . -B .playground_build/cmake
cmake --build .playground_build/cmake --config Debug
ctest --test-dir .playground_build/cmake -C Debug --output-on-failure
```

Or run tests with the playground test runner from repository root:

```powershell
go run tools/test_playground.go -l cpp -p my_project
```

Testing checklist:

- Keep test names close to behavior (`add_handles_negative_values`).
- Test boundaries (empty input, zero, large values) early.
- Prefer deterministic tests (no timing/network randomness for beginners).

Default runner behavior:

- If `CMakeLists.txt` exists, uses CMake first (`cmake -S/-B`, then `cmake --build`).
- Attempts to auto-run the built executable target.
- If no `CMakeLists.txt` exists, falls back to compiling all `.cpp/.cc/.cxx` files recursively with `g++` (or `clang++`) using `-std=c++20`.

For advanced setups (custom flags, CMake, special run command), add `playground.json` in the mini project.

## Manual Build Guidance

Use these commands when you want to build and run a mini project without `run_playground`.

### 1) CMake mini project (recommended)

From the mini project folder (example: `playground/cpp/linkage_demo`):

```powershell
cmake -S . -B .playground_build/cmake
cmake --build .playground_build/cmake --config Debug
```

Run the executable:

```powershell
.\.playground_build\cmake\Debug\linkage_demo.exe
```

Run the unit tests with CTest:

```powershell
ctest --test-dir .playground_build/cmake -C Debug --output-on-failure
```

Notes:

- Replace `linkage_demo` with your target name from `add_executable(...)`.
- On single-config generators (for example MinGW Makefiles), the binary is usually directly under `.playground_build/cmake/`.

### 2) Non-CMake mini project (compiler fallback)

From the mini project folder:

```powershell
New-Item -ItemType Directory -Force .playground_build | Out-Null
$sources = Get-ChildItem -Recurse -File -Include *.cpp,*.cc,*.cxx | ForEach-Object { $_.FullName }
g++ -std=c++20 -O2 -g -o .playground_build\run_manual.exe $sources
.\.playground_build\run_manual.exe
```

If you prefer Clang, replace `g++` with `clang++`.
