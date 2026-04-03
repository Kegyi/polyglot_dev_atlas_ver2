package main

import (
	"container/heap"
	"fmt"
)

type Item struct {
	v int
	d int
}
type PQ []Item

func (p PQ) Len() int            { return len(p) }
func (p PQ) Less(i, j int) bool  { return p[i].d < p[j].d }
func (p PQ) Swap(i, j int)       { p[i], p[j] = p[j], p[i] }
func (p *PQ) Push(x interface{}) { *p = append(*p, x.(Item)) }
func (p *PQ) Pop() interface{}   { old := *p; n := len(old); x := old[n-1]; *p = old[:n-1]; return x }

func dijkstra(src int, g map[int][][]int) map[int]int {
	INF := 1 << 30
	dist := map[int]int{}
	for k := range g {
		dist[k] = INF
	}
	dist[src] = 0
	pq := &PQ{{v: src, d: 0}}
	heap.Init(pq)
	for pq.Len() > 0 {
		it := heap.Pop(pq).(Item)
		if it.d != dist[it.v] {
			continue
		}
		for _, e := range g[it.v] {
			v := e[0]
			w := e[1]
			if dist[v] > it.d+w {
				dist[v] = it.d + w
				heap.Push(pq, Item{v: v, d: dist[v]})
			}
		}
	}
	return dist
}
func main() {
	g := map[int][][]int{0: {{1, 10}, {2, 3}}, 1: {{3, 2}}, 2: {{1, 1}, {3, 8}}, 3: {}}
	fmt.Println(dijkstra(0, g))
}
