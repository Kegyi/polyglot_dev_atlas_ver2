package main

import (
	"fmt"
	"regexp"
	"strings"
)

func main() {
	s := "A man, a plan, a canal: Panama"
	re := regexp.MustCompile(`[^a-zA-Z0-9]`)
	cleaned := strings.ToLower(re.ReplaceAllString(s, ""))

	rev := ""
	for _, c := range cleaned {
		rev = string(c) + rev
	}

	if cleaned == rev {
		fmt.Println("Palindrome")
	} else {
		fmt.Println("Not a palindrome")
	}
}
