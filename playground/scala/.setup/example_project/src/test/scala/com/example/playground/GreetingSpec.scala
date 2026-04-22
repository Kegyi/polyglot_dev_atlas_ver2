package com.example.playground

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class GreetingSpec extends AnyFlatSpec with Matchers {

  "greet" should "return greeting with name" in {
    Greeting.greet("Alice") shouldBe "Hello, Alice"
  }

  it should "return plain hello for empty string" in {
    Greeting.greet("") shouldBe "Hello"
  }

  it should "return greeting with world" in {
    Greeting.greet("world") shouldBe "Hello, world"
  }
}
