class Adaptee{ def specific() = println("Adaptee specific") }
trait Target{ def request():Unit }
class ClassAdapter extends Adaptee with Target{ def request() = specific() }
@main def runClassAdapter() = ClassAdapter().request()
