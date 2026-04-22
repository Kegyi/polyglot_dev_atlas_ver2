cmake_minimum_required(VERSION 3.16)
project(linkage_demo LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Core library — shared between the app and the tests
add_library(greeter_lib STATIC greeter.cpp)
target_include_directories(greeter_lib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})

# Main executable
add_executable(linkage_demo main.cpp)
target_link_libraries(linkage_demo PRIVATE greeter_lib)

set(LINKAGE_DEMO_GTEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../googletest")
set(LINKAGE_DEMO_HAS_GTEST OFF)

find_package(GTest QUIET)

if(GTest_FOUND)
    set(LINKAGE_DEMO_HAS_GTEST ON)
elseif(EXISTS "${LINKAGE_DEMO_GTEST_DIR}/CMakeLists.txt")
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    add_subdirectory(
        "${LINKAGE_DEMO_GTEST_DIR}"
        "${CMAKE_CURRENT_BINARY_DIR}/googletest"
        EXCLUDE_FROM_ALL
    )

    set(LINKAGE_DEMO_HAS_GTEST ON)

    if(TARGET gtest)
        add_library(GTest::gtest ALIAS gtest)
    endif()
    if(TARGET gtest_main)
        add_library(GTest::gtest_main ALIAS gtest_main)
    endif()

    message(STATUS "Using repo-local googletest from ${LINKAGE_DEMO_GTEST_DIR}")
else()
    message(STATUS "GTest not found and local googletest repo not found at ${LINKAGE_DEMO_GTEST_DIR}; skipping test targets.")
endif()

if(LINKAGE_DEMO_HAS_GTEST)
    enable_testing()
    add_subdirectory(tests)
endif()
