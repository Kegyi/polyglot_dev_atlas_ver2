#include <bits/stdc++.h>
using namespace std;int main(){
    vector<int> wt={3,4,5}, val={30,50,60}; int W=8, n=wt.size();
    vector<vector<int>> dp(n+1, vector<int>(W+1));
    for(int i=1;i<=n;i++) for(int w=0;w<=W;w++) dp[i][w]=dp[i-1][w];
    for(int i=1;i<=n;i++) for(int w=wt[i-1];w<=W;w++) dp[i][w]=max(dp[i][w], dp[i-1][w-wt[i-1]]+val[i-1]);
    cout<<dp[n][W]<<"\n";
}
