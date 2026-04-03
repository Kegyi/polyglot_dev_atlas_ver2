#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(long long n) {
    if (n < 2) return false;
    if (n % 2 == 0) return n == 2;
    for (long long i = 3; i * i <= n; i += 2) if (n % i == 0) return false;
    return true;
}

int main() {
    long long n;
    if (!(cin >> n)) n = 97;
    cout << (is_prime(n) ? "true" : "false") << "\n";
}
