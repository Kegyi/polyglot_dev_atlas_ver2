object LazySingleton:
  lazy val instance = new LazySingleton
class LazySingleton:
  var value = 0
@main def runLazy() =
  LazySingleton.instance.value = 2
  println(LazySingleton.instance.value)
