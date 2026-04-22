include(GoogleTest)

add_executable(threadpool_tests
    threadpool_test.cpp
    threadpool_edge_tests.cpp
)
target_link_libraries(threadpool_tests PRIVATE threadpool GTest::gtest_main)
gtest_discover_tests(threadpool_tests)
