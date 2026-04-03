package main

import "fmt"

func main() {
	acts := [][2]int{{1, 4}, {3, 5}, {0, 6}, {5, 7}, {8, 9}, {5, 9}}
	// sort by end (simple bubble for brevity)
	for i := 0; i < len(acts); i++ {
		for j := i + 1; j < len(acts); j++ {
			if acts[j][1] < acts[i][1] {
				acts[i], acts[j] = acts[j], acts[i]
			}
		}
	}
	last := -1
	res := [][2]int{}
	for _, a := range acts {
		if a[0] > last {
			res = append(res, a)
			last = a[1]
		}
	}
	fmt.Println("Selected", res)
}
