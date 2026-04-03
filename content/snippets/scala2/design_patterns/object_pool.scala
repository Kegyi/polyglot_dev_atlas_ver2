class PooledObject(var value: Int = 0)
class ObjectPool[T <: PooledObject](size: Int){
  private val pool = new scala.collection.mutable.Stack[T]
  def acquire(factory: => T): T = if(pool.nonEmpty) pool.pop() else factory
  def release(t: T): Unit = pool.push(t)
}
object Demo extends App{
  val p = new ObjectPool[PooledObject](2)
  val o = p.acquire(new PooledObject())
  o.value = 3
  println(o.value)
  p.release(o)
}
