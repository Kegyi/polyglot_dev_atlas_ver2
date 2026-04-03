package main

import (
	"fmt"
)

func main() {
	var n int
	if _, err := fmt.Scan(&n); err != nil {
		n = 5
	}
	arr := make([]int64, n)
	for i := 0; i < n; i++ {
		if _, err := fmt.Scan(&arr[i]); err != nil {
			arr[i] = int64(i)
		}
	}
	var mx int64 = arr[0]
	for _, v := range arr {
		if v > mx {
			mx = v
		}
	}
	fmt.Println(mx)
}
