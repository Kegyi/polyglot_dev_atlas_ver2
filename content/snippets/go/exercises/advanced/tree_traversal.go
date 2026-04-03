package main

import "fmt"

type Node struct {
	val   int
	left  *Node
	right *Node
}

func inorder(root *Node, res *[]int) {
	if root == nil {
		return
	}
	inorder(root.left, res)
	*res = append(*res, root.val)
	inorder(root.right, res)
}

func main() {
	root := &Node{val: 1}
	root.left = &Node{val: 2}
	root.right = &Node{val: 3}
	root.left.left = &Node{val: 4}

	var res []int
	inorder(root, &res)
	fmt.Println(res)
}
