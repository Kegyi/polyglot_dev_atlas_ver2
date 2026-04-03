package main

import "fmt"

type Adaptee struct{}

func (Adaptee) Specific() { fmt.Println("Adaptee specific") }

type Target interface{ Request() }

type ObjectAdapter struct{ a Adaptee }

func (o ObjectAdapter) Request() { o.a.Specific() }
func main()                      { var t Target = ObjectAdapter{}; t.Request() }
