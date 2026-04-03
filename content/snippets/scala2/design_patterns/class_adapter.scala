class Adaptee{ def specific() = println("Adaptee specific") }
trait Target{ def request():Unit }
class ClassAdapter extends Adaptee with Target{ def request() = specific() }
object Demo extends App{ new ClassAdapter().request() }
