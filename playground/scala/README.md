# Scala Playground

Create mini projects as subfolders under this folder.

For a guided setup from beginner to advanced, see [.setup/README.md](.setup/README.md).

## Create Your Own Mini Project

Copy `.setup/example_project/` to get started quickly:

```powershell
cp -r .setup/example_project my_first_project
cd my_first_project
sbt run
sbt test
```

Or create from scratch using the folder structure:

```text
playground/scala/my_project/
	build.sbt
	project/
		build.properties
	src/
		main/
			scala/
				Main.scala
		test/
			scala/
				CalcSpec.scala
```

Minimal `build.sbt`:

```scala
ThisBuild / scalaVersion := "2.13.14"

libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.19" % Test
```

Minimal `src/main/scala/Main.scala`:

```scala
object Main {
  def main(args: Array[String]): Unit = {
    println("hello from my_project")
  }
}
```

## Running Projects

Run from repository root:

```powershell
go run tools/run_playground.go -l scala -p my_project
```

Run manually (inside project):

```powershell
sbt run
```

If defaults are not enough, add `playground.json` in the mini project folder.

## Testing Projects

Run from repository root:

```powershell
go run tools/test_playground.go -l scala -p my_project
```

Run manually (inside project):

```powershell
sbt test
sbt test -v
```

### Test Runner Behavior

- `sbt test` runs all `*Spec.scala` and `*Test.scala` files in `src/test/scala/`.
- Tests use ScalaTest framework; ensure `scalatest` is in your `build.sbt` dependencies.
- `sbt test -v` provides verbose output with individual test results.

## Testing Guide (Beginner)

Start with ScalaTest and one simple behavior test.

Example `src/test/scala/CalcSpec.scala`:

```scala
import org.scalatest.funsuite.AnyFunSuite

object Calc:
	def add(a: Int, b: Int): Int = a + b

class CalcSpec extends AnyFunSuite:
	test("add returns the sum") {
		assert(Calc.add(2, 3) == 5)
	}
```

Run tests:

```powershell
sbt test
```

Testing checklist:

- Use clear test names that describe behavior.
- Keep pure logic in small methods to simplify testing.
- Add edge-case tests (empty collections, negative numbers, overflow-sensitive paths).

Recommended real-life project layout:

- `build.sbt`
- `project/build.properties`
- `src/main/scala/...`
- `src/test/scala/...` (optional)

Default runner behavior:

- Uses `sbt run` when `build.sbt` is present (and requires sbt).
- Else uses `scala-cli run .` when available.
- Else falls back to `scalac` + `scala` and expects a discoverable main object.

Use `playground.json` for custom command flows.

## Manual Build Guidance

From a mini project folder that has `build.sbt`:

```powershell
sbt compile
sbt run

# Run unit tests (ScalaTest via sbt)
sbt test
```
