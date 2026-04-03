@main def runDijkstra() =
  val g = Map(0->List((1,10),(2,3)),1->List((3,2)),2->List((1,1),(3,8)),3->List())
  import scala.collection.mutable.PriorityQueue
  given ord: Ordering[(Int,Int)] = Ordering.by(-_._2)
  def dijkstra(src:Int) =
    val dist = scala.collection.mutable.Map(g.keys.toSeq.map(k=>k->Int.MaxValue):_*)
    dist(src)=0
    val pq = PriorityQueue((src,0))
    while pq.nonEmpty do
      val (u,du) = pq.dequeue()
      if du==dist(u) then for ( (v,w) <- g(u) ) if dist(v) > du + w then dist(v)=du+w; pq.enqueue((v,dist(v)))
    dist
  println(dijkstra(0))
