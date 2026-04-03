@main def runActivity() =
  val acts = Array((1,4),(3,5),(0,6),(5,7),(8,9),(5,9))
  val sorted = acts.sortBy(_._2)
  var last = -1
  val res = scala.collection.mutable.ArrayBuffer.empty[(Int,Int)]
  for ((s,e) <- sorted) if s > last then res += ((s,e)); last = e
  println("Selected " + res)
