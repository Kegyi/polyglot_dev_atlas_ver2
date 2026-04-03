package main

import (
	"fmt"
	"regexp"
	"sort"
	"strings"
)

func main() {
	text := "This is a test. This test is simple."
	re := regexp.MustCompile(`[A-Za-z]+`)
	words := re.FindAllString(strings.ToLower(text), -1)

	freq := map[string]int{}
	for _, w := range words {
		freq[w]++
	}

	type pair struct {
		word  string
		count int
	}

	items := make([]pair, 0, len(freq))
	for w, c := range freq {
		items = append(items, pair{w, c})
	}

	sort.Slice(items, func(i, j int) bool {
		if items[i].count == items[j].count {
			return items[i].word < items[j].word
		}
		return items[i].count > items[j].count
	})

	for _, it := range items {
		fmt.Printf("%s: %d\n", it.word, it.count)
	}
}
