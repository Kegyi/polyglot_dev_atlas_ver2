include(GoogleTest)

add_executable(linkage_demo_tests greeter_test.cpp)
target_link_libraries(linkage_demo_tests PRIVATE greeter_lib GTest::gtest_main)
gtest_discover_tests(linkage_demo_tests)
