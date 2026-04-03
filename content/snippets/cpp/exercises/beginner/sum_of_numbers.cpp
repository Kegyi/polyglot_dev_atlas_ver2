#include <iostream>
using namespace std;

long long sum_n(long long n) {
    return n * (n + 1) / 2;
}

int main() {
    long long n;
    // Example: input a number, prints the sum of 1..n
    if (!(cin >> n)) n = 10;
    cout << sum_n(n) << "\n";
    return 0;
}
