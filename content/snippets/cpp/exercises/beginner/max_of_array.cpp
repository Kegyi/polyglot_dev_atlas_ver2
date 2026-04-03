#include <iostream>
#include <vector>
#include <limits>
using namespace std;

int main() {
    int n;
    if (!(cin >> n)) n = 5;
    vector<long long> a(n);
    for (int i = 0; i < n; ++i) {
        if (!(cin >> a[i])) a[i] = i;
    }
    long long mx = numeric_limits<long long>::min();
    for (auto v : a) mx = max(mx, v);
    cout << mx << "\n";
    return 0;
}
