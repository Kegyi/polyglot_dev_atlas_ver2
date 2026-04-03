package main

import (
	"fmt"
	"sync"
)

type Lazy struct{ Value int }

var (
	inst *Lazy
	once sync.Once
)

func Instance() *Lazy { once.Do(func() { inst = &Lazy{} }); return inst }
func main() {
	Instance().Value = 8
	fmt.Println(Instance().Value)
}
