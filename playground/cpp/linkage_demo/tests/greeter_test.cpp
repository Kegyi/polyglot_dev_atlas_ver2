#include <gtest/gtest.h>

#include "greeter.h"

TEST(MakeMessage, ContainsName) {
    std::string msg = make_message("Alice");
    EXPECT_NE(msg.find("Alice"), std::string::npos);
}

TEST(MakeMessage, ContainsHello) {
    std::string msg = make_message("World");
    EXPECT_NE(msg.find("Hello"), std::string::npos);
}

TEST(MakeMessage, EmptyNameProducesNonEmptyString) {
    std::string msg = make_message("");
    EXPECT_FALSE(msg.empty());
}
