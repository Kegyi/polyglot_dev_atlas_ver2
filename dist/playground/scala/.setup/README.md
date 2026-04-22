# Scala Playground Setup Guide

This folder is a reference hub — not a runnable project itself.
Copy `example_project/` to start a new mini project, then follow the tiers below to grow it.

---

## Folder layout

```text
.setup/
    README.md                   ← you are here
    example_project/            ← copy this to start a new project
        build.sbt
        project/
            build.properties
        src/
            main/
                scala/
                    com/example/playground/
                        Main.scala
                        Greeting.scala
            test/
                scala/
                    com/example/playground/
                        GreetingSpec.scala
```

---

## Tier 1 — Single-file scratch pad

Good for quick experiments that fit in one file. Minimal build configuration.

```text
playground/scala/my_scratch/
    build.sbt
    Main.scala
```

Minimal `build.sbt`:

```scala
ThisBuild / scalaVersion := "2.13.14"
```

Minimal `Main.scala`:

```scala
object Main {
  def main(args: Array[String]): Unit = {
    println("hello from my_scratch")
  }
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
sbt run
sbt compile
```

Manual test (inside the project folder):

```powershell
# Add a test file (Spec.scala), then:
sbt test
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l scala -p my_scratch
go run tools/test_playground.go -l scala -p my_scratch
```

Note: tool-based testing requires `sbt test` and ScalaTest dependencies to be configured.

When to move up: when the file exceeds ~100 lines, or you want to reuse logic across files.

---

## Tier 2 — Simple module with single package and tests

Add package structure and tests with ScalaTest using `AnyFunSuite` assertions.

```text
playground/scala/my_project/
    build.sbt
    project/
        build.properties
    src/
        main/
            scala/
                Calc.scala
                Main.scala
        test/
            scala/
                CalcSpec.scala
```

`build.sbt`:

```scala
ThisBuild / scalaVersion := "2.13.14"

libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.19" % Test
```

Example `src/main/scala/Calc.scala`:

```scala
object Calc {
  def add(a: Int, b: Int): Int = a + b
}
```

Example `src/test/scala/CalcSpec.scala`:

```scala
import org.scalatest.funsuite.AnyFunSuite

class CalcSpec extends AnyFunSuite {
  test("add returns the sum") {
    assert(Calc.add(2, 3) == 5)
  }
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
sbt run
sbt compile
```

Manual test (inside the project folder):

```powershell
sbt test
sbt test -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l scala -p my_project
go run tools/test_playground.go -l scala -p my_project
```

Note: `sbt test` runs all `*Spec.scala` and `*Test.scala` files automatically.

When to move up: when you want package organization or more expressive test assertions.

---

## Tier 3 — Package structure with ScalaTest FlatSpec (recommended)

Use the Maven directory layout with package namespacing and ScalaTest's `AnyFlatSpec` for cleaner test readability.
This is the pattern used by `example_project/` and `multi_file/`.

```text
playground/scala/my_project/
    build.sbt
    project/
        build.properties
    src/
        main/
            scala/
                com/example/playground/
                    Main.scala
                    Greeting.scala
        test/
            scala/
                com/example/playground/
                    GreetingSpec.scala
```

`build.sbt`:

```scala
ThisBuild / scalaVersion := "2.13.14"
ThisBuild / organization := "com.example.playground"
ThisBuild / version := "0.1.0-SNAPSHOT"

lazy val root = (project in file("."))
  .settings(
    name := "my_project",
    scalacOptions ++= Seq("-deprecation", "-feature", "-unchecked"),
    Compile / run / mainClass := Some("com.example.playground.Main"),
    libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.19" % Test
  )
```

Example `src/main/scala/com/example/playground/Greeting.scala`:

```scala
package com.example.playground

object Greeting {
  def greet(name: String): String = {
    if (name.isEmpty) "Hello" else s"Hello, $name"
  }
}
```

Example `src/test/scala/com/example/playground/GreetingSpec.scala`:

```scala
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
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
sbt run
sbt compile
```

Manual test (inside the project folder):

```powershell
sbt test
sbt test -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l scala -p my_project
go run tools/test_playground.go -l scala -p my_project
```

Note: `AnyFlatSpec` with `Matchers` provides readable BDD-style test naming.

When to move up: when you want parameterized tests or more advanced test patterns.

---

## Tier 4 — Better test quality with parameterized tests

Use ScalaTest's property-based testing and table-driven tests for comprehensive coverage.

Example `src/test/scala/com/example/playground/GreetingSpec.scala`:

```scala
package com.example.playground

import org.scalatest.flatspec.AnyFlatSpec
import org.scalatest.matchers.should.Matchers
import org.scalatest.prop.TableDrivenPropertyChecks

class GreetingSpec extends AnyFlatSpec with Matchers with TableDrivenPropertyChecks {

  "greet" should "return greeting with name" in {
    Greeting.greet("Alice") shouldBe "Hello, Alice"
  }

  it should "handle edge cases" in {
    val testCases = Table(
      ("input", "expected"),
      ("", "Hello"),
      ("world", "Hello, world"),
      ("  ", "Hello,   "),
    )
    forAll(testCases) { (input, expected) =>
      Greeting.greet(input) shouldBe expected
    }
  }
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
sbt run
sbt compile
```

Manual test (inside the project folder):

```powershell
sbt test
sbt test -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l scala -p my_project
go run tools/test_playground.go -l scala -p my_project
```

Note: ScalaTest's `TableDrivenPropertyChecks` allows clear parameterized test definitions.

When to move up: when you need custom build commands or environment-specific configurations.

---

## Tier 5 — Custom playground.json configuration

Override default build/run/test commands with a `playground.json` file in your project folder.

Example `playground.json`:

```json
{
  "build": ["sbt", "compile"],
  "run": ["sbt", "run"],
  "test": ["sbt", "test", "-v"],
  "workDir": ".",
  "env": {}
}
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
sbt compile
sbt run -J-Xmx2g
sbt test -v
```

Tool run/test (from repository root):

Uses the commands specified in `playground.json`:

```powershell
go run tools/run_playground.go -l scala -p my_project
go run tools/test_playground.go -l scala -p my_project
```

Note: `playground.json` is optional. Use it to customize build settings, memory flags, or test runners.

When to move up: your project is mature enough to warrant custom build logic or distributed testing.

---

## Testing Checklist

- ✓ Use clear test names that describe behavior (`"greet should return greeting with name"`).
- ✓ Keep pure logic in small objects/functions to simplify testing.
- ✓ Add edge-case tests (empty strings, boundary values, special characters).
- ✓ Use `AnyFlatSpec` + `Matchers` for readable assertions (`shouldBe`, `should contain`).
- ✓ Consider table-driven tests (`TableDrivenPropertyChecks`) for parameterized inputs.
- ✓ Run tests frequently with `sbt test` or the tool runner.

---

## Quick-start Checklist

- [ ] Copy `example_project/` to `playground/scala/my_first_try/`
- [ ] Run: `go run tools/run_playground.go -l scala -p my_first_try` (from repo root)
- [ ] Test: `go run tools/test_playground.go -l scala -p my_first_try` (from repo root)
- [ ] Modify `src/main/scala/com/example/playground/Greeting.scala` with your logic
- [ ] Add new test cases to `src/test/scala/com/example/playground/GreetingSpec.scala`
- [ ] Re-run tests to validate changes
