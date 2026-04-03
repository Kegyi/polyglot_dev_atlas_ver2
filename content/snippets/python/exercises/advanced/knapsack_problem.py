wt=[3,4,5]
val=[30,50,60]
W=8
n=len(wt)
dp=[[0]*(W+1) for _ in range(n+1)]
for i in range(1,n+1):
    for w in range(W+1):
        dp[i][w]=dp[i-1][w]
        if w>=wt[i-1]: dp[i][w]=max(dp[i][w], dp[i-1][w-wt[i-1]]+val[i-1])
print(dp[n][W])
