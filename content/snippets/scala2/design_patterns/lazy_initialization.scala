object LazySingleton {
  lazy val instance: LazySingleton = new LazySingleton
}
class LazySingleton { var value = 0 }
object Demo extends App{
  LazySingleton.instance.value = 1
  println(LazySingleton.instance.value)
}
