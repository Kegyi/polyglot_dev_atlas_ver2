#include <iostream>
#include <vector>

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5};
    std::reverse(arr.begin(), arr.end());
    
    for (int x : arr) {
        std::cout << x << " ";
    }
    std::cout << "\n";
    return 0;
}
