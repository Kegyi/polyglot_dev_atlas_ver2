#include <gtest/gtest.h>

#include "hello.h"

TEST(Greet, ContainsName) {
    EXPECT_NE(greet("Alice").find("Alice"), std::string::npos);
}

TEST(Greet, StartsWithHello) {
    EXPECT_EQ(greet("world").substr(0, 5), "Hello");
}

TEST(Greet, EmptyNameProducesNonEmptyString) {
    EXPECT_FALSE(greet("").empty());
}
