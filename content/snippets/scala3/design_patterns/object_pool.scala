class PooledObject(var value: Int = 0)
class ObjectPool[T <: PooledObject](size: Int):
  private val pool = scala.collection.mutable.Stack.empty[T]
  def acquire(factory: => T): T = if pool.nonEmpty then pool.pop() else factory
  def release(t: T): Unit = pool.push(t)

@main def runPool() =
  val p = ObjectPool[PooledObject](2)
  val o = p.acquire(PooledObject())
  o.value = 4
  println(o.value)
