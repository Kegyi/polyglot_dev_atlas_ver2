#include <iostream>

int main() {
    int n;
    std::cout << "Enter number of terms: ";
    std::cin >> n;
    
    long long a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        std::cout << a << " ";
        long long temp = a + b;
        a = b;
        b = temp;
    }
    std::cout << "\n";
    return 0;
}
