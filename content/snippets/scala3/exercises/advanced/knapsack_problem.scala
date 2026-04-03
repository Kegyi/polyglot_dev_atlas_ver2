@main def runKnapsack() =
  val wt = Array(3,4,5); val v = Array(30,50,60); val W=8; val n=wt.length
  val dp = Array.fill(n+1, W+1)(0)
  for i <- 1 to n do for w <- 0 to W do dp(i)(w) = math.max(dp(i)(w), if w>=wt(i-1) then dp(i-1)(w-wt(i-1))+v(i-1) else dp(i-1)(w))
  println(dp(n)(W))
