package main

import "fmt"

type User struct {
	ID   int
	Name string
}

func mapRow(row map[string]string) User {
	return User{ID: atoi(row["id"]), Name: row["name"]}
}
func atoi(s string) int { var v int; fmt.Sscan(s, &v); return v }
func main() {
	row := map[string]string{"id": "3", "name": "Carol"}
	u := mapRow(row)
	fmt.Println(u.ID, u.Name)
}
