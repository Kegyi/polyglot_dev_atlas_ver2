object GraphTraversal extends App{
  val g = Array(Array(1,2),Array(0,3),Array(0,3),Array(1,2))
  println("BFS:")
  import scala.collection.mutable.Queue
  val q = Queue(0); val seen = scala.collection.mutable.Set(0)
  while(q.nonEmpty){ val u=q.dequeue(); print(u+" "); for(v<-g(u)) if(!seen(v)){ seen += v; q.enqueue(v) } }
  println();
  print("DFS: "); val s = scala.collection.mutable.Set[Int]()
  def dfs(u:Int):Unit={ s += u; print(u+" "); for(v<-g(u)) if(!s(v)) dfs(v) }
  dfs(0); println();
}
