class Adaptee{ def specific() = println("Adaptee specific") }
trait Target{ def request():Unit }
class ObjectAdapter extends Target{ val a = new Adaptee(); def request() = a.specific() }
object Demo extends App{ new ObjectAdapter().request() }
