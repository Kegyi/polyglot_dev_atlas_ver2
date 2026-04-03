package main

import (
	"fmt"
)

func factorial(n int64) int64 {
	var r int64 = 1
	for i := int64(2); i <= n; i++ {
		r *= i
	}
	return r
}

func main() {
	var n int64
	if _, err := fmt.Scan(&n); err != nil {
		n = 5
	}
	fmt.Println(factorial(n))
}
