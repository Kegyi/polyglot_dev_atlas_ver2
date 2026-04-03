case class User(id:Int,name:String)
object Mapper{
  def mapRow(row: Map[String,String]) = User(row("id").toInt, row("name"))
}
object Demo extends App{ println(Mapper.mapRow(Map("id"->"5","name"->"Eve"))) }
