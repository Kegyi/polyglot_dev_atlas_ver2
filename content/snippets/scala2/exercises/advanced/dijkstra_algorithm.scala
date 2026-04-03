object Dijkstra extends App{
  val g = Map(0->List((1,10),(2,3)),1->List((3,2)),2->List((1,1),(3,8)),3->List())
  import scala.collection.mutable.PriorityQueue
  implicit val ord = Ordering.by[(Int,Int),Int](-_._2)
  def dijkstra(src:Int) ={
    val dist = scala.collection.mutable.Map(g.keys.toSeq.map(k=>k->Int.MaxValue):_*); dist(src)=0
    val pq = PriorityQueue((src,0))
    while(pq.nonEmpty){ val (u,du)=pq.dequeue(); if(du==dist(u)) for((v,w)<-g(u)) if(dist(v)>du+w){ dist(v)=du+w; pq.enqueue((v,dist(v))) } }
    dist
  }
  println(dijkstra(0))
}
