package greeter_test

import (
	"strings"
	"testing"

	"playground/example_project/internal/greeter"
)

func TestGreet_ContainsName(t *testing.T) {
	got := greeter.Greet("Alice")
	if !strings.Contains(got, "Alice") {
		t.Errorf("Greet(%q) = %q, want it to contain the name", "Alice", got)
	}
}

func TestGreet_StartsWithHello(t *testing.T) {
	got := greeter.Greet("world")
	if !strings.HasPrefix(got, "Hello") {
		t.Errorf("Greet(%q) = %q, want it to start with Hello", "world", got)
	}
}

func TestGreet_EmptyName(t *testing.T) {
	got := greeter.Greet("")
	if got == "" {
		t.Error("Greet(\"\") returned an empty string, want non-empty")
	}
}
