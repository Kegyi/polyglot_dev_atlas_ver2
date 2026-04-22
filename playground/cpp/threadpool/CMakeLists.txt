cmake_minimum_required(VERSION 3.15)
project(threadpool CXX)
set(CMAKE_CXX_STANDARD 20)

set(THREADPOOL_GTEST_DIR "${CMAKE_CURRENT_SOURCE_DIR}/../../../googletest")
set(THREADPOOL_HAS_GTEST OFF)

# Header-only library target
add_library(threadpool INTERFACE)
# Use BUILD_INTERFACE for local builds and INSTALL_INTERFACE for installed usage
target_include_directories(threadpool INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
    $<INSTALL_INTERFACE:include/threadpool>)

# Demo/main target
add_executable(threadpool_main main.cpp)
target_link_libraries(threadpool_main PRIVATE threadpool)

add_executable(threadpool_examples threadpool_examples.cpp)
target_link_libraries(threadpool_examples PRIVATE threadpool)

find_package(GTest QUIET)

if(GTest_FOUND)
    set(THREADPOOL_HAS_GTEST ON)
elseif(EXISTS "${THREADPOOL_GTEST_DIR}/CMakeLists.txt")
    set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
    add_subdirectory(
        "${THREADPOOL_GTEST_DIR}"
        "${CMAKE_CURRENT_BINARY_DIR}/googletest"
        EXCLUDE_FROM_ALL
    )

    set(THREADPOOL_HAS_GTEST ON)

    if(TARGET gtest)
        add_library(GTest::gtest ALIAS gtest)
    endif()
    if(TARGET gtest_main)
        add_library(GTest::gtest_main ALIAS gtest_main)
    endif()

    message(STATUS "Using repo-local googletest from ${THREADPOOL_GTEST_DIR}")

else()
    message(STATUS "GTest not found and local googletest repo not found at ${THREADPOOL_GTEST_DIR}; skipping test targets.")
endif()

if(THREADPOOL_HAS_GTEST)
    enable_testing()
    add_subdirectory(tests)
endif()

# Install rules for header-only library
include(CMakePackageConfigHelpers)

install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/threadpool.h DESTINATION include/threadpool)

install(TARGETS threadpool EXPORT threadpoolTargets)
install(EXPORT threadpoolTargets
                FILE threadpoolTargets.cmake
                NAMESPACE threadpool::
                DESTINATION lib/cmake/threadpool)

configure_package_config_file(${CMAKE_CURRENT_SOURCE_DIR}/cmake/threadpoolConfig.cmake.in
    ${CMAKE_CURRENT_BINARY_DIR}/threadpoolConfig.cmake
    INSTALL_DESTINATION lib/cmake/threadpool)

write_basic_package_version_file(${CMAKE_CURRENT_BINARY_DIR}/threadpoolConfigVersion.cmake
    VERSION 0.1.0
    COMPATIBILITY AnyNewerVersion)

install(FILES ${CMAKE_CURRENT_BINARY_DIR}/threadpoolConfig.cmake
                ${CMAKE_CURRENT_BINARY_DIR}/threadpoolConfigVersion.cmake
                DESTINATION lib/cmake/threadpool)
