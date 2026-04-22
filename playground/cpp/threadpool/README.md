# Threadpool Mini Project

This mini project hosts the fixed-size, header-only thread pool and its tests.

## Files

- `threadpool.h`: header-only thread pool implementation.
- `main.cpp`: simple demo using synchronized printing.
- `threadpool_examples.cpp`: extra usage examples.
- `threadpool_test.cpp`: core Google Test unit tests.
- `threadpool_edge_tests.cpp`: edge-case and specialization tests.
- `threadpool_test_fixed.cpp`: earlier fixed test variant kept for reference.

## Build

From this directory:

```powershell
cmake -S . -B build -G "MinGW Makefiles" -DCMAKE_TOOLCHAIN_FILE=../../../build/conan_toolchain.cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_PREFIX_PATH=../../../build
cmake --build build --config Release
```

## Run

```powershell
.\build\threadpool_test.exe
.\build\threadpool_edge_tests.exe
.\build\threadpool_examples.exe
.\build\threadpool_main.exe
```
