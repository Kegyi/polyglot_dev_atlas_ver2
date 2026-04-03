package main

import "fmt"

var instances = map[string]*Multiton{}

type Multiton struct{ Key string }

func Get(key string) *Multiton {
	if v, ok := instances[key]; ok {
		return v
	}
	m := &Multiton{Key: key}
	instances[key] = m
	return m
}
func main() {
	a := Get("a")
	b := Get("b")
	fmt.Println(a.Key, b.Key)
}
