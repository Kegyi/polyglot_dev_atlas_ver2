package com.kegyi.playground.multifile

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers

class HelpersSpec extends AnyFlatSpec with Matchers {

  "scaledSum" should "multiply the list sum by the factor" in {
    Helpers.scaledSum(List(1, 2, 3), 2) shouldBe 12
  }

  it should "return 0 for an empty list" in {
    Helpers.scaledSum(List.empty, 5) shouldBe 0
  }

  it should "work with a factor of 1" in {
    Helpers.scaledSum(List(4, 6), 1) shouldBe 10
  }

  it should "work with a zero factor" in {
    Helpers.scaledSum(List(1, 2, 3), 0) shouldBe 0
  }
}
