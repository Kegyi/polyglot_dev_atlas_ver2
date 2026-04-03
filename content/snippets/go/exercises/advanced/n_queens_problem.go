package main
import "fmt"
var N=8
var cols = make([]int, N)
func ok(r,c int) bool{ for i:=0;i<r;i++{ if cols[i]==c || abs(cols[i]-c)==r-i { return false } } return true }
func abs(x int) int{ if x<0 { return -x }; return x }
func solve(r int) bool{ if r==N { fmt.Println(cols); return true }; for c:=0;c<N;c++{ if ok(r,c){ cols[r]=c; if solve(r+1){ return true } } } return false }
func main(){ solve(0) }
