package main

import (
	"fmt"
	"strings"
	"sync"
)

type result struct {
	endpoint string
	ok       bool
	payload  string
}

func fetch(ep string) result {
	if strings.Contains(ep, "fail") {
		return result{ep, false, "timeout"}
	}
	return result{ep, true, fmt.Sprintf("{\"endpoint\":\"%s\"}", ep)}
}

func main() {
	endpoints := []string{"users", "orders", "fail-metrics"}
	ch := make(chan result, len(endpoints))
	var wg sync.WaitGroup

	for _, ep := range endpoints {
		wg.Add(1)
		go func(e string) {
			defer wg.Done()
			ch <- fetch(e)
		}(ep)
	}

	wg.Wait()
	close(ch)

	var data []string
	var errors []string
	for r := range ch {
		if r.ok {
			data = append(data, r.payload)
		} else {
			errors = append(errors, r.endpoint+": "+r.payload)
		}
	}

	fmt.Printf("data=%d errors=%d\n", len(data), len(errors))
}
