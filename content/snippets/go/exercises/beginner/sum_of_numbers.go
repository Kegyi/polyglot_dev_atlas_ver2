package main

import (
	"fmt"
)

func sumN(n int64) int64 {
	return n * (n + 1) / 2
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		n = 10
	}
	fmt.Println(sumN(n))
}
