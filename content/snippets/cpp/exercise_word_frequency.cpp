#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    std::string line = "This is a test. This test is simple.";
    for (char& c : line) {
        if (std::ispunct(static_cast<unsigned char>(c))) c = ' ';
        else c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
    }

    std::unordered_map<std::string, int> freq;
    std::istringstream in(line);
    std::string word;
    while (in >> word) freq[word]++;

    std::vector<std::pair<std::string, int>> items(freq.begin(), freq.end());
    std::sort(items.begin(), items.end(), [](auto& a, auto& b) {
        return a.second == b.second ? a.first < b.first : a.second > b.second;
    });

    for (const auto& p : items) {
        std::cout << p.first << ": " << p.second << "\n";
    }
}
