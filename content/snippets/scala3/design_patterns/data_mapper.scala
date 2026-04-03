case class User(id:Int,name:String)
object Mapper:
  def mapRow(row: Map[String,String]) = User(row("id").toInt, row("name"))
@main def runMapper() = println(Mapper.mapRow(Map("id"->"6","name"->"Frank")))
