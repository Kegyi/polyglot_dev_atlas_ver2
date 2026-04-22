package main

import (
	"fmt"

	"playground/multi_file/internal/stats"
)

func main() {
	values := []float64{3, 4, 5, 2, 8}
	fmt.Printf("values:  %v\n", values)
	fmt.Printf("sum:     %.1f\n", stats.Sum(values))
	fmt.Printf("average: %.1f\n", stats.Average(values))
	fmt.Printf("max:     %.1f\n", stats.Max(values))
}
