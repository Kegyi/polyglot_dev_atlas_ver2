class Adaptee{ def specific() = println("Adaptee specific") }
trait Target{ def request():Unit }
class ObjectAdapter extends Target{ val a = Adaptee(); def request() = a.specific() }
@main def runObjAdapter() = ObjectAdapter().request()
