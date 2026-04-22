# C++ Playground Setup Guide

This folder is a reference hub — not a runnable project itself.
Copy `example_project/` to start a new mini project, then follow the tiers below to grow it.

---

## Folder layout

```text
.setup/
    README.md               ← you are here
    example_project/        ← copy this to start a new project
        CMakeLists.txt
        src/
            main.cpp
            hello.cpp
            hello.h
        tests/
            CMakeLists.txt
            hello_test.cpp
```

---

## Tier 1 — Single-file scratch pad (no CMake)

Good for quick experiments that fit in one file.

```text
playground/cpp/my_scratch/
    main.cpp
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
g++ -std=c++20 -O2 -g -o main.exe main.cpp
.\main.exe
```

Manual test (inside the project folder):

```powershell
# Add a test file (for example main_test.cpp), then compile and run it.
g++ -std=c++20 -O2 -g -o main_test.exe main_test.cpp
.\main_test.exe
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l cpp -p my_scratch
go run tools/test_playground.go -l cpp -p my_scratch
```

Note: tool-based testing requires a `CMakeLists.txt`.

When to move up: when the file exceeds ~150 lines, or you want to reuse logic in tests.

---

## Tier 2 — Multi-file CMake project (no external dependencies)

Split code into a small library + `main.cpp`.
Tests use `<cassert>` — no test framework needed.

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

Minimal `CMakeLists.txt`:

```cmake
cmake_minimum_required(VERSION 3.20)
project(my_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

add_library(math_utils_lib STATIC src/math_utils.cpp)
target_include_directories(math_utils_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

add_executable(my_project src/main.cpp)
target_link_libraries(my_project PRIVATE math_utils_lib)

add_executable(my_project_tests tests/math_utils_tests.cpp)
target_link_libraries(my_project_tests PRIVATE math_utils_lib)

enable_testing()
add_test(NAME my_project_tests COMMAND my_project_tests)
```

Simple assert-based test file (`tests/math_utils_tests.cpp`):

```cpp
#include <cassert>
#include "math_utils.h"

int main() {
    assert(add(2, 3) == 5);
    assert(add(-1, 1) == 0);
    return 0;
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
cmake -S . -B .playground_build/cmake
cmake --build .playground_build/cmake --config Debug
```

Manual run executable:

```powershell
.\.playground_build\cmake\Debug\my_project.exe
```

Manual test:

```powershell
ctest --test-dir .playground_build/cmake -C Debug --output-on-failure
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l cpp -p my_project
go run tools/test_playground.go -l cpp -p my_project
```

When to move up: when you want richer test output, test filtering, or parameterized tests.

---

## Tier 3 — CMake project with GoogleTest (recommended for serious work)

This is the pattern used by `example_project/` and `linkage_demo/`.
GTest is resolved automatically — either from a system install or the repo-local
`googletest/` directory at the workspace root.

```text
playground/cpp/my_project/
    CMakeLists.txt          ← see example_project's for the GTest detection block
    src/
        main.cpp
        greeter.cpp
        greeter.h
    tests/
        CMakeLists.txt
        greeter_test.cpp
```

Root `CMakeLists.txt` — GTest detection block (paste this in):

```cmake
set(MY_GTEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../googletest")
set(MY_HAS_GTEST OFF)

find_package(GTest QUIET)

if(GTest_FOUND)
    set(MY_HAS_GTEST ON)
elseif(EXISTS "${MY_GTEST_DIR}/CMakeLists.txt")
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    add_subdirectory(
        "${MY_GTEST_DIR}"
        "${CMAKE_CURRENT_BINARY_DIR}/googletest"
        EXCLUDE_FROM_ALL
    )
    set(MY_HAS_GTEST ON)

    if(TARGET gtest AND NOT TARGET GTest::gtest)
        add_library(GTest::gtest ALIAS gtest)
    endif()
    if(TARGET gtest_main AND NOT TARGET GTest::gtest_main)
        add_library(GTest::gtest_main ALIAS gtest_main)
    endif()
else()
    message(STATUS "GTest not found; skipping test targets.")
endif()

if(MY_HAS_GTEST)
    enable_testing()
    add_subdirectory(tests)
endif()
```

`tests/CMakeLists.txt`:

```cmake
include(GoogleTest)

add_executable(my_project_tests greeter_test.cpp)
target_link_libraries(my_project_tests PRIVATE greeter_lib GTest::gtest_main)
gtest_discover_tests(my_project_tests)
```

Example test file (`tests/greeter_test.cpp`):

```cpp
#include <gtest/gtest.h>
#include "greeter.h"

TEST(Greet, ContainsName) {
    EXPECT_NE(greet("Alice").find("Alice"), std::string::npos);
}

TEST(Greet, StartsWithHello) {
    EXPECT_EQ(greet("world").substr(0, 5), "Hello");
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
cmake -S . -B .playground_build/cmake
cmake --build .playground_build/cmake --config Debug
```

Manual run executable:

```powershell
.\.playground_build\cmake\Debug\my_project.exe
```

Manual test:

```powershell
ctest --test-dir .playground_build/cmake -C Debug --output-on-failure
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l cpp -p my_project
go run tools/test_playground.go -l cpp -p my_project
```

---

## Tier 4 — Advanced: custom flags and `playground.json`

When a project needs special compiler flags, extra `#define`s, or a non-standard run
command, add a `playground.json` in the mini project folder.

Example `playground.json`:

```json
{
    "build": ["cmake", "--build", ".playground_build/cmake", "--config", "Debug"],
    "run": [".playground_build/cmake/Debug/my_project.exe"],
    "test": ["ctest", "--test-dir", ".playground_build/cmake", "-C", "Debug", "--output-on-failure"]
}
```

See `tools/run_playground.go` and `tools/test_playground.go` for the full list of supported keys.

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
cmake -S . -B .playground_build/cmake -DMY_FEATURE=ON
cmake --build .playground_build/cmake --config Debug
```

Manual run executable:

```powershell
.\.playground_build\cmake\Debug\my_project.exe
```

Manual test:

```powershell
ctest --test-dir .playground_build/cmake -C Debug --output-on-failure
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l cpp -p my_project
go run tools/test_playground.go -l cpp -p my_project
```

Note: at this tier, `playground.json` can override both run and test commands.

---

## Quick-start checklist

1. Copy `.setup/example_project/` to `playground/cpp/<your_name>/`.
2. Rename every occurrence of `example_project` / `hello` to your project name.
3. Replace `src/hello.cpp` and `src/hello.h` with your own logic.
4. Add tests in `tests/hello_test.cpp` (one passing case + one edge case minimum).
5. Run: `go run tools/run_playground.go -l cpp -p <your_name>`
6. Test: `go run tools/test_playground.go -l cpp -p <your_name>`

---

## Testing checklist

- Name tests after behaviour: `Greet_EmptyNameProducesNonEmptyString`.
- Cover the happy path, at least one boundary (empty, zero, max), and one error case.
- Keep tests deterministic — no timing, no network, no random seeds without a fixed value.
- Prefer `EXPECT_*` over `ASSERT_*` unless the test truly cannot continue after a failure.
