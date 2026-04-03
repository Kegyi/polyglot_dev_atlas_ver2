package main

import "fmt"

func main() {
	wt := []int{3, 4, 5}
	val := []int{30, 50, 60}
	W := 8
	n := len(wt)
	dp := make([][]int, n+1)
	for i := 0; i <= n; i++ {
		dp[i] = make([]int, W+1)
	}
	for i := 1; i <= n; i++ {
		for w := 0; w <= W; w++ {
			dp[i][w] = dp[i-1][w]
			if w >= wt[i-1] {
				if cand := dp[i-1][w-wt[i-1]] + val[i-1]; cand > dp[i][w] {
					dp[i][w] = cand
				}
			}
		}
	}
	fmt.Println(dp[n][W])
}
