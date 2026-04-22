package com.example.playground

object Greeting {
  def greet(name: String): String = {
    if (name.isEmpty) "Hello" else s"Hello, $name"
  }
}
