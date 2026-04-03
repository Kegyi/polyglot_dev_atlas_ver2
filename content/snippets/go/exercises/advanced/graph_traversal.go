package main

import "fmt"

func main() {
	g := [][]int{{1, 2}, {0, 3}, {0, 3}, {1, 2}}
	// BFS
	q := []int{0}
	seen := map[int]bool{0: true}
	fmt.Print("BFS:")
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		fmt.Print(" ", u)
		for _, v := range g[u] {
			if !seen[v] {
				seen[v] = true
				q = append(q, v)
			}
		}
	}
	fmt.Println()
	// DFS
	fmt.Print("DFS: ")
	seen = map[int]bool{}
	var dfs func(int)
	dfs = func(u int) {
		seen[u] = true
		fmt.Print(u, " ")
		for _, v := range g[u] {
			if !seen[v] {
				dfs(v)
			}
		}
	}
	dfs(0)
	fmt.Println()
}
