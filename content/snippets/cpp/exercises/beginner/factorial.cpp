#include <iostream>
using namespace std;

long long factorial(int n) {
    long long r = 1;
    for (int i = 2; i <= n; ++i) r *= i;
    return r;
}

int main() {
    int n;
    if (!(cin >> n)) n = 5;
    cout << factorial(n) << "\n";
    return 0;
}
