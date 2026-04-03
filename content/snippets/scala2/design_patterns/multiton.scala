object Multiton {
  private var instances = Map.empty[String, Multiton]
  def get(key: String) = instances.getOrElse(key, { val m = new Multiton(key); instances += (key -> m); m })
}
class Multiton(val key: String)
object Demo extends App{
  println(Multiton.get("a").key)
}
