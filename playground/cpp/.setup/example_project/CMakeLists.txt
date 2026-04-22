cmake_minimum_required(VERSION 3.20)
project(example_project LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Core library — shared between the app and the tests
add_library(hello_lib STATIC src/hello.cpp)
target_include_directories(hello_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/src)

# Main executable
add_executable(example_project src/main.cpp)
target_link_libraries(example_project PRIVATE hello_lib)

# ---------------------------------------------------------------------------
# Tests (optional — requires GTest via system install or repo-local googletest)
# ---------------------------------------------------------------------------
set(EXAMPLE_GTEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../googletest")
set(EXAMPLE_HAS_GTEST OFF)

find_package(GTest QUIET)

if(GTest_FOUND)
    set(EXAMPLE_HAS_GTEST ON)
elseif(EXISTS "${EXAMPLE_GTEST_DIR}/CMakeLists.txt")
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    add_subdirectory(
        "${EXAMPLE_GTEST_DIR}"
        "${CMAKE_CURRENT_BINARY_DIR}/googletest"
        EXCLUDE_FROM_ALL
    )
    set(EXAMPLE_HAS_GTEST ON)

    if(TARGET gtest AND NOT TARGET GTest::gtest)
        add_library(GTest::gtest ALIAS gtest)
    endif()
    if(TARGET gtest_main AND NOT TARGET GTest::gtest_main)
        add_library(GTest::gtest_main ALIAS gtest_main)
    endif()

    message(STATUS "Using repo-local googletest from ${EXAMPLE_GTEST_DIR}")
else()
    message(STATUS "GTest not found; skipping test targets.")
endif()

if(EXAMPLE_HAS_GTEST)
    enable_testing()
    add_subdirectory(tests)
endif()
