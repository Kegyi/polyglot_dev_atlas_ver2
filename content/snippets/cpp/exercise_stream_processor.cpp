#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8};
    
    auto sum = 0;
    std::for_each(nums.begin(), nums.end(), [&sum](int n) {
        if (n % 2 == 0) {
            sum += n * n;
        }
    });
    
    std::cout << "Sum of squares of even numbers: " << sum << "\n";
    return 0;
}
