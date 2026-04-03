const wt = [3,4,5], val=[30,50,60], W=8
const n=wt.length
const dp: number[][] = Array.from({length:n+1},()=>Array(W+1).fill(0))
for(let i=1;i<=n;i++) for(let w=0; w<=W; w++){ dp[i][w]=dp[i-1][w]; if(w>=wt[i-1]) dp[i][w]=Math.max(dp[i][w], dp[i-1][w-wt[i-1]]+val[i-1]) }
console.log(dp[n][W])
export {}
