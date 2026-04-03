@main def runGraph() =
  val g = Array(Array(1,2),Array(0,3),Array(0,3),Array(1,2))
  print("BFS:")
  import scala.collection.mutable.Queue
  val q = Queue(0); val seen = scala.collection.mutable.Set(0)
  while q.nonEmpty do val u = q.dequeue(); print(s" $u"); for v <- g(u) do if !seen(v) then seen += v; q.enqueue(v)
  println()
  print("DFS:"); val s = scala.collection.mutable.Set[Int]()
  def dfs(u:Int):Unit = { s += u; print(s" $u"); for v <- g(u) do if !s(v) then dfs(v) }
  dfs(0); println()
