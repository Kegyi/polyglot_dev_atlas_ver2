package com.kegyi.playground.multifile

object Main {
  def main(args: Array[String]): Unit = {
    val values = List(1, 2, 3)
    println(s"scaled sum: ${Helpers.scaledSum(values, 10)}")
  }
}
