package main

import "fmt"

func main() {
	celsius := 25.0
	fahrenheit := (celsius * 9 / 5) + 32
	kelvin := celsius + 273.15

	fmt.Printf("%.2f deg C = %.2f deg F = %.2f K\n", celsius, fahrenheit, kelvin)
}
