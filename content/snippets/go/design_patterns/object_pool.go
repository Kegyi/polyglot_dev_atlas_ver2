package main

import "fmt"

type PooledObject struct{ Value int }

type ObjectPool struct{ pool chan *PooledObject }

func NewObjectPool(size int) *ObjectPool {
	return &ObjectPool{pool: make(chan *PooledObject, size)}
}
func (p *ObjectPool) Acquire() *PooledObject {
	select {
	case o := <-p.pool:
		return o
	default:
		return &PooledObject{}
	}
}
func (p *ObjectPool) Release(o *PooledObject) {
	select {
	case p.pool <- o:
	default:
	}
}

func main() {
	p := NewObjectPool(2)
	o := p.Acquire()
	o.Value = 5
	fmt.Println(o.Value)
	p.Release(o)
}
