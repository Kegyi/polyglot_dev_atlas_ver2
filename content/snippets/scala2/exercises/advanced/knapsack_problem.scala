object Knapsack extends App{
  val wt = Array(3,4,5); val v = Array(30,50,60); val W=8; val n=wt.length
  val dp = Array.fill(n+1, W+1)(0)
  for(i<-1+1 to n) for(w<-0 to W){ dp(i)(w)=dp(i-1)(w); if(w>=wt(i-1)) dp(i)(w)=math.max(dp(i)(w), dp(i-1)(w-wt(i-1))+v(i-1)) }
  println(dp(n)(W))
}
