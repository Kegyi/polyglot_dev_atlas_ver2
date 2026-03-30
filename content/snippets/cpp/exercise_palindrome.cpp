#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string s = "A man, a plan, a canal: Panama";
    std::string cleaned;
    for (char c : s) {
        if (std::isalnum(static_cast<unsigned char>(c))) {
            cleaned += std::tolower(static_cast<unsigned char>(c));
        }
    }
    
    bool isPalin = std::string(cleaned.rbegin(), cleaned.rend()) == cleaned;
    std::cout << (isPalin ? "Palindrome" : "Not a palindrome") << "\n";
    return 0;
}
