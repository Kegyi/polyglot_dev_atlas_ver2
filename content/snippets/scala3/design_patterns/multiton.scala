object Multiton:
  private var instances = Map.empty[String, Multiton]
  def get(key: String) =
    instances.get(key).getOrElse({ val m = Multiton(key); instances += (key -> m); m })
case class Multiton(key: String)
@main def runMulti() = println(Multiton.get("a").key)
