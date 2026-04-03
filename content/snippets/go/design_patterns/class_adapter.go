package main

import "fmt"

// Go doesn't have class inheritance; demonstrate embedding to adapt

type Adaptee struct{}

func (Adaptee) Specific() { fmt.Println("Adaptee specific") }

type Target interface{ Request() }

type ClassAdapter struct{ Adaptee }

func (c ClassAdapter) Request() { c.Specific() }
func main()                     { var t Target = ClassAdapter{}; t.Request() }
