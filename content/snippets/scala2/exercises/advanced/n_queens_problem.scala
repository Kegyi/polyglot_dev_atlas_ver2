object NQueens extends App{
  val N=8; val cols = Array.fill(N)(0)
  def ok(r:Int,c:Int)= (0 until r).forall(i=> cols(i)!=c && math.abs(cols(i)-c)!=r-i)
  def solve(r:Int):Boolean = if(r==N){ println(cols.mkString(",")); true } else { for(c<-0 until N) if(ok(r,c)){ cols(r)=c; if(solve(r+1)) return true }; false }
  solve(0)
}
