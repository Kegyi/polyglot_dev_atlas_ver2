package main

import "fmt"

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7, 8}

	sum := 0
	for _, n := range nums {
		if n%2 == 0 {
			sum += n * n
		}
	}

	fmt.Printf("Sum of squares of even numbers: %d\n", sum)
}
