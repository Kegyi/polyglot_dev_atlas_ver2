# Codes registry — common

This file contains code snippets exported from content/codes_registry.json.
Edit this file and run `scripts/update_registry_from_md.py` to push changes back.

## classes_and_objects

- Docs: /content/docs/classes_and_objects/README.md

<!-- REGISTRY_PATH: classes_and_objects.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

class Person {
public:
    Person(std::string name, int age) : name_(std::move(name)), age_(age) {}

    std::string describe() const {
        return name_ + " is " + std::to_string(age_) + " years old";
    }

    void birthday() {
        ++age_;
    }

private:
    std::string name_;
    int age_;
};

int main() {
    Person person("Alice", 29);
    std::cout << person.describe() << "\n";
    person.birthday();
    std::cout << person.describe() << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: classes_and_objects.languages.go -->
### go

```go
package main

import "fmt"

type Person struct {
	Name string
	Age  int
}

func (person Person) Describe() string {
	return fmt.Sprintf("%s is %d years old", person.Name, person.Age)
}

func (person *Person) Birthday() {
	person.Age++
}

func main() {
	person := Person{Name: "Alice", Age: 29}
	fmt.Println(person.Describe())
	person.Birthday()
	fmt.Println(person.Describe())
}
```

<!-- REGISTRY_PATH: classes_and_objects.languages.python -->
### python

```python
#!/usr/bin/env python3
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def describe(self) -> str:
        return f"{self.name} is {self.age} years old"

    def birthday(self) -> None:
        self.age += 1


def main() -> None:
    person = Person("Alice", 29)
    print(person.describe())
    person.birthday()
    print(person.describe())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: classes_and_objects.languages.scala -->
### scala

```scala
class Person(var name: String, var age: Int) {
  def describe(): String = s"$name is $age years old"

  def birthday(): Unit = {
    age += 1
  }
}

object ClassesAndObjectsBasics {
  def main(args: Array[String]): Unit = {
    val person = new Person("Alice", 29)
    println(person.describe())
    person.birthday()
    println(person.describe())
  }
}
```

<!-- REGISTRY_PATH: classes_and_objects.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

class Person {
  constructor(public name: string, public age: number) {}

  describe(): string {
    return `${this.name} is ${this.age} years old`;
  }

  birthday(): void {
    this.age += 1;
  }
}

function main(): void {
  const person = new Person("Alice", 29);
  console.log(person.describe());
  person.birthday();
  console.log(person.describe());
}

main();
setImmediate(() => {});
```

## collections_generics

- Docs: /content/docs/collections_generics/README.md

<!-- REGISTRY_PATH: collections_generics.languages.cpp -->
### cpp

```cpp
// Common baseline
std::vector<int> nums{1,2,3};
```

<!-- REGISTRY_PATH: collections_generics.languages.go -->
### go

```go
nums := []int{1,2,3}
```

<!-- REGISTRY_PATH: collections_generics.languages.python -->
### python

```python
nums = [1,2,3]
```

<!-- REGISTRY_PATH: collections_generics.languages.scala -->
### scala

```scala
object CollectionsGenerics {
  def main(args: Array[String]): Unit = {
    val nums = Seq(1, 2, 3)
    val doubled = nums.map(_ * 2)
    val evens = doubled.filter(_ % 2 == 0)
    println(s"sum of evens in doubled: ${evens.sum}")
  }
}
```

<!-- REGISTRY_PATH: collections_generics.languages.typescript -->
### typescript

```typescript
const nums: number[] = [1,2,3]
```

## command_line_args

- Docs: /content/docs/command_line_args/README.md

<!-- REGISTRY_PATH: command_line_args.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

int main(int argc, char** argv) {
    std::string name = argc > 1 ? argv[1] : "world";
    bool excited = argc > 2 && std::string(argv[2]) == "--excited";

    std::cout << "Hello, " << name;
    if (excited) {
        std::cout << "!";
    }
    std::cout << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: command_line_args.languages.go -->
### go

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	name := "world"
	if len(os.Args) > 1 {
		name = os.Args[1]
	}

	excited := len(os.Args) > 2 && os.Args[2] == "--excited"
	message := fmt.Sprintf("Hello, %s", name)
	if excited {
		message += "!"
	}

	fmt.Println(message)
}
```

<!-- REGISTRY_PATH: command_line_args.languages.python -->
### python

```python
#!/usr/bin/env python3
import sys


def main() -> None:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    excited = len(sys.argv) > 2 and sys.argv[2] == "--excited"

    message = f"Hello, {name}"
    if excited:
        message += "!"
    print(message)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: command_line_args.languages.scala -->
### scala

```scala
object CommandLineArgsBasics {
  def main(args: Array[String]): Unit = {
    val name = if (args.nonEmpty) args(0) else "world"
    val excited = args.contains("--excited")

    val suffix = if (excited) "!" else ""
    println(s"Hello, $name$suffix")
  }
}
```

<!-- REGISTRY_PATH: command_line_args.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const args = process.argv.slice(2);
  const name = args[0] ?? "world";
  const excited = args.includes("--excited");

  let message = `Hello, ${name}`;
  if (excited) {
    message += "!";
  }

  console.log(message);
}

main();
setImmediate(() => {});
```

## conditions

- Docs: /content/docs/conditions/README.md

<!-- REGISTRY_PATH: conditions.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

std::string grade_to_label(int grade) {
    if (grade >= 90) {
        return "excellent";
    } else if (grade >= 75) {
        return "good";
    } else if (grade >= 60) {
        return "pass";
    }
    return "fail";
}

int main() {
    const int grade = 82;
    const int code = 2;

    std::cout << "if/else result: " << grade_to_label(grade) << "\n";

    switch (code) {
        case 1:
            std::cout << "switch: created\n";
            break;
        case 2:
            std::cout << "switch: updated\n";
            break;
        case 3:
            std::cout << "switch: deleted\n";
            break;
        default:
            std::cout << "switch: unknown\n";
            break;
    }

    bool ready = grade >= 60;
    std::cout << "ternary: " << (ready ? "can continue" : "needs retry") << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: conditions.languages.go -->
### go

```go
package main

import "fmt"

func gradeToLabel(grade int) string {
	if grade >= 90 {
		return "excellent"
	} else if grade >= 75 {
		return "good"
	} else if grade >= 60 {
		return "pass"
	}
	return "fail"
}

func main() {
	grade := 82
	code := 2

	fmt.Println("if/else:", gradeToLabel(grade))

	switch code {
	case 1:
		fmt.Println("switch: created")
	case 2:
		fmt.Println("switch: updated")
	case 3:
		fmt.Println("switch: deleted")
	default:
		fmt.Println("switch: unknown")
	}

	ready := grade >= 60
	if ready {
		fmt.Println("decision: can continue")
	} else {
		fmt.Println("decision: needs retry")
	}
}
```

<!-- REGISTRY_PATH: conditions.languages.python -->
### python

```python
#!/usr/bin/env python3

def grade_to_label(grade: int) -> str:
    if grade >= 90:
        return "excellent"
    if grade >= 75:
        return "good"
    if grade >= 60:
        return "pass"
    return "fail"


def main() -> None:
    grade = 82
    code = 2

    print("if/elif/else:", grade_to_label(grade))

    match code:
        case 1:
            print("match: created")
        case 2:
            print("match: updated")
        case 3:
            print("match: deleted")
        case _:
            print("match: unknown")

    ready = grade >= 60
    print("conditional expression:", "can continue" if ready else "needs retry")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: conditions.languages.scala -->
### scala

```scala
object ConditionsBasics {
  def gradeToLabel(grade: Int): String = {
    if (grade >= 90) "excellent"
    else if (grade >= 75) "good"
    else if (grade >= 60) "pass"
    else "fail"
  }

  def main(args: Array[String]): Unit = {
    val grade = 82
    val code = 2

    println(s"if/else: ${gradeToLabel(grade)}")

    code match {
      case 1 => println("match: created")
      case 2 => println("match: updated")
      case 3 => println("match: deleted")
      case _ => println("match: unknown")
    }

    val message = if (grade >= 60) "can continue" else "needs retry"
    println(s"if-expression: $message")
  }
}
```

<!-- REGISTRY_PATH: conditions.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function gradeToLabel(grade: number): string {
  if (grade >= 90) return "excellent";
  if (grade >= 75) return "good";
  if (grade >= 60) return "pass";
  return "fail";
}

function main(): void {
  const grade = 82;
  const code = 2;

  console.log("if/else:", gradeToLabel(grade));

  switch (code) {
    case 1:
      console.log("switch: created");
      break;
    case 2:
      console.log("switch: updated");
      break;
    case 3:
      console.log("switch: deleted");
      break;
    default:
      console.log("switch: unknown");
  }

  const ready = grade >= 60;
  console.log("ternary:", ready ? "can continue" : "needs retry");
}

main();
setImmediate(() => {});
```

## dates_and_time

- Docs: /content/docs/dates_and_time/README.md

<!-- REGISTRY_PATH: dates_and_time.languages.cpp -->
### cpp

```cpp
#include <chrono>
#include <iostream>

int main() {
    using namespace std::chrono;

    const auto now = system_clock::now();
    const auto later = now + minutes(90);
    const auto now_seconds = duration_cast<seconds>(now.time_since_epoch()).count();
    const auto later_seconds = duration_cast<seconds>(later.time_since_epoch()).count();

    std::cout << "now (epoch seconds): " << now_seconds << "\n";
    std::cout << "later (epoch seconds): " << later_seconds << "\n";
    std::cout << "later > now: " << (later > now) << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: dates_and_time.languages.go -->
### go

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	now := time.Now()
	later := now.Add(90 * time.Minute)

	fmt.Println("now:", now.Format(time.RFC3339))
	fmt.Println("later:", later.Format(time.RFC3339))
	fmt.Println("later > now:", later.After(now))
}
```

<!-- REGISTRY_PATH: dates_and_time.languages.python -->
### python

```python
#!/usr/bin/env python3
from datetime import datetime, timedelta


def main() -> None:
    now = datetime.now()
    later = now + timedelta(minutes=90)

    print("now:", now.isoformat(timespec="seconds"))
    print("later:", later.isoformat(timespec="seconds"))
    print("later > now:", later > now)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: dates_and_time.languages.scala -->
### scala

```scala
import java.time.LocalDateTime

object DatesAndTimeBasics {
  def main(args: Array[String]): Unit = {
    val now = LocalDateTime.now()
    val later = now.plusMinutes(90)

    println(s"now: $now")
    println(s"later: $later")
    println(s"later > now: ${later.isAfter(now)}")
  }
}
```

<!-- REGISTRY_PATH: dates_and_time.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const now = new Date();
  const later = new Date(now.getTime() + 90 * 60 * 1000);

  console.log("now:", now.toISOString());
  console.log("later:", later.toISOString());
  console.log("later > now:", later > now);
}

main();
setImmediate(() => {});
```

## enums_and_constants

- Docs: /content/docs/enums_and_constants/README.md

<!-- REGISTRY_PATH: enums_and_constants.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

enum class Status {
    Pending,
    Running,
    Done,
};

constexpr int kMaxRetries = 3;

std::string to_string(Status status) {
    switch (status) {
        case Status::Pending:
            return "pending";
        case Status::Running:
            return "running";
        case Status::Done:
            return "done";
    }
    return "unknown";
}

int main() {
    Status status = Status::Running;
    std::cout << "status: " << to_string(status) << "\n";
    std::cout << "max retries: " << kMaxRetries << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: enums_and_constants.languages.go -->
### go

```go
package main

import "fmt"

type Status int

const (
	Pending Status = iota
	Running
	Done
)

const MaxRetries = 3

func (status Status) String() string {
	switch status {
	case Pending:
		return "pending"
	case Running:
		return "running"
	case Done:
		return "done"
	default:
		return "unknown"
	}
}

func main() {
	status := Running
	fmt.Println("status:", status.String())
	fmt.Println("max retries:", MaxRetries)
}
```

<!-- REGISTRY_PATH: enums_and_constants.languages.python -->
### python

```python
#!/usr/bin/env python3
from enum import Enum


class Status(Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"


MAX_RETRIES = 3


def main() -> None:
    status = Status.RUNNING
    print("status:", status.value)
    print("max retries:", MAX_RETRIES)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: enums_and_constants.languages.scala -->
### scala

```scala
object Status extends Enumeration {
  type Status = Value
  val Pending, Running, Done = Value
}

object EnumsAndConstantsBasics {
  val MaxRetries = 3

  def main(args: Array[String]): Unit = {
    val status = Status.Running
    println(s"status: ${status.toString.toLowerCase}")
    println(s"max retries: $MaxRetries")
  }
}
```

<!-- REGISTRY_PATH: enums_and_constants.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

enum Status {
  Pending = "pending",
  Running = "running",
  Done = "done",
}

const MAX_RETRIES = 3;

function main(): void {
  const status = Status.Running;
  console.log("status:", status);
  console.log("max retries:", MAX_RETRIES);
}

main();
setImmediate(() => {});
```

## environment_variables

- Docs: /content/docs/environment_variables/README.md

<!-- REGISTRY_PATH: environment_variables.languages.cpp -->
### cpp

```cpp
#include <cstdlib>
#include <iostream>
#include <string>

int main() {
    const char* mode_raw = std::getenv("APP_MODE");
    const char* port_raw = std::getenv("APP_PORT");

    std::string mode = mode_raw ? mode_raw : "development";
    std::string port = port_raw ? port_raw : "8080";

    std::cout << "mode: " << mode << "\n";
    std::cout << "port: " << port << "\n";
    std::cout << "has APP_MODE: " << (mode_raw != nullptr) << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: environment_variables.languages.go -->
### go

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	mode, hasMode := os.LookupEnv("APP_MODE")
	if !hasMode {
		mode = "development"
	}

	port, hasPort := os.LookupEnv("APP_PORT")
	if !hasPort {
		port = "8080"
	}

	fmt.Println("mode:", mode)
	fmt.Println("port:", port)
	fmt.Println("has APP_MODE:", hasMode)
}
```

<!-- REGISTRY_PATH: environment_variables.languages.python -->
### python

```python
#!/usr/bin/env python3
import os


def main() -> None:
    mode = os.getenv("APP_MODE", "development")
    port = os.getenv("APP_PORT", "8080")

    print("mode:", mode)
    print("port:", port)
    print("has APP_MODE:", "APP_MODE" in os.environ)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: environment_variables.languages.scala -->
### scala

```scala
object EnvironmentVariablesBasics {
  def main(args: Array[String]): Unit = {
    val env = sys.env
    val mode = env.getOrElse("APP_MODE", "development")
    val port = env.getOrElse("APP_PORT", "8080")

    println(s"mode: $mode")
    println(s"port: $port")
    println(s"has APP_MODE: ${env.contains("APP_MODE")}")
  }
}
```

<!-- REGISTRY_PATH: environment_variables.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const mode = process.env.APP_MODE ?? "development";
  const port = process.env.APP_PORT ?? "8080";

  console.log("mode:", mode);
  console.log("port:", port);
  console.log("has APP_MODE:", process.env.APP_MODE !== undefined);
}

main();
setImmediate(() => {});
```

## exceptions_and_recovery

- Docs: /content/docs/exceptions_and_recovery/README.md

<!-- REGISTRY_PATH: exceptions_and_recovery.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

int parse_port(const std::string& value) {
    return std::stoi(value);
}

int main() {
    try {
        int port = parse_port("not-a-number");
        std::cout << "port: " << port << "\n";
    } catch (const std::exception& ex) {
        std::cout << "parse failed: " << ex.what() << "\n";
        std::cout << "fallback port: 8080\n";
    }

    std::cout << "program continues\n";
    return 0;
}
```

<!-- REGISTRY_PATH: exceptions_and_recovery.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strconv"
)

func parsePort(value string) (int, error) {
	return strconv.Atoi(value)
}

func main() {
	port, err := parsePort("not-a-number")
	if err != nil {
		fmt.Println("parse failed:", err)
		fmt.Println("fallback port:", 8080)
	} else {
		fmt.Println("port:", port)
	}

	fmt.Println("program continues")
}
```

<!-- REGISTRY_PATH: exceptions_and_recovery.languages.python -->
### python

```python
#!/usr/bin/env python3


def parse_port(value: str) -> int:
    return int(value)


def main() -> None:
    try:
        port = parse_port("not-a-number")
        print("port:", port)
    except ValueError as error:
        print("parse failed:", error)
        print("fallback port:", 8080)

    print("program continues")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: exceptions_and_recovery.languages.scala -->
### scala

```scala
import scala.util.Try

object ExceptionsAndRecoveryBasics {
  def parsePort(value: String): Int = value.toInt

  def main(args: Array[String]): Unit = {
    val result = Try(parsePort("not-a-number"))

    result.fold(
      error => {
        println(s"parse failed: ${error.getMessage}")
        println("fallback port: 8080")
      },
      port => println(s"port: $port")
    )

    println("program continues")
  }
}
```

<!-- REGISTRY_PATH: exceptions_and_recovery.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function parsePort(value: string): number {
  const parsed = Number(value);
  if (!Number.isFinite(parsed)) {
    throw new Error("invalid port");
  }
  return parsed;
}

function main(): void {
  try {
    const port = parsePort("not-a-number");
    console.log("port:", port);
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.log("parse failed:", message);
    console.log("fallback port:", 8080);
  }

  console.log("program continues");
}

main();
setImmediate(() => {});
```

## exercise_array_reverse

<!-- REGISTRY_PATH: exercise_array_reverse.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> arr = {1, 2, 3, 4, 5};
    std::reverse(arr.begin(), arr.end());
    
    for (int x : arr) {
        std::cout << x << " ";
    }
    std::cout << "\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_array_reverse.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    arr := []int{1, 2, 3, 4, 5}
    for i, j := 0, len(arr)-1; i < j; i, j = i+1, j-1 {
        arr[i], arr[j] = arr[j], arr[i]
    }
    fmt.Println(arr)
}
```

<!-- REGISTRY_PATH: exercise_array_reverse.languages.python -->
### python

```python
arr = [1, 2, 3, 4, 5]
arr.reverse()  # or arr = arr[::-1]
print(arr)
```

<!-- REGISTRY_PATH: exercise_array_reverse.languages.scala2 -->
### scala2

```scala2
val arr = List(1, 2, 3, 4, 5)
val reversed = arr.reverse
println(reversed)
```

<!-- REGISTRY_PATH: exercise_array_reverse.languages.scala3 -->
### scala3

```scala3
val arr = List(1, 2, 3, 4, 5)
val reversed = arr.reverse
println(reversed)
```

<!-- REGISTRY_PATH: exercise_array_reverse.languages.typescript -->
### typescript

```typescript
const arr = [1, 2, 3, 4, 5];
arr.reverse();
console.log(arr);
```

## exercise_even_odd

<!-- REGISTRY_PATH: exercise_even_odd.languages.cpp -->
### cpp

```cpp
#include <iostream>

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    
    if (n % 2 == 0)
        std::cout << n << " is even\
";
    else
        std::cout << n << " is odd\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_even_odd.languages.go -->
### go

```go
package main

import (
    "fmt"
)

func main() {
    var n int
    fmt.Print("Enter a number: ")
    fmt.Scan(&n)
    
    if n%2 == 0 {
        fmt.Printf("%d is even\
", n)
    } else {
        fmt.Printf("%d is odd\
", n)
    }
}
```

<!-- REGISTRY_PATH: exercise_even_odd.languages.python -->
### python

```python
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
```

<!-- REGISTRY_PATH: exercise_even_odd.languages.scala2 -->
### scala2

```scala2
val n = scala.io.StdIn.readInt()
if (n % 2 == 0) println(s"$n is even")
else println(s"$n is odd")
```

<!-- REGISTRY_PATH: exercise_even_odd.languages.scala3 -->
### scala3

```scala3
val n = scala.io.StdIn.readInt()
if n % 2 == 0 then println(s"$n is even")
else println(s"$n is odd")
```

<!-- REGISTRY_PATH: exercise_even_odd.languages.typescript -->
### typescript

```typescript
import * as readline from "readline";
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
rl.question("Enter a number: ", (input) => {
  const n = parseInt(input);
  console.log(n % 2 === 0 ? `${n} is even` : `${n} is odd`);
  rl.close();
});
```

## exercise_fibonacci

<!-- REGISTRY_PATH: exercise_fibonacci.languages.cpp -->
### cpp

```cpp
#include <iostream>

int main() {
    int n;
    std::cout << "Enter number of terms: ";
    std::cin >> n;
    
    long long a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        std::cout << a << " ";
        long long temp = a + b;
        a = b;
        b = temp;
    }
    std::cout << "\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_fibonacci.languages.go -->
### go

```go
package main
import ("fmt")
func main() {
    var n int
    fmt.Print("Enter number of terms: ")
    fmt.Scan(&n)
    a, b := 0, 1
    for i := 0; i < n; i++ {
        fmt.Print(a, " ")
        a, b = b, a+b
    }
    fmt.Println()
}
```

<!-- REGISTRY_PATH: exercise_fibonacci.languages.python -->
### python

```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

<!-- REGISTRY_PATH: exercise_fibonacci.languages.scala2 -->
### scala2

```scala2
val n = scala.io.StdIn.readInt()
var a = 0L
var b = 1L
for (_ <- 0 until n) {
  print(a + " ")
  val temp = a + b
  a = b
  b = temp
}
println()
```

<!-- REGISTRY_PATH: exercise_fibonacci.languages.scala3 -->
### scala3

```scala3
val n = scala.io.StdIn.readInt()
var a = 0L
var b = 1L
for _ <- 0 until n do
  print(a + " ")
  val temp = a + b
  a = b
  b = temp
println()
```

<!-- REGISTRY_PATH: exercise_fibonacci.languages.typescript -->
### typescript

```typescript
const n = parseInt(process.argv[2] || "10");
let a = 0, b = 1;
for (let i = 0; i < n; i++) {
  process.stdout.write(a + " ");
  [a, b] = [b, a + b];
}
console.log();
```

## exercise_fizzbuzz

<!-- REGISTRY_PATH: exercise_fizzbuzz.languages.cpp -->
### cpp

```cpp
#include <iostream>

int main() {
    for (int i = 1; i <= 100; ++i) {
        if (i % 15 == 0) std::cout << "FizzBuzz\
";
        else if (i % 3 == 0) std::cout << "Fizz\
";
        else if (i % 5 == 0) std::cout << "Buzz\
";
        else std::cout << i << "\
";
    }
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_fizzbuzz.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    for i := 1; i <= 100; i++ {
        switch {
        case i%15 == 0:
            fmt.Println("FizzBuzz")
        case i%3 == 0:
            fmt.Println("Fizz")
        case i%5 == 0:
            fmt.Println("Buzz")
        default:
            fmt.Println(i)
        }
    }
}
```

<!-- REGISTRY_PATH: exercise_fizzbuzz.languages.python -->
### python

```python
for i in range(1, 101):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)
```

<!-- REGISTRY_PATH: exercise_fizzbuzz.languages.scala2 -->
### scala2

```scala2
(1 to 100).foreach { i =>
  if (i % 15 == 0) println("FizzBuzz")
  else if (i % 3 == 0) println("Fizz")
  else if (i % 5 == 0) println("Buzz")
  else println(i)
}
```

<!-- REGISTRY_PATH: exercise_fizzbuzz.languages.scala3 -->
### scala3

```scala3
(1 to 100).foreach { i =>
  if i % 15 == 0 then println("FizzBuzz")
  else if i % 3 == 0 then println("Fizz")
  else if i % 5 == 0 then println("Buzz")
  else println(i)
}
```

<!-- REGISTRY_PATH: exercise_fizzbuzz.languages.typescript -->
### typescript

```typescript
for (let i = 1; i <= 100; i++) {
  if (i % 15 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

## exercise_hello_world

<!-- REGISTRY_PATH: exercise_hello_world.languages.cpp -->
### cpp

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_hello_world.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

<!-- REGISTRY_PATH: exercise_hello_world.languages.python -->
### python

```python
print("Hello, World!")
```

<!-- REGISTRY_PATH: exercise_hello_world.languages.scala2 -->
### scala2

```scala2
object Main extends App {
  println("Hello, World!")
}
```

<!-- REGISTRY_PATH: exercise_hello_world.languages.scala3 -->
### scala3

```scala3
@main def hello(): Unit =
  println("Hello, World!")
```

<!-- REGISTRY_PATH: exercise_hello_world.languages.typescript -->
### typescript

```typescript
console.log("Hello, World!");
```

## exercise_palindrome

<!-- REGISTRY_PATH: exercise_palindrome.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <cctype>
#include <iostream>
#include <string>

int main() {
    std::string s = "A man, a plan, a canal: Panama";
    std::string cleaned;
    for (char c : s) {
        if (std::isalnum(c)) {
            cleaned += std::tolower(c);
        }
    }
    
    bool isPalin = std::string(cleaned.rbegin(), cleaned.rend()) == cleaned;
    std::cout << (isPalin ? "Palindrome" : "Not a palindrome") << "\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_palindrome.languages.go -->
### go

```go
package main

import (
    "fmt"
    "regexp"
    "strings"
)

func main() {
    s := "A man, a plan, a canal: Panama"
    re := regexp.MustCompile(`[^a-zA-Z0-9]`)
    cleaned := strings.ToLower(re.ReplaceAllString(s, ""))
    
    rev := ""
    for _, c := range cleaned {
        rev = string(c) + rev
    }
    
    if cleaned == rev {
        fmt.Println("Palindrome")
    } else {
        fmt.Println("Not a palindrome")
    }
}
```

<!-- REGISTRY_PATH: exercise_palindrome.languages.python -->
### python

```python
s = "A man, a plan, a canal: Panama"
cleaned = "".join(c.lower() for c in s if c.isalnum())
is_palin = cleaned == cleaned[::-1]
print("Palindrome" if is_palin else "Not a palindrome")
```

<!-- REGISTRY_PATH: exercise_palindrome.languages.scala2 -->
### scala2

```scala2
val s = "A man, a plan, a canal: Panama"
val cleaned = s.filter(_.isLetterOrDigit).toLowerCase
val isPalin = cleaned == cleaned.reverse
println(if (isPalin) "Palindrome" else "Not a palindrome")
```

<!-- REGISTRY_PATH: exercise_palindrome.languages.scala3 -->
### scala3

```scala3
val s = "A man, a plan, a canal: Panama"
val cleaned = s.filter(_.isLetterOrDigit).toLowerCase
val isPalin = cleaned == cleaned.reverse
println(if isPalin then "Palindrome" else "Not a palindrome")
```

<!-- REGISTRY_PATH: exercise_palindrome.languages.typescript -->
### typescript

```typescript
const s = "A man, a plan, a canal: Panama";
const cleaned = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
const isPalin = cleaned === cleaned.split("").reverse().join("");
console.log(isPalin ? "Palindrome" : "Not a palindrome");
```

## exercise_parallel_aggregator

<!-- REGISTRY_PATH: exercise_parallel_aggregator.languages.cpp -->
### cpp

```cpp
#include <future>
#include <iostream>
#include <string>
#include <vector>

struct Result {
    std::string endpoint;
    bool ok;
    std::string payloadOrError;
};

Result fetch(const std::string& endpoint) {
    if (endpoint.find("fail") != std::string::npos) {
        return {endpoint, false, "timeout"};
    }
    return {endpoint, true, "{\"endpoint\":\"" + endpoint + "\"}"};
}

int main() {
    std::vector<std::string> endpoints{ "users", "orders", "fail-metrics" };
    std::vector<std::future<Result>> jobs;

    for (const auto& ep : endpoints) {
        jobs.push_back(std::async(std::launch::async, fetch, ep));
    }

    std::vector<std::string> data;
    std::vector<std::string> errors;

    for (auto& j : jobs) {
        Result r = j.get();
        if (r.ok) data.push_back(r.payloadOrError);
        else errors.push_back(r.endpoint + ": " + r.payloadOrError);
    }

    std::cout << "data=" << data.size() << ", errors=" << errors.size() << "\
";
}
```

<!-- REGISTRY_PATH: exercise_parallel_aggregator.languages.go -->
### go

```go
package main

import (
    "fmt"
    "strings"
    "sync"
)

type result struct {
    endpoint string
    ok       bool
    payload  string
}

func fetch(ep string) result {
    if strings.Contains(ep, "fail") {
        return result{ep, false, "timeout"}
    }
    return result{ep, true, fmt.Sprintf("{\"endpoint\":\"%s\"}", ep)}
}

func main() {
    endpoints := []string{"users", "orders", "fail-metrics"}
    ch := make(chan result, len(endpoints))
    var wg sync.WaitGroup

    for _, ep := range endpoints {
        wg.Add(1)
        go func(e string) {
            defer wg.Done()
            ch <- fetch(e)
        }(ep)
    }

    wg.Wait()
    close(ch)

    var data []string
    var errors []string
    for r := range ch {
        if r.ok {
            data = append(data, r.payload)
        } else {
            errors = append(errors, r.endpoint+": "+r.payload)
        }
    }

    fmt.Printf("data=%d errors=%d\
", len(data), len(errors))
}
```

<!-- REGISTRY_PATH: exercise_parallel_aggregator.languages.python -->
### python

```python
import asyncio

async def fetch(endpoint: str) -> tuple[str, bool, str]:
    await asyncio.sleep(0.05)
    if "fail" in endpoint:
        return endpoint, False, "timeout"
    return endpoint, True, f"{{\"endpoint\": \"{endpoint}\"}}"

async def main() -> None:
    endpoints = ["users", "orders", "fail-metrics"]
    results = await asyncio.gather(*(fetch(ep) for ep in endpoints), return_exceptions=False)

    data = [payload for _, ok, payload in results if ok]
    errors = [f"{ep}: {payload}" for ep, ok, payload in results if not ok]

    print({"data": data, "errors": errors})

asyncio.run(main())
```

<!-- REGISTRY_PATH: exercise_parallel_aggregator.languages.scala2 -->
### scala2

```scala2
import scala.concurrent._
import scala.concurrent.duration._
import ExecutionContext.Implicits.global

case class Result(endpoint: String, ok: Boolean, payload: String)

def fetch(endpoint: String): Future[Result] = Future {
  if (endpoint.contains("fail")) Result(endpoint, ok = false, "timeout")
  else Result(endpoint, ok = true, s"{\"endpoint\":\"$endpoint\"}")
}

object Main extends App {
  val endpoints = List("users", "orders", "fail-metrics")
  val results = Await.result(Future.sequence(endpoints.map(fetch)), 3.seconds)

  val data = results.collect { case Result(_, true, payload) => payload }
  val errors = results.collect { case Result(ep, false, payload) => s"$ep: $payload" }

  println(s"data=${data.size}, errors=${errors.size}")
}
```

<!-- REGISTRY_PATH: exercise_parallel_aggregator.languages.scala3 -->
### scala3

```scala3
import scala.concurrent.*
import scala.concurrent.duration.*
import scala.concurrent.ExecutionContext.Implicits.global

case class Result(endpoint: String, ok: Boolean, payload: String)

def fetch(endpoint: String): Future[Result] = Future {
  if endpoint.contains("fail") then Result(endpoint, ok = false, "timeout")
  else Result(endpoint, ok = true, s"{\"endpoint\":\"$endpoint\"}")
}

@main def main(): Unit =
  val endpoints = List("users", "orders", "fail-metrics")
  val results = Await.result(Future.sequence(endpoints.map(fetch)), 3.seconds)

  val data = results.collect { case Result(_, true, payload) => payload }
  val errors = results.collect { case Result(ep, false, payload) => s"$ep: $payload" }

  println(s"data=${data.size}, errors=${errors.size}")
```

<!-- REGISTRY_PATH: exercise_parallel_aggregator.languages.typescript -->
### typescript

```typescript
type Result = { endpoint: string; ok: boolean; payload: string };

async function fetchEndpoint(endpoint: string): Promise<Result> {
  await new Promise((r) => setTimeout(r, 50));
  if (endpoint.includes("fail")) return { endpoint, ok: false, payload: "timeout" };
  return { endpoint, ok: true, payload: JSON.stringify({ endpoint }) };
}

async function main() {
  const endpoints = ["users", "orders", "fail-metrics"];
  const results = await Promise.all(endpoints.map(fetchEndpoint));

  const data = results.filter(r => r.ok).map(r => r.payload);
  const errors = results.filter(r => !r.ok).map(r => `${r.endpoint}: ${r.payload}`);

  console.log({ data, errors });
}

void main();
```

## exercise_stream_processor

<!-- REGISTRY_PATH: exercise_stream_processor.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    std::vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8};
    
    auto sum = 0;
    std::for_each(nums.begin(), nums.end(), [&sum](int n) {
        if (n % 2 == 0) {
            sum += n * n;
        }
    });
    
    std::cout << "Sum of squares of even numbers: " << sum << "\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_stream_processor.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    nums := []int{1, 2, 3, 4, 5, 6, 7, 8}
    
    sum := 0
    for _, n := range nums {
        if n%2 == 0 {
            sum += n * n
        }
    }
    
    fmt.Printf("Sum of squares of even numbers: %d\
", sum)
}
```

<!-- REGISTRY_PATH: exercise_stream_processor.languages.python -->
### python

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum(n**2 for n in nums if n % 2 == 0)
print(f"Sum of squares of even numbers: {result}")
```

<!-- REGISTRY_PATH: exercise_stream_processor.languages.scala2 -->
### scala2

```scala2
val nums = List(1, 2, 3, 4, 5, 6, 7, 8)
val result = nums
  .filter(_ % 2 == 0)
  .map(n => n * n)
  .sum

println(s"Sum of squares of even numbers: $result")
```

<!-- REGISTRY_PATH: exercise_stream_processor.languages.scala3 -->
### scala3

```scala3
val nums = List(1, 2, 3, 4, 5, 6, 7, 8)
val result = nums
  .filter(_ % 2 == 0)
  .map(n => n * n)
  .sum

println(s"Sum of squares of even numbers: $result")
```

<!-- REGISTRY_PATH: exercise_stream_processor.languages.typescript -->
### typescript

```typescript
const nums = [1, 2, 3, 4, 5, 6, 7, 8];
const result = nums
  .filter(n => n % 2 === 0)
  .map(n => n * n)
  .reduce((a, b) => a + b, 0);

console.log(`Sum of squares of even numbers: ${result}`);
```

## exercise_temperature_converter

<!-- REGISTRY_PATH: exercise_temperature_converter.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <iomanip>

int main() {
    double celsius = 25.0;
    double fahrenheit = (celsius * 9/5) + 32;
    double kelvin = celsius + 273.15;
    
    std::cout << std::fixed << std::setprecision(2);
    std::cout << celsius << " deg C = " << fahrenheit << " deg F = " << kelvin << "K\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_temperature_converter.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    celsius := 25.0
    fahrenheit := (celsius * 9 / 5) + 32
    kelvin := celsius + 273.15
    
    fmt.Printf("%.2f deg C = %.2f deg F = %.2f K\
", celsius, fahrenheit, kelvin)
}
```

<!-- REGISTRY_PATH: exercise_temperature_converter.languages.python -->
### python

```python
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius} deg C = {fahrenheit:.2f} deg F = {kelvin:.2f}K")
```

<!-- REGISTRY_PATH: exercise_temperature_converter.languages.scala2 -->
### scala2

```scala2
val celsius = 25.0
val fahrenheit = (celsius * 9/5) + 32
val kelvin = celsius + 273.15

println(f"$celsius deg C = $fahrenheit%.2f deg F = $kelvin%.2f K")
```

<!-- REGISTRY_PATH: exercise_temperature_converter.languages.scala3 -->
### scala3

```scala3
val celsius = 25.0
val fahrenheit = (celsius * 9/5) + 32
val kelvin = celsius + 273.15

println(f"$celsius deg C = $fahrenheit%.2f deg F = $kelvin%.2f K")
```

<!-- REGISTRY_PATH: exercise_temperature_converter.languages.typescript -->
### typescript

```typescript
const celsius = 25.0;
const fahrenheit = (celsius * 9/5) + 32;
const kelvin = celsius + 273.15;

console.log(`${celsius} deg C = ${fahrenheit.toFixed(2)} deg F = ${kelvin.toFixed(2)}K`);
```

## exercise_tree_traversal

<!-- REGISTRY_PATH: exercise_tree_traversal.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct Node {
    int val;
    Node* left;
    Node* right;
    Node(int v) : val(v), left(nullptr), right(nullptr) {}
};

void inorder(Node* root, std::vector<int>& res) {
    if (!root) return;
    inorder(root->left, res);
    res.push_back(root->val);
    inorder(root->right, res);
}

int main() {
    Node* root = new Node(1);
    root->left = new Node(2);
    root->right = new Node(3);
    root->left->left = new Node(4);
    
    std::vector<int> res;
    inorder(root, res);
    
    for (int x : res) std::cout << x << " ";
    std::cout << "\
";
    return 0;
}
```

<!-- REGISTRY_PATH: exercise_tree_traversal.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
    val   int
    left  *Node
    right *Node
}

func inorder(root *Node, res *[]int) {
    if root == nil {
        return
    }
    inorder(root.left, res)
    *res = append(*res, root.val)
    inorder(root.right, res)
}

func main() {
    root := &Node{val: 1}
    root.left = &Node{val: 2}
    root.right = &Node{val: 3}
    root.left.left = &Node{val: 4}
    
    var res []int
    inorder(root, &res)
    fmt.Println(res)
}
```

<!-- REGISTRY_PATH: exercise_tree_traversal.languages.python -->
### python

```python
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root, res):
    if not root:
        return
    inorder(root.left, res)
    res.append(root.val)
    inorder(root.right, res)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)

res = []
inorder(root, res)
print(res)
```

<!-- REGISTRY_PATH: exercise_tree_traversal.languages.scala2 -->
### scala2

```scala2
case class Node(val: Int, var left: Option[Node] = None, var right: Option[Node] = None)

def inorder(root: Option[Node], res: scala.collection.mutable.Buffer[Int]): Unit = {
  root.foreach { node =>
    inorder(node.left, res)
    res += node.val
    inorder(node.right, res)
  }
}

val root = Node(1, Some(Node(2, Some(Node(4)))), Some(Node(3)))
val res = scala.collection.mutable.Buffer[Int]()
inorder(Some(root), res)
println(res)
```

<!-- REGISTRY_PATH: exercise_tree_traversal.languages.scala3 -->
### scala3

```scala3
case class Node(val: Int, var left: Option[Node] = None, var right: Option[Node] = None)

def inorder(root: Option[Node], res: scala.collection.mutable.Buffer[Int]): Unit =
  root.foreach { node =>
    inorder(node.left, res)
    res += node.val
    inorder(node.right, res)
  }

val root = Node(1, Some(Node(2, Some(Node(4)))), Some(Node(3)))
val res = scala.collection.mutable.Buffer[Int]()
inorder(Some(root), res)
println(res)
```

<!-- REGISTRY_PATH: exercise_tree_traversal.languages.typescript -->
### typescript

```typescript
class Node {
  val: number;
  left: Node | null;
  right: Node | null;
  constructor(val: number) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

function inorder(root: Node | null, res: number[]): void {
  if (!root) return;
  inorder(root.left, res);
  res.push(root.val);
  inorder(root.right, res);
}

const root = new Node(1);
root.left = new Node(2);
root.right = new Node(3);
root.left.left = new Node(4);

const res: number[] = [];
inorder(root, res);
console.log(res);
```

## exercise_word_frequency

<!-- REGISTRY_PATH: exercise_word_frequency.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <cctype>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

int main() {
    std::string line = "This is a test. This test is simple.";
    for (char& c : line) {
        if (std::ispunct(static_cast<unsigned char>(c))) c = ' ';
        else c = static_cast<char>(std::tolower(static_cast<unsigned char>(c)));
    }

    std::unordered_map<std::string, int> freq;
    std::istringstream in(line);
    std::string word;
    while (in >> word) freq[word]++;

    std::vector<std::pair<std::string, int>> items(freq.begin(), freq.end());
    std::sort(items.begin(), items.end(), [](auto& a, auto& b) {
        return a.second == b.second ? a.first < b.first : a.second > b.second;
    });

    for (const auto& [w, n] : items) {
        std::cout << w << ": " << n << "\
";
    }
}
```

<!-- REGISTRY_PATH: exercise_word_frequency.languages.go -->
### go

```go
package main

import (
    "fmt"
    "regexp"
    "sort"
    "strings"
)

func main() {
    text := "This is a test. This test is simple."
    re := regexp.MustCompile(`[A-Za-z]+`)
    words := re.FindAllString(strings.ToLower(text), -1)

    freq := map[string]int{}
    for _, w := range words {
        freq[w]++
    }

    type pair struct {
        word  string
        count int
    }

    items := make([]pair, 0, len(freq))
    for w, c := range freq {
        items = append(items, pair{w, c})
    }

    sort.Slice(items, func(i, j int) bool {
        if items[i].count == items[j].count {
            return items[i].word < items[j].word
        }
        return items[i].count > items[j].count
    })

    for _, it := range items {
        fmt.Printf("%s: %d\
", it.word, it.count)
    }
}
```

<!-- REGISTRY_PATH: exercise_word_frequency.languages.python -->
### python

```python
from collections import Counter
import re

text = "This is a test. This test is simple."
words = re.findall(r"[a-zA-Z]+", text.lower())
counts = Counter(words)

for word, count in sorted(counts.items(), key=lambda p: (-p[1], p[0])):
    print(f"{word}: {count}")
```

<!-- REGISTRY_PATH: exercise_word_frequency.languages.scala2 -->
### scala2

```scala2
object Main extends App {
  val text = "This is a test. This test is simple."
  val words = "[A-Za-z]+".r.findAllIn(text.toLowerCase).toList
  val counts = words.groupBy(identity).view.mapValues(_.size).toMap

  counts.toList
    .sortBy { case (w, c) => (-c, w) }
    .foreach { case (w, c) => println(s"$w: $c") }
}
```

<!-- REGISTRY_PATH: exercise_word_frequency.languages.scala3 -->
### scala3

```scala3
@main def main(): Unit =
  val text = "This is a test. This test is simple."
  val words = "[A-Za-z]+".r.findAllIn(text.toLowerCase).toList
  val counts = words.groupBy(identity).view.mapValues(_.size).toMap

  counts.toList
    .sortBy((w, c) => (-c, w))
    .foreach((w, c) => println(s"$w: $c"))
```

<!-- REGISTRY_PATH: exercise_word_frequency.languages.typescript -->
### typescript

```typescript
const text = "This is a test. This test is simple.";
const words = (text.toLowerCase().match(/[a-z]+/g) ?? []);

const freq = new Map<string, number>();
for (const w of words) {
  freq.set(w, (freq.get(w) ?? 0) + 1);
}

const items = [...freq.entries()]
  .sort((a, b) => b[1] - a[1] || a[0].localeCompare(b[0]));

for (const [word, count] of items) {
  console.log(`${word}: ${count}`);
}
```

## file_aggregate

- Docs: /content/docs/file_aggregate/README.md

<!-- REGISTRY_PATH: file_aggregate.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <numeric>
#include <algorithm>
#include <future>
#include <stdexcept>
#include <optional>

struct Record {
    std::string name;
    int score;
};

class FileProcessor {
public:
    explicit FileProcessor(const std::string& path) : path_(path) {}
    std::vector<Record> readAll() const {
        std::ifstream in(path_);
        if (!in) throw std::runtime_error("unable to open file");
        std::vector<Record> out;
        std::string line;
        while (std::getline(in, line)) {
            if (line.empty() || line[0] == '#') continue;
            if (auto r = parseLine(line)) out.push_back(*r);
        }
        return out;
    }
private:
    std::string path_;
    static std::optional<Record> parseLine(const std::string& line) {
        std::istringstream iss(line);
        std::string name;
        int score;
        if (!std::getline(iss, name, ',')) return std::nullopt;
        if (!(iss >> score)) return std::nullopt;
        return Record{ name, score };
    }
};

static double average(const std::vector<int>& v) {
    if (v.empty()) return 0.0;
    return std::accumulate(v.begin(), v.end(), 0.0) / v.size();
}

int main(int argc, char** argv) {
    try {
        const std::string path = (argc > 1) ? argv[1] : "data.txt";
        FileProcessor fp(path);
        auto records = fp.readAll();

        std::map<std::string, std::vector<int>> buckets;
        for (const auto& r : records) buckets[r.name].push_back(r.score);

        std::vector<std::future<std::pair<std::string, double>>> futures;
        for (const auto& p : buckets) {
            auto name = p.first;
            auto scores = p.second;
            futures.push_back(std::async(std::launch::async,
                [name, scores]() {
                    return std::make_pair(name,
                        average(scores));
                }));
        }

        std::vector<std::pair<std::string, double>> results;
        for (auto& f : futures) results.push_back(f.get());

        std::sort(results.begin(), results.end(),
            [](const auto& a, const auto& b){ return a.second > b.second; });

        for (const auto& r : results) {
            std::cout << r.first << ": " << r.second << std::endl;
        }
    } catch (const std::exception& ex) {
        std::cerr << "Error: " << ex.what() << std::endl;
        return 1;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: file_aggregate.languages.go -->
### go

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "strconv"
    "strings"
    "sync"
    "sort"
)

type Record struct {
    Name  string
    Score int
}

func readAll(path string) ([]Record, error) {
    f, err := os.Open(path)
    if err != nil {
        return nil, err
    }
    defer f.Close()
    var out []Record
    scanner := bufio.NewScanner(f)
    for scanner.Scan() {
        line := strings.TrimSpace(scanner.Text())
        if line == "" || strings.HasPrefix(line, "#") {
            continue
        }
        parts := strings.SplitN(line, ",", 2)
        if len(parts) != 2 {
            continue
        }
        name := strings.TrimSpace(parts[0])
        s := strings.TrimSpace(parts[1])
        score, err := strconv.Atoi(s)
        if err != nil {
            continue
        }
        out = append(out, Record{name, score})
    }
    if err := scanner.Err(); err != nil {
        return nil, err
    }
    return out, nil
}

func average(nums []int) float64 {
    if len(nums) == 0 {
        return 0
    }
    sum := 0
    for _, v := range nums {
        sum += v
    }
    return float64(sum) / float64(len(nums))
}

func main() {
    path := "data.txt"
    if len(os.Args) > 1 {
        path = os.Args[1]
    }
    records, err := readAll(path)
    if err != nil {
        fmt.Println("Error:", err)
        os.Exit(1)
    }

    buckets := map[string][]int{}
    for _, r := range records {
        buckets[r.Name] = append(buckets[r.Name], r.Score)
    }

    type Res struct {
        Name string
        Avg  float64
    }

    var wg sync.WaitGroup
    ch := make(chan Res, len(buckets))
    for name, scores := range buckets {
        wg.Add(1)
        go func(n string, s []int) {
            defer wg.Done()
            ch <- Res{n, average(s)}
        }(name, scores)
    }
    wg.Wait()
    close(ch)

    var results []Res
    for r := range ch {
        results = append(results, r)
    }

    sort.Slice(results, func(i, j int) bool { return results[i].Avg > results[j].Avg })
    for _, r := range results {
        fmt.Printf("%s: %.2f\n", r.Name, r.Avg)
    }
}
```

<!-- REGISTRY_PATH: file_aggregate.languages.python -->
### python

```python
#!/usr/bin/env python3
from dataclasses import dataclass
from typing import List, Dict
from concurrent.futures import ThreadPoolExecutor
import statistics
import sys

@dataclass
class Record:
    name: str
    score: int

class FileProcessor:
    def __init__(self, path: str):
        self.path = path

    def read_all(self) -> List[Record]:
        records: List[Record] = []
        with open(self.path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                try:
                    name, s = [x.strip() for x in line.split(",", 1)]
                    score = int(s)
                    records.append(Record(name, score))
                except Exception:
                    continue
        return records


def average(scores: List[int]) -> float:
    return statistics.mean(scores) if scores else 0.0


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data.txt"
    fp = FileProcessor(path)
    try:
        records = fp.read_all()
        buckets: Dict[str, List[int]] = {}
        for r in records:
            buckets.setdefault(r.name, []).append(r.score)

        results = []
        with ThreadPoolExecutor() as ex:
            futures = {ex.submit(average, scores): name for name, scores in buckets.items()}
            for fut in futures:
                name = futures[fut]
                results.append((name, fut.result()))

        results.sort(key=lambda x: x[1], reverse=True)
        for name, avg in results:
            print(f"{name}: {avg:.2f}")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: file_aggregate.languages.scala -->
### scala

```scala
import scala.io.Source
import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.Duration
import scala.util.{Try, Success, Failure}

case class Record(name: String, score: Int)

object FileProcessor {
  def readAll(path: String): List[Record] = {
    val src = Source.fromFile(path)
    try {
      src.getLines().toList.flatMap { raw =>
        val line = raw.trim
        if (line.isEmpty || line.startsWith("#")) None
        else {
          line.split(",", 2).toList match {
            case name :: s :: Nil =>
              Try(s.trim.toInt) match {
                case Success(v) => Some(Record(name.trim, v))
                case Failure(_) => None
              }
            case _ => None
          }
        }
      }
    } finally {
      src.close()
    }
  }
}

object Main extends App {
  val path = if (args.nonEmpty) args(0) else "data.txt"
  try {
    val records = FileProcessor.readAll(path)
    val buckets = records.groupBy(_.name).view.mapValues(_.map(_.score)).toMap
    val futures = buckets.map { case (name, scores) =>
      Future { (name, if (scores.isEmpty) 0.0 else scores.sum.toDouble / scores.size) }
    }
    val aggregated = Future.sequence(futures.toList).map(_.sortBy(-_._2))
    val results = Await.result(aggregated, Duration.Inf)
    results.foreach { case (name, avg) => println(f"$name: $avg%.2f") }
  } catch {
    case ex: Throwable => System.err.println(s"Error: ${ex.getMessage}"); System.exit(1)
  }
}
```

<!-- REGISTRY_PATH: file_aggregate.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node
import * as fs from "fs/promises";

type Record = { name: string; score: number };

class FileProcessor {
    path: string;
    constructor(path: string) {
        this.path = path;
    }

    async readAll(): Promise<Record[]> {
        const text = await fs.readFile(this.path, { encoding: "utf8" });
        const out: Record[] = [];
        for (const raw of text.split(/\r?\n/)) {
            const line = raw.trim();
            if (!line || line.startsWith("#")) continue;
            const parts = line.split(",", 2);
            if (parts.length < 2) continue;
            const name = parts[0].trim();
            const score = Number(parts[1].trim());
            if (Number.isNaN(score)) continue;
            out.push({ name, score });
        }
        return out;
    }
}

function average(nums: number[]): number {
    if (nums.length === 0) return 0;
    return nums.reduce((a, b) => a + b, 0) / nums.length;
}

async function main() {
    const path = process.argv[2] || "data.txt";
    try {
        const fp = new FileProcessor(path);
        const records = await fp.readAll();
        const buckets = new Map<string, number[]>();
        for (const r of records) {
            if (!buckets.has(r.name)) buckets.set(r.name, []);
            buckets.get(r.name)!.push(r.score);
        }

        const promises: Promise<[string, number]>[] = [];
        for (const [name, scores] of buckets.entries()) {
            promises.push(Promise.resolve([name, average(scores)]));
        }
        const results = (await Promise.all(promises)).sort((a, b) => b[1] - a[1]);
        for (const [name, avg] of results) {
            console.log(`${name}: ${avg.toFixed(2)}`);
        }
    } catch (err) {
        console.error("Error:", err);
        process.exit(1);
    }
}

main();
```

## file_io

- Docs: /content/docs/file_io/README.md

<!-- REGISTRY_PATH: file_io.languages.cpp -->
### cpp

```cpp
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main() {
    const std::string path = "file_io_demo.txt";

    {
        std::ofstream out(path);
        out << "apple\nbanana\ncarrot\n";
    }

    std::ifstream in(path);
    std::vector<std::string> lines;
    for (std::string line; std::getline(in, line);) {
        lines.push_back(line);
    }

    std::cout << "read lines: ";
    for (const auto& line : lines) {
        std::cout << line << ' ';
    }
    std::cout << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: file_io.languages.go -->
### go

```go
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	const path = "file_io_demo.txt"

	err := os.WriteFile(path, []byte("apple\nbanana\ncarrot\n"), 0o644)
	if err != nil {
		panic(err)
	}

	content, err := os.ReadFile(path)
	if err != nil {
		panic(err)
	}

	lines := strings.Fields(string(content))
	fmt.Println("read lines:", lines)
}
```

<!-- REGISTRY_PATH: file_io.languages.python -->
### python

```python
#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    path = Path("file_io_demo.txt")
    path.write_text("apple\nbanana\ncarrot\n", encoding="utf-8")

    lines = path.read_text(encoding="utf-8").splitlines()
    print("read lines:", lines)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: file_io.languages.scala -->
### scala

```scala
import java.nio.file.{Files, Path}
import scala.jdk.CollectionConverters._

object FileIOBasics {
  def main(args: Array[String]): Unit = {
    val path = Path.of("file_io_demo.txt")
    Files.writeString(path, "apple\nbanana\ncarrot\n")

    val lines = Files.readAllLines(path).asScala.toSeq
    println(s"read lines: $lines")
  }
}
```

<!-- REGISTRY_PATH: file_io.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";
import { promises as fs } from "fs";

async function main(): Promise<void> {
  const path = "file_io_demo.txt";
  await fs.writeFile(path, "apple\nbanana\ncarrot\n", "utf8");

  const content = await fs.readFile(path, "utf8");
  const lines = content.trim().split(/\r?\n/);
  console.log("read lines:", lines);
}

main()
  .then(() => setImmediate(() => {}))
  .catch((err) => {
    console.error("error:", err);
    process.exit(1);
  });
```

## file_paths_and_directories

- Docs: /content/docs/file_paths_and_directories/README.md

<!-- REGISTRY_PATH: file_paths_and_directories.languages.cpp -->
### cpp

```cpp
#include <filesystem>
#include <iostream>

int main() {
    namespace fs = std::filesystem;

    fs::path base = "demo_folder";
    fs::path file_path = base / "sub" / "data.txt";

    fs::create_directories(file_path.parent_path());

    std::cout << "file path: " << file_path.string() << "\n";
    std::cout << "parent path: " << file_path.parent_path().string() << "\n";
    std::cout << "directory exists: " << fs::exists(file_path.parent_path()) << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: file_paths_and_directories.languages.go -->
### go

```go
package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	base := "demo_folder"
	filePath := filepath.Join(base, "sub", "data.txt")
	parent := filepath.Dir(filePath)

	if err := os.MkdirAll(parent, 0o755); err != nil {
		panic(err)
	}

	fmt.Println("file path:", filePath)
	fmt.Println("parent path:", parent)
	fmt.Println("directory exists:", pathExists(parent))
}

func pathExists(path string) bool {
	_, err := os.Stat(path)
	return err == nil
}
```

<!-- REGISTRY_PATH: file_paths_and_directories.languages.python -->
### python

```python
#!/usr/bin/env python3
from pathlib import Path


def main() -> None:
    base = Path("demo_folder")
    file_path = base / "sub" / "data.txt"
    file_path.parent.mkdir(parents=True, exist_ok=True)

    print("file path:", file_path)
    print("parent path:", file_path.parent)
    print("directory exists:", file_path.parent.exists())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: file_paths_and_directories.languages.scala -->
### scala

```scala
import java.nio.file.{Files, Paths}

object FilePathsAndDirectoriesBasics {
  def main(args: Array[String]): Unit = {
    val filePath = Paths.get("demo_folder", "sub", "data.txt")
    val parent = filePath.getParent

    Files.createDirectories(parent)

    println(s"file path: $filePath")
    println(s"parent path: $parent")
    println(s"directory exists: ${Files.exists(parent)}")
  }
}
```

<!-- REGISTRY_PATH: file_paths_and_directories.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";
import { mkdirSync, existsSync } from "fs";
import path from "path";

function main(): void {
  const base = "demo_folder";
  const filePath = path.join(base, "sub", "data.txt");
  const parent = path.dirname(filePath);

  mkdirSync(parent, { recursive: true });

  console.log("file path:", filePath);
  console.log("parent path:", parent);
  console.log("directory exists:", existsSync(parent));
}

main();
setImmediate(() => {});
```

## functions_and_errors

- Docs: /content/docs/functions_and_errors/README.md

<!-- REGISTRY_PATH: functions_and_errors.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <optional>
#include <stdexcept>

int add(int a, int b) {
    return a + b;
}

std::optional<double> safe_div(double a, double b) {
    if (b == 0.0) {
        return std::nullopt;
    }
    return a / b;
}

int main() {
    std::cout << "add(2, 3): " << add(2, 3) << "\n";

    if (auto result = safe_div(10, 2)) {
        std::cout << "safe_div(10, 2): " << *result << "\n";
    }

    try {
        auto bad = safe_div(10, 0);
        if (!bad) {
            throw std::runtime_error("division by zero");
        }
    } catch (const std::exception& ex) {
        std::cerr << "error: " << ex.what() << "\n";
    }

    return 0;
}
```

<!-- REGISTRY_PATH: functions_and_errors.languages.go -->
### go

```go
package main

import (
	"errors"
	"fmt"
)

func add(a, b int) int {
	return a + b
}

func safeDiv(a, b float64) (float64, error) {
	if b == 0 {
		return 0, errors.New("division by zero")
	}
	return a / b, nil
}

func main() {
	fmt.Println("add(2, 3):", add(2, 3))

	if v, err := safeDiv(10, 2); err == nil {
		fmt.Println("safeDiv(10, 2):", v)
	}

	if _, err := safeDiv(10, 0); err != nil {
		fmt.Println("error:", err)
	}
}
```

<!-- REGISTRY_PATH: functions_and_errors.languages.python -->
### python

```python
#!/usr/bin/env python3
from typing import Optional


def add(a: int, b: int) -> int:
    return a + b


def safe_div(a: float, b: float) -> Optional[float]:
    if b == 0:
        return None
    return a / b


def strict_div(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def main() -> None:
    print("add(2, 3):", add(2, 3))
    print("safe_div(10, 2):", safe_div(10, 2))

    try:
        print("strict_div(10, 0):", strict_div(10, 0))
    except ValueError as err:
        print("error:", err)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: functions_and_errors.languages.scala -->
### scala

```scala
object FunctionsAndErrorsBasics {
  def add(a: Int, b: Int): Int = a + b

  def safeDiv(a: Double, b: Double): Option[Double] = {
    if (b == 0) None else Some(a / b)
  }

  def strictDiv(a: Double, b: Double): Double = {
    if (b == 0) throw new IllegalArgumentException("division by zero")
    a / b
  }

  def main(args: Array[String]): Unit = {
    println(s"add(2, 3): ${add(2, 3)}")
    println(s"safeDiv(10, 2): ${safeDiv(10, 2)}")

    try {
      println(s"strictDiv(10, 0): ${strictDiv(10, 0)}")
    } catch {
      case ex: IllegalArgumentException => println(s"error: ${ex.getMessage}")
    }
  }
}
```

<!-- REGISTRY_PATH: functions_and_errors.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function add(a: number, b: number): number {
  return a + b;
}

function safeDiv(a: number, b: number): number | null {
  if (b === 0) return null;
  return a / b;
}

function strictDiv(a: number, b: number): number {
  if (b === 0) throw new Error("division by zero");
  return a / b;
}

function main(): void {
  console.log("add(2, 3):", add(2, 3));
  console.log("safeDiv(10, 2):", safeDiv(10, 2));

  try {
    console.log("strictDiv(10, 0):", strictDiv(10, 0));
  } catch (err) {
    console.error("error:", err);
  }
}

main();
setImmediate(() => {});
```

## hashing_and_checksums

- Docs: /content/docs/hashing_and_checksums/README.md

<!-- REGISTRY_PATH: hashing_and_checksums.languages.cpp -->
### cpp

```cpp
#include <functional>
#include <iostream>
#include <numeric>
#include <string>

int main() {
    std::string text = "hello-world";

    std::size_t hash_value = std::hash<std::string>{}(text);
    int checksum = std::accumulate(text.begin(), text.end(), 0);

    std::cout << "text: " << text << "\n";
    std::cout << "hash: " << hash_value << "\n";
    std::cout << "checksum: " << checksum << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: hashing_and_checksums.languages.go -->
### go

```go
package main

import (
	"crypto/sha256"
	"fmt"
	"hash/crc32"
)

func main() {
	text := "hello-world"
	bytes := []byte(text)

	sha256Sum := sha256.Sum256(bytes)
	crc32Value := crc32.ChecksumIEEE(bytes)

	fmt.Println("text:", text)
	fmt.Printf("sha256: %x\n", sha256Sum)
	fmt.Println("crc32:", crc32Value)
}
```

<!-- REGISTRY_PATH: hashing_and_checksums.languages.python -->
### python

```python
#!/usr/bin/env python3
import hashlib
import zlib


def main() -> None:
    text = "hello-world"
    encoded = text.encode("utf-8")

    sha256_hex = hashlib.sha256(encoded).hexdigest()
    crc32_value = zlib.crc32(encoded)

    print("text:", text)
    print("sha256:", sha256_hex)
    print("crc32:", crc32_value)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: hashing_and_checksums.languages.scala -->
### scala

```scala
import java.security.MessageDigest
import java.util.zip.CRC32

object HashingAndChecksumsBasics {
  private def sha256Hex(text: String): String = {
    val digest = MessageDigest.getInstance("SHA-256").digest(text.getBytes("UTF-8"))
    digest.map(b => f"$b%02x").mkString
  }

  def main(args: Array[String]): Unit = {
    val text = "hello-world"
    val crc = new CRC32()
    crc.update(text.getBytes("UTF-8"))

    println(s"text: $text")
    println(s"sha256: ${sha256Hex(text)}")
    println(s"crc32: ${crc.getValue}")
  }
}
```

<!-- REGISTRY_PATH: hashing_and_checksums.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { createHash } from "node:crypto";
import { setImmediate } from "node:timers";

function checksum(text: string): number {
  return Array.from(text).reduce((acc, ch) => acc + ch.charCodeAt(0), 0);
}

function main(): void {
  const text = "hello-world";
  const sha256Hex = createHash("sha256").update(text).digest("hex");
  const sum = checksum(text);

  console.log("text:", text);
  console.log("sha256:", sha256Hex);
  console.log("checksum:", sum);
}

main();
setImmediate(() => {});
```

## heaps_and_priority_queues

- Docs: /content/docs/heaps_and_priority_queues/README.md

<!-- REGISTRY_PATH: heaps_and_priority_queues.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <queue>
#include <vector>

int main() {
    // max-heap (default)
    std::priority_queue<int> maxHeap;
    for (int v : {3, 1, 4, 1, 5, 9}) maxHeap.push(v);
    std::cout << "max: " << maxHeap.top() << "\n";  // 9

    // min-heap via greater<>
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap;
    for (int v : {3, 1, 4, 1, 5, 9}) minHeap.push(v);
    std::cout << "drain min-heap: ";
    while (!minHeap.empty()) {
        std::cout << minHeap.top() << ' ';
        minHeap.pop();
    }
    std::cout << "\n";  // 1 1 3 4 5 9
    return 0;
}
```

<!-- REGISTRY_PATH: heaps_and_priority_queues.languages.go -->
### go

```go
package main

import (
	"container/heap"
	"fmt"
)

// MinHeap implements heap.Interface for int
type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(v any)        { *h = append(*h, v.(int)) }
func (h *MinHeap) Pop() any          { old := *h; n := len(old); v := old[n-1]; *h = old[:n-1]; return v }

func main() {
	data := []int{3, 1, 4, 1, 5, 9}

	// max via negation
	maxH := &MinHeap{}
	for _, v := range data {
		heap.Push(maxH, -v)
	}
	fmt.Println("max:", -(*maxH)[0]) // 9

	// min-heap
	minH := &MinHeap{}
	for _, v := range data {
		heap.Push(minH, v)
	}
	fmt.Print("drain min-heap: ")
	for minH.Len() > 0 {
		fmt.Print(heap.Pop(minH).(int), " ")
	}
	fmt.Println() // 1 1 3 4 5 9
}
```

<!-- REGISTRY_PATH: heaps_and_priority_queues.languages.python -->
### python

```python
#!/usr/bin/env python3
import heapq


def main() -> None:
    data = [3, 1, 4, 1, 5, 9]

    # min-heap (default)
    min_heap: list[int] = []
    for v in data:
        heapq.heappush(min_heap, v)
    print("min:", min_heap[0])  # 1
    print("drain min-heap:", [heapq.heappop(min_heap) for _ in range(len(min_heap))])  # [1,1,3,4,5,9]

    # max-heap via negation
    max_heap: list[int] = []
    for v in data:
        heapq.heappush(max_heap, -v)
    print("max:", -max_heap[0])  # 9


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: heaps_and_priority_queues.languages.scala -->
### scala

```scala
import scala.collection.mutable

object HeapsAndPriorityQueues {
  def main(args: Array[String]): Unit = {
    val data = List(3, 1, 4, 1, 5, 9)

    // max priority queue (default)
    val maxPQ = mutable.PriorityQueue[Int]()
    data.foreach(maxPQ.enqueue)
    println(s"max: ${maxPQ.head}")  // 9

    // min priority queue via reverse ordering
    val minPQ = mutable.PriorityQueue[Int]()(Ordering[Int].reverse)
    data.foreach(minPQ.enqueue)
    print("drain min-heap: ")
    while (minPQ.nonEmpty) print(s"${minPQ.dequeue()} ")
    println()  // 1 1 3 4 5 9
  }
}
```

<!-- REGISTRY_PATH: heaps_and_priority_queues.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

class MinHeap {
  private data: number[] = [];

  push(v: number): void {
    this.data.push(v);
    this.bubbleUp(this.data.length - 1);
  }

  pop(): number {
    const top = this.data[0];
    const last = this.data.pop()!;
    if (this.data.length > 0) { this.data[0] = last; this.sinkDown(0); }
    return top;
  }

  peek(): number { return this.data[0]; }
  size(): number { return this.data.length; }

  private bubbleUp(i: number): void {
    while (i > 0) {
      const parent = (i - 1) >> 1;
      if (this.data[parent] <= this.data[i]) break;
      [this.data[parent], this.data[i]] = [this.data[i], this.data[parent]];
      i = parent;
    }
  }

  private sinkDown(i: number): void {
    const n = this.data.length;
    while (true) {
      let min = i;
      const l = 2 * i + 1, r = 2 * i + 2;
      if (l < n && this.data[l] < this.data[min]) min = l;
      if (r < n && this.data[r] < this.data[min]) min = r;
      if (min === i) break;
      [this.data[min], this.data[i]] = [this.data[i], this.data[min]];
      i = min;
    }
  }
}

function main(): void {
  const data = [3, 1, 4, 1, 5, 9];

  // min-heap
  const minHeap = new MinHeap();
  for (const v of data) minHeap.push(v);
  console.log("min:", minHeap.peek());  // 1
  const drained: number[] = [];
  while (minHeap.size() > 0) drained.push(minHeap.pop());
  console.log("drain min-heap:", drained);  // [1,1,3,4,5,9]

  // max-heap via negation
  const maxHeap = new MinHeap();
  for (const v of data) maxHeap.push(-v);
  console.log("max:", -maxHeap.peek());  // 9
}

main();
```

## interfaces_and_polymorphism

- Docs: /content/docs/interfaces_and_polymorphism/README.md

<!-- REGISTRY_PATH: interfaces_and_polymorphism.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Speaker {
public:
    virtual ~Speaker() = default;
    virtual std::string speak() const = 0;
};

class Dog : public Speaker {
public:
    std::string speak() const override { return "woof"; }
};

class Cat : public Speaker {
public:
    std::string speak() const override { return "meow"; }
};

int main() {
    std::vector<std::unique_ptr<Speaker>> speakers;
    speakers.push_back(std::make_unique<Dog>());
    speakers.push_back(std::make_unique<Cat>());

    for (const auto& speaker : speakers) {
        std::cout << speaker->speak() << "\n";
    }
    return 0;
}
```

<!-- REGISTRY_PATH: interfaces_and_polymorphism.languages.go -->
### go

```go
package main

import "fmt"

type Speaker interface {
	Speak() string
}

type Dog struct{}

type Cat struct{}

func (Dog) Speak() string {
	return "woof"
}

func (Cat) Speak() string {
	return "meow"
}

func main() {
	speakers := []Speaker{Dog{}, Cat{}}
	for _, speaker := range speakers {
		fmt.Println(speaker.Speak())
	}
}
```

<!-- REGISTRY_PATH: interfaces_and_polymorphism.languages.python -->
### python

```python
#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Speaker(ABC):
    @abstractmethod
    def speak(self) -> str:
        raise NotImplementedError


class Dog(Speaker):
    def speak(self) -> str:
        return "woof"


class Cat(Speaker):
    def speak(self) -> str:
        return "meow"


def main() -> None:
    speakers: list[Speaker] = [Dog(), Cat()]
    for speaker in speakers:
        print(speaker.speak())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: interfaces_and_polymorphism.languages.scala -->
### scala

```scala
trait Speaker {
  def speak(): String
}

class Dog extends Speaker {
  override def speak(): String = "woof"
}

class Cat extends Speaker {
  override def speak(): String = "meow"
}

object InterfacesAndPolymorphismBasics {
  def main(args: Array[String]): Unit = {
    val speakers: Seq[Speaker] = Seq(new Dog, new Cat)
    speakers.foreach(speaker => println(speaker.speak()))
  }
}
```

<!-- REGISTRY_PATH: interfaces_and_polymorphism.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

interface Speaker {
  speak(): string;
}

class Dog implements Speaker {
  speak(): string {
    return "woof";
  }
}

class Cat implements Speaker {
  speak(): string {
    return "meow";
  }
}

function main(): void {
  const speakers: Speaker[] = [new Dog(), new Cat()];
  for (const speaker of speakers) {
    console.log(speaker.speak());
  }
}

main();
setImmediate(() => {});
```

## interview

- Docs: /content/docs/interview/README.md

<!-- REGISTRY_PATH: interview.languages.cpp -->
### cpp

```cpp
#include <array>
#include <iostream>
#include <string>

bool isUnique(const std::string& s) {
    std::array<bool, 256> seen{};
    for (unsigned char ch : s) {
        if (seen[ch]) {
            return false;
        }
        seen[ch] = true;
    }
    return true;
}

int main() {
    std::cout << "leetcode -> " << std::boolalpha << isUnique("leetcode") << '\n';
    std::cout << "abc -> " << std::boolalpha << isUnique("abc") << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: interview.languages.go -->
### go

```go
package main

import "fmt"

func isUnique(s string) bool {
	seen := [256]bool{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if seen[ch] {
			return false
		}
		seen[ch] = true
	}
	return true
}

func main() {
	fmt.Printf("leetcode -> %t\n", isUnique("leetcode"))
	fmt.Printf("abc -> %t\n", isUnique("abc"))
}
```

<!-- REGISTRY_PATH: interview.languages.python -->
### python

```python
def is_unique(s: str) -> bool:
    seen: set[str] = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True


def main() -> None:
    print(f"leetcode -> {is_unique('leetcode')}")
    print(f"abc -> {is_unique('abc')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: interview.languages.scala -->
### scala

```scala
object Lcci0101IsUnique {
  def isUnique(s: String): Boolean = {
    val seen = scala.collection.mutable.HashSet.empty[Char]
    s.forall { ch =>
      if (seen.contains(ch)) {
        false
      } else {
        seen += ch
        true
      }
    }
  }

  def main(args: Array[String]): Unit = {
    println(s"leetcode -> ${isUnique("leetcode")}")
    println(s"abc -> ${isUnique("abc")}")
  }
}
```

<!-- REGISTRY_PATH: interview.languages.typescript -->
### typescript

```typescript
function isUnique(s: string): boolean {
  const seen = new Set<string>();
  for (const ch of s) {
    if (seen.has(ch)) {
      return false;
    }
    seen.add(ch);
  }
  return true;
}

function main(): void {
  console.log(`leetcode -> ${isUnique("leetcode")}`);
  console.log(`abc -> ${isUnique("abc")}`);
}

main();
```

## json_and_serialization

- Docs: /content/docs/json_and_serialization/README.md

<!-- REGISTRY_PATH: json_and_serialization.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <sstream>
#include <string>

struct User {
    std::string name;
    int age;
};

std::string to_json(const User& user) {
    std::ostringstream out;
    out << "{\"name\":\"" << user.name << "\",\"age\":" << user.age << "}";
    return out.str();
}

std::string extract_name(const std::string& json) {
    const std::string needle = "\"name\":\"";
    auto start = json.find(needle);
    if (start == std::string::npos) {
        return "";
    }
    start += needle.size();
    auto end = json.find('"', start);
    if (end == std::string::npos) {
        return "";
    }
    return json.substr(start, end - start);
}

int main() {
    User user{"Alice", 29};
    std::string json = to_json(user);

    std::cout << "json: " << json << "\n";
    std::cout << "parsed name: " << extract_name(json) << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: json_and_serialization.languages.go -->
### go

```go
package main

import (
	"encoding/json"
	"fmt"
)

type User struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}

func main() {
	user := User{Name: "Alice", Age: 29}
	data, err := json.Marshal(user)
	if err != nil {
		panic(err)
	}

	var parsed User
	if err := json.Unmarshal(data, &parsed); err != nil {
		panic(err)
	}

	fmt.Println("json:", string(data))
	fmt.Println("parsed name:", parsed.Name)
}
```

<!-- REGISTRY_PATH: json_and_serialization.languages.python -->
### python

```python
#!/usr/bin/env python3
import json


def main() -> None:
    user = {"name": "Alice", "age": 29}
    text = json.dumps(user)
    parsed = json.loads(text)

    print("json:", text)
    print("parsed name:", parsed["name"])


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: json_and_serialization.languages.scala -->
### scala

```scala
object JsonAndSerializationBasics {
  def toJson(name: String, age: Int): String = {
    s"{\"name\":\"$name\",\"age\":$age}"
  }

  def extractName(json: String): String = {
    val pattern = """\"name\":\"([^\"]+)\""".r
    pattern.findFirstMatchIn(json).map(_.group(1)).getOrElse("")
  }

  def main(args: Array[String]): Unit = {
    val json = toJson("Alice", 29)
    println(s"json: $json")
    println(s"parsed name: ${extractName(json)}")
  }
}
```

<!-- REGISTRY_PATH: json_and_serialization.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

type User = {
  name: string;
  age: number;
};

function main(): void {
  const user: User = { name: "Alice", age: 29 };
  const text = JSON.stringify(user);
  const parsed = JSON.parse(text) as User;

  console.log("json:", text);
  console.log("parsed name:", parsed.name);
}

main();
setImmediate(() => {});
```

## lcci_01_01_is_unique

<!-- REGISTRY_PATH: lcci_01_01_is_unique.languages.cpp -->
### cpp

```cpp
#include <array>
#include <iostream>
#include <string>

bool isUnique(const std::string& s) {
    std::array<bool, 256> seen{};
    for (unsigned char ch : s) {
        if (seen[ch]) {
            return false;
        }
        seen[ch] = true;
    }
    return true;
}

int main() {
    std::cout << "leetcode -> " << std::boolalpha << isUnique("leetcode") << '\n';
    std::cout << "abc -> " << std::boolalpha << isUnique("abc") << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_01_is_unique.languages.go -->
### go

```go
package main

import "fmt"

func isUnique(s string) bool {
	seen := [256]bool{}
	for i := 0; i < len(s); i++ {
		ch := s[i]
		if seen[ch] {
			return false
		}
		seen[ch] = true
	}
	return true
}

func main() {
	fmt.Printf("leetcode -> %t\n", isUnique("leetcode"))
	fmt.Printf("abc -> %t\n", isUnique("abc"))
}
```

<!-- REGISTRY_PATH: lcci_01_01_is_unique.languages.python -->
### python

```python
def is_unique(s: str) -> bool:
    seen: set[str] = set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True


def main() -> None:
    print(f"leetcode -> {is_unique('leetcode')}")
    print(f"abc -> {is_unique('abc')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_01_is_unique.languages.scala -->
### scala

```scala
object Lcci0101IsUnique {
  def isUnique(s: String): Boolean = {
    val seen = scala.collection.mutable.HashSet.empty[Char]
    s.forall { ch =>
      if (seen.contains(ch)) {
        false
      } else {
        seen += ch
        true
      }
    }
  }

  def main(args: Array[String]): Unit = {
    println(s"leetcode -> ${isUnique("leetcode")}")
    println(s"abc -> ${isUnique("abc")}")
  }
}
```

<!-- REGISTRY_PATH: lcci_01_01_is_unique.languages.typescript -->
### typescript

```typescript
function isUnique(s: string): boolean {
  const seen = new Set<string>();
  for (const ch of s) {
    if (seen.has(ch)) {
      return false;
    }
    seen.add(ch);
  }
  return true;
}

function main(): void {
  console.log(`leetcode -> ${isUnique("leetcode")}`);
  console.log(`abc -> ${isUnique("abc")}`);
}

main();
```

## lcci_01_02_check_permutation

<!-- REGISTRY_PATH: lcci_01_02_check_permutation.languages.cpp -->
### cpp

```cpp
#include <array>
#include <iostream>
#include <string>

bool checkPermutation(const std::string& a, const std::string& b) {
    if (a.size() != b.size()) {
        return false;
    }

    std::array<int, 256> freq{};
    for (unsigned char ch : a) {
        ++freq[ch];
    }
    for (unsigned char ch : b) {
        --freq[ch];
        if (freq[ch] < 0) {
            return false;
        }
    }
    return true;
}

int main() {
    std::cout << "abcde vs edcba -> " << std::boolalpha << checkPermutation("abcde", "edcba") << '\n';
    std::cout << "abc vs abz -> " << std::boolalpha << checkPermutation("abc", "abz") << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_02_check_permutation.languages.go -->
### go

```go
package main

import "fmt"

func checkPermutation(a string, b string) bool {
	if len(a) != len(b) {
		return false
	}

	freq := [256]int{}
	for i := 0; i < len(a); i++ {
		freq[a[i]]++
	}
	for i := 0; i < len(b); i++ {
		freq[b[i]]--
		if freq[b[i]] < 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Printf("abcde vs edcba -> %t\n", checkPermutation("abcde", "edcba"))
	fmt.Printf("abc vs abz -> %t\n", checkPermutation("abc", "abz"))
}
```

<!-- REGISTRY_PATH: lcci_01_02_check_permutation.languages.python -->
### python

```python
from collections import Counter


def check_permutation(a: str, b: str) -> bool:
    return len(a) == len(b) and Counter(a) == Counter(b)


def main() -> None:
    print(f"abcde vs edcba -> {check_permutation('abcde', 'edcba')}")
    print(f"abc vs abz -> {check_permutation('abc', 'abz')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_02_check_permutation.languages.scala -->
### scala

```scala
object Lcci0102CheckPermutation {
  def checkPermutation(a: String, b: String): Boolean = {
    if (a.length != b.length) {
      return false
    }

    val freq = Array.fill(256)(0)
    a.foreach(ch => freq(ch) += 1)

    b.foreach { ch =>
      freq(ch) -= 1
      if (freq(ch) < 0) {
        return false
      }
    }

    true
  }

  def main(args: Array[String]): Unit = {
    println(s"abcde vs edcba -> ${checkPermutation("abcde", "edcba")}")
    println(s"abc vs abz -> ${checkPermutation("abc", "abz")}")
  }
}
```

<!-- REGISTRY_PATH: lcci_01_02_check_permutation.languages.typescript -->
### typescript

```typescript
function checkPermutation(a: string, b: string): boolean {
  if (a.length !== b.length) {
    return false;
  }

  const freq = new Map<string, number>();
  for (const ch of a) {
    freq.set(ch, (freq.get(ch) ?? 0) + 1);
  }

  for (const ch of b) {
    const left = (freq.get(ch) ?? 0) - 1;
    if (left < 0) {
      return false;
    }
    freq.set(ch, left);
  }

  return true;
}

function main(): void {
  console.log(`abcde vs edcba -> ${checkPermutation("abcde", "edcba")}`);
  console.log(`abc vs abz -> ${checkPermutation("abc", "abz")}`);
}

main();
```

## lcci_01_03_string_to_url

<!-- REGISTRY_PATH: lcci_01_03_string_to_url.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

std::string urlify(const std::string& s, int trueLength) {
    std::string out;
    out.reserve(static_cast<size_t>(trueLength) * 3);

    for (int i = 0; i < trueLength; ++i) {
        if (s[static_cast<size_t>(i)] == ' ') {
            out += "%20";
        } else {
            out.push_back(s[static_cast<size_t>(i)]);
        }
    }

    return out;
}

int main() {
    const std::string input = "Mr John Smith    ";
    std::cout << urlify(input, 13) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_03_string_to_url.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

func urlify(s string, trueLength int) string {
	var b strings.Builder
	for i := 0; i < trueLength; i++ {
		if s[i] == ' ' {
			b.WriteString("%20")
		} else {
			b.WriteByte(s[i])
		}
	}
	return b.String()
}

func main() {
	fmt.Println(urlify("Mr John Smith    ", 13))
}
```

<!-- REGISTRY_PATH: lcci_01_03_string_to_url.languages.python -->
### python

```python
def urlify(s: str, true_length: int) -> str:
    return "".join("%20" if ch == " " else ch for ch in s[:true_length])


def main() -> None:
    print(urlify("Mr John Smith    ", 13))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_03_string_to_url.languages.scala -->
### scala

```scala
object Lcci0103StringToUrl {
  def urlify(s: String, trueLength: Int): String = {
    val b = new StringBuilder
    for (i <- 0 until trueLength) {
      if (s(i) == ' ') {
        b.append("%20")
      } else {
        b.append(s(i))
      }
    }
    b.toString()
  }

  def main(args: Array[String]): Unit = {
    println(urlify("Mr John Smith    ", 13))
  }
}
```

<!-- REGISTRY_PATH: lcci_01_03_string_to_url.languages.typescript -->
### typescript

```typescript
function urlify(s: string, trueLength: number): string {
  let out = "";
  for (let i = 0; i < trueLength; i++) {
    out += s[i] === " " ? "%20" : s[i];
  }
  return out;
}

function main(): void {
  console.log(urlify("Mr John Smith    ", 13));
}

main();
```

## lcci_01_04_palindrome_permutation

<!-- REGISTRY_PATH: lcci_01_04_palindrome_permutation.languages.cpp -->
### cpp

```cpp
#include <array>
#include <cctype>
#include <iostream>
#include <string>

bool canPermutePalindrome(const std::string& s) {
    std::array<int, 256> freq{};
    for (unsigned char ch : s) {
        if (std::isspace(ch)) {
            continue;
        }
        unsigned char lower = static_cast<unsigned char>(std::tolower(ch));
        ++freq[lower];
    }

    int odd = 0;
    for (int count : freq) {
        if ((count & 1) == 1) {
            ++odd;
            if (odd > 1) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    std::cout << "tact coa -> " << std::boolalpha << canPermutePalindrome("tact coa") << '\n';
    std::cout << "daily -> " << std::boolalpha << canPermutePalindrome("daily") << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_04_palindrome_permutation.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

func canPermutePalindrome(s string) bool {
	freq := map[rune]int{}
	for _, ch := range strings.ToLower(s) {
		if ch == ' ' {
			continue
		}
		freq[ch]++
	}

	odd := 0
	for _, count := range freq {
		if count%2 == 1 {
			odd++
			if odd > 1 {
				return false
			}
		}
	}
	return true
}

func main() {
	fmt.Printf("tact coa -> %t\n", canPermutePalindrome("tact coa"))
	fmt.Printf("daily -> %t\n", canPermutePalindrome("daily"))
}
```

<!-- REGISTRY_PATH: lcci_01_04_palindrome_permutation.languages.python -->
### python

```python
def can_permute_palindrome(s: str) -> bool:
    counts: dict[str, int] = {}
    for ch in s.lower():
        if ch.isspace():
            continue
        counts[ch] = counts.get(ch, 0) + 1
    odd = sum(1 for c in counts.values() if c % 2 == 1)
    return odd <= 1


def main() -> None:
    print(f"tact coa -> {can_permute_palindrome('tact coa')}")
    print(f"daily -> {can_permute_palindrome('daily')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_04_palindrome_permutation.languages.scala -->
### scala

```scala
object Lcci0104PalindromePermutation {
  def canPermutePalindrome(s: String): Boolean = {
    val freq = scala.collection.mutable.Map.empty[Char, Int].withDefaultValue(0)

    s.toLowerCase.foreach { ch =>
      if (!ch.isWhitespace) {
        freq.update(ch, freq(ch) + 1)
      }
    }

    freq.values.count(_ % 2 == 1) <= 1
  }

  def main(args: Array[String]): Unit = {
    println(s"tact coa -> ${canPermutePalindrome("tact coa")}")
    println(s"daily -> ${canPermutePalindrome("daily")}")
  }
}
```

<!-- REGISTRY_PATH: lcci_01_04_palindrome_permutation.languages.typescript -->
### typescript

```typescript
function canPermutePalindrome(s: string): boolean {
  const freq = new Map<string, number>();
  for (const ch of s.toLowerCase()) {
    if (ch === " ") {
      continue;
    }
    freq.set(ch, (freq.get(ch) ?? 0) + 1);
  }

  let odd = 0;
  for (const count of freq.values()) {
    if (count % 2 === 1) {
      odd += 1;
      if (odd > 1) {
        return false;
      }
    }
  }
  return true;
}

function main(): void {
  console.log(`tact coa -> ${canPermutePalindrome("tact coa")}`);
  console.log(`daily -> ${canPermutePalindrome("daily")}`);
}

main();
```

## lcci_01_05_one_away

<!-- REGISTRY_PATH: lcci_01_05_one_away.languages.cpp -->
### cpp

```cpp
#include <cstdlib>
#include <iostream>
#include <string>

bool oneAway(const std::string& a, const std::string& b) {
    if (std::abs(static_cast<int>(a.size()) - static_cast<int>(b.size())) > 1) {
        return false;
    }

    const std::string& s1 = a.size() <= b.size() ? a : b;
    const std::string& s2 = a.size() <= b.size() ? b : a;

    std::size_t i = 0;
    std::size_t j = 0;
    bool foundDiff = false;

    while (i < s1.size() && j < s2.size()) {
        if (s1[i] == s2[j]) {
            ++i;
            ++j;
            continue;
        }

        if (foundDiff) {
            return false;
        }
        foundDiff = true;

        if (s1.size() == s2.size()) {
            ++i;
        }
        ++j;
    }

    return true;
}

int main() {
    std::cout << "pale vs ple -> " << std::boolalpha << oneAway("pale", "ple") << '\n';
    std::cout << "pales vs pale -> " << std::boolalpha << oneAway("pales", "pale") << '\n';
    std::cout << "pale vs bake -> " << std::boolalpha << oneAway("pale", "bake") << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_05_one_away.languages.go -->
### go

```go
package main

import "fmt"

func oneAway(a string, b string) bool {
	if len(a)-len(b) > 1 || len(b)-len(a) > 1 {
		return false
	}

	s1, s2 := a, b
	if len(s1) > len(s2) {
		s1, s2 = s2, s1
	}

	i, j := 0, 0
	found := false

	for i < len(s1) && j < len(s2) {
		if s1[i] == s2[j] {
			i++
			j++
			continue
		}

		if found {
			return false
		}
		found = true

		if len(s1) == len(s2) {
			i++
		}
		j++
	}

	return true
}

func main() {
	fmt.Printf("pale vs ple -> %t\n", oneAway("pale", "ple"))
	fmt.Printf("pales vs pale -> %t\n", oneAway("pales", "pale"))
	fmt.Printf("pale vs bake -> %t\n", oneAway("pale", "bake"))
}
```

<!-- REGISTRY_PATH: lcci_01_05_one_away.languages.python -->
### python

```python
def one_away(a: str, b: str) -> bool:
    if abs(len(a) - len(b)) > 1:
        return False

    s1, s2 = (a, b) if len(a) <= len(b) else (b, a)
    i = j = 0
    found = False

    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
            j += 1
            continue

        if found:
            return False
        found = True

        if len(s1) == len(s2):
            i += 1
        j += 1

    return True


def main() -> None:
    print(f"pale vs ple -> {one_away('pale', 'ple')}")
    print(f"pales vs pale -> {one_away('pales', 'pale')}")
    print(f"pale vs bake -> {one_away('pale', 'bake')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_05_one_away.languages.scala -->
### scala

```scala
object Lcci0105OneAway {
  def oneAway(a: String, b: String): Boolean = {
    if (math.abs(a.length - b.length) > 1) {
      return false
    }

    val (s1, s2) = if (a.length <= b.length) (a, b) else (b, a)
    var i = 0
    var j = 0
    var found = false

    while (i < s1.length && j < s2.length) {
      if (s1(i) == s2(j)) {
        i += 1
        j += 1
      } else {
        if (found) {
          return false
        }
        found = true
        if (s1.length == s2.length) {
          i += 1
        }
        j += 1
      }
    }

    true
  }

  def main(args: Array[String]): Unit = {
    println(s"pale vs ple -> ${oneAway("pale", "ple")}")
    println(s"pales vs pale -> ${oneAway("pales", "pale")}")
    println(s"pale vs bake -> ${oneAway("pale", "bake")}")
  }
}
```

<!-- REGISTRY_PATH: lcci_01_05_one_away.languages.typescript -->
### typescript

```typescript
function oneAway(a: string, b: string): boolean {
  if (Math.abs(a.length - b.length) > 1) {
    return false;
  }

  let s1 = a;
  let s2 = b;
  if (s1.length > s2.length) {
    [s1, s2] = [s2, s1];
  }

  let i = 0;
  let j = 0;
  let found = false;

  while (i < s1.length && j < s2.length) {
    if (s1[i] === s2[j]) {
      i += 1;
      j += 1;
      continue;
    }

    if (found) {
      return false;
    }
    found = true;

    if (s1.length === s2.length) {
      i += 1;
    }
    j += 1;
  }

  return true;
}

function main(): void {
  console.log(`pale vs ple -> ${oneAway("pale", "ple")}`);
  console.log(`pales vs pale -> ${oneAway("pales", "pale")}`);
  console.log(`pale vs bake -> ${oneAway("pale", "bake")}`);
}

main();
```

## lcci_01_06_compress_string

<!-- REGISTRY_PATH: lcci_01_06_compress_string.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

std::string compressString(const std::string& s) {
    if (s.empty()) {
        return s;
    }

    std::string out;
    out.reserve(s.size());

    int run = 1;
    for (std::size_t i = 1; i <= s.size(); ++i) {
        if (i < s.size() && s[i] == s[i - 1]) {
            ++run;
            continue;
        }

        out.push_back(s[i - 1]);
        out += std::to_string(run);
        run = 1;
    }

    return out.size() < s.size() ? out : s;
}

int main() {
    std::cout << "aabcccccaaa -> " << compressString("aabcccccaaa") << '\n';
    std::cout << "abbccd -> " << compressString("abbccd") << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_06_compress_string.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func compressString(s string) string {
	if len(s) == 0 {
		return s
	}

	var b strings.Builder
	run := 1

	for i := 1; i <= len(s); i++ {
		if i < len(s) && s[i] == s[i-1] {
			run++
			continue
		}

		b.WriteByte(s[i-1])
		b.WriteString(strconv.Itoa(run))
		run = 1
	}

	compressed := b.String()
	if len(compressed) < len(s) {
		return compressed
	}
	return s
}

func main() {
	fmt.Printf("aabcccccaaa -> %s\n", compressString("aabcccccaaa"))
	fmt.Printf("abbccd -> %s\n", compressString("abbccd"))
}
```

<!-- REGISTRY_PATH: lcci_01_06_compress_string.languages.python -->
### python

```python
def compress_string(s: str) -> str:
    if not s:
        return s

    out: list[str] = []
    run = 1

    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            run += 1
            continue

        out.append(s[i - 1])
        out.append(str(run))
        run = 1

    compressed = "".join(out)
    return compressed if len(compressed) < len(s) else s


def main() -> None:
    print(f"aabcccccaaa -> {compress_string('aabcccccaaa')}")
    print(f"abbccd -> {compress_string('abbccd')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_06_compress_string.languages.scala -->
### scala

```scala
object Lcci0106CompressString {
  def compressString(s: String): String = {
    if (s.isEmpty) {
      return s
    }

    val b = new StringBuilder
    var run = 1

    for (i <- 1 to s.length) {
      if (i < s.length && s(i) == s(i - 1)) {
        run += 1
      } else {
        b.append(s(i - 1))
        b.append(run)
        run = 1
      }
    }

    val compressed = b.toString()
    if (compressed.length < s.length) compressed else s
  }

  def main(args: Array[String]): Unit = {
    println(s"aabcccccaaa -> ${compressString("aabcccccaaa")}")
    println(s"abbccd -> ${compressString("abbccd")}")
  }
}
```

<!-- REGISTRY_PATH: lcci_01_06_compress_string.languages.typescript -->
### typescript

```typescript
function compressString(s: string): string {
  if (s.length === 0) {
    return s;
  }

  let out = "";
  let run = 1;

  for (let i = 1; i <= s.length; i++) {
    if (i < s.length && s[i] === s[i - 1]) {
      run += 1;
      continue;
    }

    out += s[i - 1] + String(run);
    run = 1;
  }

  return out.length < s.length ? out : s;
}

function main(): void {
  console.log(`aabcccccaaa -> ${compressString("aabcccccaaa")}`);
  console.log(`abbccd -> ${compressString("abbccd")}`);
}

main();
```

## lcci_01_07_rotate_matrix

<!-- REGISTRY_PATH: lcci_01_07_rotate_matrix.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

void rotate(std::vector<std::vector<int>>& m) {
    const int n = static_cast<int>(m.size());
    for (int layer = 0; layer < n / 2; ++layer) {
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < last; ++i) {
            int offset = i - first;
            int top = m[first][i];
            m[first][i] = m[last - offset][first];
            m[last - offset][first] = m[last][last - offset];
            m[last][last - offset] = m[i][last];
            m[i][last] = top;
        }
    }
}

int main() {
    std::vector<std::vector<int>> m = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    rotate(m);

    for (const auto& row : m) {
        std::cout << row[0] << ' ' << row[1] << ' ' << row[2] << '\n';
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_07_rotate_matrix.languages.go -->
### go

```go
package main

import "fmt"

func rotate(matrix [][]int) {
	n := len(matrix)
	for layer := 0; layer < n/2; layer++ {
		first := layer
		last := n - 1 - layer
		for i := first; i < last; i++ {
			offset := i - first
			top := matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = top
		}
	}
}

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
	}

	rotate(matrix)
	for _, row := range matrix {
		fmt.Printf("%d %d %d\n", row[0], row[1], row[2])
	}
}
```

<!-- REGISTRY_PATH: lcci_01_07_rotate_matrix.languages.python -->
### python

```python
def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top


def main() -> None:
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    rotate(matrix)
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_07_rotate_matrix.languages.scala -->
### scala

```scala
object Lcci0107RotateMatrix {
  def rotate(matrix: Array[Array[Int]]): Unit = {
    val n = matrix.length
    for (layer <- 0 until n / 2) {
      val first = layer
      val last = n - 1 - layer
      for (i <- first until last) {
        val offset = i - first
        val top = matrix(first)(i)
        matrix(first)(i) = matrix(last - offset)(first)
        matrix(last - offset)(first) = matrix(last)(last - offset)
        matrix(last)(last - offset) = matrix(i)(last)
        matrix(i)(last) = top
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val matrix = Array(
      Array(1, 2, 3),
      Array(4, 5, 6),
      Array(7, 8, 9)
    )

    rotate(matrix)
    matrix.foreach(row => println(row.mkString(" ")))
  }
}
```

<!-- REGISTRY_PATH: lcci_01_07_rotate_matrix.languages.typescript -->
### typescript

```typescript
function rotate(matrix: number[][]): void {
  const n = matrix.length;
  for (let layer = 0; layer < Math.floor(n / 2); layer++) {
    const first = layer;
    const last = n - 1 - layer;

    for (let i = first; i < last; i++) {
      const offset = i - first;
      const top = matrix[first][i];
      matrix[first][i] = matrix[last - offset][first];
      matrix[last - offset][first] = matrix[last][last - offset];
      matrix[last][last - offset] = matrix[i][last];
      matrix[i][last] = top;
    }
  }
}

function main(): void {
  const matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];

  rotate(matrix);
  for (const row of matrix) {
    console.log(row.join(" "));
  }
}

main();
```

## lcci_01_08_zero_matrix

<!-- REGISTRY_PATH: lcci_01_08_zero_matrix.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>

void setZeroes(std::vector<std::vector<int>>& matrix) {
    int rows = static_cast<int>(matrix.size());
    int cols = static_cast<int>(matrix[0].size());

    std::unordered_set<int> zeroRows;
    std::unordered_set<int> zeroCols;

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (matrix[r][c] == 0) {
                zeroRows.insert(r);
                zeroCols.insert(c);
            }
        }
    }

    for (int r = 0; r < rows; ++r) {
        for (int c = 0; c < cols; ++c) {
            if (zeroRows.count(r) || zeroCols.count(c)) {
                matrix[r][c] = 0;
            }
        }
    }
}

int main() {
    std::vector<std::vector<int>> matrix = {
        {1, 2, 3},
        {4, 0, 6},
        {7, 8, 9}
    };

    setZeroes(matrix);

    for (const auto& row : matrix) {
        std::cout << row[0] << ' ' << row[1] << ' ' << row[2] << '\n';
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_08_zero_matrix.languages.go -->
### go

```go
package main

import "fmt"

func setZeroes(matrix [][]int) {
	zeroRows := map[int]bool{}
	zeroCols := map[int]bool{}

	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if matrix[r][c] == 0 {
				zeroRows[r] = true
				zeroCols[c] = true
			}
		}
	}

	for r := 0; r < len(matrix); r++ {
		for c := 0; c < len(matrix[0]); c++ {
			if zeroRows[r] || zeroCols[c] {
				matrix[r][c] = 0
			}
		}
	}
}

func main() {
	matrix := [][]int{
		{1, 2, 3},
		{4, 0, 6},
		{7, 8, 9},
	}

	setZeroes(matrix)
	for _, row := range matrix {
		fmt.Printf("%d %d %d\n", row[0], row[1], row[2])
	}
}
```

<!-- REGISTRY_PATH: lcci_01_08_zero_matrix.languages.python -->
### python

```python
def set_zeroes(matrix: list[list[int]]) -> None:
    rows = set()
    cols = set()

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                rows.add(r)
                cols.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in rows or c in cols:
                matrix[r][c] = 0


def main() -> None:
    matrix = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 9],
    ]

    set_zeroes(matrix)
    for row in matrix:
        print(*row)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_08_zero_matrix.languages.scala -->
### scala

```scala
object Lcci0108ZeroMatrix {
  def setZeroes(matrix: Array[Array[Int]]): Unit = {
    val zeroRows = scala.collection.mutable.Set.empty[Int]
    val zeroCols = scala.collection.mutable.Set.empty[Int]

    for (r <- matrix.indices; c <- matrix(0).indices) {
      if (matrix(r)(c) == 0) {
        zeroRows += r
        zeroCols += c
      }
    }

    for (r <- matrix.indices; c <- matrix(0).indices) {
      if (zeroRows.contains(r) || zeroCols.contains(c)) {
        matrix(r)(c) = 0
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val matrix = Array(
      Array(1, 2, 3),
      Array(4, 0, 6),
      Array(7, 8, 9)
    )

    setZeroes(matrix)
    matrix.foreach(row => println(row.mkString(" ")))
  }
}
```

<!-- REGISTRY_PATH: lcci_01_08_zero_matrix.languages.typescript -->
### typescript

```typescript
function setZeroes(matrix: number[][]): void {
  const zeroRows = new Set<number>();
  const zeroCols = new Set<number>();

  for (let r = 0; r < matrix.length; r++) {
    for (let c = 0; c < matrix[0].length; c++) {
      if (matrix[r][c] === 0) {
        zeroRows.add(r);
        zeroCols.add(c);
      }
    }
  }

  for (let r = 0; r < matrix.length; r++) {
    for (let c = 0; c < matrix[0].length; c++) {
      if (zeroRows.has(r) || zeroCols.has(c)) {
        matrix[r][c] = 0;
      }
    }
  }
}

function main(): void {
  const matrix = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9],
  ];

  setZeroes(matrix);
  for (const row of matrix) {
    console.log(row.join(" "));
  }
}

main();
```

## lcci_01_09_string_rotation

<!-- REGISTRY_PATH: lcci_01_09_string_rotation.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

bool isStringRotation(const std::string& s1, const std::string& s2) {
    if (s1.size() != s2.size()) {
        return false;
    }
    return (s1 + s1).find(s2) != std::string::npos;
}

int main() {
    std::cout << "waterbottle vs erbottlewat -> "
              << std::boolalpha
              << isStringRotation("waterbottle", "erbottlewat")
              << '\n';
    std::cout << "aa vs aba -> "
              << std::boolalpha
              << isStringRotation("aa", "aba")
              << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_01_09_string_rotation.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

func isStringRotation(s1 string, s2 string) bool {
	return len(s1) == len(s2) && strings.Contains(s1+s1, s2)
}

func main() {
	fmt.Printf("waterbottle vs erbottlewat -> %t\n", isStringRotation("waterbottle", "erbottlewat"))
	fmt.Printf("aa vs aba -> %t\n", isStringRotation("aa", "aba"))
}
```

<!-- REGISTRY_PATH: lcci_01_09_string_rotation.languages.python -->
### python

```python
def is_string_rotation(s1: str, s2: str) -> bool:
    return len(s1) == len(s2) and s2 in (s1 + s1)


def main() -> None:
    print(f"waterbottle vs erbottlewat -> {is_string_rotation('waterbottle', 'erbottlewat')}")
    print(f"aa vs aba -> {is_string_rotation('aa', 'aba')}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_01_09_string_rotation.languages.scala -->
### scala

```scala
object Lcci0109StringRotation {
  def isStringRotation(s1: String, s2: String): Boolean = {
    s1.length == s2.length && (s1 + s1).contains(s2)
  }

  def main(args: Array[String]): Unit = {
    println(s"waterbottle vs erbottlewat -> ${isStringRotation("waterbottle", "erbottlewat")}")
    println(s"aa vs aba -> ${isStringRotation("aa", "aba")}")
  }
}
```

<!-- REGISTRY_PATH: lcci_01_09_string_rotation.languages.typescript -->
### typescript

```typescript
function isStringRotation(s1: string, s2: string): boolean {
  return s1.length === s2.length && (s1 + s1).includes(s2);
}

function main(): void {
  console.log(`waterbottle vs erbottlewat -> ${isStringRotation("waterbottle", "erbottlewat")}`);
  console.log(`aa vs aba -> ${isStringRotation("aa", "aba")}`);
}

main();
```

## lcci_02_01_remove_duplicate_node

<!-- REGISTRY_PATH: lcci_02_01_remove_duplicate_node.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

void removeDuplicateNodes(ListNode* head) {
    std::unordered_set<int> seen;
    ListNode* prev = nullptr;
    ListNode* cur = head;

    while (cur) {
        if (seen.count(cur->val)) {
            prev->next = cur->next;
            cur = cur->next;
            continue;
        }
        seen.insert(cur->val);
        prev = cur;
        cur = cur->next;
    }
}

void printList(ListNode* head) {
    bool first = true;
    while (head) {
        if (!first) std::cout << ' ';
        std::cout << head->val;
        first = false;
        head = head->next;
    }
    std::cout << '\n';
}

int main() {
    ListNode* head = buildList({1, 2, 3, 3, 2, 1, 4});
    removeDuplicateNodes(head);
    printList(head);
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_01_remove_duplicate_node.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func removeDuplicateNodes(head *ListNode) {
	seen := map[int]bool{}
	var prev *ListNode
	cur := head

	for cur != nil {
		if seen[cur.Val] {
			prev.Next = cur.Next
			cur = cur.Next
			continue
		}
		seen[cur.Val] = true
		prev = cur
		cur = cur.Next
	}
}

func printList(head *ListNode) {
	first := true
	for head != nil {
		if !first {
			fmt.Print(" ")
		}
		fmt.Print(head.Val)
		first = false
		head = head.Next
	}
	fmt.Println()
}

func main() {
	head := buildList([]int{1, 2, 3, 3, 2, 1, 4})
	removeDuplicateNodes(head)
	printList(head)
}
```

<!-- REGISTRY_PATH: lcci_02_01_remove_duplicate_node.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def remove_duplicate_nodes(head: ListNode | None) -> None:
    seen: set[int] = set()
    prev: ListNode | None = None
    cur = head

    while cur is not None:
        if cur.val in seen:
            assert prev is not None
            prev.next = cur.next
            cur = cur.next
            continue
        seen.add(cur.val)
        prev = cur
        cur = cur.next


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    head = build_list([1, 2, 3, 3, 2, 1, 4])
    remove_duplicate_nodes(head)
    print_list(head)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_01_remove_duplicate_node.languages.scala -->
### scala

```scala
object Lcci0201RemoveDuplicateNode {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def removeDuplicateNodes(head: ListNode | Null): Unit = {
    val seen = scala.collection.mutable.HashSet.empty[Int]
    var prev: ListNode | Null = null
    var cur = head

    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      if (seen.contains(node.value)) {
        prev.asInstanceOf[ListNode].next = node.next
        cur = node.next
      } else {
        seen += node.value
        prev = cur
        cur = node.next
      }
    }
  }

  def printList(head: ListNode | Null): Unit = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      out += node.value
      cur = node.next
    }
    println(out.mkString(" "))
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(Vector(1, 2, 3, 3, 2, 1, 4))
    removeDuplicateNodes(head)
    printList(head)
  }
}
```

<!-- REGISTRY_PATH: lcci_02_01_remove_duplicate_node.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function removeDuplicateNodes(head: ListNode | null): void {
  const seen = new Set<number>();
  let prev: ListNode | null = null;
  let cur = head;

  while (cur !== null) {
    if (seen.has(cur.val)) {
      if (prev !== null) {
        prev.next = cur.next;
      }
      cur = cur.next;
      continue;
    }

    seen.add(cur.val);
    prev = cur;
    cur = cur.next;
  }
}

function printList(head: ListNode | null): void {
  const out: number[] = [];
  while (head !== null) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
}

function main(): void {
  const head = buildList([1, 2, 3, 3, 2, 1, 4]);
  removeDuplicateNodes(head);
  printList(head);
}

main();
```

## lcci_02_02_kth_node_from_end

<!-- REGISTRY_PATH: lcci_02_02_kth_node_from_end.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

int kthToLast(ListNode* head, int k) {
    ListNode* fast = head;
    ListNode* slow = head;
    for (int i = 0; i < k; ++i) {
        fast = fast->next;
    }
    while (fast) {
        fast = fast->next;
        slow = slow->next;
    }
    return slow->val;
}

int main() {
    ListNode* head = buildList({1, 2, 3, 4, 5});
    std::cout << kthToLast(head, 2) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_02_kth_node_from_end.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func kthToLast(head *ListNode, k int) int {
	fast := head
	slow := head
	for i := 0; i < k; i++ {
		fast = fast.Next
	}
	for fast != nil {
		fast = fast.Next
		slow = slow.Next
	}
	return slow.Val
}

func main() {
	head := buildList([]int{1, 2, 3, 4, 5})
	fmt.Println(kthToLast(head, 2))
}
```

<!-- REGISTRY_PATH: lcci_02_02_kth_node_from_end.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def kth_to_last(head: ListNode, k: int) -> int:
    fast: ListNode | None = head
    slow: ListNode | None = head

    for _ in range(k):
        assert fast is not None
        fast = fast.next

    while fast is not None:
        fast = fast.next
        assert slow is not None
        slow = slow.next

    assert slow is not None
    return slow.val


def main() -> None:
    head = build_list([1, 2, 3, 4, 5])
    assert head is not None
    print(kth_to_last(head, 2))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_02_kth_node_from_end.languages.scala -->
### scala

```scala
object Lcci0202KthNodeFromEnd {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def kthToLast(head: ListNode, k: Int): Int = {
    var fast: ListNode | Null = head
    var slow: ListNode | Null = head

    for (_ <- 0 until k) {
      fast = fast.asInstanceOf[ListNode].next
    }

    while (fast != null) {
      fast = fast.asInstanceOf[ListNode].next
      slow = slow.asInstanceOf[ListNode].next
    }

    slow.asInstanceOf[ListNode].value
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(Vector(1, 2, 3, 4, 5)).asInstanceOf[ListNode]
    println(kthToLast(head, 2))
  }
}
```

<!-- REGISTRY_PATH: lcci_02_02_kth_node_from_end.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function kthToLast(head: ListNode, k: number): number {
  let fast: ListNode | null = head;
  let slow: ListNode | null = head;

  for (let i = 0; i < k; i++) {
    fast = fast!.next;
  }

  while (fast !== null) {
    fast = fast.next;
    slow = slow!.next;
  }

  return slow!.val;
}

function main(): void {
  const head = buildList([1, 2, 3, 4, 5])!;
  console.log(kthToLast(head, 2));
}

main();
```

## lcci_02_03_delete_middle_node

<!-- REGISTRY_PATH: lcci_02_03_delete_middle_node.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

bool deleteMiddleNode(ListNode* node) {
    if (!node || !node->next) {
        return false;
    }
    node->val = node->next->val;
    node->next = node->next->next;
    return true;
}

void printList(ListNode* head) {
    bool first = true;
    while (head) {
        if (!first) std::cout << ' ';
        std::cout << head->val;
        first = false;
        head = head->next;
    }
    std::cout << '\n';
}

int main() {
    ListNode* head = buildList({1, 2, 3, 4, 5});
    ListNode* node = head->next->next;
    deleteMiddleNode(node);
    printList(head);
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_03_delete_middle_node.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func deleteMiddleNode(node *ListNode) bool {
	if node == nil || node.Next == nil {
		return false
	}
	node.Val = node.Next.Val
	node.Next = node.Next.Next
	return true
}

func printList(head *ListNode) {
	first := true
	for head != nil {
		if !first {
			fmt.Print(" ")
		}
		fmt.Print(head.Val)
		first = false
		head = head.Next
	}
	fmt.Println()
}

func main() {
	head := buildList([]int{1, 2, 3, 4, 5})
	deleteMiddleNode(head.Next.Next)
	printList(head)
}
```

<!-- REGISTRY_PATH: lcci_02_03_delete_middle_node.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def delete_middle_node(node: ListNode | None) -> bool:
    if node is None or node.next is None:
        return False
    node.val = node.next.val
    node.next = node.next.next
    return True


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    head = build_list([1, 2, 3, 4, 5])
    assert head and head.next and head.next.next
    delete_middle_node(head.next.next)
    print_list(head)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_03_delete_middle_node.languages.scala -->
### scala

```scala
object Lcci0203DeleteMiddleNode {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def deleteMiddleNode(node: ListNode | Null): Boolean = {
    if (node == null || node.asInstanceOf[ListNode].next == null) {
      return false
    }
    val cur = node.asInstanceOf[ListNode]
    val next = cur.next.asInstanceOf[ListNode]
    cur.value = next.value
    cur.next = next.next
    true
  }

  def printList(head: ListNode | Null): Unit = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      out += node.value
      cur = node.next
    }
    println(out.mkString(" "))
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(Vector(1, 2, 3, 4, 5)).asInstanceOf[ListNode]
    deleteMiddleNode(head.next.asInstanceOf[ListNode].next)
    printList(head)
  }
}
```

<!-- REGISTRY_PATH: lcci_02_03_delete_middle_node.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function deleteMiddleNode(node: ListNode | null): boolean {
  if (node === null || node.next === null) {
    return false;
  }
  node.val = node.next.val;
  node.next = node.next.next;
  return true;
}

function printList(head: ListNode | null): void {
  const out: number[] = [];
  while (head !== null) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
}

function main(): void {
  const head = buildList([1, 2, 3, 4, 5])!;
  deleteMiddleNode(head.next!.next!);
  printList(head);
}

main();
```

## lcci_02_04_partition_list

<!-- REGISTRY_PATH: lcci_02_04_partition_list.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

ListNode* partition(ListNode* head, int x) {
    ListNode lessDummy(0), greaterDummy(0);
    ListNode* lessTail = &lessDummy;
    ListNode* greaterTail = &greaterDummy;

    while (head) {
        if (head->val < x) {
            lessTail->next = head;
            lessTail = lessTail->next;
        } else {
            greaterTail->next = head;
            greaterTail = greaterTail->next;
        }
        head = head->next;
    }

    greaterTail->next = nullptr;
    lessTail->next = greaterDummy.next;
    return lessDummy.next;
}

void printList(ListNode* head) {
    bool first = true;
    while (head) {
        if (!first) std::cout << ' ';
        std::cout << head->val;
        first = false;
        head = head->next;
    }
    std::cout << '\n';
}

int main() {
    ListNode* head = buildList({3, 5, 8, 5, 10, 2, 1});
    head = partition(head, 5);
    printList(head);
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_04_partition_list.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func partition(head *ListNode, x int) *ListNode {
	lessDummy := &ListNode{}
	greaterDummy := &ListNode{}
	lessTail := lessDummy
	greaterTail := greaterDummy

	for head != nil {
		if head.Val < x {
			lessTail.Next = head
			lessTail = lessTail.Next
		} else {
			greaterTail.Next = head
			greaterTail = greaterTail.Next
		}
		head = head.Next
	}

	greaterTail.Next = nil
	lessTail.Next = greaterDummy.Next
	return lessDummy.Next
}

func printList(head *ListNode) {
	first := true
	for head != nil {
		if !first {
			fmt.Print(" ")
		}
		fmt.Print(head.Val)
		first = false
		head = head.Next
	}
	fmt.Println()
}

func main() {
	head := buildList([]int{3, 5, 8, 5, 10, 2, 1})
	head = partition(head, 5)
	printList(head)
}
```

<!-- REGISTRY_PATH: lcci_02_04_partition_list.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def partition(head: ListNode | None, x: int) -> ListNode | None:
    less_dummy = ListNode(0)
    greater_dummy = ListNode(0)
    less_tail = less_dummy
    greater_tail = greater_dummy

    while head is not None:
        if head.val < x:
            less_tail.next = head
            less_tail = less_tail.next
        else:
            greater_tail.next = head
            greater_tail = greater_tail.next
        head = head.next

    greater_tail.next = None
    less_tail.next = greater_dummy.next
    return less_dummy.next


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    head = build_list([3, 5, 8, 5, 10, 2, 1])
    print_list(partition(head, 5))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_04_partition_list.languages.scala -->
### scala

```scala
object Lcci0204PartitionList {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def partition(head: ListNode | Null, x: Int): ListNode | Null = {
    val lessDummy = ListNode(0, null)
    val greaterDummy = ListNode(0, null)
    var lessTail: ListNode = lessDummy
    var greaterTail: ListNode = greaterDummy
    var cur = head

    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      if (node.value < x) {
        lessTail.next = node
        lessTail = node
      } else {
        greaterTail.next = node
        greaterTail = node
      }
      cur = node.next
    }

    greaterTail.next = null
    lessTail.next = greaterDummy.next
    lessDummy.next
  }

  def printList(head: ListNode | Null): Unit = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      out += node.value
      cur = node.next
    }
    println(out.mkString(" "))
  }

  def main(args: Array[String]): Unit = {
    val head = buildList(Vector(3, 5, 8, 5, 10, 2, 1))
    printList(partition(head, 5))
  }
}
```

<!-- REGISTRY_PATH: lcci_02_04_partition_list.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function partition(head: ListNode | null, x: number): ListNode | null {
  const lessDummy = new ListNode(0);
  const greaterDummy = new ListNode(0);
  let lessTail = lessDummy;
  let greaterTail = greaterDummy;

  while (head !== null) {
    if (head.val < x) {
      lessTail.next = head;
      lessTail = lessTail.next;
    } else {
      greaterTail.next = head;
      greaterTail = greaterTail.next;
    }
    head = head.next;
  }

  greaterTail.next = null;
  lessTail.next = greaterDummy.next;
  return lessDummy.next;
}

function printList(head: ListNode | null): void {
  const out: number[] = [];
  while (head !== null) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
}

function main(): void {
  const head = buildList([3, 5, 8, 5, 10, 2, 1]);
  printList(partition(head, 5));
}

main();
```

## lcci_02_05_sum_lists

<!-- REGISTRY_PATH: lcci_02_05_sum_lists.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    int carry = 0;

    while (l1 || l2 || carry) {
        int sum = carry;
        if (l1) {
            sum += l1->val;
            l1 = l1->next;
        }
        if (l2) {
            sum += l2->val;
            l2 = l2->next;
        }

        tail->next = new ListNode(sum % 10);
        tail = tail->next;
        carry = sum / 10;
    }

    return dummy.next;
}

void printList(ListNode* head) {
    bool first = true;
    while (head) {
        if (!first) std::cout << ' ';
        std::cout << head->val;
        first = false;
        head = head->next;
    }
    std::cout << '\n';
}

int main() {
    ListNode* a = buildList({7, 1, 6}); // 617
    ListNode* b = buildList({5, 9, 2}); // 295
    ListNode* c = addTwoNumbers(a, b);  // 912 -> 2 1 9
    printList(c);
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_05_sum_lists.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func addTwoNumbers(l1, l2 *ListNode) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	carry := 0

	for l1 != nil || l2 != nil || carry > 0 {
		sum := carry
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}
		tail.Next = &ListNode{Val: sum % 10}
		tail = tail.Next
		carry = sum / 10
	}

	return dummy.Next
}

func printList(head *ListNode) {
	first := true
	for head != nil {
		if !first {
			fmt.Print(" ")
		}
		fmt.Print(head.Val)
		first = false
		head = head.Next
	}
	fmt.Println()
}

func main() {
	a := buildList([]int{7, 1, 6})
	b := buildList([]int{5, 9, 2})
	c := addTwoNumbers(a, b)
	printList(c)
}
```

<!-- REGISTRY_PATH: lcci_02_05_sum_lists.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry:
        total = carry
        if l1 is not None:
            total += l1.val
            l1 = l1.next
        if l2 is not None:
            total += l2.val
            l2 = l2.next

        tail.next = ListNode(total % 10)
        tail = tail.next
        carry = total // 10

    return dummy.next


def print_list(head: ListNode | None) -> None:
    out: list[str] = []
    while head is not None:
        out.append(str(head.val))
        head = head.next
    print(" ".join(out))


def main() -> None:
    a = build_list([7, 1, 6])
    b = build_list([5, 9, 2])
    print_list(add_two_numbers(a, b))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_05_sum_lists.languages.scala -->
### scala

```scala
object Lcci0205SumLists {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def addTwoNumbers(a: ListNode | Null, b: ListNode | Null): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    var l1 = a
    var l2 = b
    var carry = 0

    while (l1 != null || l2 != null || carry > 0) {
      var sum = carry
      if (l1 != null) {
        sum += l1.asInstanceOf[ListNode].value
        l1 = l1.asInstanceOf[ListNode].next
      }
      if (l2 != null) {
        sum += l2.asInstanceOf[ListNode].value
        l2 = l2.asInstanceOf[ListNode].next
      }
      tail.next = ListNode(sum % 10, null)
      tail = tail.next.asInstanceOf[ListNode]
      carry = sum / 10
    }

    dummy.next
  }

  def printList(head: ListNode | Null): Unit = {
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    var cur = head
    while (cur != null) {
      out += cur.asInstanceOf[ListNode].value
      cur = cur.asInstanceOf[ListNode].next
    }
    println(out.mkString(" "))
  }

  def main(args: Array[String]): Unit = {
    val a = buildList(Vector(7, 1, 6))
    val b = buildList(Vector(5, 9, 2))
    printList(addTwoNumbers(a, b))
  }
}
```

<!-- REGISTRY_PATH: lcci_02_05_sum_lists.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  let carry = 0;

  while (l1 !== null || l2 !== null || carry > 0) {
    let sum = carry;
    if (l1 !== null) {
      sum += l1.val;
      l1 = l1.next;
    }
    if (l2 !== null) {
      sum += l2.val;
      l2 = l2.next;
    }

    tail.next = new ListNode(sum % 10);
    tail = tail.next;
    carry = Math.floor(sum / 10);
  }

  return dummy.next;
}

function printList(head: ListNode | null): void {
  const out: number[] = [];
  while (head !== null) {
    out.push(head.val);
    head = head.next;
  }
  console.log(out.join(" "));
}

function main(): void {
  const a = buildList([7, 1, 6]);
  const b = buildList([5, 9, 2]);
  printList(addTwoNumbers(a, b));
}

main();
```

## lcci_02_06_palindrome_linked_list

<!-- REGISTRY_PATH: lcci_02_06_palindrome_linked_list.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

ListNode* reverseList(ListNode* head) {
    ListNode* prev = nullptr;
    while (head) {
        ListNode* nextNode = head->next;
        head->next = prev;
        prev = head;
        head = nextNode;
    }
    return prev;
}

bool isPalindrome(ListNode* head) {
    if (!head || !head->next) return true;

    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    ListNode* secondHalf = reverseList(slow);
    ListNode* p1 = head;
    ListNode* p2 = secondHalf;

    while (p2) {
        if (p1->val != p2->val) return false;
        p1 = p1->next;
        p2 = p2->next;
    }
    return true;
}

int main() {
    ListNode* a = buildList({1, 2, 2, 1});
    ListNode* b = buildList({1, 2, 3, 2, 1});
    std::cout << std::boolalpha << isPalindrome(a) << '\n';
    std::cout << std::boolalpha << isPalindrome(b) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_06_palindrome_linked_list.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func reverseList(head *ListNode) *ListNode {
	var prev *ListNode
	for head != nil {
		nextNode := head.Next
		head.Next = prev
		prev = head
		head = nextNode
	}
	return prev
}

func isPalindrome(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return true
	}

	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
	}

	second := reverseList(slow)
	p1, p2 := head, second
	for p2 != nil {
		if p1.Val != p2.Val {
			return false
		}
		p1 = p1.Next
		p2 = p2.Next
	}
	return true
}

func main() {
	a := buildList([]int{1, 2, 2, 1})
	b := buildList([]int{1, 2, 3, 2, 1})
	fmt.Println(isPalindrome(a))
	fmt.Println(isPalindrome(b))
}
```

<!-- REGISTRY_PATH: lcci_02_06_palindrome_linked_list.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    while head is not None:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev


def is_palindrome(head: ListNode | None) -> bool:
    if head is None or head.next is None:
        return True

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    second = reverse_list(slow)
    p1 = head
    p2 = second
    while p2 is not None:
        if p1 is None or p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True


def main() -> None:
    a = build_list([1, 2, 2, 1])
    b = build_list([1, 2, 3, 2, 1])
    print(is_palindrome(a))
    print(is_palindrome(b))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_06_palindrome_linked_list.languages.scala -->
### scala

```scala
object Lcci0206PalindromeLinkedList {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def reverseList(head: ListNode | Null): ListNode | Null = {
    var prev: ListNode | Null = null
    var cur = head
    while (cur != null) {
      val node = cur.asInstanceOf[ListNode]
      val nextNode = node.next
      node.next = prev
      prev = node
      cur = nextNode
    }
    prev
  }

  def isPalindrome(head: ListNode | Null): Boolean = {
    if (head == null || head.asInstanceOf[ListNode].next == null) return true

    var slow = head
    var fast = head
    while (fast != null && fast.asInstanceOf[ListNode].next != null) {
      slow = slow.asInstanceOf[ListNode].next
      fast = fast.asInstanceOf[ListNode].next.asInstanceOf[ListNode].next
    }

    var p1 = head
    var p2 = reverseList(slow)
    while (p2 != null) {
      if (p1.asInstanceOf[ListNode].value != p2.asInstanceOf[ListNode].value) return false
      p1 = p1.asInstanceOf[ListNode].next
      p2 = p2.asInstanceOf[ListNode].next
    }
    true
  }

  def main(args: Array[String]): Unit = {
    val a = buildList(Vector(1, 2, 2, 1))
    val b = buildList(Vector(1, 2, 3, 2, 1))
    println(isPalindrome(a))
    println(isPalindrome(b))
  }
}
```

<!-- REGISTRY_PATH: lcci_02_06_palindrome_linked_list.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function reverseList(head: ListNode | null): ListNode | null {
  let prev: ListNode | null = null;
  while (head !== null) {
    const nextNode = head.next;
    head.next = prev;
    prev = head;
    head = nextNode;
  }
  return prev;
}

function isPalindrome(head: ListNode | null): boolean {
  if (head === null || head.next === null) {
    return true;
  }

  let slow: ListNode | null = head;
  let fast: ListNode | null = head;
  while (fast !== null && fast.next !== null) {
    slow = slow!.next;
    fast = fast.next.next;
  }

  let p1: ListNode | null = head;
  let p2: ListNode | null = reverseList(slow);
  while (p2 !== null) {
    if (p1 === null || p1.val !== p2.val) {
      return false;
    }
    p1 = p1.next;
    p2 = p2.next;
  }
  return true;
}

function main(): void {
  const a = buildList([1, 2, 2, 1]);
  const b = buildList([1, 2, 3, 2, 1]);
  console.log(isPalindrome(a));
  console.log(isPalindrome(b));
}

main();
```

## lcci_02_07_intersection_of_two_linked_lists

<!-- REGISTRY_PATH: lcci_02_07_intersection_of_two_linked_lists.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

ListNode* getIntersectionNode(ListNode* a, ListNode* b) {
    if (!a || !b) return nullptr;
    ListNode* p1 = a;
    ListNode* p2 = b;
    while (p1 != p2) {
        p1 = p1 ? p1->next : b;
        p2 = p2 ? p2->next : a;
    }
    return p1;
}

int main() {
    ListNode* common = buildList({8, 10});

    ListNode* a = buildList({3, 1, 5, 9});
    ListNode* b = buildList({4, 6});

    ListNode* tailA = a;
    while (tailA->next) tailA = tailA->next;
    tailA->next = common;

    ListNode* tailB = b;
    while (tailB->next) tailB = tailB->next;
    tailB->next = common;

    ListNode* intersection = getIntersectionNode(a, b);
    if (intersection) {
        std::cout << intersection->val << '\n';
    } else {
        std::cout << "null\n";
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_07_intersection_of_two_linked_lists.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func getIntersectionNode(a, b *ListNode) *ListNode {
	if a == nil || b == nil {
		return nil
	}

	p1, p2 := a, b
	for p1 != p2 {
		if p1 != nil {
			p1 = p1.Next
		} else {
			p1 = b
		}
		if p2 != nil {
			p2 = p2.Next
		} else {
			p2 = a
		}
	}
	return p1
}

func main() {
	common := buildList([]int{8, 10})
	a := buildList([]int{3, 1, 5, 9})
	b := buildList([]int{4, 6})

	tailA := a
	for tailA.Next != nil {
		tailA = tailA.Next
	}
	tailA.Next = common

	tailB := b
	for tailB.Next != nil {
		tailB = tailB.Next
	}
	tailB.Next = common

	node := getIntersectionNode(a, b)
	if node != nil {
		fmt.Println(node.Val)
	} else {
		fmt.Println("null")
	}
}
```

<!-- REGISTRY_PATH: lcci_02_07_intersection_of_two_linked_lists.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def get_intersection_node(a: ListNode | None, b: ListNode | None) -> ListNode | None:
    if a is None or b is None:
        return None

    p1, p2 = a, b
    while p1 is not p2:
        p1 = p1.next if p1 is not None else b
        p2 = p2.next if p2 is not None else a
    return p1


def main() -> None:
    common = build_list([8, 10])

    a = build_list([3, 1, 5, 9])
    b = build_list([4, 6])

    tail_a = a
    while tail_a is not None and tail_a.next is not None:
        tail_a = tail_a.next
    if tail_a is not None:
        tail_a.next = common

    tail_b = b
    while tail_b is not None and tail_b.next is not None:
        tail_b = tail_b.next
    if tail_b is not None:
        tail_b.next = common

    node = get_intersection_node(a, b)
    print(node.val if node else "null")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_07_intersection_of_two_linked_lists.languages.scala -->
### scala

```scala
object Lcci0207IntersectionOfTwoLinkedLists {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def getIntersectionNode(a: ListNode | Null, b: ListNode | Null): ListNode | Null = {
    if (a == null || b == null) return null

    var p1 = a
    var p2 = b
    while (p1 != p2) {
      p1 = if (p1 != null) p1.asInstanceOf[ListNode].next else b
      p2 = if (p2 != null) p2.asInstanceOf[ListNode].next else a
    }
    p1
  }

  def main(args: Array[String]): Unit = {
    val common = buildList(Vector(8, 10))
    val a = buildList(Vector(3, 1, 5, 9))
    val b = buildList(Vector(4, 6))

    var tailA = a
    while (tailA != null && tailA.asInstanceOf[ListNode].next != null) {
      tailA = tailA.asInstanceOf[ListNode].next
    }
    if (tailA != null) {
      tailA.asInstanceOf[ListNode].next = common
    }

    var tailB = b
    while (tailB != null && tailB.asInstanceOf[ListNode].next != null) {
      tailB = tailB.asInstanceOf[ListNode].next
    }
    if (tailB != null) {
      tailB.asInstanceOf[ListNode].next = common
    }

    val node = getIntersectionNode(a, b)
    println(if (node != null) node.asInstanceOf[ListNode].value else "null")
  }
}
```

<!-- REGISTRY_PATH: lcci_02_07_intersection_of_two_linked_lists.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function getIntersectionNode(a: ListNode | null, b: ListNode | null): ListNode | null {
  if (a === null || b === null) {
    return null;
  }

  let p1: ListNode | null = a;
  let p2: ListNode | null = b;
  while (p1 !== p2) {
    p1 = p1 !== null ? p1.next : b;
    p2 = p2 !== null ? p2.next : a;
  }
  return p1;
}

function main(): void {
  const common = buildList([8, 10]);
  const a = buildList([3, 1, 5, 9]);
  const b = buildList([4, 6]);

  let tailA = a;
  while (tailA !== null && tailA.next !== null) {
    tailA = tailA.next;
  }
  if (tailA !== null) {
    tailA.next = common;
  }

  let tailB = b;
  while (tailB !== null && tailB.next !== null) {
    tailB = tailB.next;
  }
  if (tailB !== null) {
    tailB.next = common;
  }

  const node = getIntersectionNode(a, b);
  console.log(node ? node.val : "null");
}

main();
```

## lcci_02_08_linked_list_cycle

<!-- REGISTRY_PATH: lcci_02_08_linked_list_cycle.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct ListNode {
    int val;
    ListNode* next;
    ListNode(int v) : val(v), next(nullptr) {}
};

ListNode* buildList(const std::vector<int>& nums) {
    ListNode dummy(0);
    ListNode* tail = &dummy;
    for (int n : nums) {
        tail->next = new ListNode(n);
        tail = tail->next;
    }
    return dummy.next;
}

bool hasCycle(ListNode* head) {
    ListNode* slow = head;
    ListNode* fast = head;
    while (fast && fast->next) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) return true;
    }
    return false;
}

int main() {
    ListNode* a = buildList({1, 2, 3, 4});
    ListNode* tail = a;
    while (tail->next) tail = tail->next;
    tail->next = a->next; // create cycle

    ListNode* b = buildList({1, 2, 3, 4});

    std::cout << std::boolalpha << hasCycle(a) << '\n';
    std::cout << std::boolalpha << hasCycle(b) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_02_08_linked_list_cycle.languages.go -->
### go

```go
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func buildList(nums []int) *ListNode {
	dummy := &ListNode{}
	tail := dummy
	for _, n := range nums {
		tail.Next = &ListNode{Val: n}
		tail = tail.Next
	}
	return dummy.Next
}

func hasCycle(head *ListNode) bool {
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			return true
		}
	}
	return false
}

func main() {
	a := buildList([]int{1, 2, 3, 4})
	tail := a
	for tail.Next != nil {
		tail = tail.Next
	}
	tail.Next = a.Next

	b := buildList([]int{1, 2, 3, 4})

	fmt.Println(hasCycle(a))
	fmt.Println(hasCycle(b))
}
```

<!-- REGISTRY_PATH: lcci_02_08_linked_list_cycle.languages.python -->
### python

```python
class ListNode:
    def __init__(self, val: int, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def build_list(nums: list[int]) -> ListNode | None:
    dummy = ListNode(0)
    tail = dummy
    for n in nums:
        tail.next = ListNode(n)
        tail = tail.next
    return dummy.next


def has_cycle(head: ListNode | None) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next if slow is not None else None
        fast = fast.next.next
        if slow is fast:
            return True
    return False


def main() -> None:
    a = build_list([1, 2, 3, 4])
    tail = a
    while tail is not None and tail.next is not None:
        tail = tail.next
    if tail is not None and a is not None and a.next is not None:
        tail.next = a.next

    b = build_list([1, 2, 3, 4])

    print(has_cycle(a))
    print(has_cycle(b))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_02_08_linked_list_cycle.languages.scala -->
### scala

```scala
object Lcci0208LinkedListCycle {
  final case class ListNode(var value: Int, var next: ListNode | Null = null)

  def buildList(nums: Vector[Int]): ListNode | Null = {
    val dummy = ListNode(0, null)
    var tail: ListNode = dummy
    nums.foreach { n =>
      tail.next = ListNode(n, null)
      tail = tail.next.asInstanceOf[ListNode]
    }
    dummy.next
  }

  def hasCycle(head: ListNode | Null): Boolean = {
    var slow = head
    var fast = head
    while (fast != null && fast.asInstanceOf[ListNode].next != null) {
      slow = slow.asInstanceOf[ListNode].next
      fast = fast.asInstanceOf[ListNode].next.asInstanceOf[ListNode].next
      if (slow == fast) return true
    }
    false
  }

  def main(args: Array[String]): Unit = {
    val a = buildList(Vector(1, 2, 3, 4))
    var tail = a
    while (tail != null && tail.asInstanceOf[ListNode].next != null) {
      tail = tail.asInstanceOf[ListNode].next
    }
    if (tail != null && a != null && a.asInstanceOf[ListNode].next != null) {
      tail.asInstanceOf[ListNode].next = a.asInstanceOf[ListNode].next
    }

    val b = buildList(Vector(1, 2, 3, 4))

    println(hasCycle(a))
    println(hasCycle(b))
  }
}
```

<!-- REGISTRY_PATH: lcci_02_08_linked_list_cycle.languages.typescript -->
### typescript

```typescript
class ListNode {
  val: number;
  next: ListNode | null;

  constructor(val: number, next: ListNode | null = null) {
    this.val = val;
    this.next = next;
  }
}

function buildList(nums: number[]): ListNode | null {
  const dummy = new ListNode(0);
  let tail = dummy;
  for (const n of nums) {
    tail.next = new ListNode(n);
    tail = tail.next;
  }
  return dummy.next;
}

function hasCycle(head: ListNode | null): boolean {
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;
  while (fast !== null && fast.next !== null) {
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) {
      return true;
    }
  }
  return false;
}

function main(): void {
  const a = buildList([1, 2, 3, 4]);
  let tail = a;
  while (tail !== null && tail.next !== null) {
    tail = tail.next;
  }
  if (tail !== null && a !== null && a.next !== null) {
    tail.next = a.next;
  }

  const b = buildList([1, 2, 3, 4]);

  console.log(hasCycle(a));
  console.log(hasCycle(b));
}

main();
```

## lcci_03_01_three_in_one

<!-- REGISTRY_PATH: lcci_03_01_three_in_one.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

class TripleInOne {
public:
    TripleInOne(int stackSize)
        : size(stackSize), data(3 * stackSize, 0), tops(3, 0) {}

    void push(int stackNum, int value) {
        if (isFull(stackNum)) return;
        int index = stackNum * size + tops[stackNum];
        data[index] = value;
        tops[stackNum]++;
    }

    int pop(int stackNum) {
        if (isEmpty(stackNum)) return -1;
        tops[stackNum]--;
        int index = stackNum * size + tops[stackNum];
        return data[index];
    }

    int peek(int stackNum) const {
        if (isEmpty(stackNum)) return -1;
        int index = stackNum * size + tops[stackNum] - 1;
        return data[index];
    }

    bool isEmpty(int stackNum) const {
        return tops[stackNum] == 0;
    }

private:
    int size;
    std::vector<int> data;
    std::vector<int> tops;

    bool isFull(int stackNum) const {
        return tops[stackNum] == size;
    }
};

int main() {
    TripleInOne stacks(2);
    stacks.push(0, 10);
    stacks.push(0, 11);
    stacks.push(0, 12);
    stacks.push(1, 20);
    std::cout << stacks.peek(0) << '\n';
    std::cout << stacks.pop(0) << '\n';
    std::cout << stacks.pop(0) << '\n';
    std::cout << stacks.pop(0) << '\n';
    std::cout << std::boolalpha << stacks.isEmpty(1) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_03_01_three_in_one.languages.go -->
### go

```go
package main

import "fmt"

type TripleInOne struct {
	size int
	data []int
	tops [3]int
}

func NewTripleInOne(stackSize int) *TripleInOne {
	return &TripleInOne{
		size: stackSize,
		data: make([]int, 3*stackSize),
	}
}

func (t *TripleInOne) Push(stackNum int, value int) {
	if t.tops[stackNum] == t.size {
		return
	}
	index := stackNum*t.size + t.tops[stackNum]
	t.data[index] = value
	t.tops[stackNum]++
}

func (t *TripleInOne) Pop(stackNum int) int {
	if t.tops[stackNum] == 0 {
		return -1
	}
	t.tops[stackNum]--
	index := stackNum*t.size + t.tops[stackNum]
	return t.data[index]
}

func (t *TripleInOne) Peek(stackNum int) int {
	if t.tops[stackNum] == 0 {
		return -1
	}
	index := stackNum*t.size + t.tops[stackNum] - 1
	return t.data[index]
}

func (t *TripleInOne) IsEmpty(stackNum int) bool {
	return t.tops[stackNum] == 0
}

func main() {
	s := NewTripleInOne(2)
	s.Push(0, 10)
	s.Push(0, 11)
	s.Push(0, 12)
	s.Push(1, 20)
	fmt.Println(s.Peek(0))
	fmt.Println(s.Pop(0))
	fmt.Println(s.Pop(0))
	fmt.Println(s.Pop(0))
	fmt.Println(s.IsEmpty(1))
}
```

<!-- REGISTRY_PATH: lcci_03_01_three_in_one.languages.python -->
### python

```python
class TripleInOne:
    def __init__(self, stack_size: int) -> None:
        self.size = stack_size
        self.data = [0] * (3 * stack_size)
        self.tops = [0, 0, 0]

    def push(self, stack_num: int, value: int) -> None:
        if self.tops[stack_num] == self.size:
            return
        index = stack_num * self.size + self.tops[stack_num]
        self.data[index] = value
        self.tops[stack_num] += 1

    def pop(self, stack_num: int) -> int:
        if self.tops[stack_num] == 0:
            return -1
        self.tops[stack_num] -= 1
        index = stack_num * self.size + self.tops[stack_num]
        return self.data[index]

    def peek(self, stack_num: int) -> int:
        if self.tops[stack_num] == 0:
            return -1
        index = stack_num * self.size + self.tops[stack_num] - 1
        return self.data[index]

    def is_empty(self, stack_num: int) -> bool:
        return self.tops[stack_num] == 0


def main() -> None:
    stacks = TripleInOne(2)
    stacks.push(0, 10)
    stacks.push(0, 11)
    stacks.push(0, 12)
    stacks.push(1, 20)
    print(stacks.peek(0))
    print(stacks.pop(0))
    print(stacks.pop(0))
    print(stacks.pop(0))
    print(stacks.is_empty(1))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_03_01_three_in_one.languages.scala -->
### scala

```scala
object Lcci0301ThreeInOne {
  final class TripleInOne(stackSize: Int) {
    private val size = stackSize
    private val data = Array.fill(3 * stackSize)(0)
    private val tops = Array(0, 0, 0)

    def push(stackNum: Int, value: Int): Unit = {
      if (tops(stackNum) == size) return
      val index = stackNum * size + tops(stackNum)
      data(index) = value
      tops(stackNum) += 1
    }

    def pop(stackNum: Int): Int = {
      if (tops(stackNum) == 0) return -1
      tops(stackNum) -= 1
      val index = stackNum * size + tops(stackNum)
      data(index)
    }

    def peek(stackNum: Int): Int = {
      if (tops(stackNum) == 0) return -1
      val index = stackNum * size + tops(stackNum) - 1
      data(index)
    }

    def isEmpty(stackNum: Int): Boolean = tops(stackNum) == 0
  }

  def main(args: Array[String]): Unit = {
    val stacks = new TripleInOne(2)
    stacks.push(0, 10)
    stacks.push(0, 11)
    stacks.push(0, 12)
    stacks.push(1, 20)
    println(stacks.peek(0))
    println(stacks.pop(0))
    println(stacks.pop(0))
    println(stacks.pop(0))
    println(stacks.isEmpty(1))
  }
}
```

<!-- REGISTRY_PATH: lcci_03_01_three_in_one.languages.typescript -->
### typescript

```typescript
class TripleInOne {
  private readonly size: number;
  private readonly data: number[];
  private readonly tops: number[];

  constructor(stackSize: number) {
    this.size = stackSize;
    this.data = new Array(3 * stackSize).fill(0);
    this.tops = [0, 0, 0];
  }

  push(stackNum: number, value: number): void {
    if (this.tops[stackNum] === this.size) {
      return;
    }
    const index = stackNum * this.size + this.tops[stackNum];
    this.data[index] = value;
    this.tops[stackNum] += 1;
  }

  pop(stackNum: number): number {
    if (this.tops[stackNum] === 0) {
      return -1;
    }
    this.tops[stackNum] -= 1;
    const index = stackNum * this.size + this.tops[stackNum];
    return this.data[index];
  }

  peek(stackNum: number): number {
    if (this.tops[stackNum] === 0) {
      return -1;
    }
    const index = stackNum * this.size + this.tops[stackNum] - 1;
    return this.data[index];
  }

  isEmpty(stackNum: number): boolean {
    return this.tops[stackNum] === 0;
  }
}

function main(): void {
  const stacks = new TripleInOne(2);
  stacks.push(0, 10);
  stacks.push(0, 11);
  stacks.push(0, 12);
  stacks.push(1, 20);
  console.log(stacks.peek(0));
  console.log(stacks.pop(0));
  console.log(stacks.pop(0));
  console.log(stacks.pop(0));
  console.log(stacks.isEmpty(1));
}

main();
```

## lcci_03_02_min_stack

<!-- REGISTRY_PATH: lcci_03_02_min_stack.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <stack>

class MinStack {
public:
    void push(int x) {
        values.push(x);
        if (mins.empty() || x <= mins.top()) {
            mins.push(x);
        }
    }

    void pop() {
        if (values.empty()) return;
        if (values.top() == mins.top()) {
            mins.pop();
        }
        values.pop();
    }

    int top() const {
        return values.empty() ? -1 : values.top();
    }

    int getMin() const {
        return mins.empty() ? -1 : mins.top();
    }

private:
    std::stack<int> values;
    std::stack<int> mins;
};

int main() {
    MinStack st;
    st.push(3);
    st.push(5);
    st.push(2);
    st.push(2);
    std::cout << st.getMin() << '\n';
    st.pop();
    std::cout << st.getMin() << '\n';
    st.pop();
    std::cout << st.getMin() << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_03_02_min_stack.languages.go -->
### go

```go
package main

import "fmt"

type MinStack struct {
	values []int
	mins   []int
}

func (m *MinStack) Push(x int) {
	m.values = append(m.values, x)
	if len(m.mins) == 0 || x <= m.mins[len(m.mins)-1] {
		m.mins = append(m.mins, x)
	}
}

func (m *MinStack) Pop() {
	if len(m.values) == 0 {
		return
	}
	top := m.values[len(m.values)-1]
	if top == m.mins[len(m.mins)-1] {
		m.mins = m.mins[:len(m.mins)-1]
	}
	m.values = m.values[:len(m.values)-1]
}

func (m *MinStack) Top() int {
	if len(m.values) == 0 {
		return -1
	}
	return m.values[len(m.values)-1]
}

func (m *MinStack) GetMin() int {
	if len(m.mins) == 0 {
		return -1
	}
	return m.mins[len(m.mins)-1]
}

func main() {
	st := &MinStack{}
	st.Push(3)
	st.Push(5)
	st.Push(2)
	st.Push(2)
	fmt.Println(st.GetMin())
	st.Pop()
	fmt.Println(st.GetMin())
	st.Pop()
	fmt.Println(st.GetMin())
}
```

<!-- REGISTRY_PATH: lcci_03_02_min_stack.languages.python -->
### python

```python
class MinStack:
    def __init__(self) -> None:
        self.values: list[int] = []
        self.mins: list[int] = []

    def push(self, x: int) -> None:
        self.values.append(x)
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)

    def pop(self) -> None:
        if not self.values:
            return
        if self.values[-1] == self.mins[-1]:
            self.mins.pop()
        self.values.pop()

    def top(self) -> int:
        return self.values[-1] if self.values else -1

    def get_min(self) -> int:
        return self.mins[-1] if self.mins else -1


def main() -> None:
    st = MinStack()
    st.push(3)
    st.push(5)
    st.push(2)
    st.push(2)
    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_03_02_min_stack.languages.scala -->
### scala

```scala
object Lcci0302MinStack {
  final class MinStack {
    private val values = scala.collection.mutable.ArrayBuffer.empty[Int]
    private val mins = scala.collection.mutable.ArrayBuffer.empty[Int]

    def push(x: Int): Unit = {
      values += x
      if (mins.isEmpty || x <= mins.last) mins += x
    }

    def pop(): Unit = {
      if (values.isEmpty) return
      val top = values.remove(values.length - 1)
      if (top == mins.last) mins.remove(mins.length - 1)
    }

    def top(): Int = if (values.isEmpty) -1 else values.last

    def getMin(): Int = if (mins.isEmpty) -1 else mins.last
  }

  def main(args: Array[String]): Unit = {
    val st = new MinStack
    st.push(3)
    st.push(5)
    st.push(2)
    st.push(2)
    println(st.getMin())
    st.pop()
    println(st.getMin())
    st.pop()
    println(st.getMin())
  }
}
```

<!-- REGISTRY_PATH: lcci_03_02_min_stack.languages.typescript -->
### typescript

```typescript
class MinStack {
  private readonly values: number[] = [];
  private readonly mins: number[] = [];

  push(x: number): void {
    this.values.push(x);
    if (this.mins.length === 0 || x <= this.mins[this.mins.length - 1]) {
      this.mins.push(x);
    }
  }

  pop(): void {
    if (this.values.length === 0) {
      return;
    }
    const top = this.values.pop()!;
    if (top === this.mins[this.mins.length - 1]) {
      this.mins.pop();
    }
  }

  top(): number {
    return this.values.length ? this.values[this.values.length - 1] : -1;
  }

  getMin(): number {
    return this.mins.length ? this.mins[this.mins.length - 1] : -1;
  }
}

function main(): void {
  const st = new MinStack();
  st.push(3);
  st.push(5);
  st.push(2);
  st.push(2);
  console.log(st.getMin());
  st.pop();
  console.log(st.getMin());
  st.pop();
  console.log(st.getMin());
}

main();
```

## lcci_03_03_stack_of_plates

<!-- REGISTRY_PATH: lcci_03_03_stack_of_plates.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

class StackOfPlates {
public:
    explicit StackOfPlates(int cap) : capacity(cap) {}

    void push(int val) {
        if (capacity <= 0) return;
        if (stacks.empty() || stacks.back().size() == static_cast<size_t>(capacity)) {
            stacks.push_back({});
        }
        stacks.back().push_back(val);
    }

    int pop() {
        return popAt(static_cast<int>(stacks.size()) - 1);
    }

    int popAt(int index) {
        if (index < 0 || index >= static_cast<int>(stacks.size()) || stacks[index].empty()) {
            return -1;
        }
        int val = stacks[index].back();
        stacks[index].pop_back();
        if (stacks[index].empty()) {
            stacks.erase(stacks.begin() + index);
        }
        return val;
    }

private:
    int capacity;
    std::vector<std::vector<int>> stacks;
};

int main() {
    StackOfPlates s(2);
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    std::cout << s.popAt(0) << '\n';
    std::cout << s.pop() << '\n';
    std::cout << s.pop() << '\n';
    std::cout << s.pop() << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_03_03_stack_of_plates.languages.go -->
### go

```go
package main

import "fmt"

type StackOfPlates struct {
	cap    int
	stacks [][]int
}

func NewStackOfPlates(capacity int) *StackOfPlates {
	return &StackOfPlates{cap: capacity}
}

func (s *StackOfPlates) Push(val int) {
	if s.cap <= 0 {
		return
	}
	if len(s.stacks) == 0 || len(s.stacks[len(s.stacks)-1]) == s.cap {
		s.stacks = append(s.stacks, []int{})
	}
	last := len(s.stacks) - 1
	s.stacks[last] = append(s.stacks[last], val)
}

func (s *StackOfPlates) Pop() int {
	return s.PopAt(len(s.stacks) - 1)
}

func (s *StackOfPlates) PopAt(index int) int {
	if index < 0 || index >= len(s.stacks) || len(s.stacks[index]) == 0 {
		return -1
	}
	last := len(s.stacks[index]) - 1
	val := s.stacks[index][last]
	s.stacks[index] = s.stacks[index][:last]
	if len(s.stacks[index]) == 0 {
		s.stacks = append(s.stacks[:index], s.stacks[index+1:]...)
	}
	return val
}

func main() {
	s := NewStackOfPlates(2)
	s.Push(1)
	s.Push(2)
	s.Push(3)
	s.Push(4)
	fmt.Println(s.PopAt(0))
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
	fmt.Println(s.Pop())
}
```

<!-- REGISTRY_PATH: lcci_03_03_stack_of_plates.languages.python -->
### python

```python
class StackOfPlates:
    def __init__(self, cap: int) -> None:
        self.cap = cap
        self.stacks: list[list[int]] = []

    def push(self, val: int) -> None:
        if self.cap <= 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self.cap:
            self.stacks.append([])
        self.stacks[-1].append(val)

    def pop(self) -> int:
        return self.pop_at(len(self.stacks) - 1)

    def pop_at(self, index: int) -> int:
        if index < 0 or index >= len(self.stacks) or not self.stacks[index]:
            return -1
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return val


def main() -> None:
    s = StackOfPlates(2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s.pop_at(0))
    print(s.pop())
    print(s.pop())
    print(s.pop())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_03_03_stack_of_plates.languages.scala -->
### scala

```scala
object Lcci0303StackOfPlates {
  final class StackOfPlates(capacity: Int) {
    private val stacks = scala.collection.mutable.ArrayBuffer.empty[scala.collection.mutable.ArrayBuffer[Int]]

    def push(value: Int): Unit = {
      if (capacity <= 0) return
      if (stacks.isEmpty || stacks.last.length == capacity) {
        stacks += scala.collection.mutable.ArrayBuffer.empty[Int]
      }
      stacks.last += value
    }

    def pop(): Int = popAt(stacks.length - 1)

    def popAt(index: Int): Int = {
      if (index < 0 || index >= stacks.length || stacks(index).isEmpty) return -1
      val value = stacks(index).remove(stacks(index).length - 1)
      if (stacks(index).isEmpty) stacks.remove(index)
      value
    }
  }

  def main(args: Array[String]): Unit = {
    val s = new StackOfPlates(2)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    println(s.popAt(0))
    println(s.pop())
    println(s.pop())
    println(s.pop())
  }
}
```

<!-- REGISTRY_PATH: lcci_03_03_stack_of_plates.languages.typescript -->
### typescript

```typescript
class StackOfPlates {
  private readonly cap: number;
  private stacks: number[][] = [];

  constructor(capacity: number) {
    this.cap = capacity;
  }

  push(val: number): void {
    if (this.cap <= 0) {
      return;
    }
    if (this.stacks.length === 0 || this.stacks[this.stacks.length - 1].length === this.cap) {
      this.stacks.push([]);
    }
    this.stacks[this.stacks.length - 1].push(val);
  }

  pop(): number {
    return this.popAt(this.stacks.length - 1);
  }

  popAt(index: number): number {
    if (index < 0 || index >= this.stacks.length || this.stacks[index].length === 0) {
      return -1;
    }
    const val = this.stacks[index].pop()!;
    if (this.stacks[index].length === 0) {
      this.stacks.splice(index, 1);
    }
    return val;
  }
}

function main(): void {
  const s = new StackOfPlates(2);
  s.push(1);
  s.push(2);
  s.push(3);
  s.push(4);
  console.log(s.popAt(0));
  console.log(s.pop());
  console.log(s.pop());
  console.log(s.pop());
}

main();
```

## lcci_03_04_queue_via_stacks

<!-- REGISTRY_PATH: lcci_03_04_queue_via_stacks.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <stack>

class MyQueue {
public:
    void push(int x) {
        in.push(x);
    }

    int pop() {
        moveIfNeeded();
        if (out.empty()) return -1;
        int v = out.top();
        out.pop();
        return v;
    }

    int peek() {
        moveIfNeeded();
        return out.empty() ? -1 : out.top();
    }

    bool empty() const {
        return in.empty() && out.empty();
    }

private:
    std::stack<int> in;
    std::stack<int> out;

    void moveIfNeeded() {
        if (!out.empty()) return;
        while (!in.empty()) {
            out.push(in.top());
            in.pop();
        }
    }
};

int main() {
    MyQueue q;
    q.push(1);
    q.push(2);
    q.push(3);
    std::cout << q.peek() << '\n';
    std::cout << q.pop() << '\n';
    std::cout << q.pop() << '\n';
    std::cout << std::boolalpha << q.empty() << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_03_04_queue_via_stacks.languages.go -->
### go

```go
package main

import "fmt"

type MyQueue struct {
	inStack  []int
	outStack []int
}

func (q *MyQueue) Push(x int) {
	q.inStack = append(q.inStack, x)
}

func (q *MyQueue) moveIfNeeded() {
	if len(q.outStack) > 0 {
		return
	}
	for len(q.inStack) > 0 {
		n := len(q.inStack) - 1
		q.outStack = append(q.outStack, q.inStack[n])
		q.inStack = q.inStack[:n]
	}
}

func (q *MyQueue) Pop() int {
	q.moveIfNeeded()
	if len(q.outStack) == 0 {
		return -1
	}
	n := len(q.outStack) - 1
	v := q.outStack[n]
	q.outStack = q.outStack[:n]
	return v
}

func (q *MyQueue) Peek() int {
	q.moveIfNeeded()
	if len(q.outStack) == 0 {
		return -1
	}
	return q.outStack[len(q.outStack)-1]
}

func (q *MyQueue) Empty() bool {
	return len(q.inStack) == 0 && len(q.outStack) == 0
}

func main() {
	q := &MyQueue{}
	q.Push(1)
	q.Push(2)
	q.Push(3)
	fmt.Println(q.Peek())
	fmt.Println(q.Pop())
	fmt.Println(q.Pop())
	fmt.Println(q.Empty())
}
```

<!-- REGISTRY_PATH: lcci_03_04_queue_via_stacks.languages.python -->
### python

```python
class MyQueue:
    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def _move_if_needed(self) -> None:
        if self.out_stack:
            return
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        self._move_if_needed()
        return self.out_stack.pop() if self.out_stack else -1

    def peek(self) -> int:
        self._move_if_needed()
        return self.out_stack[-1] if self.out_stack else -1

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack


def main() -> None:
    q = MyQueue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.peek())
    print(q.pop())
    print(q.pop())
    print(q.empty())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_03_04_queue_via_stacks.languages.scala -->
### scala

```scala
object Lcci0304QueueViaStacks {
  final class MyQueue {
    private val inStack = scala.collection.mutable.ArrayBuffer.empty[Int]
    private val outStack = scala.collection.mutable.ArrayBuffer.empty[Int]

    def push(x: Int): Unit = inStack += x

    private def moveIfNeeded(): Unit = {
      if (outStack.nonEmpty) return
      while (inStack.nonEmpty) {
        outStack += inStack.remove(inStack.length - 1)
      }
    }

    def pop(): Int = {
      moveIfNeeded()
      if (outStack.isEmpty) -1 else outStack.remove(outStack.length - 1)
    }

    def peek(): Int = {
      moveIfNeeded()
      if (outStack.isEmpty) -1 else outStack.last
    }

    def empty(): Boolean = inStack.isEmpty && outStack.isEmpty
  }

  def main(args: Array[String]): Unit = {
    val q = new MyQueue
    q.push(1)
    q.push(2)
    q.push(3)
    println(q.peek())
    println(q.pop())
    println(q.pop())
    println(q.empty())
  }
}
```

<!-- REGISTRY_PATH: lcci_03_04_queue_via_stacks.languages.typescript -->
### typescript

```typescript
class MyQueue {
  private readonly inStack: number[] = [];
  private readonly outStack: number[] = [];

  push(x: number): void {
    this.inStack.push(x);
  }

  private moveIfNeeded(): void {
    if (this.outStack.length) {
      return;
    }
    while (this.inStack.length) {
      this.outStack.push(this.inStack.pop()!);
    }
  }

  pop(): number {
    this.moveIfNeeded();
    return this.outStack.length ? this.outStack.pop()! : -1;
  }

  peek(): number {
    this.moveIfNeeded();
    return this.outStack.length ? this.outStack[this.outStack.length - 1] : -1;
  }

  empty(): boolean {
    return this.inStack.length === 0 && this.outStack.length === 0;
  }
}

function main(): void {
  const q = new MyQueue();
  q.push(1);
  q.push(2);
  q.push(3);
  console.log(q.peek());
  console.log(q.pop());
  console.log(q.pop());
  console.log(q.empty());
}

main();
```

## lcci_03_05_sort_stack

<!-- REGISTRY_PATH: lcci_03_05_sort_stack.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <stack>
#include <vector>

void sortStack(std::stack<int>& st) {
    std::stack<int> tmp;

    while (!st.empty()) {
        int cur = st.top();
        st.pop();
        while (!tmp.empty() && tmp.top() > cur) {
            st.push(tmp.top());
            tmp.pop();
        }
        tmp.push(cur);
    }

    while (!tmp.empty()) {
        st.push(tmp.top());
        tmp.pop();
    }
}

void printStackTopToBottom(std::stack<int> st) {
    bool first = true;
    while (!st.empty()) {
        if (!first) std::cout << ' ';
        std::cout << st.top();
        st.pop();
        first = false;
    }
    std::cout << '\n';
}

int main() {
    std::stack<int> st;
    for (int n : std::vector<int>{3, 1, 4, 2}) {
        st.push(n);
    }
    sortStack(st);
    printStackTopToBottom(st);
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_03_05_sort_stack.languages.go -->
### go

```go
package main

import "fmt"

func sortStack(st []int) []int {
	tmp := []int{}
	for len(st) > 0 {
		cur := st[len(st)-1]
		st = st[:len(st)-1]
		for len(tmp) > 0 && tmp[len(tmp)-1] > cur {
			st = append(st, tmp[len(tmp)-1])
			tmp = tmp[:len(tmp)-1]
		}
		tmp = append(tmp, cur)
	}
	for len(tmp) > 0 {
		st = append(st, tmp[len(tmp)-1])
		tmp = tmp[:len(tmp)-1]
	}
	return st
}

func main() {
	st := []int{3, 1, 4, 2}
	st = sortStack(st)
	for i := len(st) - 1; i >= 0; i-- {
		if i != len(st)-1 {
			fmt.Print(" ")
		}
		fmt.Print(st[i])
	}
	fmt.Println()
}
```

<!-- REGISTRY_PATH: lcci_03_05_sort_stack.languages.python -->
### python

```python
def sort_stack(st: list[int]) -> None:
    tmp: list[int] = []
    while st:
        cur = st.pop()
        while tmp and tmp[-1] > cur:
            st.append(tmp.pop())
        tmp.append(cur)
    while tmp:
        st.append(tmp.pop())


def main() -> None:
    st = [3, 1, 4, 2]
    sort_stack(st)
    print(" ".join(str(x) for x in reversed(st)))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_03_05_sort_stack.languages.scala -->
### scala

```scala
object Lcci0305SortStack {
  def sortStack(st: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    val tmp = scala.collection.mutable.ArrayBuffer.empty[Int]
    while (st.nonEmpty) {
      val cur = st.remove(st.length - 1)
      while (tmp.nonEmpty && tmp.last > cur) {
        st += tmp.remove(tmp.length - 1)
      }
      tmp += cur
    }
    while (tmp.nonEmpty) {
      st += tmp.remove(tmp.length - 1)
    }
  }

  def main(args: Array[String]): Unit = {
    val st = scala.collection.mutable.ArrayBuffer(3, 1, 4, 2)
    sortStack(st)
    println(st.reverse.mkString(" "))
  }
}
```

<!-- REGISTRY_PATH: lcci_03_05_sort_stack.languages.typescript -->
### typescript

```typescript
function sortStack(st: number[]): void {
  const tmp: number[] = [];
  while (st.length > 0) {
    const cur = st.pop()!;
    while (tmp.length > 0 && tmp[tmp.length - 1] > cur) {
      st.push(tmp.pop()!);
    }
    tmp.push(cur);
  }
  while (tmp.length > 0) {
    st.push(tmp.pop()!);
  }
}

function main(): void {
  const st = [3, 1, 4, 2];
  sortStack(st);
  console.log([...st].reverse().join(" "));
}

main();
```

## lcci_03_06_animal_shelter

<!-- REGISTRY_PATH: lcci_03_06_animal_shelter.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <queue>
#include <string>

struct Animal {
    int id;
    std::string type;
    int order;
};

class AnimalShelter {
public:
    AnimalShelter() : ticket(0) {}

    void enqueue(const Animal& a) {
        Animal withOrder = a;
        withOrder.order = ticket++;
        if (withOrder.type == "dog") {
            dogs.push(withOrder);
        } else {
            cats.push(withOrder);
        }
    }

    int dequeueAny() {
        if (dogs.empty() && cats.empty()) return -1;
        if (dogs.empty()) return dequeueCat();
        if (cats.empty()) return dequeueDog();
        if (dogs.front().order < cats.front().order) return dequeueDog();
        return dequeueCat();
    }

    int dequeueDog() {
        if (dogs.empty()) return -1;
        int id = dogs.front().id;
        dogs.pop();
        return id;
    }

    int dequeueCat() {
        if (cats.empty()) return -1;
        int id = cats.front().id;
        cats.pop();
        return id;
    }

private:
    int ticket;
    std::queue<Animal> dogs;
    std::queue<Animal> cats;
};

int main() {
    AnimalShelter shelter;
    shelter.enqueue({1, "dog", 0});
    shelter.enqueue({2, "cat", 0});
    shelter.enqueue({3, "dog", 0});
    std::cout << shelter.dequeueAny() << '\n';
    std::cout << shelter.dequeueCat() << '\n';
    std::cout << shelter.dequeueDog() << '\n';
    std::cout << shelter.dequeueAny() << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_03_06_animal_shelter.languages.go -->
### go

```go
package main

import "fmt"

type Animal struct {
	order int
	id    int
}

type AnimalShelter struct {
	ticket int
	dogs   []Animal
	cats   []Animal
}

func (s *AnimalShelter) Enqueue(id int, kind string) {
	item := Animal{order: s.ticket, id: id}
	s.ticket++
	if kind == "dog" {
		s.dogs = append(s.dogs, item)
	} else {
		s.cats = append(s.cats, item)
	}
}

func (s *AnimalShelter) DequeueAny() int {
	if len(s.dogs) == 0 && len(s.cats) == 0 {
		return -1
	}
	if len(s.dogs) == 0 {
		return s.DequeueCat()
	}
	if len(s.cats) == 0 {
		return s.DequeueDog()
	}
	if s.dogs[0].order < s.cats[0].order {
		return s.DequeueDog()
	}
	return s.DequeueCat()
}

func (s *AnimalShelter) DequeueDog() int {
	if len(s.dogs) == 0 {
		return -1
	}
	id := s.dogs[0].id
	s.dogs = s.dogs[1:]
	return id
}

func (s *AnimalShelter) DequeueCat() int {
	if len(s.cats) == 0 {
		return -1
	}
	id := s.cats[0].id
	s.cats = s.cats[1:]
	return id
}

func main() {
	s := &AnimalShelter{}
	s.Enqueue(1, "dog")
	s.Enqueue(2, "cat")
	s.Enqueue(3, "dog")
	fmt.Println(s.DequeueAny())
	fmt.Println(s.DequeueCat())
	fmt.Println(s.DequeueDog())
	fmt.Println(s.DequeueAny())
}
```

<!-- REGISTRY_PATH: lcci_03_06_animal_shelter.languages.python -->
### python

```python
from collections import deque


class AnimalShelter:
    def __init__(self) -> None:
        self.ticket = 0
        self.dogs: deque[tuple[int, int]] = deque()
        self.cats: deque[tuple[int, int]] = deque()

    def enqueue(self, animal_id: int, animal_type: str) -> None:
        item = (self.ticket, animal_id)
        self.ticket += 1
        if animal_type == "dog":
            self.dogs.append(item)
        else:
            self.cats.append(item)

    def dequeue_any(self) -> int:
        if not self.dogs and not self.cats:
            return -1
        if not self.dogs:
            return self.dequeue_cat()
        if not self.cats:
            return self.dequeue_dog()
        if self.dogs[0][0] < self.cats[0][0]:
            return self.dequeue_dog()
        return self.dequeue_cat()

    def dequeue_dog(self) -> int:
        return self.dogs.popleft()[1] if self.dogs else -1

    def dequeue_cat(self) -> int:
        return self.cats.popleft()[1] if self.cats else -1


def main() -> None:
    shelter = AnimalShelter()
    shelter.enqueue(1, "dog")
    shelter.enqueue(2, "cat")
    shelter.enqueue(3, "dog")
    print(shelter.dequeue_any())
    print(shelter.dequeue_cat())
    print(shelter.dequeue_dog())
    print(shelter.dequeue_any())


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_03_06_animal_shelter.languages.scala -->
### scala

```scala
object Lcci0306AnimalShelter {
  final case class Animal(order: Int, id: Int)

  final class AnimalShelter {
    private var ticket = 0
    private val dogs = scala.collection.mutable.Queue.empty[Animal]
    private val cats = scala.collection.mutable.Queue.empty[Animal]

    def enqueue(id: Int, kind: String): Unit = {
      val item = Animal(ticket, id)
      ticket += 1
      if (kind == "dog") dogs.enqueue(item) else cats.enqueue(item)
    }

    def dequeueAny(): Int = {
      if (dogs.isEmpty && cats.isEmpty) return -1
      if (dogs.isEmpty) return dequeueCat()
      if (cats.isEmpty) return dequeueDog()
      if (dogs.front.order < cats.front.order) dequeueDog() else dequeueCat()
    }

    def dequeueDog(): Int = if (dogs.isEmpty) -1 else dogs.dequeue().id

    def dequeueCat(): Int = if (cats.isEmpty) -1 else cats.dequeue().id
  }

  def main(args: Array[String]): Unit = {
    val shelter = new AnimalShelter
    shelter.enqueue(1, "dog")
    shelter.enqueue(2, "cat")
    shelter.enqueue(3, "dog")
    println(shelter.dequeueAny())
    println(shelter.dequeueCat())
    println(shelter.dequeueDog())
    println(shelter.dequeueAny())
  }
}
```

<!-- REGISTRY_PATH: lcci_03_06_animal_shelter.languages.typescript -->
### typescript

```typescript
type Animal = {
  order: number;
  id: number;
};

class AnimalShelter {
  private ticket = 0;
  private dogs: Animal[] = [];
  private cats: Animal[] = [];

  enqueue(id: number, kind: "dog" | "cat"): void {
    const item: Animal = { order: this.ticket, id };
    this.ticket += 1;
    if (kind === "dog") {
      this.dogs.push(item);
    } else {
      this.cats.push(item);
    }
  }

  dequeueAny(): number {
    if (!this.dogs.length && !this.cats.length) {
      return -1;
    }
    if (!this.dogs.length) {
      return this.dequeueCat();
    }
    if (!this.cats.length) {
      return this.dequeueDog();
    }
    return this.dogs[0].order < this.cats[0].order ? this.dequeueDog() : this.dequeueCat();
  }

  dequeueDog(): number {
    return this.dogs.length ? this.dogs.shift()!.id : -1;
  }

  dequeueCat(): number {
    return this.cats.length ? this.cats.shift()!.id : -1;
  }
}

function main(): void {
  const shelter = new AnimalShelter();
  shelter.enqueue(1, "dog");
  shelter.enqueue(2, "cat");
  shelter.enqueue(3, "dog");
  console.log(shelter.dequeueAny());
  console.log(shelter.dequeueCat());
  console.log(shelter.dequeueDog());
  console.log(shelter.dequeueAny());
}

main();
```

## lcci_04_01_route_between_nodes

<!-- REGISTRY_PATH: lcci_04_01_route_between_nodes.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <queue>
#include <vector>

bool hasRoute(int n, const std::vector<std::pair<int, int>>& edges, int start, int target) {
    std::vector<std::vector<int>> g(n);
    for (auto [u, v] : edges) g[u].push_back(v);
    std::vector<int> seen(n, 0);
    std::queue<int> q;
    q.push(start);
    seen[start] = 1;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        if (u == target) return true;
        for (int v : g[u]) if (!seen[v]) { seen[v] = 1; q.push(v); }
    }
    return false;
}

int main() {
    std::vector<std::pair<int, int>> edges{{0,1},{0,2},{1,3},{2,4}};
    std::cout << std::boolalpha << hasRoute(5, edges, 0, 4) << '\n';
    std::cout << std::boolalpha << hasRoute(5, edges, 3, 4) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_01_route_between_nodes.languages.go -->
### go

```go
package main

import "fmt"

func hasRoute(n int, edges [][2]int, start int, target int) bool {
	g := make([][]int, n)
	for _, e := range edges {
		g[e[0]] = append(g[e[0]], e[1])
	}
	seen := make([]bool, n)
	q := []int{start}
	seen[start] = true
	for len(q) > 0 {
		u := q[0]
		q = q[1:]
		if u == target {
			return true
		}
		for _, v := range g[u] {
			if !seen[v] {
				seen[v] = true
				q = append(q, v)
			}
		}
	}
	return false
}

func main() {
	edges := [][2]int{{0, 1}, {0, 2}, {1, 3}, {2, 4}}
	fmt.Println(hasRoute(5, edges, 0, 4))
	fmt.Println(hasRoute(5, edges, 3, 4))
}
```

<!-- REGISTRY_PATH: lcci_04_01_route_between_nodes.languages.python -->
### python

```python
from collections import deque


def has_route(n: int, edges: list[tuple[int, int]], start: int, target: int) -> bool:
    g = [[] for _ in range(n)]
    for u, v in edges:
        g[u].append(v)
    seen = [False] * n
    q: deque[int] = deque([start])
    seen[start] = True
    while q:
        u = q.popleft()
        if u == target:
            return True
        for v in g[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return False


def main() -> None:
    edges = [(0, 1), (0, 2), (1, 3), (2, 4)]
    print(has_route(5, edges, 0, 4))
    print(has_route(5, edges, 3, 4))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_01_route_between_nodes.languages.scala -->
### scala

```scala
import scala.collection.mutable

object Lcci0401RouteBetweenNodes {
  def hasRoute(n: Int, edges: Vector[(Int, Int)], start: Int, target: Int): Boolean = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    edges.foreach { case (u, v) => g(u) += v }
    val seen = Array.fill(n)(false)
    val q = mutable.Queue(start)
    seen(start) = true
    while (q.nonEmpty) {
      val u = q.dequeue()
      if (u == target) return true
      g(u).foreach { v => if (!seen(v)) { seen(v) = true; q.enqueue(v) } }
    }
    false
  }

  def main(args: Array[String]): Unit = {
    val edges = Vector((0, 1), (0, 2), (1, 3), (2, 4))
    println(hasRoute(5, edges, 0, 4))
    println(hasRoute(5, edges, 3, 4))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_01_route_between_nodes.languages.typescript -->
### typescript

```typescript
function hasRoute(n: number, edges: Array<[number, number]>, start: number, target: number): boolean {
  const g: number[][] = Array.from({ length: n }, () => []);
  for (const [u, v] of edges) g[u].push(v);
  const seen = Array(n).fill(false);
  const q: number[] = [start];
  seen[start] = true;
  while (q.length) {
    const u = q.shift()!;
    if (u === target) return true;
    for (const v of g[u]) {
      if (!seen[v]) {
        seen[v] = true;
        q.push(v);
      }
    }
  }
  return false;
}

const edges: Array<[number, number]> = [[0, 1], [0, 2], [1, 3], [2, 4]];
console.log(hasRoute(5, edges, 0, 4));
console.log(hasRoute(5, edges, 3, 4));
```

## lcci_04_02_minimum_height_tree

<!-- REGISTRY_PATH: lcci_04_02_minimum_height_tree.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

Node* build(const std::vector<int>& a, int lo, int hi) {
    if (lo > hi) return nullptr;
    int mid = (lo + hi) / 2;
    Node* root = new Node(a[mid]);
    root->l = build(a, lo, mid - 1);
    root->r = build(a, mid + 1, hi);
    return root;
}

void inorder(Node* n) { if (!n) return; inorder(n->l); std::cout << n->v << ' '; inorder(n->r); }

int main() {
    std::vector<int> nums{1,2,3,4,5,6,7};
    Node* root = build(nums, 0, static_cast<int>(nums.size()) - 1);
    inorder(root);
    std::cout << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_02_minimum_height_tree.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func build(a []int, lo int, hi int) *Node {
	if lo > hi {
		return nil
	}
	mid := (lo + hi) / 2
	root := &Node{Val: a[mid]}
	root.Left = build(a, lo, mid-1)
	root.Right = build(a, mid+1, hi)
	return root
}

func inorder(n *Node, out *[]int) {
	if n == nil {
		return
	}
	inorder(n.Left, out)
	*out = append(*out, n.Val)
	inorder(n.Right, out)
}

func main() {
	nums := []int{1, 2, 3, 4, 5, 6, 7}
	root := build(nums, 0, len(nums)-1)
	out := []int{}
	inorder(root, &out)
	for i, v := range out {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(v)
	}
	fmt.Println()
}
```

<!-- REGISTRY_PATH: lcci_04_02_minimum_height_tree.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def build(nums: list[int], lo: int, hi: int) -> Node | None:
    if lo > hi:
        return None
    mid = (lo + hi) // 2
    root = Node(nums[mid])
    root.left = build(nums, lo, mid - 1)
    root.right = build(nums, mid + 1, hi)
    return root


def inorder(root: Node | None) -> list[int]:
    if root is None:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


def main() -> None:
    nums = [1, 2, 3, 4, 5, 6, 7]
    print(" ".join(map(str, inorder(build(nums, 0, len(nums) - 1)))))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_02_minimum_height_tree.languages.scala -->
### scala

```scala
object Lcci0402MinimumHeightTree {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def build(nums: Vector[Int], lo: Int, hi: Int): Node | Null = {
    if (lo > hi) return null
    val mid = (lo + hi) / 2
    val root = Node(nums(mid))
    root.left = build(nums, lo, mid - 1)
    root.right = build(nums, mid + 1, hi)
    root
  }

  def inorder(n: Node | Null, out: scala.collection.mutable.ArrayBuffer[Int]): Unit = {
    if (n == null) return
    inorder(n.asInstanceOf[Node].left, out)
    out += n.asInstanceOf[Node].value
    inorder(n.asInstanceOf[Node].right, out)
  }

  def main(args: Array[String]): Unit = {
    val nums = Vector(1, 2, 3, 4, 5, 6, 7)
    val root = build(nums, 0, nums.length - 1)
    val out = scala.collection.mutable.ArrayBuffer.empty[Int]
    inorder(root, out)
    println(out.mkString(" "))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_02_minimum_height_tree.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function build(a: number[], lo: number, hi: number): Node | null {
  if (lo > hi) return null;
  const mid = Math.floor((lo + hi) / 2);
  return new Node(a[mid], build(a, lo, mid - 1), build(a, mid + 1, hi));
}

function inorder(n: Node | null, out: number[]): void {
  if (!n) return;
  inorder(n.left, out);
  out.push(n.val);
  inorder(n.right, out);
}

const nums = [1, 2, 3, 4, 5, 6, 7];
const root = build(nums, 0, nums.length - 1);
const out: number[] = [];
inorder(root, out);
console.log(out.join(" "));
```

## lcci_04_03_list_of_depth

<!-- REGISTRY_PATH: lcci_04_03_list_of_depth.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <queue>
#include <vector>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

std::vector<std::vector<int>> listOfDepth(Node* root) {
    if (!root) return {};
    std::vector<std::vector<int>> out;
    std::queue<Node*> q; q.push(root);
    while (!q.empty()) {
        int n = static_cast<int>(q.size());
        std::vector<int> level;
        while (n--) {
            Node* cur = q.front(); q.pop();
            level.push_back(cur->v);
            if (cur->l) q.push(cur->l);
            if (cur->r) q.push(cur->r);
        }
        out.push_back(level);
    }
    return out;
}

int main() {
    Node* root = new Node(1);
    root->l = new Node(2); root->r = new Node(3);
    root->l->l = new Node(4); root->l->r = new Node(5);
    root->r->l = new Node(6); root->r->r = new Node(7);
    auto levels = listOfDepth(root);
    for (size_t i = 0; i < levels.size(); ++i) {
        if (i) std::cout << " | ";
        for (size_t j = 0; j < levels[i].size(); ++j) {
            if (j) std::cout << ' ';
            std::cout << levels[i][j];
        }
    }
    std::cout << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_03_list_of_depth.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func listOfDepth(root *Node) [][]int {
	if root == nil {
		return nil
	}
	out := [][]int{}
	q := []*Node{root}
	for len(q) > 0 {
		n := len(q)
		level := []int{}
		for i := 0; i < n; i++ {
			cur := q[0]
			q = q[1:]
			level = append(level, cur.Val)
			if cur.Left != nil {
				q = append(q, cur.Left)
			}
			if cur.Right != nil {
				q = append(q, cur.Right)
			}
		}
		out = append(out, level)
	}
	return out
}

func main() {
	root := &Node{Val: 1}
	root.Left, root.Right = &Node{Val: 2}, &Node{Val: 3}
	root.Left.Left, root.Left.Right = &Node{Val: 4}, &Node{Val: 5}
	root.Right.Left, root.Right.Right = &Node{Val: 6}, &Node{Val: 7}
	levels := listOfDepth(root)
	for i, lvl := range levels {
		if i > 0 {
			fmt.Print(" | ")
		}
		for j, v := range lvl {
			if j > 0 {
				fmt.Print(" ")
			}
			fmt.Print(v)
		}
	}
	fmt.Println()
}
```

<!-- REGISTRY_PATH: lcci_04_03_list_of_depth.languages.python -->
### python

```python
from collections import deque


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def list_of_depth(root: Node | None) -> list[list[int]]:
    if root is None:
        return []
    out: list[list[int]] = []
    q: deque[Node] = deque([root])
    while q:
        level: list[int] = []
        for _ in range(len(q)):
            cur = q.popleft()
            level.append(cur.val)
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        out.append(level)
    return out


def main() -> None:
    root = Node(1)
    root.left, root.right = Node(2), Node(3)
    root.left.left, root.left.right = Node(4), Node(5)
    root.right.left, root.right.right = Node(6), Node(7)
    print(" | ".join(" ".join(map(str, lvl)) for lvl in list_of_depth(root)))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_03_list_of_depth.languages.scala -->
### scala

```scala
import scala.collection.mutable

object Lcci0403ListOfDepth {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def listOfDepth(root: Node | Null): Vector[Vector[Int]] = {
    if (root == null) return Vector.empty
    val q = mutable.Queue(root.asInstanceOf[Node])
    val out = mutable.ArrayBuffer.empty[Vector[Int]]
    while (q.nonEmpty) {
      val n = q.size
      val level = mutable.ArrayBuffer.empty[Int]
      (0 until n).foreach { _ =>
        val cur = q.dequeue()
        level += cur.value
        if (cur.left != null) q.enqueue(cur.left.asInstanceOf[Node])
        if (cur.right != null) q.enqueue(cur.right.asInstanceOf[Node])
      }
      out += level.toVector
    }
    out.toVector
  }

  def main(args: Array[String]): Unit = {
    val root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    println(listOfDepth(root).map(_.mkString(" ")).mkString(" | "))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_03_list_of_depth.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function listOfDepth(root: Node | null): number[][] {
  if (!root) return [];
  const out: number[][] = [];
  const q: Node[] = [root];
  while (q.length) {
    const n = q.length;
    const level: number[] = [];
    for (let i = 0; i < n; i++) {
      const cur = q.shift()!;
      level.push(cur.val);
      if (cur.left) q.push(cur.left);
      if (cur.right) q.push(cur.right);
    }
    out.push(level);
  }
  return out;
}

const root = new Node(1, new Node(2, new Node(4), new Node(5)), new Node(3, new Node(6), new Node(7)));
console.log(listOfDepth(root).map((lvl) => lvl.join(" ")).join(" | "));
```

## lcci_04_04_check_balance

<!-- REGISTRY_PATH: lcci_04_04_check_balance.languages.cpp -->
### cpp

```cpp
#include <iostream>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

int heightOrFail(Node* n) {
    if (!n) return 0;
    int lh = heightOrFail(n->l); if (lh == -1) return -1;
    int rh = heightOrFail(n->r); if (rh == -1) return -1;
    if (lh - rh > 1 || rh - lh > 1) return -1;
    return 1 + (lh > rh ? lh : rh);
}

bool isBalanced(Node* root) { return heightOrFail(root) != -1; }

int main() {
    Node* a = new Node(1); a->l = new Node(2); a->r = new Node(3);
    Node* b = new Node(1); b->l = new Node(2); b->l->l = new Node(3); b->l->l->l = new Node(4);
    std::cout << std::boolalpha << isBalanced(a) << '\n';
    std::cout << std::boolalpha << isBalanced(b) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_04_check_balance.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func heightOrFail(n *Node) int {
	if n == nil {
		return 0
	}
	lh := heightOrFail(n.Left)
	if lh == -1 {
		return -1
	}
	rh := heightOrFail(n.Right)
	if rh == -1 {
		return -1
	}
	if lh-rh > 1 || rh-lh > 1 {
		return -1
	}
	if lh > rh {
		return lh + 1
	}
	return rh + 1
}

func isBalanced(root *Node) bool { return heightOrFail(root) != -1 }

func main() {
	a := &Node{Val: 1, Left: &Node{Val: 2}, Right: &Node{Val: 3}}
	b := &Node{Val: 1, Left: &Node{Val: 2, Left: &Node{Val: 3, Left: &Node{Val: 4}}}}
	fmt.Println(isBalanced(a))
	fmt.Println(isBalanced(b))
}
```

<!-- REGISTRY_PATH: lcci_04_04_check_balance.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def height_or_fail(node: Node | None) -> int:
    if node is None:
        return 0
    lh = height_or_fail(node.left)
    if lh == -1:
        return -1
    rh = height_or_fail(node.right)
    if rh == -1:
        return -1
    if abs(lh - rh) > 1:
        return -1
    return 1 + max(lh, rh)


def is_balanced(root: Node | None) -> bool:
    return height_or_fail(root) != -1


def main() -> None:
    a = Node(1); a.left = Node(2); a.right = Node(3)
    b = Node(1); b.left = Node(2); b.left.left = Node(3); b.left.left.left = Node(4)
    print(is_balanced(a))
    print(is_balanced(b))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_04_check_balance.languages.scala -->
### scala

```scala
object Lcci0404CheckBalance {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def heightOrFail(n: Node | Null): Int = {
    if (n == null) return 0
    val lh = heightOrFail(n.asInstanceOf[Node].left)
    if (lh == -1) return -1
    val rh = heightOrFail(n.asInstanceOf[Node].right)
    if (rh == -1) return -1
    if (math.abs(lh - rh) > 1) return -1
    1 + math.max(lh, rh)
  }

  def isBalanced(root: Node | Null): Boolean = heightOrFail(root) != -1

  def main(args: Array[String]): Unit = {
    val a = Node(1, Node(2), Node(3))
    val b = Node(1, Node(2, Node(3, Node(4), null), null), null)
    println(isBalanced(a))
    println(isBalanced(b))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_04_check_balance.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function heightOrFail(n: Node | null): number {
  if (!n) return 0;
  const lh = heightOrFail(n.left);
  if (lh === -1) return -1;
  const rh = heightOrFail(n.right);
  if (rh === -1) return -1;
  if (Math.abs(lh - rh) > 1) return -1;
  return 1 + Math.max(lh, rh);
}

function isBalanced(root: Node | null): boolean {
  return heightOrFail(root) !== -1;
}

const a = new Node(1, new Node(2), new Node(3));
const b = new Node(1, new Node(2, new Node(3, new Node(4))));
console.log(isBalanced(a));
console.log(isBalanced(b));
```

## lcci_04_05_legal_binary_search_tree

<!-- REGISTRY_PATH: lcci_04_05_legal_binary_search_tree.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <limits>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

bool isValid(Node* n, long long lo, long long hi) {
    if (!n) return true;
    if (n->v <= lo || n->v >= hi) return false;
    return isValid(n->l, lo, n->v) && isValid(n->r, n->v, hi);
}

int main() {
    Node* ok = new Node(5); ok->l = new Node(3); ok->r = new Node(7);
    Node* bad = new Node(5); bad->l = new Node(3); bad->r = new Node(7); bad->l->r = new Node(6);
    std::cout << std::boolalpha << isValid(ok, std::numeric_limits<long long>::min(), std::numeric_limits<long long>::max()) << '\n';
    std::cout << std::boolalpha << isValid(bad, std::numeric_limits<long long>::min(), std::numeric_limits<long long>::max()) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_05_legal_binary_search_tree.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func isValid(n *Node, lo int64, hi int64) bool {
	if n == nil {
		return true
	}
	v := int64(n.Val)
	if v <= lo || v >= hi {
		return false
	}
	return isValid(n.Left, lo, v) && isValid(n.Right, v, hi)
}

func main() {
	ok := &Node{Val: 5, Left: &Node{Val: 3}, Right: &Node{Val: 7}}
	bad := &Node{Val: 5, Left: &Node{Val: 3, Right: &Node{Val: 6}}, Right: &Node{Val: 7}}
	fmt.Println(isValid(ok, -1<<62, 1<<62))
	fmt.Println(isValid(bad, -1<<62, 1<<62))
}
```

<!-- REGISTRY_PATH: lcci_04_05_legal_binary_search_tree.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def is_valid(node: Node | None, lo: int, hi: int) -> bool:
    if node is None:
        return True
    if not (lo < node.val < hi):
        return False
    return is_valid(node.left, lo, node.val) and is_valid(node.right, node.val, hi)


def main() -> None:
    ok = Node(5); ok.left = Node(3); ok.right = Node(7)
    bad = Node(5); bad.left = Node(3); bad.right = Node(7); bad.left.right = Node(6)
    print(is_valid(ok, -10**18, 10**18))
    print(is_valid(bad, -10**18, 10**18))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_05_legal_binary_search_tree.languages.scala -->
### scala

```scala
object Lcci0405LegalBinarySearchTree {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def isValid(n: Node | Null, lo: Long, hi: Long): Boolean = {
    if (n == null) return true
    val v = n.asInstanceOf[Node].value.toLong
    if (v <= lo || v >= hi) return false
    isValid(n.asInstanceOf[Node].left, lo, v) && isValid(n.asInstanceOf[Node].right, v, hi)
  }

  def main(args: Array[String]): Unit = {
    val ok = Node(5, Node(3), Node(7))
    val bad = Node(5, Node(3, null, Node(6)), Node(7))
    println(isValid(ok, Long.MinValue, Long.MaxValue))
    println(isValid(bad, Long.MinValue, Long.MaxValue))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_05_legal_binary_search_tree.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function isValid(n: Node | null, lo: number, hi: number): boolean {
  if (!n) return true;
  if (!(lo < n.val && n.val < hi)) return false;
  return isValid(n.left, lo, n.val) && isValid(n.right, n.val, hi);
}

const ok = new Node(5, new Node(3), new Node(7));
const bad = new Node(5, new Node(3, null, new Node(6)), new Node(7));
console.log(isValid(ok, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY));
console.log(isValid(bad, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY));
```

## lcci_04_06_successor

<!-- REGISTRY_PATH: lcci_04_06_successor.languages.cpp -->
### cpp

```cpp
#include <iostream>

struct Node { int v; Node* l; Node* r; Node(int x): v(x), l(nullptr), r(nullptr) {} };

Node* inorderSuccessor(Node* root, int p) {
    Node* ans = nullptr;
    while (root) {
        if (p < root->v) { ans = root; root = root->l; }
        else root = root->r;
    }
    return ans;
}

int main() {
    Node* root = new Node(5);
    root->l = new Node(3); root->r = new Node(7);
    root->l->l = new Node(2); root->l->r = new Node(4);
    Node* s1 = inorderSuccessor(root, 3);
    Node* s2 = inorderSuccessor(root, 7);
    std::cout << (s1 ? s1->v : -1) << '\n';
    std::cout << (s2 ? s2->v : -1) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_06_successor.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func inorderSuccessor(root *Node, p int) *Node {
	var ans *Node
	for root != nil {
		if p < root.Val {
			ans = root
			root = root.Left
		} else {
			root = root.Right
		}
	}
	return ans
}

func main() {
	root := &Node{Val: 5, Left: &Node{Val: 3, Left: &Node{Val: 2}, Right: &Node{Val: 4}}, Right: &Node{Val: 7}}
	s1 := inorderSuccessor(root, 3)
	s2 := inorderSuccessor(root, 7)
	if s1 != nil {
		fmt.Println(s1.Val)
	} else {
		fmt.Println(-1)
	}
	if s2 != nil {
		fmt.Println(s2.Val)
	} else {
		fmt.Println(-1)
	}
}
```

<!-- REGISTRY_PATH: lcci_04_06_successor.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def inorder_successor(root: Node | None, p: int) -> Node | None:
    ans = None
    while root is not None:
        if p < root.val:
            ans = root
            root = root.left
        else:
            root = root.right
    return ans


def main() -> None:
    root = Node(5)
    root.left = Node(3); root.right = Node(7)
    root.left.left = Node(2); root.left.right = Node(4)
    s1 = inorder_successor(root, 3)
    s2 = inorder_successor(root, 7)
    print(s1.val if s1 else -1)
    print(s2.val if s2 else -1)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_06_successor.languages.scala -->
### scala

```scala
object Lcci0406Successor {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def inorderSuccessor(root0: Node | Null, p: Int): Node | Null = {
    var root = root0
    var ans: Node | Null = null
    while (root != null) {
      val cur = root.asInstanceOf[Node]
      if (p < cur.value) {
        ans = cur
        root = cur.left
      } else {
        root = cur.right
      }
    }
    ans
  }

  def main(args: Array[String]): Unit = {
    val root = Node(5, Node(3, Node(2), Node(4)), Node(7))
    val s1 = inorderSuccessor(root, 3)
    val s2 = inorderSuccessor(root, 7)
    println(if (s1 == null) -1 else s1.asInstanceOf[Node].value)
    println(if (s2 == null) -1 else s2.asInstanceOf[Node].value)
  }
}
```

<!-- REGISTRY_PATH: lcci_04_06_successor.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function inorderSuccessor(root: Node | null, p: number): Node | null {
  let ans: Node | null = null;
  while (root) {
    if (p < root.val) {
      ans = root;
      root = root.left;
    } else {
      root = root.right;
    }
  }
  return ans;
}

const root = new Node(5, new Node(3, new Node(2), new Node(4)), new Node(7));
console.log(inorderSuccessor(root, 3)?.val ?? -1);
console.log(inorderSuccessor(root, 7)?.val ?? -1);
```

## lcci_04_08_first_common_ancestor

<!-- REGISTRY_PATH: lcci_04_08_first_common_ancestor.languages.cpp -->
### cpp

```cpp
#include <iostream>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

Node* lca(Node* root, int p, int q) {
    if (!root || root->v == p || root->v == q) return root;
    Node* left = lca(root->l, p, q);
    Node* right = lca(root->r, p, q);
    if (left && right) return root;
    return left ? left : right;
}

int main() {
    Node* root = new Node(3);
    root->l = new Node(5); root->r = new Node(1);
    root->l->l = new Node(6); root->l->r = new Node(2);
    root->r->l = new Node(0); root->r->r = new Node(8);

    std::cout << lca(root, 6, 2)->v << '\n';
    std::cout << lca(root, 6, 8)->v << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_08_first_common_ancestor.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func lca(root *Node, p int, q int) *Node {
	if root == nil || root.Val == p || root.Val == q {
		return root
	}
	left := lca(root.Left, p, q)
	right := lca(root.Right, p, q)
	if left != nil && right != nil {
		return root
	}
	if left != nil {
		return left
	}
	return right
}

func main() {
	root := &Node{Val: 3}
	root.Left = &Node{Val: 5, Left: &Node{Val: 6}, Right: &Node{Val: 2}}
	root.Right = &Node{Val: 1, Left: &Node{Val: 0}, Right: &Node{Val: 8}}

	fmt.Println(lca(root, 6, 2).Val)
	fmt.Println(lca(root, 6, 8).Val)
}
```

<!-- REGISTRY_PATH: lcci_04_08_first_common_ancestor.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def lca(root: Node | None, p: int, q: int) -> Node | None:
    if root is None or root.val == p or root.val == q:
        return root
    left = lca(root.left, p, q)
    right = lca(root.right, p, q)
    if left and right:
        return root
    return left if left else right


def main() -> None:
    root = Node(3)
    root.left = Node(5); root.right = Node(1)
    root.left.left = Node(6); root.left.right = Node(2)
    root.right.left = Node(0); root.right.right = Node(8)

    print(lca(root, 6, 2).val)
    print(lca(root, 6, 8).val)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_08_first_common_ancestor.languages.scala -->
### scala

```scala
object Lcci0408FirstCommonAncestor {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def lca(root: Node | Null, p: Int, q: Int): Node | Null = {
    if (root == null) return null
    val cur = root.asInstanceOf[Node]
    if (cur.value == p || cur.value == q) return cur
    val left = lca(cur.left, p, q)
    val right = lca(cur.right, p, q)
    if (left != null && right != null) cur else if (left != null) left else right
  }

  def main(args: Array[String]): Unit = {
    val root = Node(3,
      Node(5, Node(6), Node(2)),
      Node(1, Node(0), Node(8))
    )
    println(lca(root, 6, 2).asInstanceOf[Node].value)
    println(lca(root, 6, 8).asInstanceOf[Node].value)
  }
}
```

<!-- REGISTRY_PATH: lcci_04_08_first_common_ancestor.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function lca(root: Node | null, p: number, q: number): Node | null {
  if (!root || root.val === p || root.val === q) return root;
  const left = lca(root.left, p, q);
  const right = lca(root.right, p, q);
  if (left && right) return root;
  return left ?? right;
}

const root = new Node(
  3,
  new Node(5, new Node(6), new Node(2)),
  new Node(1, new Node(0), new Node(8))
);

console.log(lca(root, 6, 2)?.val ?? -1);
console.log(lca(root, 6, 8)?.val ?? -1);
```

## lcci_04_09_bst_sequences

<!-- REGISTRY_PATH: lcci_04_09_bst_sequences.languages.cpp -->
### cpp

```cpp
#include <deque>
#include <iostream>
#include <vector>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

void weave(std::deque<int> first, std::deque<int> second, std::vector<int> prefix,
           std::vector<std::vector<int>>& out) {
    if (first.empty() || second.empty()) {
        std::vector<int> merged = prefix;
        merged.insert(merged.end(), first.begin(), first.end());
        merged.insert(merged.end(), second.begin(), second.end());
        out.push_back(std::move(merged));
        return;
    }

    int h1 = first.front(); first.pop_front();
    auto p1 = prefix; p1.push_back(h1);
    weave(first, second, p1, out);

    int h2 = second.front(); second.pop_front();
    auto p2 = prefix; p2.push_back(h2);
    weave(first, second, p2, out);
}

std::vector<std::vector<int>> allSeq(Node* root) {
    if (!root) return { { } };

    auto leftSeq = allSeq(root->l);
    auto rightSeq = allSeq(root->r);
    std::vector<std::vector<int>> result;

    for (const auto& l : leftSeq) {
        for (const auto& r : rightSeq) {
            std::vector<std::vector<int>> weaved;
            weave(std::deque<int>(l.begin(), l.end()), std::deque<int>(r.begin(), r.end()), {root->v}, weaved);
            result.insert(result.end(), weaved.begin(), weaved.end());
        }
    }
    return result;
}

int main() {
    Node* root = new Node(2);
    root->l = new Node(1);
    root->r = new Node(3);

    auto ans = allSeq(root);
    for (const auto& seq : ans) {
        for (size_t i = 0; i < seq.size(); ++i) {
            std::cout << seq[i] << (i + 1 == seq.size() ? '\n' : ' ');
        }
    }
}
```

<!-- REGISTRY_PATH: lcci_04_09_bst_sequences.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func weave(first []int, second []int, prefix []int, out *[][]int) {
	if len(first) == 0 || len(second) == 0 {
		merged := append([]int{}, prefix...)
		merged = append(merged, first...)
		merged = append(merged, second...)
		*out = append(*out, merged)
		return
	}

	weave(first[1:], second, append(append([]int{}, prefix...), first[0]), out)
	weave(first, second[1:], append(append([]int{}, prefix...), second[0]), out)
}

func allSeq(root *Node) [][]int {
	if root == nil {
		return [][]int{{}}
	}
	left := allSeq(root.Left)
	right := allSeq(root.Right)
	result := [][]int{}

	for _, l := range left {
		for _, r := range right {
			weaved := [][]int{}
			weave(l, r, []int{root.Val}, &weaved)
			result = append(result, weaved...)
		}
	}
	return result
}

func main() {
	root := &Node{Val: 2, Left: &Node{Val: 1}, Right: &Node{Val: 3}}
	for _, seq := range allSeq(root) {
		fmt.Println(seq)
	}
}
```

<!-- REGISTRY_PATH: lcci_04_09_bst_sequences.languages.python -->
### python

```python
from collections import deque


class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def weave(first: deque[int], second: deque[int], prefix: list[int], out: list[list[int]]) -> None:
    if not first or not second:
        out.append(prefix + list(first) + list(second))
        return

    h1 = first.popleft()
    weave(first, second, prefix + [h1], out)
    first.appendleft(h1)

    h2 = second.popleft()
    weave(first, second, prefix + [h2], out)
    second.appendleft(h2)


def all_seq(root: Node | None) -> list[list[int]]:
    if root is None:
        return [[]]
    left = all_seq(root.left)
    right = all_seq(root.right)
    result: list[list[int]] = []
    for l in left:
        for r in right:
            weaved: list[list[int]] = []
            weave(deque(l), deque(r), [root.val], weaved)
            result.extend(weaved)
    return result


def main() -> None:
    root = Node(2)
    root.left = Node(1)
    root.right = Node(3)
    for seq in all_seq(root):
        print(*seq)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_09_bst_sequences.languages.scala -->
### scala

```scala
object Lcci0409BstSequences {
  final case class Node(value: Int, left: Node | Null = null, right: Node | Null = null)

  def weave(first: List[Int], second: List[Int], prefix: List[Int]): List[List[Int]] = {
    if (first.isEmpty || second.isEmpty) return List(prefix ++ first ++ second)
    val withFirst = weave(first.tail, second, prefix :+ first.head)
    val withSecond = weave(first, second.tail, prefix :+ second.head)
    withFirst ++ withSecond
  }

  def allSeq(root: Node | Null): List[List[Int]] = {
    if (root == null) return List(Nil)
    val cur = root.asInstanceOf[Node]
    val left = allSeq(cur.left)
    val right = allSeq(cur.right)

    for {
      l <- left
      r <- right
      w <- weave(l, r, List(cur.value))
    } yield w
  }

  def main(args: Array[String]): Unit = {
    val root = Node(2, Node(1), Node(3))
    allSeq(root).foreach(seq => println(seq.mkString(" ")))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_09_bst_sequences.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function weave(first: number[], second: number[], prefix: number[], out: number[][]): void {
  if (first.length === 0 || second.length === 0) {
    out.push([...prefix, ...first, ...second]);
    return;
  }

  weave(first.slice(1), second, [...prefix, first[0]], out);
  weave(first, second.slice(1), [...prefix, second[0]], out);
}

function allSeq(root: Node | null): number[][] {
  if (!root) return [[]];
  const left = allSeq(root.left);
  const right = allSeq(root.right);
  const result: number[][] = [];

  for (const l of left) {
    for (const r of right) {
      const weaved: number[][] = [];
      weave(l, r, [root.val], weaved);
      result.push(...weaved);
    }
  }
  return result;
}

const root = new Node(2, new Node(1), new Node(3));
for (const seq of allSeq(root)) {
  console.log(seq.join(" "));
}
```

## lcci_04_10_check_subtree

<!-- REGISTRY_PATH: lcci_04_10_check_subtree.languages.cpp -->
### cpp

```cpp
#include <iostream>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

bool same(Node* a, Node* b) {
    if (!a && !b) return true;
    if (!a || !b) return false;
    return a->v == b->v && same(a->l, b->l) && same(a->r, b->r);
}

bool isSubtree(Node* t1, Node* t2) {
    if (!t2) return true;
    if (!t1) return false;
    if (same(t1, t2)) return true;
    return isSubtree(t1->l, t2) || isSubtree(t1->r, t2);
}

int main() {
    Node* t1 = new Node(3);
    t1->l = new Node(4); t1->r = new Node(5);
    t1->l->l = new Node(1); t1->l->r = new Node(2);

    Node* t2 = new Node(4); t2->l = new Node(1); t2->r = new Node(2);
    Node* t3 = new Node(4); t3->l = new Node(1); t3->r = new Node(3);

    std::cout << std::boolalpha << isSubtree(t1, t2) << '\n';
    std::cout << std::boolalpha << isSubtree(t1, t3) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_10_check_subtree.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func same(a *Node, b *Node) bool {
	if a == nil && b == nil {
		return true
	}
	if a == nil || b == nil {
		return false
	}
	return a.Val == b.Val && same(a.Left, b.Left) && same(a.Right, b.Right)
}

func isSubtree(t1 *Node, t2 *Node) bool {
	if t2 == nil {
		return true
	}
	if t1 == nil {
		return false
	}
	if same(t1, t2) {
		return true
	}
	return isSubtree(t1.Left, t2) || isSubtree(t1.Right, t2)
}

func main() {
	t1 := &Node{Val: 3, Left: &Node{Val: 4, Left: &Node{Val: 1}, Right: &Node{Val: 2}}, Right: &Node{Val: 5}}
	t2 := &Node{Val: 4, Left: &Node{Val: 1}, Right: &Node{Val: 2}}
	t3 := &Node{Val: 4, Left: &Node{Val: 1}, Right: &Node{Val: 3}}
	fmt.Println(isSubtree(t1, t2))
	fmt.Println(isSubtree(t1, t3))
}
```

<!-- REGISTRY_PATH: lcci_04_10_check_subtree.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def same(a: Node | None, b: Node | None) -> bool:
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return a.val == b.val and same(a.left, b.left) and same(a.right, b.right)


def is_subtree(t1: Node | None, t2: Node | None) -> bool:
    if t2 is None:
        return True
    if t1 is None:
        return False
    if same(t1, t2):
        return True
    return is_subtree(t1.left, t2) or is_subtree(t1.right, t2)


def main() -> None:
    t1 = Node(3)
    t1.left = Node(4); t1.right = Node(5)
    t1.left.left = Node(1); t1.left.right = Node(2)

    t2 = Node(4); t2.left = Node(1); t2.right = Node(2)
    t3 = Node(4); t3.left = Node(1); t3.right = Node(3)

    print(is_subtree(t1, t2))
    print(is_subtree(t1, t3))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_10_check_subtree.languages.scala -->
### scala

```scala
object Lcci0410CheckSubtree {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def same(a: Node | Null, b: Node | Null): Boolean = {
    if (a == null && b == null) return true
    if (a == null || b == null) return false
    val x = a.asInstanceOf[Node]
    val y = b.asInstanceOf[Node]
    x.value == y.value && same(x.left, y.left) && same(x.right, y.right)
  }

  def isSubtree(t1: Node | Null, t2: Node | Null): Boolean = {
    if (t2 == null) return true
    if (t1 == null) return false
    val cur = t1.asInstanceOf[Node]
    same(cur, t2) || isSubtree(cur.left, t2) || isSubtree(cur.right, t2)
  }

  def main(args: Array[String]): Unit = {
    val t1 = Node(3, Node(4, Node(1), Node(2)), Node(5))
    val t2 = Node(4, Node(1), Node(2))
    val t3 = Node(4, Node(1), Node(3))
    println(isSubtree(t1, t2))
    println(isSubtree(t1, t3))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_10_check_subtree.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function same(a: Node | null, b: Node | null): boolean {
  if (!a && !b) return true;
  if (!a || !b) return false;
  return a.val === b.val && same(a.left, b.left) && same(a.right, b.right);
}

function isSubtree(t1: Node | null, t2: Node | null): boolean {
  if (!t2) return true;
  if (!t1) return false;
  if (same(t1, t2)) return true;
  return isSubtree(t1.left, t2) || isSubtree(t1.right, t2);
}

const t1 = new Node(3, new Node(4, new Node(1), new Node(2)), new Node(5));
const t2 = new Node(4, new Node(1), new Node(2));
const t3 = new Node(4, new Node(1), new Node(3));

console.log(isSubtree(t1, t2));
console.log(isSubtree(t1, t3));
```

## lcci_04_12_paths_with_sum

<!-- REGISTRY_PATH: lcci_04_12_paths_with_sum.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <unordered_map>

struct Node {
    int v;
    Node* l;
    Node* r;
    Node(int x): v(x), l(nullptr), r(nullptr) {}
};

int dfs(Node* node, int target, long long prefix, std::unordered_map<long long, int>& cnt) {
    if (!node) return 0;
    prefix += node->v;
    int res = 0;
    auto it = cnt.find(prefix - target);
    if (it != cnt.end()) res += it->second;

    cnt[prefix]++;
    res += dfs(node->l, target, prefix, cnt);
    res += dfs(node->r, target, prefix, cnt);
    cnt[prefix]--;

    return res;
}

int pathSum(Node* root, int target) {
    std::unordered_map<long long, int> cnt;
    cnt[0] = 1;
    return dfs(root, target, 0, cnt);
}

int main() {
    Node* root = new Node(10);
    root->l = new Node(5); root->r = new Node(-3);
    root->l->l = new Node(3); root->l->r = new Node(2);
    root->r->r = new Node(11);
    root->l->l->l = new Node(3); root->l->l->r = new Node(-2);
    root->l->r->r = new Node(1);

    std::cout << pathSum(root, 8) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_04_12_paths_with_sum.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	Val         int
	Left, Right *Node
}

func pathSum(root *Node, target int) int {
	count := map[int]int{0: 1}
	var dfs func(*Node, int) int

	dfs = func(node *Node, prefix int) int {
		if node == nil {
			return 0
		}
		prefix += node.Val
		res := count[prefix-target]
		count[prefix]++
		res += dfs(node.Left, prefix)
		res += dfs(node.Right, prefix)
		count[prefix]--
		return res
	}

	return dfs(root, 0)
}

func main() {
	root := &Node{Val: 10}
	root.Left = &Node{Val: 5, Left: &Node{Val: 3, Left: &Node{Val: 3}, Right: &Node{Val: -2}}, Right: &Node{Val: 2, Right: &Node{Val: 1}}}
	root.Right = &Node{Val: -3, Right: &Node{Val: 11}}
	fmt.Println(pathSum(root, 8))
}
```

<!-- REGISTRY_PATH: lcci_04_12_paths_with_sum.languages.python -->
### python

```python
class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left: Node | None = None
        self.right: Node | None = None


def path_sum(root: Node | None, target: int) -> int:
    counts: dict[int, int] = {0: 1}

    def dfs(node: Node | None, prefix: int) -> int:
        if node is None:
            return 0
        prefix += node.val
        res = counts.get(prefix - target, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
        res += dfs(node.left, prefix)
        res += dfs(node.right, prefix)
        counts[prefix] -= 1
        return res

    return dfs(root, 0)


def main() -> None:
    root = Node(10)
    root.left = Node(5); root.right = Node(-3)
    root.left.left = Node(3); root.left.right = Node(2)
    root.right.right = Node(11)
    root.left.left.left = Node(3); root.left.left.right = Node(-2)
    root.left.right.right = Node(1)
    print(path_sum(root, 8))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_04_12_paths_with_sum.languages.scala -->
### scala

```scala
object Lcci0412PathsWithSum {
  final case class Node(value: Int, var left: Node | Null = null, var right: Node | Null = null)

  def pathSum(root: Node | Null, target: Int): Int = {
    val counts = scala.collection.mutable.Map[Long, Int](0L -> 1)

    def dfs(node: Node | Null, prefix: Long): Int = {
      if (node == null) return 0
      val cur = node.asInstanceOf[Node]
      val next = prefix + cur.value
      var res = counts.getOrElse(next - target, 0)
      counts.update(next, counts.getOrElse(next, 0) + 1)
      res += dfs(cur.left, next)
      res += dfs(cur.right, next)
      counts.update(next, counts(next) - 1)
      res
    }

    dfs(root, 0L)
  }

  def main(args: Array[String]): Unit = {
    val root = Node(
      10,
      Node(5, Node(3, Node(3), Node(-2)), Node(2, null, Node(1))),
      Node(-3, null, Node(11))
    )
    println(pathSum(root, 8))
  }
}
```

<!-- REGISTRY_PATH: lcci_04_12_paths_with_sum.languages.typescript -->
### typescript

```typescript
class Node {
  constructor(
    public val: number,
    public left: Node | null = null,
    public right: Node | null = null
  ) {}
}

function pathSum(root: Node | null, target: number): number {
  const count = new Map<number, number>();
  count.set(0, 1);

  const dfs = (node: Node | null, prefix: number): number => {
    if (!node) return 0;
    prefix += node.val;
    let res = count.get(prefix - target) ?? 0;
    count.set(prefix, (count.get(prefix) ?? 0) + 1);
    res += dfs(node.left, prefix);
    res += dfs(node.right, prefix);
    count.set(prefix, (count.get(prefix) ?? 1) - 1);
    return res;
  };

  return dfs(root, 0);
}

const root = new Node(
  10,
  new Node(5, new Node(3, new Node(3), new Node(-2)), new Node(2, null, new Node(1))),
  new Node(-3, null, new Node(11))
);
console.log(pathSum(root, 8));
```

## lcci_05_01_insert

<!-- REGISTRY_PATH: lcci_05_01_insert.languages.cpp -->
### cpp

```cpp
#include <iostream>

// Insert bits of M into N from bit i to bit j (inclusive).
int insert(int N, int M, int i, int j) {
    int mask = ~(((1 << (j - i + 1)) - 1) << i);
    return (N & mask) | (M << i);
}

int main() {
    // N = 10000000000, M = 10011, i = 2, j = 6  -> 10001001100
    std::cout << insert(1024, 19, 2, 6) << '\n';
    // N = 0, M = 10011, i = 0, j = 4            -> 10011
    std::cout << insert(0, 19, 0, 4) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_05_01_insert.languages.go -->
### go

```go
package main

import "fmt"

func insert(N int, M int, i int, j int) int {
	mask := ^(((1 << (j - i + 1)) - 1) << i)
	return (N & mask) | (M << i)
}

func main() {
	fmt.Println(insert(1024, 19, 2, 6))
	fmt.Println(insert(0, 19, 0, 4))
}
```

<!-- REGISTRY_PATH: lcci_05_01_insert.languages.python -->
### python

```python
def insert(N: int, M: int, i: int, j: int) -> int:
    mask = ~(((1 << (j - i + 1)) - 1) << i)
    return (N & mask) | (M << i)


def main() -> None:
    print(insert(1024, 19, 2, 6))
    print(insert(0, 19, 0, 4))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_01_insert.languages.scala -->
### scala

```scala
object Lcci0501Insert {
  def insert(N: Int, M: Int, i: Int, j: Int): Int = {
    val mask = ~(((1 << (j - i + 1)) - 1) << i)
    (N & mask) | (M << i)
  }

  def main(args: Array[String]): Unit = {
    println(insert(1024, 19, 2, 6))
    println(insert(0, 19, 0, 4))
  }
}
```

<!-- REGISTRY_PATH: lcci_05_01_insert.languages.typescript -->
### typescript

```typescript
function insert(N: number, M: number, i: number, j: number): number {
  const mask = ~(((1 << (j - i + 1)) - 1) << i);
  return (N & mask) | (M << i);
}

console.log(insert(1024, 19, 2, 6));
console.log(insert(0, 19, 0, 4));
```

## lcci_05_02_binary_number_to_string

<!-- REGISTRY_PATH: lcci_05_02_binary_number_to_string.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>

// Convert a decimal fraction (0 < n < 1) to its binary string representation.
// Return "ERROR" if the representation exceeds 32 characters.
std::string binaryToString(double n) {
    std::string result = "0.";
    while (n > 0) {
        if (result.size() > 32) return "ERROR";
        n *= 2;
        if (n >= 1) { result += '1'; n -= 1; }
        else result += '0';
    }
    return result;
}

int main() {
    std::cout << binaryToString(0.625) << '\n';
    std::cout << binaryToString(0.1) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_05_02_binary_number_to_string.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

func binaryToString(n float64) string {
	var sb strings.Builder
	sb.WriteString("0.")
	for n > 0 {
		if sb.Len() > 32 {
			return "ERROR"
		}
		n *= 2
		if n >= 1 {
			sb.WriteByte('1')
			n -= 1
		} else {
			sb.WriteByte('0')
		}
	}
	return sb.String()
}

func main() {
	fmt.Println(binaryToString(0.625))
	fmt.Println(binaryToString(0.1))
}
```

<!-- REGISTRY_PATH: lcci_05_02_binary_number_to_string.languages.python -->
### python

```python
def binary_to_string(n: float) -> str:
    result = ["0."]
    while n > 0:
        if len(result) > 32:
            return "ERROR"
        n *= 2
        if n >= 1:
            result.append("1")
            n -= 1
        else:
            result.append("0")
    return "".join(result)


def main() -> None:
    print(binary_to_string(0.625))
    print(binary_to_string(0.1))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_02_binary_number_to_string.languages.scala -->
### scala

```scala
object Lcci0502BinaryNumberToString {
  def binaryToString(n0: Double): String = {
    val sb = new StringBuilder("0.")
    var n = n0
    while (n > 0) {
      if (sb.length > 32) return "ERROR"
      n *= 2
      if (n >= 1) { sb.append('1'); n -= 1 }
      else sb.append('0')
    }
    sb.toString
  }

  def main(args: Array[String]): Unit = {
    println(binaryToString(0.625))
    println(binaryToString(0.1))
  }
}
```

<!-- REGISTRY_PATH: lcci_05_02_binary_number_to_string.languages.typescript -->
### typescript

```typescript
function binaryToString(n: number): string {
  let result = "0.";
  while (n > 0) {
    if (result.length > 32) return "ERROR";
    n *= 2;
    if (n >= 1) {
      result += "1";
      n -= 1;
    } else {
      result += "0";
    }
  }
  return result;
}

console.log(binaryToString(0.625));
console.log(binaryToString(0.1));
```

## lcci_05_03_flip_bit_to_win

<!-- REGISTRY_PATH: lcci_05_03_flip_bit_to_win.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>

// Find the longest sequence of 1s achievable by flipping one 0 bit.
int flipBit(int num) {
    if (~num == 0) return 32;  // all 1s already
    int cur = 0, prev = 0, best = 1;
    while (num > 0) {
        if (num & 1) { cur++; }
        else { prev = cur; cur = 0; }
        best = std::max(best, prev + 1 + cur);
        num >>= 1;
    }
    return best;
}

int main() {
    // 1775 = 11011101111, longest run after one flip = 8
    std::cout << flipBit(1775) << '\n';
    // 7 = 111, already 3 ones; flipping a 0 at bit 3 gives 4
    std::cout << flipBit(7) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_05_03_flip_bit_to_win.languages.go -->
### go

```go
package main

import "fmt"

func flipBit(num uint32) int {
	if num == 0xFFFFFFFF {
		return 32
	}
	cur, prev, best := 0, 0, 1
	for num > 0 {
		if num&1 == 1 {
			cur++
		} else {
			prev = cur
			cur = 0
		}
		if v := prev + 1 + cur; v > best {
			best = v
		}
		num >>= 1
	}
	return best
}

func main() {
	fmt.Println(flipBit(1775))
	fmt.Println(flipBit(7))
}
```

<!-- REGISTRY_PATH: lcci_05_03_flip_bit_to_win.languages.python -->
### python

```python
def flip_bit(num: int) -> int:
    # Treat as 32-bit unsigned integer
    if num & 0xFFFFFFFF == 0xFFFFFFFF:
        return 32
    num = num & 0xFFFFFFFF
    cur = prev = 0
    best = 1
    while num > 0:
        if num & 1:
            cur += 1
        else:
            prev = cur
            cur = 0
        best = max(best, prev + 1 + cur)
        num >>= 1
    return best


def main() -> None:
    print(flip_bit(1775))
    print(flip_bit(7))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_03_flip_bit_to_win.languages.scala -->
### scala

```scala
object Lcci0503FlipBitToWin {
  def flipBit(num: Int): Int = {
    if (~num == 0) return 32
    var n = num & 0xFFFFFFFFL.toInt
    // Use unsigned right shift via Long
    var uNum = num.toLong & 0xFFFFFFFFL
    var cur = 0; var prev = 0; var best = 1
    while (uNum > 0) {
      if ((uNum & 1) == 1) cur += 1
      else { prev = cur; cur = 0 }
      val v = prev + 1 + cur
      if (v > best) best = v
      uNum >>>= 1
    }
    best
  }

  def main(args: Array[String]): Unit = {
    println(flipBit(1775))
    println(flipBit(7))
  }
}
```

<!-- REGISTRY_PATH: lcci_05_03_flip_bit_to_win.languages.typescript -->
### typescript

```typescript
function flipBit(num: number): number {
  // Work with 32-bit unsigned
  num = num >>> 0;
  if (num === 0xffffffff) return 32;
  let cur = 0, prev = 0, best = 1;
  while (num > 0) {
    if (num & 1) {
      cur++;
    } else {
      prev = cur;
      cur = 0;
    }
    best = Math.max(best, prev + 1 + cur);
    num >>>= 1;
  }
  return best;
}

console.log(flipBit(1775));
console.log(flipBit(7));
```

## lcci_05_04_closed_number

<!-- REGISTRY_PATH: lcci_05_04_closed_number.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

// Return the next smaller and next larger numbers with the same popcount.
// Returns {next smaller, next larger}.
std::vector<int> findClosedNumbers(int num) {
    int bigger = num, smaller = num;

    // Next larger: find rightmost 01 pattern and flip
    for (int i = 1; i < 32; i++) {
        if ((bigger & (1 << (i - 1))) && !(bigger & (1 << i))) {
            bigger |= (1 << i);
            bigger &= ~(1 << (i - 1));
            break;
        }
    }

    // Next smaller: find rightmost 10 pattern and flip
    for (int i = 1; i < 32; i++) {
        if (!(smaller & (1 << (i - 1))) && (smaller & (1 << i))) {
            smaller &= ~(1 << i);
            smaller |= (1 << (i - 1));
            break;
        }
    }

    return {bigger, smaller};
}

int main() {
    auto res = findClosedNumbers(2);  // 010 -> bigger=100(4), smaller=001(1)
    std::cout << res[0] << '\n' << res[1] << '\n';
}
```

<!-- REGISTRY_PATH: lcci_05_04_closed_number.languages.go -->
### go

```go
package main

import "fmt"

func findClosedNumbers(num int) (int, int) {
	bigger, smaller := num, num

	for i := 1; i < 32; i++ {
		if bigger>>(i-1)&1 == 1 && bigger>>i&1 == 0 {
			bigger |= 1 << i
			bigger &^= 1 << (i - 1)
			break
		}
	}

	for i := 1; i < 32; i++ {
		if smaller>>(i-1)&1 == 0 && smaller>>i&1 == 1 {
			smaller &^= 1 << i
			smaller |= 1 << (i - 1)
			break
		}
	}

	return bigger, smaller
}

func main() {
	bigger, smaller := findClosedNumbers(2)
	fmt.Println(bigger)
	fmt.Println(smaller)
}
```

<!-- REGISTRY_PATH: lcci_05_04_closed_number.languages.python -->
### python

```python
def find_closed_numbers(num: int) -> tuple[int, int]:
    bigger = num
    smaller = num

    # Next larger: find rightmost '01' and flip to '10'
    for i in range(1, 32):
        if (bigger >> (i - 1)) & 1 == 1 and (bigger >> i) & 1 == 0:
            bigger |= (1 << i)
            bigger &= ~(1 << (i - 1))
            break

    # Next smaller: find rightmost '10' and flip to '01'
    for i in range(1, 32):
        if (smaller >> (i - 1)) & 1 == 0 and (smaller >> i) & 1 == 1:
            smaller &= ~(1 << i)
            smaller |= (1 << (i - 1))
            break

    return bigger, smaller


def main() -> None:
    bigger, smaller = find_closed_numbers(2)
    print(bigger)
    print(smaller)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_04_closed_number.languages.scala -->
### scala

```scala
object Lcci0504ClosedNumber {
  def findClosedNumbers(num: Int): (Int, Int) = {
    var bigger = num
    var smaller = num

    var i = 1
    while (i < 32) {
      if ((bigger >> (i - 1) & 1) == 1 && (bigger >> i & 1) == 0) {
        bigger |= 1 << i; bigger &= ~(1 << (i - 1)); i = 32
      }
      i += 1
    }

    i = 1
    while (i < 32) {
      if ((smaller >> (i - 1) & 1) == 0 && (smaller >> i & 1) == 1) {
        smaller &= ~(1 << i); smaller |= 1 << (i - 1); i = 32
      }
      i += 1
    }

    (bigger, smaller)
  }

  def main(args: Array[String]): Unit = {
    val (bigger, smaller) = findClosedNumbers(2)
    println(bigger)
    println(smaller)
  }
}
```

<!-- REGISTRY_PATH: lcci_05_04_closed_number.languages.typescript -->
### typescript

```typescript
function findClosedNumbers(num: number): [number, number] {
  let bigger = num, smaller = num;

  for (let i = 1; i < 32; i++) {
    if ((bigger >> (i - 1)) & 1 && !((bigger >> i) & 1)) {
      bigger |= 1 << i;
      bigger &= ~(1 << (i - 1));
      break;
    }
  }

  for (let i = 1; i < 32; i++) {
    if (!((smaller >> (i - 1)) & 1) && (smaller >> i) & 1) {
      smaller &= ~(1 << i);
      smaller |= 1 << (i - 1);
      break;
    }
  }

  return [bigger, smaller];
}

const [bigger, smaller] = findClosedNumbers(2);
console.log(bigger);
console.log(smaller);
```

## lcci_05_06_number_of_1

<!-- REGISTRY_PATH: lcci_05_06_number_of_1.languages.cpp -->
### cpp

```cpp
#include <iostream>

// Count the number of bits you must flip to convert integer A to integer B.
int convertInteger(int A, int B) {
    unsigned int x = (unsigned int)(A ^ B);
    int count = 0;
    while (x) { count += x & 1; x >>= 1; }
    return count;
}

int main() {
    std::cout << convertInteger(29, 15) << '\n';  // 29=11101, 15=01111 -> 2 bits differ
    std::cout << convertInteger(1, 5)  << '\n';  //  1=001, 5=101   -> 1 bit differs
}
```

<!-- REGISTRY_PATH: lcci_05_06_number_of_1.languages.go -->
### go

```go
package main

import (
	"fmt"
	"math/bits"
)

func convertInteger(A int32, B int32) int {
	return bits.OnesCount32(uint32(A ^ B))
}

func main() {
	fmt.Println(convertInteger(29, 15))
	fmt.Println(convertInteger(1, 5))
}
```

<!-- REGISTRY_PATH: lcci_05_06_number_of_1.languages.python -->
### python

```python
def convert_integer(A: int, B: int) -> int:
    # Work with 32-bit two's complement representation
    x = (A ^ B) & 0xFFFFFFFF
    return bin(x).count('1')


def main() -> None:
    print(convert_integer(29, 15))
    print(convert_integer(1, 5))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_06_number_of_1.languages.scala -->
### scala

```scala
object Lcci0506NumberOf1 {
  def convertInteger(A: Int, B: Int): Int =
    Integer.bitCount(A ^ B)

  def main(args: Array[String]): Unit = {
    println(convertInteger(29, 15))
    println(convertInteger(1, 5))
  }
}
```

<!-- REGISTRY_PATH: lcci_05_06_number_of_1.languages.typescript -->
### typescript

```typescript
function convertInteger(A: number, B: number): number {
  let x = (A ^ B) >>> 0;
  let count = 0;
  while (x) {
    count += x & 1;
    x >>>= 1;
  }
  return count;
}

console.log(convertInteger(29, 15));
console.log(convertInteger(1, 5));
```

## lcci_05_07_exchange

<!-- REGISTRY_PATH: lcci_05_07_exchange.languages.cpp -->
### cpp

```cpp
#include <iostream>

// Swap all odd and even bits of an integer.
// Odd bits (0-indexed): mask 0x55555555; even bits: mask 0xAAAAAAAA.
int exchangeBits(int num) {
    unsigned int unum = (unsigned int)num;
    return (int)(((unum & 0xAAAAAAAAu) >> 1) | ((unum & 0x55555555u) << 1));
}

int main() {
    // 2 = 010 -> after swap -> 001 = 1
    std::cout << exchangeBits(2) << '\n';
    // 3 = 011 -> 11 -> swap -> 11 = 3
    std::cout << exchangeBits(3) << '\n';
}
```

<!-- REGISTRY_PATH: lcci_05_07_exchange.languages.go -->
### go

```go
package main

import "fmt"

func exchangeBits(num int) int {
	u := uint32(num)
	return int(((u & 0xAAAAAAAA) >> 1) | ((u & 0x55555555) << 1))
}

func main() {
	fmt.Println(exchangeBits(2))
	fmt.Println(exchangeBits(3))
}
```

<!-- REGISTRY_PATH: lcci_05_07_exchange.languages.python -->
### python

```python
def exchange_bits(num: int) -> int:
    u = num & 0xFFFFFFFF
    return (((u & 0xAAAAAAAA) >> 1) | ((u & 0x55555555) << 1)) & 0xFFFFFFFF


def main() -> None:
    print(exchange_bits(2))
    print(exchange_bits(3))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_07_exchange.languages.scala -->
### scala

```scala
object Lcci0507Exchange {
  def exchangeBits(num: Int): Int = {
    val u = num & 0xFFFFFFFFL
    val odd  = (u & 0xAAAAAAAAL) >> 1
    val even = (u & 0x55555555L) << 1
    (odd | even).toInt
  }

  def main(args: Array[String]): Unit = {
    println(exchangeBits(2))
    println(exchangeBits(3))
  }
}
```

<!-- REGISTRY_PATH: lcci_05_07_exchange.languages.typescript -->
### typescript

```typescript
function exchangeBits(num: number): number {
  const u = num >>> 0;
  return (((u & 0xAAAAAAAA) >>> 1) | ((u & 0x55555555) << 1)) >>> 0;
}

console.log(exchangeBits(2));
console.log(exchangeBits(3));
```

## lcci_05_08_draw_line

<!-- REGISTRY_PATH: lcci_05_08_draw_line.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

// Draw a horizontal line from pixel x1 to x2 in a screen of 32-bit words per row.
// width is the number of pixels per row (multiple of 32).
std::vector<int> drawLine(int length, int w, int x1, int x2, int y) {
    int words_per_row = w / 32;
    std::vector<int> screen(length, 0);
    int offset = y * words_per_row;

    int start_byte = x1 / 32 + offset;
    int end_byte   = x2 / 32 + offset;
    int start_bit  = x1 % 32;
    int end_bit    = x2 % 32;

    for (int i = start_byte; i <= end_byte; i++) {
        int hi = (i == start_byte) ? (0xFF >> start_bit) : 0xFF;
        int lo = (i == end_byte)   ? ~(0xFF >> (end_bit + 1)) : 0xFF;
        screen[i] = hi & lo;
    }
    return screen;
}

int main() {
    // width=32, draw from x1=1 to x2=30 on row 0
    auto result = drawLine(1, 32, 1, 30, 0);
    // Print as hex
    for (int v : result) std::cout << std::hex << v << '\n';
}
```

<!-- REGISTRY_PATH: lcci_05_08_draw_line.languages.go -->
### go

```go
package main

import "fmt"

func drawLine(length int, w int, x1 int, x2 int, y int) []int {
	wordsPerRow := w / 32
	screen := make([]int, length)
	offset := y * wordsPerRow

	startWord := x1/32 + offset
	endWord := x2/32 + offset
	startBit := x1 % 32
	endBit := x2 % 32

	for i := startWord; i <= endWord; i++ {
		hi := 0xFF
		if i == startWord {
			hi = 0xFF >> startBit
		}
		lo := 0xFF
		if i == endWord {
			lo = ^(0xFF >> (endBit + 1))
		}
		screen[i] = hi & lo
	}
	return screen
}

func main() {
	result := drawLine(1, 32, 1, 30, 0)
	for _, v := range result {
		fmt.Printf("%x\n", v)
	}
}
```

<!-- REGISTRY_PATH: lcci_05_08_draw_line.languages.python -->
### python

```python
def draw_line(length: int, w: int, x1: int, x2: int, y: int) -> list[int]:
    words_per_row = w // 32
    screen = [0] * length
    offset = y * words_per_row

    start_word = x1 // 32 + offset
    end_word   = x2 // 32 + offset
    start_bit  = x1 % 32
    end_bit    = x2 % 32

    for i in range(start_word, end_word + 1):
        hi = (0xFF >> start_bit) if i == start_word else 0xFF
        lo = (~(0xFF >> (end_bit + 1))) & 0xFF if i == end_word else 0xFF
        screen[i] = hi & lo

    return screen


def main() -> None:
    result = draw_line(1, 32, 1, 30, 0)
    for v in result:
        print(hex(v))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_05_08_draw_line.languages.scala -->
### scala

```scala
object Lcci0508DrawLine {
  def drawLine(length: Int, w: Int, x1: Int, x2: Int, y: Int): Array[Int] = {
    val wordsPerRow = w / 32
    val screen = new Array[Int](length)
    val offset = y * wordsPerRow
    val startWord = x1 / 32 + offset
    val endWord = x2 / 32 + offset
    val startBit = x1 % 32
    val endBit = x2 % 32

    for (i <- startWord to endWord) {
      val hi = if (i == startWord) 0xFF >> startBit else 0xFF
      val lo = if (i == endWord) ~(0xFF >> (endBit + 1)) else 0xFF
      screen(i) = hi & lo
    }
    screen
  }

  def main(args: Array[String]): Unit = {
    val result = drawLine(1, 32, 1, 30, 0)
    result.foreach(v => println(v.toHexString))
  }
}
```

<!-- REGISTRY_PATH: lcci_05_08_draw_line.languages.typescript -->
### typescript

```typescript
function drawLine(
  length: number,
  w: number,
  x1: number,
  x2: number,
  y: number
): number[] {
  const wordsPerRow = (w / 32) | 0;
  const screen = new Array<number>(length).fill(0);
  const offset = y * wordsPerRow;

  const startWord = ((x1 / 32) | 0) + offset;
  const endWord = ((x2 / 32) | 0) + offset;
  const startBit = x1 % 32;
  const endBit = x2 % 32;

  for (let i = startWord; i <= endWord; i++) {
    let hi = i === startWord ? 0xff >> startBit : 0xff;
    let lo = i === endWord ? ~(0xff >> (endBit + 1)) & 0xff : 0xff;
    screen[i] = hi & lo;
  }
  return screen;
}

const result = drawLine(1, 32, 1, 30, 0);
for (const v of result) console.log(v.toString(16));
```

## lcci_08_01_three_steps

<!-- REGISTRY_PATH: lcci_08_01_three_steps.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

int waysToStep(int n) {
    const long long MOD = 1e9 + 7;
    if (n == 1) return 1;
    if (n == 2) return 2;
    if (n == 3) return 4;
    long long a = 1, b = 2, c = 4;
    for (int i = 3; i < n; i++) {
        long long d = ((a + b) % MOD + c) % MOD;
        a = b; b = c; c = d;
    }
    return (int)c;
}

int main() {
    cout << waysToStep(3) << endl; // 4
    cout << waysToStep(5) << endl; // 13
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_01_three_steps.languages.go -->
### go

```go
package main

import "fmt"

func waysToStep(n int) int {
	const MOD = 1000000007
	if n == 1 {
		return 1
	}
	if n == 2 {
		return 2
	}
	if n == 3 {
		return 4
	}
	a, b, c := 1, 2, 4
	for i := 3; i < n; i++ {
		a, b, c = b, c, ((a+b)%MOD+c)%MOD
	}
	return c
}

func main() {
	fmt.Println(waysToStep(3)) // 4
	fmt.Println(waysToStep(5)) // 13
}
```

<!-- REGISTRY_PATH: lcci_08_01_three_steps.languages.python -->
### python

```python
def waysToStep(n: int) -> int:
    MOD = 10**9 + 7
    if n == 1: return 1
    if n == 2: return 2
    if n == 3: return 4
    a, b, c = 1, 2, 4
    for _ in range(n - 3):
        a, b, c = b, c, (a + b + c) % MOD
    return c

def main():
    print(waysToStep(3))  # 4
    print(waysToStep(5))  # 13

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_01_three_steps.languages.scala -->
### scala

```scala
object Lcci0801ThreeSteps {
    def waysToStep(n: Int): Int = {
        val MOD = 1000000007L
        if (n == 1) return 1
        if (n == 2) return 2
        if (n == 3) return 4
        var a = 1L; var b = 2L; var c = 4L
        for (_ <- 3 until n) {
            val d = ((a + b) % MOD + c) % MOD
            a = b; b = c; c = d
        }
        c.toInt
    }

    def main(args: Array[String]): Unit = {
        println(waysToStep(3)) // 4
        println(waysToStep(5)) // 13
    }
}
```

<!-- REGISTRY_PATH: lcci_08_01_three_steps.languages.typescript -->
### typescript

```typescript
function waysToStep(n: number): number {
    const MOD = 1000000007n;
    if (n === 1) return 1;
    if (n === 2) return 2;
    if (n === 3) return 4;
    let a = 1n, b = 2n, c = 4n;
    for (let i = 3; i < n; i++) {
        [a, b, c] = [b, c, ((a + b) % MOD + c) % MOD];
    }
    return Number(c);
}

console.log(waysToStep(3)); // 4
console.log(waysToStep(5)); // 13
```

## lcci_08_02_robot_in_a_grid

<!-- REGISTRY_PATH: lcci_08_02_robot_in_a_grid.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

vector<vector<int>> pathWithObstacles(vector<vector<int>>& obstacleGrid) {
    int r = obstacleGrid.size(), c = obstacleGrid[0].size();
    vector<vector<int>> path;
    vector<vector<bool>> visited(r, vector<bool>(c, false));

    function<bool(int, int)> dfs = [&](int i, int j) -> bool {
        if (i >= r || j >= c || obstacleGrid[i][j] == 1 || visited[i][j]) return false;
        visited[i][j] = true;
        path.push_back({i, j});
        if (i == r - 1 && j == c - 1) return true;
        if (dfs(i + 1, j) || dfs(i, j + 1)) return true;
        path.pop_back();
        return false;
    };

    dfs(0, 0);
    return path;
}

int main() {
    vector<vector<int>> grid = {{0,0,0},{0,1,0},{0,0,0}};
    auto path = pathWithObstacles(grid);
    cout << "[";
    for (int i = 0; i < (int)path.size(); i++) {
        cout << "[" << path[i][0] << "," << path[i][1] << "]";
        if (i + 1 < (int)path.size()) cout << ",";
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_02_robot_in_a_grid.languages.go -->
### go

```go
package main

import "fmt"

func pathWithObstacles(obstacleGrid [][]int) [][]int {
	r, c := len(obstacleGrid), len(obstacleGrid[0])
	path := [][]int{}
	visited := make([][]bool, r)
	for i := range visited {
		visited[i] = make([]bool, c)
	}

	var dfs func(i, j int) bool
	dfs = func(i, j int) bool {
		if i >= r || j >= c || obstacleGrid[i][j] == 1 || visited[i][j] {
			return false
		}
		visited[i][j] = true
		path = append(path, []int{i, j})
		if i == r-1 && j == c-1 {
			return true
		}
		if dfs(i+1, j) || dfs(i, j+1) {
			return true
		}
		path = path[:len(path)-1]
		return false
	}

	dfs(0, 0)
	return path
}

func main() {
	grid := [][]int{{0, 0, 0}, {0, 1, 0}, {0, 0, 0}}
	fmt.Println(pathWithObstacles(grid))
}
```

<!-- REGISTRY_PATH: lcci_08_02_robot_in_a_grid.languages.python -->
### python

```python
from typing import List

def pathWithObstacles(obstacleGrid: List[List[int]]) -> List[List[int]]:
    r, c = len(obstacleGrid), len(obstacleGrid[0])
    path = []
    visited = [[False] * c for _ in range(r)]

    def dfs(i, j):
        if i >= r or j >= c or obstacleGrid[i][j] == 1 or visited[i][j]:
            return False
        visited[i][j] = True
        path.append([i, j])
        if i == r - 1 and j == c - 1:
            return True
        if dfs(i + 1, j) or dfs(i, j + 1):
            return True
        path.pop()
        return False

    dfs(0, 0)
    return path

def main():
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(pathWithObstacles(grid))

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_02_robot_in_a_grid.languages.scala -->
### scala

```scala
import scala.collection.mutable.ArrayBuffer

object Lcci0802RobotInAGrid {
    def pathWithObstacles(obstacleGrid: Array[Array[Int]]): Array[Array[Int]] = {
        val r = obstacleGrid.length; val c = obstacleGrid(0).length
        val path = ArrayBuffer[Array[Int]]()
        val visited = Array.ofDim[Boolean](r, c)

        def dfs(i: Int, j: Int): Boolean = {
            if (i >= r || j >= c || obstacleGrid(i)(j) == 1 || visited(i)(j)) return false
            visited(i)(j) = true
            path += Array(i, j)
            if (i == r - 1 && j == c - 1) return true
            if (dfs(i + 1, j) || dfs(i, j + 1)) return true
            path.remove(path.length - 1)
            false
        }

        dfs(0, 0)
        path.toArray
    }

    def main(args: Array[String]): Unit = {
        val grid = Array(Array(0,0,0), Array(0,1,0), Array(0,0,0))
        val path = pathWithObstacles(grid)
        println(path.map(p => s"[${p(0)},${p(1)}]").mkString("[", ",", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_08_02_robot_in_a_grid.languages.typescript -->
### typescript

```typescript
function pathWithObstacles(obstacleGrid: number[][]): number[][] {
    const r = obstacleGrid.length, c = obstacleGrid[0].length;
    const path: number[][] = [];
    const visited = Array.from({ length: r }, () => new Array(c).fill(false));

    function dfs(i: number, j: number): boolean {
        if (i >= r || j >= c || obstacleGrid[i][j] === 1 || visited[i][j]) return false;
        visited[i][j] = true;
        path.push([i, j]);
        if (i === r - 1 && j === c - 1) return true;
        if (dfs(i + 1, j) || dfs(i, j + 1)) return true;
        path.pop();
        return false;
    }

    dfs(0, 0);
    return path;
}

console.log(JSON.stringify(pathWithObstacles([[0,0,0],[0,1,0],[0,0,0]])));
```

## lcci_08_03_magic_index

<!-- REGISTRY_PATH: lcci_08_03_magic_index.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

int findMagicIndex(vector<int>& nums) {
    int lo = 0, hi = (int)nums.size() - 1;
    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;
        if (nums[mid] == mid) return mid;
        if (nums[mid] < mid) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> a = {-1, 1, 3, 4, 6};
    cout << findMagicIndex(a) << endl; // 1
    vector<int> b = {0, 2, 3, 4, 5};
    cout << findMagicIndex(b) << endl; // 0
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_03_magic_index.languages.go -->
### go

```go
package main

import "fmt"

func findMagicIndex(nums []int) int {
	lo, hi := 0, len(nums)-1
	for lo <= hi {
		mid := lo + (hi-lo)/2
		if nums[mid] == mid {
			return mid
		}
		if nums[mid] < mid {
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return -1
}

func main() {
	fmt.Println(findMagicIndex([]int{-1, 1, 3, 4, 6})) // 1
	fmt.Println(findMagicIndex([]int{0, 2, 3, 4, 5}))  // 0
}
```

<!-- REGISTRY_PATH: lcci_08_03_magic_index.languages.python -->
### python

```python
from typing import List

def findMagicIndex(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == mid:
            return mid
        if nums[mid] < mid:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def main():
    print(findMagicIndex([-1, 1, 3, 4, 6]))  # 1
    print(findMagicIndex([0, 2, 3, 4, 5]))   # 0

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_03_magic_index.languages.scala -->
### scala

```scala
object Lcci0803MagicIndex {
    def findMagicIndex(nums: Array[Int]): Int = {
        var lo = 0; var hi = nums.length - 1
        while (lo <= hi) {
            val mid = lo + (hi - lo) / 2
            if (nums(mid) == mid) return mid
            if (nums(mid) < mid) lo = mid + 1
            else hi = mid - 1
        }
        -1
    }

    def main(args: Array[String]): Unit = {
        println(findMagicIndex(Array(-1, 1, 3, 4, 6))) // 1
        println(findMagicIndex(Array(0, 2, 3, 4, 5)))  // 0
    }
}
```

<!-- REGISTRY_PATH: lcci_08_03_magic_index.languages.typescript -->
### typescript

```typescript
function findMagicIndex(nums: number[]): number {
    let lo = 0, hi = nums.length - 1;
    while (lo <= hi) {
        const mid = (lo + hi) >> 1;
        if (nums[mid] === mid) return mid;
        if (nums[mid] < mid) lo = mid + 1;
        else hi = mid - 1;
    }
    return -1;
}

console.log(findMagicIndex([-1, 1, 3, 4, 6])); // 1
console.log(findMagicIndex([0, 2, 3, 4, 5]));  // 0
```

## lcci_08_04_power_set

<!-- REGISTRY_PATH: lcci_08_04_power_set.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<vector<int>> subsets(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    int n = nums.size();
    vector<vector<int>> result;
    for (int mask = 0; mask < (1 << n); mask++) {
        vector<int> subset;
        for (int i = 0; i < n; i++) {
            if (mask & (1 << i)) subset.push_back(nums[i]);
        }
        result.push_back(subset);
    }
    return result;
}

int main() {
    vector<int> nums = {1, 2, 3};
    auto result = subsets(nums);
    for (auto& s : result) {
        cout << "[";
        for (int i = 0; i < (int)s.size(); i++) {
            cout << s[i];
            if (i + 1 < (int)s.size()) cout << ",";
        }
        cout << "]" << endl;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_04_power_set.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func subsets(nums []int) [][]int {
	sort.Ints(nums)
	n := len(nums)
	result := [][]int{}
	for mask := 0; mask < (1 << n); mask++ {
		subset := []int{}
		for i := 0; i < n; i++ {
			if mask&(1<<i) != 0 {
				subset = append(subset, nums[i])
			}
		}
		result = append(result, subset)
	}
	return result
}

func main() {
	for _, s := range subsets([]int{1, 2, 3}) {
		fmt.Println(s)
	}
}
```

<!-- REGISTRY_PATH: lcci_08_04_power_set.languages.python -->
### python

```python
from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    result = []
    for mask in range(1 << n):
        subset = [nums[i] for i in range(n) if mask & (1 << i)]
        result.append(subset)
    return result

def main():
    for s in subsets([1, 2, 3]):
        print(s)

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_04_power_set.languages.scala -->
### scala

```scala
object Lcci0804PowerSet {
    def subsets(nums: Array[Int]): Array[Array[Int]] = {
        val sorted = nums.sorted
        val n = sorted.length
        (0 until (1 << n)).map { mask =>
            (0 until n).filter(i => (mask & (1 << i)) != 0).map(sorted(_)).toArray
        }.toArray
    }

    def main(args: Array[String]): Unit = {
        for (s <- subsets(Array(1, 2, 3))) {
            println(s.mkString("[", ",", "]"))
        }
    }
}
```

<!-- REGISTRY_PATH: lcci_08_04_power_set.languages.typescript -->
### typescript

```typescript
function subsets(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const result: number[][] = [];
    for (let mask = 0; mask < (1 << n); mask++) {
        const subset: number[] = [];
        for (let i = 0; i < n; i++) {
            if (mask & (1 << i)) subset.push(nums[i]);
        }
        result.push(subset);
    }
    return result;
}

for (const s of subsets([1, 2, 3])) {
    console.log(JSON.stringify(s));
}
```

## lcci_08_06_hanota

<!-- REGISTRY_PATH: lcci_08_06_hanota.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

void hanota(vector<int>& A, vector<int>& B, vector<int>& C) {
    function<void(int, vector<int>&, vector<int>&, vector<int>&)> move =
        [&](int n, vector<int>& src, vector<int>& aux, vector<int>& dst) {
            if (n == 0) return;
            move(n - 1, src, dst, aux);
            dst.push_back(src.back());
            src.pop_back();
            move(n - 1, aux, src, dst);
        };
    move((int)A.size(), A, B, C);
}

int main() {
    vector<int> A = {2, 1, 0}, B = {}, C = {};
    hanota(A, B, C);
    cout << "A: ["; for (int i = 0; i < (int)A.size(); i++) cout << (i?",":"") << A[i]; cout << "]" << endl;
    cout << "B: ["; for (int i = 0; i < (int)B.size(); i++) cout << (i?",":"") << B[i]; cout << "]" << endl;
    cout << "C: ["; for (int i = 0; i < (int)C.size(); i++) cout << (i?",":"") << C[i]; cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_06_hanota.languages.go -->
### go

```go
package main

import "fmt"

func hanota(A *[]int, B *[]int, C *[]int) {
	var move func(n int, src, aux, dst *[]int)
	move = func(n int, src, aux, dst *[]int) {
		if n == 0 {
			return
		}
		move(n-1, src, dst, aux)
		*dst = append(*dst, (*src)[len(*src)-1])
		*src = (*src)[:len(*src)-1]
		move(n-1, aux, src, dst)
	}
	move(len(*A), A, B, C)
}

func main() {
	A := []int{2, 1, 0}
	B := []int{}
	C := []int{}
	hanota(&A, &B, &C)
	fmt.Println("A:", A)
	fmt.Println("B:", B)
	fmt.Println("C:", C)
}
```

<!-- REGISTRY_PATH: lcci_08_06_hanota.languages.python -->
### python

```python
from typing import List

def hanota(A: List[int], B: List[int], C: List[int]) -> None:
    def move(n, src, aux, dst):
        if n == 0:
            return
        move(n - 1, src, dst, aux)
        dst.append(src.pop())
        move(n - 1, aux, src, dst)

    move(len(A), A, B, C)

def main():
    A, B, C = [2, 1, 0], [], []
    hanota(A, B, C)
    print(f"A: {A}")
    print(f"B: {B}")
    print(f"C: {C}")

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_06_hanota.languages.scala -->
### scala

```scala
import scala.collection.mutable.ArrayBuffer

object Lcci0806Hanota {
    def hanota(A: ArrayBuffer[Int], B: ArrayBuffer[Int], C: ArrayBuffer[Int]): Unit = {
        def move(n: Int, src: ArrayBuffer[Int], aux: ArrayBuffer[Int], dst: ArrayBuffer[Int]): Unit = {
            if (n == 0) return
            move(n - 1, src, dst, aux)
            dst += src.remove(src.length - 1)
            move(n - 1, aux, src, dst)
        }
        move(A.length, A, B, C)
    }

    def main(args: Array[String]): Unit = {
        val A = ArrayBuffer(2, 1, 0)
        val B = ArrayBuffer[Int]()
        val C = ArrayBuffer[Int]()
        hanota(A, B, C)
        println(s"A: ${A.mkString("[", ",", "]")}")
        println(s"B: ${B.mkString("[", ",", "]")}")
        println(s"C: ${C.mkString("[", ",", "]")}")
    }
}
```

<!-- REGISTRY_PATH: lcci_08_06_hanota.languages.typescript -->
### typescript

```typescript
function hanota(A: number[], B: number[], C: number[]): void {
    function move(n: number, src: number[], aux: number[], dst: number[]): void {
        if (n === 0) return;
        move(n - 1, src, dst, aux);
        dst.push(src.pop()!);
        move(n - 1, aux, src, dst);
    }
    move(A.length, A, B, C);
}

const A = [2, 1, 0], B: number[] = [], C: number[] = [];
hanota(A, B, C);
console.log("A:", A);
console.log("B:", B);
console.log("C:", C);
```

## lcci_08_07_permutation_i

<!-- REGISTRY_PATH: lcci_08_07_permutation_i.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> permutation(string S) {
    sort(S.begin(), S.end());
    vector<string> result;
    do {
        result.push_back(S);
    } while (next_permutation(S.begin(), S.end()));
    return result;
}

int main() {
    for (const auto& p : permutation("qwe")) {
        cout << p << endl;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_07_permutation_i.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func permutation(S string) []string {
	chars := []byte(S)
	sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
	result := []string{}
	used := make([]bool, len(chars))
	path := []byte{}

	var backtrack func()
	backtrack = func() {
		if len(path) == len(chars) {
			result = append(result, string(path))
			return
		}
		for i, c := range chars {
			if !used[i] {
				used[i] = true
				path = append(path, c)
				backtrack()
				path = path[:len(path)-1]
				used[i] = false
			}
		}
	}

	backtrack()
	return result
}

func main() {
	for _, p := range permutation("qwe") {
		fmt.Println(p)
	}
}
```

<!-- REGISTRY_PATH: lcci_08_07_permutation_i.languages.python -->
### python

```python
from typing import List

def permutation(S: str) -> List[str]:
    result = []
    chars = sorted(S)
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            result.append("".join(path))
            return
        for i, c in enumerate(chars):
            if not used[i]:
                used[i] = True
                path.append(c)
                backtrack(path)
                path.pop()
                used[i] = False

    backtrack([])
    return result

def main():
    for p in permutation("qwe"):
        print(p)

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_07_permutation_i.languages.scala -->
### scala

```scala
object Lcci0807PermutationI {
    def permutation(S: String): Array[String] = {
        val chars = S.toCharArray.sorted
        val result = scala.collection.mutable.ArrayBuffer[String]()
        val used = Array.fill(chars.length)(false)
        val path = scala.collection.mutable.ArrayBuffer[Char]()

        def backtrack(): Unit = {
            if (path.length == chars.length) {
                result += path.mkString
                return
            }
            for (i <- chars.indices) {
                if (!used(i)) {
                    used(i) = true
                    path += chars(i)
                    backtrack()
                    path.remove(path.length - 1)
                    used(i) = false
                }
            }
        }

        backtrack()
        result.toArray
    }

    def main(args: Array[String]): Unit = {
        permutation("qwe").foreach(println)
    }
}
```

<!-- REGISTRY_PATH: lcci_08_07_permutation_i.languages.typescript -->
### typescript

```typescript
function permutation(S: string): string[] {
    const chars = S.split("").sort();
    const result: string[] = [];
    const used = new Array(chars.length).fill(false);
    const path: string[] = [];

    function backtrack(): void {
        if (path.length === chars.length) {
            result.push(path.join(""));
            return;
        }
        for (let i = 0; i < chars.length; i++) {
            if (!used[i]) {
                used[i] = true;
                path.push(chars[i]);
                backtrack();
                path.pop();
                used[i] = false;
            }
        }
    }

    backtrack();
    return result;
}

for (const p of permutation("qwe")) {
    console.log(p);
}
```

## lcci_08_08_permutation_ii

<!-- REGISTRY_PATH: lcci_08_08_permutation_ii.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

vector<string> permutation(string S) {
    sort(S.begin(), S.end());
    vector<string> result;
    do {
        result.push_back(S);
    } while (next_permutation(S.begin(), S.end()));
    return result;
}

int main() {
    for (const auto& p : permutation("qqe")) {
        cout << p << endl;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_08_permutation_ii.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func permutation(S string) []string {
	chars := []byte(S)
	sort.Slice(chars, func(i, j int) bool { return chars[i] < chars[j] })
	result := []string{}
	used := make([]bool, len(chars))
	path := []byte{}

	var backtrack func()
	backtrack = func() {
		if len(path) == len(chars) {
			result = append(result, string(path))
			return
		}
		for i, c := range chars {
			if used[i] {
				continue
			}
			if i > 0 && chars[i] == chars[i-1] && !used[i-1] {
				continue
			}
			used[i] = true
			path = append(path, c)
			backtrack()
			path = path[:len(path)-1]
			used[i] = false
		}
	}

	backtrack()
	return result
}

func main() {
	for _, p := range permutation("qqe") {
		fmt.Println(p)
	}
}
```

<!-- REGISTRY_PATH: lcci_08_08_permutation_ii.languages.python -->
### python

```python
from typing import List

def permutation(S: str) -> List[str]:
    result = []
    chars = sorted(S)
    used = [False] * len(chars)

    def backtrack(path):
        if len(path) == len(chars):
            result.append("".join(path))
            return
        for i, c in enumerate(chars):
            if used[i]:
                continue
            # Skip duplicate: if chars[i] == chars[i-1] and chars[i-1] was not used in this branch
            if i > 0 and chars[i] == chars[i - 1] and not used[i - 1]:
                continue
            used[i] = True
            path.append(c)
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result

def main():
    for p in permutation("qqe"):
        print(p)

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_08_permutation_ii.languages.scala -->
### scala

```scala
object Lcci0808PermutationIi {
    def permutation(S: String): Array[String] = {
        val chars = S.toCharArray.sorted
        val result = scala.collection.mutable.ArrayBuffer[String]()
        val used = Array.fill(chars.length)(false)
        val path = scala.collection.mutable.ArrayBuffer[Char]()

        def backtrack(): Unit = {
            if (path.length == chars.length) {
                result += path.mkString
                return
            }
            for (i <- chars.indices) {
                if (!used(i)) {
                    if (i > 0 && chars(i) == chars(i - 1) && !used(i - 1)) ()
                    else {
                        used(i) = true
                        path += chars(i)
                        backtrack()
                        path.remove(path.length - 1)
                        used(i) = false
                    }
                }
            }
        }

        backtrack()
        result.toArray
    }

    def main(args: Array[String]): Unit = {
        permutation("qqe").foreach(println)
    }
}
```

<!-- REGISTRY_PATH: lcci_08_08_permutation_ii.languages.typescript -->
### typescript

```typescript
function permutation(S: string): string[] {
    const chars = S.split("").sort();
    const result: string[] = [];
    const used = new Array(chars.length).fill(false);
    const path: string[] = [];

    function backtrack(): void {
        if (path.length === chars.length) {
            result.push(path.join(""));
            return;
        }
        for (let i = 0; i < chars.length; i++) {
            if (used[i]) continue;
            if (i > 0 && chars[i] === chars[i - 1] && !used[i - 1]) continue;
            used[i] = true;
            path.push(chars[i]);
            backtrack();
            path.pop();
            used[i] = false;
        }
    }

    backtrack();
    return result;
}

for (const p of permutation("qqe")) {
    console.log(p);
}
```

## lcci_08_09_bracket

<!-- REGISTRY_PATH: lcci_08_09_bracket.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <functional>
using namespace std;

vector<string> generateParenthesis(int n) {
    vector<string> result;
    function<void(string, int, int)> bt = [&](string cur, int open, int close) {
        if ((int)cur.size() == 2 * n) { result.push_back(cur); return; }
        if (open < n) bt(cur + "(", open + 1, close);
        if (close < open) bt(cur + ")", open, close + 1);
    };
    bt("", 0, 0);
    return result;
}

int main() {
    for (const auto& s : generateParenthesis(3)) {
        cout << s << endl;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_09_bracket.languages.go -->
### go

```go
package main

import "fmt"

func generateParenthesis(n int) []string {
	result := []string{}

	var bt func(cur string, open, close int)
	bt = func(cur string, open, close int) {
		if len(cur) == 2*n {
			result = append(result, cur)
			return
		}
		if open < n {
			bt(cur+"(", open+1, close)
		}
		if close < open {
			bt(cur+")", open, close+1)
		}
	}

	bt("", 0, 0)
	return result
}

func main() {
	for _, s := range generateParenthesis(3) {
		fmt.Println(s)
	}
}
```

<!-- REGISTRY_PATH: lcci_08_09_bracket.languages.python -->
### python

```python
from typing import List

def generateParenthesis(n: int) -> List[str]:
    result = []

    def bt(cur, open_count, close_count):
        if len(cur) == 2 * n:
            result.append(cur)
            return
        if open_count < n:
            bt(cur + "(", open_count + 1, close_count)
        if close_count < open_count:
            bt(cur + ")", open_count, close_count + 1)

    bt("", 0, 0)
    return result

def main():
    for s in generateParenthesis(3):
        print(s)

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_09_bracket.languages.scala -->
### scala

```scala
object Lcci0809Bracket {
    def generateParenthesis(n: Int): Array[String] = {
        val result = scala.collection.mutable.ArrayBuffer[String]()

        def bt(cur: String, open: Int, close: Int): Unit = {
            if (cur.length == 2 * n) { result += cur; return }
            if (open < n) bt(cur + "(", open + 1, close)
            if (close < open) bt(cur + ")", open, close + 1)
        }

        bt("", 0, 0)
        result.toArray
    }

    def main(args: Array[String]): Unit = {
        generateParenthesis(3).foreach(println)
    }
}
```

<!-- REGISTRY_PATH: lcci_08_09_bracket.languages.typescript -->
### typescript

```typescript
function generateParenthesis(n: number): string[] {
    const result: string[] = [];

    function bt(cur: string, open: number, close: number): void {
        if (cur.length === 2 * n) { result.push(cur); return; }
        if (open < n) bt(cur + "(", open + 1, close);
        if (close < open) bt(cur + ")", open, close + 1);
    }

    bt("", 0, 0);
    return result;
}

for (const s of generateParenthesis(3)) {
    console.log(s);
}
```

## lcci_08_10_color_fill

<!-- REGISTRY_PATH: lcci_08_10_color_fill.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <functional>
using namespace std;

vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int newColor) {
    int old = image[sr][sc];
    if (old == newColor) return image;
    int r = image.size(), c = image[0].size();
    function<void(int, int)> dfs = [&](int i, int j) {
        if (i < 0 || i >= r || j < 0 || j >= c || image[i][j] != old) return;
        image[i][j] = newColor;
        dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1);
    };
    dfs(sr, sc);
    return image;
}

int main() {
    vector<vector<int>> image = {{1,1,1},{1,1,0},{1,0,1}};
    auto result = floodFill(image, 1, 1, 2);
    for (auto& row : result) {
        for (int i = 0; i < (int)row.size(); i++) {
            cout << row[i] << (i + 1 < (int)row.size() ? " " : "\n");
        }
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_10_color_fill.languages.go -->
### go

```go
package main

import "fmt"

func floodFill(image [][]int, sr int, sc int, newColor int) [][]int {
	old := image[sr][sc]
	if old == newColor {
		return image
	}
	r, c := len(image), len(image[0])

	var dfs func(i, j int)
	dfs = func(i, j int) {
		if i < 0 || i >= r || j < 0 || j >= c || image[i][j] != old {
			return
		}
		image[i][j] = newColor
		dfs(i+1, j)
		dfs(i-1, j)
		dfs(i, j+1)
		dfs(i, j-1)
	}

	dfs(sr, sc)
	return image
}

func main() {
	image := [][]int{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}
	result := floodFill(image, 1, 1, 2)
	for _, row := range result {
		fmt.Println(row)
	}
}
```

<!-- REGISTRY_PATH: lcci_08_10_color_fill.languages.python -->
### python

```python
from typing import List

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    old = image[sr][sc]
    if old == newColor:
        return image
    r, c = len(image), len(image[0])

    def dfs(i, j):
        if i < 0 or i >= r or j < 0 or j >= c or image[i][j] != old:
            return
        image[i][j] = newColor
        dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1)

    dfs(sr, sc)
    return image

def main():
    result = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2)
    for row in result:
        print(row)

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_10_color_fill.languages.scala -->
### scala

```scala
object Lcci0810ColorFill {
    def floodFill(image: Array[Array[Int]], sr: Int, sc: Int, newColor: Int): Array[Array[Int]] = {
        val old = image(sr)(sc)
        if (old == newColor) return image
        val r = image.length; val c = image(0).length

        def dfs(i: Int, j: Int): Unit = {
            if (i < 0 || i >= r || j < 0 || j >= c || image(i)(j) != old) return
            image(i)(j) = newColor
            dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1)
        }

        dfs(sr, sc)
        image
    }

    def main(args: Array[String]): Unit = {
        val image = Array(Array(1,1,1), Array(1,1,0), Array(1,0,1))
        val result = floodFill(image, 1, 1, 2)
        result.foreach(row => println(row.mkString("[", ",", "]")))
    }
}
```

<!-- REGISTRY_PATH: lcci_08_10_color_fill.languages.typescript -->
### typescript

```typescript
function floodFill(image: number[][], sr: number, sc: number, newColor: number): number[][] {
    const old = image[sr][sc];
    if (old === newColor) return image;
    const r = image.length, c = image[0].length;

    function dfs(i: number, j: number): void {
        if (i < 0 || i >= r || j < 0 || j >= c || image[i][j] !== old) return;
        image[i][j] = newColor;
        dfs(i + 1, j); dfs(i - 1, j); dfs(i, j + 1); dfs(i, j - 1);
    }

    dfs(sr, sc);
    return image;
}

const result = floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2);
for (const row of result) {
    console.log(row);
}
```

## lcci_08_11_coin

<!-- REGISTRY_PATH: lcci_08_11_coin.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

int waysToChange(int n) {
    const int MOD = 1e9 + 7;
    int coins[] = {1, 5, 10, 25};
    vector<long long> dp(n + 1, 0);
    dp[0] = 1;
    for (int coin : coins) {
        for (int i = coin; i <= n; i++) {
            dp[i] = (dp[i] + dp[i - coin]) % MOD;
        }
    }
    return (int)dp[n];
}

int main() {
    cout << waysToChange(5)  << endl; // 2
    cout << waysToChange(10) << endl; // 4
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_11_coin.languages.go -->
### go

```go
package main

import "fmt"

func waysToChange(n int) int {
	const MOD = 1000000007
	coins := []int{1, 5, 10, 25}
	dp := make([]int, n+1)
	dp[0] = 1
	for _, coin := range coins {
		for i := coin; i <= n; i++ {
			dp[i] = (dp[i] + dp[i-coin]) % MOD
		}
	}
	return dp[n]
}

func main() {
	fmt.Println(waysToChange(5))  // 2
	fmt.Println(waysToChange(10)) // 4
}
```

<!-- REGISTRY_PATH: lcci_08_11_coin.languages.python -->
### python

```python
def waysToChange(n: int) -> int:
    MOD = 10**9 + 7
    coins = [1, 5, 10, 25]
    dp = [0] * (n + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = (dp[i] + dp[i - coin]) % MOD
    return dp[n]

def main():
    print(waysToChange(5))   # 2
    print(waysToChange(10))  # 4

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_11_coin.languages.scala -->
### scala

```scala
object Lcci0811Coin {
    def waysToChange(n: Int): Int = {
        val MOD = 1000000007L
        val coins = Array(1, 5, 10, 25)
        val dp = Array.fill(n + 1)(0L)
        dp(0) = 1L
        for (coin <- coins) {
            for (i <- coin to n) {
                dp(i) = (dp(i) + dp(i - coin)) % MOD
            }
        }
        dp(n).toInt
    }

    def main(args: Array[String]): Unit = {
        println(waysToChange(5))   // 2
        println(waysToChange(10))  // 4
    }
}
```

<!-- REGISTRY_PATH: lcci_08_11_coin.languages.typescript -->
### typescript

```typescript
function waysToChange(n: number): number {
    const MOD = 1000000007n;
    const coins = [1, 5, 10, 25];
    const dp = new Array(n + 1).fill(0n);
    dp[0] = 1n;
    for (const coin of coins) {
        for (let i = coin; i <= n; i++) {
            dp[i] = (dp[i] + dp[i - coin]) % MOD;
        }
    }
    return Number(dp[n]);
}

console.log(waysToChange(5));   // 2
console.log(waysToChange(10));  // 4
```

## lcci_08_12_eight_queens

<!-- REGISTRY_PATH: lcci_08_12_eight_queens.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <functional>
using namespace std;

vector<vector<string>> solveNQueens(int n) {
    vector<vector<string>> result;
    set<int> usedCols, diag1, diag2;

    function<void(int, vector<string>&)> bt = [&](int row, vector<string>& board) {
        if (row == n) { result.push_back(board); return; }
        for (int col = 0; col < n; col++) {
            if (usedCols.count(col) || diag1.count(row - col) || diag2.count(row + col)) continue;
            board[row][col] = 'Q';
            usedCols.insert(col); diag1.insert(row - col); diag2.insert(row + col);
            bt(row + 1, board);
            board[row][col] = '.';
            usedCols.erase(col); diag1.erase(row - col); diag2.erase(row + col);
        }
    };

    vector<string> board(n, string(n, '.'));
    bt(0, board);
    return result;
}

int main() {
    auto result = solveNQueens(4);
    cout << result.size() << " solutions" << endl;
    for (auto& board : result) {
        for (auto& row : board) cout << row << endl;
        cout << endl;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_12_eight_queens.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

func solveNQueens(n int) [][]string {
	result := [][]string{}
	usedCols := map[int]bool{}
	diag1 := map[int]bool{}
	diag2 := map[int]bool{}
	board := make([][]byte, n)
	for i := range board {
		board[i] = []byte(strings.Repeat(".", n))
	}

	var bt func(row int)
	bt = func(row int) {
		if row == n {
			snapshot := make([]string, n)
			for i, r := range board {
				snapshot[i] = string(r)
			}
			result = append(result, snapshot)
			return
		}
		for col := 0; col < n; col++ {
			if usedCols[col] || diag1[row-col] || diag2[row+col] {
				continue
			}
			board[row][col] = 'Q'
			usedCols[col] = true
			diag1[row-col] = true
			diag2[row+col] = true
			bt(row + 1)
			board[row][col] = '.'
			delete(usedCols, col)
			delete(diag1, row-col)
			delete(diag2, row+col)
		}
	}

	bt(0)
	return result
}

func main() {
	result := solveNQueens(4)
	fmt.Printf("%d solutions\n", len(result))
	for _, board := range result {
		for _, row := range board {
			fmt.Println(row)
		}
		fmt.Println()
	}
}
```

<!-- REGISTRY_PATH: lcci_08_12_eight_queens.languages.python -->
### python

```python
from typing import List

def solveNQueens(n: int) -> List[List[str]]:
    result = []
    used_cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def bt(row, board):
        if row == n:
            result.append(["".join(r) for r in board])
            return
        for col in range(n):
            if col in used_cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            board[row][col] = 'Q'
            used_cols.add(col); diag1.add(row - col); diag2.add(row + col)
            bt(row + 1, board)
            board[row][col] = '.'
            used_cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)

    board = [['.' for _ in range(n)] for _ in range(n)]
    bt(0, board)
    return result

def main():
    result = solveNQueens(4)
    print(f"{len(result)} solutions")
    for board in result:
        for row in board:
            print(row)
        print()

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_12_eight_queens.languages.scala -->
### scala

```scala
object Lcci0812EightQueens {
    def solveNQueens(n: Int): Array[Array[String]] = {
        val result = scala.collection.mutable.ArrayBuffer[Array[String]]()
        val usedCols = scala.collection.mutable.Set[Int]()
        val diag1 = scala.collection.mutable.Set[Int]()
        val diag2 = scala.collection.mutable.Set[Int]()
        val board = Array.fill(n)(Array.fill(n)('.'))

        def bt(row: Int): Unit = {
            if (row == n) {
                result += board.map(_.mkString)
                return
            }
            for (col <- 0 until n) {
                if (!usedCols(col) && !diag1(row - col) && !diag2(row + col)) {
                    board(row)(col) = 'Q'
                    usedCols += col; diag1 += (row - col); diag2 += (row + col)
                    bt(row + 1)
                    board(row)(col) = '.'
                    usedCols -= col; diag1 -= (row - col); diag2 -= (row + col)
                }
            }
        }

        bt(0)
        result.toArray
    }

    def main(args: Array[String]): Unit = {
        val result = solveNQueens(4)
        println(s"${result.length} solutions")
        for (board <- result) {
            board.foreach(println)
            println()
        }
    }
}
```

<!-- REGISTRY_PATH: lcci_08_12_eight_queens.languages.typescript -->
### typescript

```typescript
function solveNQueens(n: number): string[][] {
    const result: string[][] = [];
    const usedCols = new Set<number>();
    const diag1 = new Set<number>();
    const diag2 = new Set<number>();
    const board: string[][] = Array.from({ length: n }, () => Array(n).fill("."));

    function bt(row: number): void {
        if (row === n) {
            result.push(board.map(r => r.join("")));
            return;
        }
        for (let col = 0; col < n; col++) {
            if (usedCols.has(col) || diag1.has(row - col) || diag2.has(row + col)) continue;
            board[row][col] = "Q";
            usedCols.add(col); diag1.add(row - col); diag2.add(row + col);
            bt(row + 1);
            board[row][col] = ".";
            usedCols.delete(col); diag1.delete(row - col); diag2.delete(row + col);
        }
    }

    bt(0);
    return result;
}

const result = solveNQueens(4);
console.log(`${result.length} solutions`);
for (const board of result) {
    for (const row of board) console.log(row);
    console.log();
}
```

## lcci_08_13_pile_box

<!-- REGISTRY_PATH: lcci_08_13_pile_box.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int pileBox(vector<vector<int>>& box) {
    // Sort by width descending, then depth descending
    sort(box.begin(), box.end(), [](const vector<int>& a, const vector<int>& b) {
        return a[0] != b[0] ? a[0] > b[0] : a[1] > b[1];
    });
    int n = box.size();
    // dp[i] = max height with box[i] on top
    vector<int> dp(n);
    for (int i = 0; i < n; i++) dp[i] = box[i][2];
    int ans = *max_element(dp.begin(), dp.end());
    for (int i = 1; i < n; i++) {
        for (int j = 0; j < i; j++) {
            if (box[j][0] > box[i][0] && box[j][1] > box[i][1] && box[j][2] > box[i][2]) {
                dp[i] = max(dp[i], dp[j] + box[i][2]);
            }
        }
        ans = max(ans, dp[i]);
    }
    return ans;
}

int main() {
    vector<vector<int>> box = {{2,2,2},{3,3,3},{4,4,4}};
    cout << pileBox(box) << endl; // 9
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_13_pile_box.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func pileBox(box [][]int) int {
	sort.Slice(box, func(i, j int) bool {
		if box[i][0] != box[j][0] {
			return box[i][0] > box[j][0]
		}
		return box[i][1] > box[j][1]
	})
	n := len(box)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = box[i][2]
	}
	ans := dp[0]
	for i := 1; i < n; i++ {
		for j := 0; j < i; j++ {
			if box[j][0] > box[i][0] && box[j][1] > box[i][1] && box[j][2] > box[i][2] {
				if dp[j]+box[i][2] > dp[i] {
					dp[i] = dp[j] + box[i][2]
				}
			}
		}
		if dp[i] > ans {
			ans = dp[i]
		}
	}
	return ans
}

func main() {
	fmt.Println(pileBox([][]int{{2, 2, 2}, {3, 3, 3}, {4, 4, 4}})) // 9
}
```

<!-- REGISTRY_PATH: lcci_08_13_pile_box.languages.python -->
### python

```python
from typing import List

def pileBox(box: List[List[int]]) -> int:
    box.sort(key=lambda b: (-b[0], -b[1]))
    n = len(box)
    dp = [b[2] for b in box]
    ans = max(dp)
    for i in range(1, n):
        for j in range(i):
            if box[j][0] > box[i][0] and box[j][1] > box[i][1] and box[j][2] > box[i][2]:
                dp[i] = max(dp[i], dp[j] + box[i][2])
        ans = max(ans, dp[i])
    return ans

def main():
    print(pileBox([[2,2,2],[3,3,3],[4,4,4]]))  # 9

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_13_pile_box.languages.scala -->
### scala

```scala
object Lcci0813PileBox {
    def pileBox(box: Array[Array[Int]]): Int = {
        val sorted = box.sortWith((a, b) => if (a(0) != b(0)) a(0) > b(0) else a(1) > b(1))
        val n = sorted.length
        val dp = sorted.map(_(2))
        var ans = dp.max
        for (i <- 1 until n) {
            for (j <- 0 until i) {
                if (sorted(j)(0) > sorted(i)(0) && sorted(j)(1) > sorted(i)(1) && sorted(j)(2) > sorted(i)(2)) {
                    if (dp(j) + sorted(i)(2) > dp(i)) dp(i) = dp(j) + sorted(i)(2)
                }
            }
            if (dp(i) > ans) ans = dp(i)
        }
        ans
    }

    def main(args: Array[String]): Unit = {
        println(pileBox(Array(Array(2,2,2), Array(3,3,3), Array(4,4,4)))) // 9
    }
}
```

<!-- REGISTRY_PATH: lcci_08_13_pile_box.languages.typescript -->
### typescript

```typescript
function pileBox(box: number[][]): number {
    box.sort((a, b) => a[0] !== b[0] ? b[0] - a[0] : b[1] - a[1]);
    const n = box.length;
    const dp = box.map(b => b[2]);
    let ans = Math.max(...dp);
    for (let i = 1; i < n; i++) {
        for (let j = 0; j < i; j++) {
            if (box[j][0] > box[i][0] && box[j][1] > box[i][1] && box[j][2] > box[i][2]) {
                dp[i] = Math.max(dp[i], dp[j] + box[i][2]);
            }
        }
        ans = Math.max(ans, dp[i]);
    }
    return ans;
}

console.log(pileBox([[2,2,2],[3,3,3],[4,4,4]])); // 9
```

## lcci_08_14_boolean_evaluation

<!-- REGISTRY_PATH: lcci_08_14_boolean_evaluation.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

const int MOD = 1e9 + 7;

int countEval(string s, int result) {
    int n = s.size();
    // dp[i][j][v] = ways to evaluate s[i..j] to v (0 or 1)
    // s has digits at even indices, operators at odd indices
    int len = (n + 1) / 2; // number of operands
    vector<vector<array<long long,2>>> dp(n, vector<array<long long,2>>(n, {0,0}));
    for (int i = 0; i < n; i += 2) {
        dp[i][i][s[i] - '0'] = 1;
    }
    for (int size = 3; size <= n; size += 2) {
        for (int i = 0; i <= n - size; i += 2) {
            int j = i + size - 1;
            for (int k = i + 1; k < j; k += 2) {
                char op = s[k];
                long long lf = dp[i][k-1][0], lt = dp[i][k-1][1];
                long long rf = dp[k+1][j][0], rt = dp[k+1][j][1];
                if (op == '&') {
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % MOD;
                } else if (op == '|') {
                    dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf * rf) % MOD;
                } else { // '^'
                    dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % MOD;
                }
            }
        }
    }
    return (int)dp[0][n-1][result];
}

int main() {
    cout << countEval("1^0|0|1", 0) << endl; // 2
    cout << countEval("0&0&0&1^1|0", 1) << endl; // 10
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_08_14_boolean_evaluation.languages.go -->
### go

```go
package main

import "fmt"

const modBE = 1_000_000_007

func countEval(s string, result int) int {
	n := len(s)
	// dp[i][j][v] = ways substring s[i..j] evaluates to v
	dp := make([][][2]int64, n)
	for i := range dp {
		dp[i] = make([][2]int64, n)
	}
	for i := 0; i < n; i += 2 {
		dp[i][i][s[i]-'0'] = 1
	}
	for size := 3; size <= n; size += 2 {
		for i := 0; i <= n-size; i += 2 {
			j := i + size - 1
			for k := i + 1; k < j; k += 2 {
				op := s[k]
				lf, lt := dp[i][k-1][0], dp[i][k-1][1]
				rf, rt := dp[k+1][j][0], dp[k+1][j][1]
				switch op {
				case '&':
					dp[i][j][1] = (dp[i][j][1] + lt*rt) % modBE
					dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % modBE
				case '|':
					dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % modBE
					dp[i][j][0] = (dp[i][j][0] + lf*rf) % modBE
				case '^':
					dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % modBE
					dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % modBE
				}
			}
		}
	}
	return int(dp[0][n-1][result])
}

func main() {
	fmt.Println(countEval("1^0|0|1", 0))     // 2
	fmt.Println(countEval("0&0&0&1^1|0", 1)) // 10
}
```

<!-- REGISTRY_PATH: lcci_08_14_boolean_evaluation.languages.python -->
### python

```python
MOD = 10**9 + 7

def countEval(s: str, result: int) -> int:
    n = len(s)
    # dp[i][j] = [ways_false, ways_true] for s[i..j]
    dp = [[[0, 0] for _ in range(n)] for _ in range(n)]
    for i in range(0, n, 2):
        dp[i][i][int(s[i])] = 1
    for size in range(3, n + 1, 2):
        for i in range(0, n - size + 1, 2):
            j = i + size - 1
            for k in range(i + 1, j, 2):
                op = s[k]
                lf, lt = dp[i][k-1]
                rf, rt = dp[k+1][j]
                if op == '&':
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % MOD
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % MOD
                elif op == '|':
                    dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % MOD
                    dp[i][j][0] = (dp[i][j][0] + lf * rf) % MOD
                else:  # '^'
                    dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % MOD
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % MOD
    return dp[0][n-1][result]

def main():
    print(countEval("1^0|0|1", 0))       # 2
    print(countEval("0&0&0&1^1|0", 1))   # 10

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_08_14_boolean_evaluation.languages.scala -->
### scala

```scala
object Lcci0814BooleanEvaluation {
    val MOD = 1000000007L

    def countEval(s: String, result: Int): Int = {
        val n = s.length
        // dp(i)(j)(v) = ways s[i..j] evaluates to v
        val dp = Array.ofDim[Long](n, n, 2)
        for (i <- 0 until n by 2) dp(i)(i)(s(i) - '0') = 1L
        var size = 3
        while (size <= n) {
            var i = 0
            while (i <= n - size) {
                val j = i + size - 1
                var k = i + 1
                while (k < j) {
                    val op = s(k)
                    val lf = dp(i)(k-1)(0); val lt = dp(i)(k-1)(1)
                    val rf = dp(k+1)(j)(0); val rt = dp(k+1)(j)(1)
                    op match {
                        case '&' =>
                            dp(i)(j)(1) = (dp(i)(j)(1) + lt * rt) % MOD
                            dp(i)(j)(0) = (dp(i)(j)(0) + lf*rf + lf*rt + lt*rf) % MOD
                        case '|' =>
                            dp(i)(j)(1) = (dp(i)(j)(1) + lt*rt + lf*rt + lt*rf) % MOD
                            dp(i)(j)(0) = (dp(i)(j)(0) + lf*rf) % MOD
                        case '^' =>
                            dp(i)(j)(1) = (dp(i)(j)(1) + lf*rt + lt*rf) % MOD
                            dp(i)(j)(0) = (dp(i)(j)(0) + lf*rf + lt*rt) % MOD
                    }
                    k += 2
                }
                i += 2
            }
            size += 2
        }
        dp(0)(n-1)(result).toInt
    }

    def main(args: Array[String]): Unit = {
        println(countEval("1^0|0|1", 0))      // 2
        println(countEval("0&0&0&1^1|0", 1))  // 10
    }
}
```

<!-- REGISTRY_PATH: lcci_08_14_boolean_evaluation.languages.typescript -->
### typescript

```typescript
const MOD = BigInt(1_000_000_007);

function countEval(s: string, result: number): number {
    const n = s.length;
    // dp[i][j] = [ways_false, ways_true]
    const dp: [bigint, bigint][][] = Array.from({length: n}, () =>
        Array.from({length: n}, () => [0n, 0n] as [bigint, bigint])
    );
    for (let i = 0; i < n; i += 2) {
        dp[i][i][s[i] === '1' ? 1 : 0] = 1n;
    }
    for (let size = 3; size <= n; size += 2) {
        for (let i = 0; i <= n - size; i += 2) {
            const j = i + size - 1;
            for (let k = i + 1; k < j; k += 2) {
                const op = s[k];
                const lf = dp[i][k-1][0], lt = dp[i][k-1][1];
                const rf = dp[k+1][j][0], rt = dp[k+1][j][1];
                if (op === '&') {
                    dp[i][j][1] = (dp[i][j][1] + lt * rt) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lf*rt + lt*rf) % MOD;
                } else if (op === '|') {
                    dp[i][j][1] = (dp[i][j][1] + lt*rt + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf) % MOD;
                } else { // '^'
                    dp[i][j][1] = (dp[i][j][1] + lf*rt + lt*rf) % MOD;
                    dp[i][j][0] = (dp[i][j][0] + lf*rf + lt*rt) % MOD;
                }
            }
        }
    }
    return Number(dp[0][n-1][result]);
}

console.log(countEval("1^0|0|1", 0));      // 2
console.log(countEval("0&0&0&1^1|0", 1));  // 10
```

## lcci_10_01_sorted_merge

<!-- REGISTRY_PATH: lcci_10_01_sorted_merge.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

void merge(vector<int>& a, int m, const vector<int>& b, int n) {
    int i = m - 1;
    int j = n - 1;
    int k = m + n - 1;
    while (j >= 0) {
        if (i >= 0 && a[i] > b[j]) {
            a[k--] = a[i--];
        } else {
            a[k--] = b[j--];
        }
    }
}

int main() {
    vector<int> a = {1, 2, 3, 0, 0, 0};
    vector<int> b = {2, 5, 6};
    merge(a, 3, b, 3);
    cout << "[";
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        if (i) cout << ", ";
        cout << a[i];
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_01_sorted_merge.languages.go -->
### go

```go
package main

import "fmt"

func merge(a []int, m int, b []int, n int) {
	i, j, k := m-1, n-1, m+n-1
	for j >= 0 {
		if i >= 0 && a[i] > b[j] {
			a[k] = a[i]
			i--
		} else {
			a[k] = b[j]
			j--
		}
		k--
	}
}

func main() {
	a := []int{1, 2, 3, 0, 0, 0}
	merge(a, 3, []int{2, 5, 6}, 3)
	fmt.Println(a)
}
```

<!-- REGISTRY_PATH: lcci_10_01_sorted_merge.languages.python -->
### python

```python
from typing import List


def merge(a: List[int], m: int, b: List[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    while j >= 0:
        if i >= 0 and a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1


def main() -> None:
    a = [1, 2, 3, 0, 0, 0]
    merge(a, 3, [2, 5, 6], 3)
    print(a)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_01_sorted_merge.languages.scala -->
### scala

```scala
object Lcci1001SortedMerge {
    def merge(a: Array[Int], m: Int, b: Array[Int], n: Int): Unit = {
        var i = m - 1
        var j = n - 1
        var k = m + n - 1
        while (j >= 0) {
            if (i >= 0 && a(i) > b(j)) {
                a(k) = a(i)
                i -= 1
            } else {
                a(k) = b(j)
                j -= 1
            }
            k -= 1
        }
    }

    def main(args: Array[String]): Unit = {
        val a = Array(1, 2, 3, 0, 0, 0)
        merge(a, 3, Array(2, 5, 6), 3)
        println(a.mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_01_sorted_merge.languages.typescript -->
### typescript

```typescript
function merge(a: number[], m: number, b: number[], n: number): void {
    let i = m - 1;
    let j = n - 1;
    let k = m + n - 1;
    while (j >= 0) {
        if (i >= 0 && a[i] > b[j]) {
            a[k--] = a[i--];
        } else {
            a[k--] = b[j--];
        }
    }
}

const mergedValues = [1, 2, 3, 0, 0, 0];
merge(mergedValues, 3, [2, 5, 6], 3);
console.log(mergedValues);
```

## lcci_10_02_group_anagrams

<!-- REGISTRY_PATH: lcci_10_02_group_anagrams.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

vector<vector<string>> groupAnagrams(const vector<string>& strs) {
    unordered_map<string, vector<string>> groups;
    for (const string& s : strs) {
        string key = s;
        sort(key.begin(), key.end());
        groups[key].push_back(s);
    }

    vector<vector<string>> result;
    for (auto& entry : groups) {
        sort(entry.second.begin(), entry.second.end());
        result.push_back(entry.second);
    }
    sort(result.begin(), result.end(), [](const vector<string>& a, const vector<string>& b) {
        return a[0] < b[0];
    });
    return result;
}

int main() {
    vector<vector<string>> groups = groupAnagrams({"eat", "tea", "tan", "ate", "nat", "bat"});
    cout << "[";
    for (int i = 0; i < static_cast<int>(groups.size()); ++i) {
        if (i) cout << ", ";
        cout << "[";
        for (int j = 0; j < static_cast<int>(groups[i].size()); ++j) {
            if (j) cout << ", ";
            cout << groups[i][j];
        }
        cout << "]";
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_02_group_anagrams.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
	"strings"
)

func groupAnagrams(strs []string) [][]string {
	groups := map[string][]string{}
	for _, word := range strs {
		chars := strings.Split(word, "")
		sort.Strings(chars)
		key := strings.Join(chars, "")
		groups[key] = append(groups[key], word)
	}

	result := make([][]string, 0, len(groups))
	for _, group := range groups {
		sort.Strings(group)
		result = append(result, group)
	}
	sort.Slice(result, func(i, j int) bool {
		return result[i][0] < result[j][0]
	})
	return result
}

func main() {
	fmt.Println(groupAnagrams([]string{"eat", "tea", "tan", "ate", "nat", "bat"}))
}
```

<!-- REGISTRY_PATH: lcci_10_02_group_anagrams.languages.python -->
### python

```python
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups: dict[str, List[str]] = defaultdict(list)
    for word in strs:
        groups["".join(sorted(word))].append(word)
    result = [sorted(group) for group in groups.values()]
    result.sort(key=lambda group: group[0])
    return result


def main() -> None:
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_02_group_anagrams.languages.scala -->
### scala

```scala
object Lcci1002GroupAnagrams {
    def groupAnagrams(strs: Array[String]): Array[Array[String]] = {
        val groups = strs.groupBy(word => word.sorted).values.map(_.sorted).toArray
        groups.sortBy(_(0))
    }

    def main(args: Array[String]): Unit = {
        val result = groupAnagrams(Array("eat", "tea", "tan", "ate", "nat", "bat"))
        println(result.map(_.mkString("[", ", ", "]")).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_02_group_anagrams.languages.typescript -->
### typescript

```typescript
function groupAnagrams(strs: string[]): string[][] {
    const groups = new Map<string, string[]>();
    for (const word of strs) {
        const key = [...word].sort().join("");
        const group = groups.get(key) ?? [];
        group.push(word);
        groups.set(key, group);
    }
    const result = [...groups.values()].map((group) => group.sort());
    result.sort((a, b) => a[0].localeCompare(b[0]));
    return result;
}

console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
```

## lcci_10_03_search_rotate_array

<!-- REGISTRY_PATH: lcci_10_03_search_rotate_array.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

int search(const vector<int>& arr, int target) {
    if (arr.empty()) {
        return -1;
    }
    int left = 0;
    int right = static_cast<int>(arr.size()) - 1;
    while (left < right && arr[left] == arr[right]) {
        --right;
    }
    while (left < right) {
        int mid = (left + right) >> 1;
        if (arr[mid] > arr[right]) {
            if (arr[left] <= target && target <= arr[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        } else if (arr[mid] < arr[right]) {
            if (arr[mid] < target && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        } else {
            --right;
        }
    }
    return arr[left] == target ? left : -1;
}

int main() {
    vector<int> arr = {15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14};
    cout << search(arr, 5) << endl;
    cout << search(arr, 11) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_03_search_rotate_array.languages.go -->
### go

```go
package main

import "fmt"

func search(arr []int, target int) int {
	if len(arr) == 0 {
		return -1
	}
	left, right := 0, len(arr)-1
	for left < right && arr[left] == arr[right] {
		right--
	}
	for left < right {
		mid := (left + right) / 2
		if arr[mid] > arr[right] {
			if arr[left] <= target && target <= arr[mid] {
				right = mid
			} else {
				left = mid + 1
			}
		} else if arr[mid] < arr[right] {
			if arr[mid] < target && target <= arr[right] {
				left = mid + 1
			} else {
				right = mid
			}
		} else {
			right--
		}
	}
	if arr[left] == target {
		return left
	}
	return -1
}

func main() {
	arr := []int{15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14}
	fmt.Println(search(arr, 5))
	fmt.Println(search(arr, 11))
}
```

<!-- REGISTRY_PATH: lcci_10_03_search_rotate_array.languages.python -->
### python

```python
from typing import List


def search(arr: List[int], target: int) -> int:
    if not arr:
        return -1
    left, right = 0, len(arr) - 1
    while left < right and arr[left] == arr[right]:
        right -= 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            if arr[left] <= target <= arr[mid]:
                right = mid
            else:
                left = mid + 1
        elif arr[mid] < arr[right]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid
        else:
            right -= 1
    return left if arr[left] == target else -1


def main() -> None:
    arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    print(search(arr, 5))
    print(search(arr, 11))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_03_search_rotate_array.languages.scala -->
### scala

```scala
object Lcci1003SearchRotateArray {
    def search(arr: Array[Int], target: Int): Int = {
        if (arr.isEmpty) {
            return -1
        }
        var left = 0
        var right = arr.length - 1
        while (left < right && arr(left) == arr(right)) {
            right -= 1
        }
        while (left < right) {
            val mid = (left + right) / 2
            if (arr(mid) > arr(right)) {
                if (arr(left) <= target && target <= arr(mid)) right = mid else left = mid + 1
            } else if (arr(mid) < arr(right)) {
                if (arr(mid) < target && target <= arr(right)) left = mid + 1 else right = mid
            } else {
                right -= 1
            }
        }
        if (arr(left) == target) left else -1
    }

    def main(args: Array[String]): Unit = {
        val arr = Array(15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14)
        println(search(arr, 5))
        println(search(arr, 11))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_03_search_rotate_array.languages.typescript -->
### typescript

```typescript
function search(arr: number[], target: number): number {
    if (arr.length === 0) {
        return -1;
    }
    let left = 0;
    let right = arr.length - 1;
    while (left < right && arr[left] === arr[right]) {
        right -= 1;
    }
    while (left < right) {
        const mid = (left + right) >> 1;
        if (arr[mid] > arr[right]) {
            if (arr[left] <= target && target <= arr[mid]) {
                right = mid;
            } else {
                left = mid + 1;
            }
        } else if (arr[mid] < arr[right]) {
            if (arr[mid] < target && target <= arr[right]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        } else {
            right -= 1;
        }
    }
    return arr[left] === target ? left : -1;
}

const arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14];
console.log(search(arr, 5));
console.log(search(arr, 11));
```

## lcci_10_05_sparse_array_search

<!-- REGISTRY_PATH: lcci_10_05_sparse_array_search.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int findString(const vector<string>& words, const string& target) {
    int left = 0;
    int right = static_cast<int>(words.size()) - 1;
    int answer = -1;

    while (left <= right) {
        int mid = (left + right) >> 1;
        int l = mid;
        int r = mid;
        int actual = -1;
        while (l >= left || r <= right) {
            if (l >= left && !words[l].empty()) {
                actual = l;
                break;
            }
            if (r <= right && !words[r].empty()) {
                actual = r;
                break;
            }
            --l;
            ++r;
        }
        if (actual == -1) {
            break;
        }
        if (words[actual] == target) {
            answer = actual;
            right = actual - 1;
        } else if (words[actual] < target) {
            left = actual + 1;
        } else {
            right = actual - 1;
        }
    }
    return answer;
}

int main() {
    vector<string> words = {"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""};
    cout << findString(words, "ta") << endl;
    cout << findString(words, "ball") << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_05_sparse_array_search.languages.go -->
### go

```go
package main

import "fmt"

func findString(words []string, target string) int {
	left, right := 0, len(words)-1
	answer := -1
	for left <= right {
		mid := (left + right) / 2
		lo, hi := mid, mid
		actual := -1
		for lo >= left || hi <= right {
			if lo >= left && words[lo] != "" {
				actual = lo
				break
			}
			if hi <= right && words[hi] != "" {
				actual = hi
				break
			}
			lo--
			hi++
		}
		if actual == -1 {
			break
		}
		if words[actual] == target {
			answer = actual
			right = actual - 1
		} else if words[actual] < target {
			left = actual + 1
		} else {
			right = actual - 1
		}
	}
	return answer
}

func main() {
	words := []string{"at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""}
	fmt.Println(findString(words, "ta"))
	fmt.Println(findString(words, "ball"))
}
```

<!-- REGISTRY_PATH: lcci_10_05_sparse_array_search.languages.python -->
### python

```python
from typing import List


def find_string(words: List[str], target: str) -> int:
    left, right = 0, len(words) - 1
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        lo = mid
        hi = mid
        actual = -1
        while lo >= left or hi <= right:
            if lo >= left and words[lo]:
                actual = lo
                break
            if hi <= right and words[hi]:
                actual = hi
                break
            lo -= 1
            hi += 1
        if actual == -1:
            break
        if words[actual] == target:
            answer = actual
            right = actual - 1
        elif words[actual] < target:
            left = actual + 1
        else:
            right = actual - 1
    return answer


def main() -> None:
    words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(find_string(words, "ta"))
    print(find_string(words, "ball"))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_05_sparse_array_search.languages.scala -->
### scala

```scala
object Lcci1005SparseArraySearch {
    def findString(words: Array[String], target: String): Int = {
        var left = 0
        var right = words.length - 1
        var answer = -1
        while (left <= right) {
            val mid = (left + right) / 2
            var lo = mid
            var hi = mid
            var actual = -1
            while (actual == -1 && (lo >= left || hi <= right)) {
                if (lo >= left && words(lo).nonEmpty) actual = lo
                else if (hi <= right && words(hi).nonEmpty) actual = hi
                lo -= 1
                hi += 1
            }
            if (actual == -1) {
                return answer
            }
            if (words(actual) == target) {
                answer = actual
                right = actual - 1
            } else if (words(actual) < target) {
                left = actual + 1
            } else {
                right = actual - 1
            }
        }
        answer
    }

    def main(args: Array[String]): Unit = {
        val words = Array("at", "", "", "", "ball", "", "", "car", "", "", "dad", "", "")
        println(findString(words, "ta"))
        println(findString(words, "ball"))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_05_sparse_array_search.languages.typescript -->
### typescript

```typescript
function findString(words: string[], target: string): number {
    let left = 0;
    let right = words.length - 1;
    let answer = -1;
    while (left <= right) {
        const mid = (left + right) >> 1;
        let lo = mid;
        let hi = mid;
        let actual = -1;
        while (lo >= left || hi <= right) {
            if (lo >= left && words[lo] !== "") {
                actual = lo;
                break;
            }
            if (hi <= right && words[hi] !== "") {
                actual = hi;
                break;
            }
            lo -= 1;
            hi += 1;
        }
        if (actual === -1) {
            break;
        }
        if (words[actual] === target) {
            answer = actual;
            right = actual - 1;
        } else if (words[actual] < target) {
            left = actual + 1;
        } else {
            right = actual - 1;
        }
    }
    return answer;
}

const words = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""];
console.log(findString(words, "ta"));
console.log(findString(words, "ball"));
```

## lcci_10_09_sorted_matrix_search

<!-- REGISTRY_PATH: lcci_10_09_sorted_matrix_search.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool searchMatrix(const vector<vector<int>>& matrix, int target) {
    if (matrix.empty() || matrix[0].empty()) {
        return false;
    }
    int row = 0;
    int col = static_cast<int>(matrix[0].size()) - 1;
    while (row < static_cast<int>(matrix.size()) && col >= 0) {
        if (matrix[row][col] == target) {
            return true;
        }
        if (matrix[row][col] > target) {
            --col;
        } else {
            ++row;
        }
    }
    return false;
}

int main() {
    vector<vector<int>> matrix = {
        {1, 4, 7, 11, 15},
        {2, 5, 8, 12, 19},
        {3, 6, 9, 16, 22},
        {10, 13, 14, 17, 24},
        {18, 21, 23, 26, 30}
    };
    cout << boolalpha << searchMatrix(matrix, 5) << endl;
    cout << boolalpha << searchMatrix(matrix, 20) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_09_sorted_matrix_search.languages.go -->
### go

```go
package main

import "fmt"

func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	row, col := 0, len(matrix[0])-1
	for row < len(matrix) && col >= 0 {
		if matrix[row][col] == target {
			return true
		}
		if matrix[row][col] > target {
			col--
		} else {
			row++
		}
	}
	return false
}

func main() {
	matrix := [][]int{
		{1, 4, 7, 11, 15},
		{2, 5, 8, 12, 19},
		{3, 6, 9, 16, 22},
		{10, 13, 14, 17, 24},
		{18, 21, 23, 26, 30},
	}
	fmt.Println(searchMatrix(matrix, 5))
	fmt.Println(searchMatrix(matrix, 20))
}
```

<!-- REGISTRY_PATH: lcci_10_09_sorted_matrix_search.languages.python -->
### python

```python
from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return True
        if matrix[row][col] > target:
            col -= 1
        else:
            row += 1
    return False


def main() -> None:
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    print(search_matrix(matrix, 5))
    print(search_matrix(matrix, 20))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_09_sorted_matrix_search.languages.scala -->
### scala

```scala
object Lcci1009SortedMatrixSearch {
    def searchMatrix(matrix: Array[Array[Int]], target: Int): Boolean = {
        if (matrix.isEmpty || matrix(0).isEmpty) {
            return false
        }
        var row = 0
        var col = matrix(0).length - 1
        while (row < matrix.length && col >= 0) {
            if (matrix(row)(col) == target) return true
            if (matrix(row)(col) > target) col -= 1 else row += 1
        }
        false
    }

    def main(args: Array[String]): Unit = {
        val matrix = Array(
            Array(1, 4, 7, 11, 15),
            Array(2, 5, 8, 12, 19),
            Array(3, 6, 9, 16, 22),
            Array(10, 13, 14, 17, 24),
            Array(18, 21, 23, 26, 30)
        )
        println(searchMatrix(matrix, 5))
        println(searchMatrix(matrix, 20))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_09_sorted_matrix_search.languages.typescript -->
### typescript

```typescript
function searchMatrix(matrix: number[][], target: number): boolean {
    if (matrix.length === 0 || matrix[0].length === 0) {
        return false;
    }
    let row = 0;
    let col = matrix[0].length - 1;
    while (row < matrix.length && col >= 0) {
        if (matrix[row][col] === target) {
            return true;
        }
        if (matrix[row][col] > target) {
            col -= 1;
        } else {
            row += 1;
        }
    }
    return false;
}

const matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30],
];
console.log(searchMatrix(matrix, 5));
console.log(searchMatrix(matrix, 20));
```

## lcci_10_10_rank_from_stream

<!-- REGISTRY_PATH: lcci_10_10_rank_from_stream.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

class BinaryIndexedTree {
public:
    explicit BinaryIndexedTree(int n) : tree(n + 1, 0) {}

    void update(int index, int delta) {
        while (index < static_cast<int>(tree.size())) {
            tree[index] += delta;
            index += index & -index;
        }
    }

    int query(int index) const {
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & -index;
        }
        return sum;
    }

private:
    vector<int> tree;
};

class StreamRank {
public:
    StreamRank() : bit(50010) {}

    void track(int x) {
        bit.update(x + 1, 1);
    }

    int getRankOfNumber(int x) const {
        return bit.query(x + 1);
    }

private:
    BinaryIndexedTree bit;
};

int main() {
    StreamRank streamRank;
    cout << streamRank.getRankOfNumber(1) << endl;
    streamRank.track(0);
    cout << streamRank.getRankOfNumber(0) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_10_rank_from_stream.languages.go -->
### go

```go
package main

import "fmt"

type binaryIndexedTree struct {
	tree []int
}

func newBinaryIndexedTree(n int) *binaryIndexedTree {
	return &binaryIndexedTree{tree: make([]int, n+1)}
}

func (b *binaryIndexedTree) update(index int, delta int) {
	for index < len(b.tree) {
		b.tree[index] += delta
		index += index & -index
	}
}

func (b *binaryIndexedTree) query(index int) int {
	sum := 0
	for index > 0 {
		sum += b.tree[index]
		index -= index & -index
	}
	return sum
}

type StreamRank struct {
	bit *binaryIndexedTree
}

func Constructor() StreamRank {
	return StreamRank{bit: newBinaryIndexedTree(50010)}
}

func (s *StreamRank) Track(x int) {
	s.bit.update(x+1, 1)
}

func (s *StreamRank) GetRankOfNumber(x int) int {
	return s.bit.query(x + 1)
}

func main() {
	streamRank := Constructor()
	fmt.Println(streamRank.GetRankOfNumber(1))
	streamRank.Track(0)
	fmt.Println(streamRank.GetRankOfNumber(0))
}
```

<!-- REGISTRY_PATH: lcci_10_10_rank_from_stream.languages.python -->
### python

```python
class BinaryIndexedTree:
    def __init__(self, n: int) -> None:
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, index: int, delta: int) -> None:
        while index <= self.n:
            self.tree[index] += delta
            index += index & -index

    def query(self, index: int) -> int:
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index
        return total


class StreamRank:
    def __init__(self) -> None:
        self.bit = BinaryIndexedTree(50010)

    def track(self, x: int) -> None:
        self.bit.update(x + 1, 1)

    def get_rank_of_number(self, x: int) -> int:
        return self.bit.query(x + 1)


def main() -> None:
    stream_rank = StreamRank()
    print(stream_rank.get_rank_of_number(1))
    stream_rank.track(0)
    print(stream_rank.get_rank_of_number(0))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_10_rank_from_stream.languages.scala -->
### scala

```scala
object Lcci1010RankFromStream {
    final class BinaryIndexedTree(size: Int) {
        private val tree = Array.fill(size + 1)(0)

        def update(index0: Int, delta: Int): Unit = {
            var index = index0
            while (index < tree.length) {
                tree(index) += delta
                index += index & -index
            }
        }

        def query(index0: Int): Int = {
            var index = index0
            var sum = 0
            while (index > 0) {
                sum += tree(index)
                index -= index & -index
            }
            sum
        }
    }

    final class StreamRank {
        private val bit = new BinaryIndexedTree(50010)

        def track(x: Int): Unit = bit.update(x + 1, 1)

        def getRankOfNumber(x: Int): Int = bit.query(x + 1)
    }

    def main(args: Array[String]): Unit = {
        val streamRank = new StreamRank
        println(streamRank.getRankOfNumber(1))
        streamRank.track(0)
        println(streamRank.getRankOfNumber(0))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_10_rank_from_stream.languages.typescript -->
### typescript

```typescript
class BinaryIndexedTree {
    private readonly tree: number[];

    constructor(size: number) {
        this.tree = new Array(size + 1).fill(0);
    }

    update(index: number, delta: number): void {
        while (index < this.tree.length) {
            this.tree[index] += delta;
            index += index & -index;
        }
    }

    query(index: number): number {
        let sum = 0;
        while (index > 0) {
            sum += this.tree[index];
            index -= index & -index;
        }
        return sum;
    }
}

class StreamRank {
    private readonly bit = new BinaryIndexedTree(50010);

    track(x: number): void {
        this.bit.update(x + 1, 1);
    }

    getRankOfNumber(x: number): number {
        return this.bit.query(x + 1);
    }
}

const streamRank = new StreamRank();
console.log(streamRank.getRankOfNumber(1));
streamRank.track(0);
console.log(streamRank.getRankOfNumber(0));
```

## lcci_10_11_peaks_and_valleys

<!-- REGISTRY_PATH: lcci_10_11_peaks_and_valleys.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

void wiggleSort(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    for (int i = 0; i + 1 < static_cast<int>(nums.size()); i += 2) {
        swap(nums[i], nums[i + 1]);
    }
}

int main() {
    vector<int> nums = {5, 3, 1, 2, 3};
    wiggleSort(nums);
    cout << "[";
    for (int i = 0; i < static_cast<int>(nums.size()); ++i) {
        if (i) cout << ", ";
        cout << nums[i];
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_10_11_peaks_and_valleys.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func wiggleSort(nums []int) {
	sort.Ints(nums)
	for i := 0; i+1 < len(nums); i += 2 {
		nums[i], nums[i+1] = nums[i+1], nums[i]
	}
}

func main() {
	nums := []int{5, 3, 1, 2, 3}
	wiggleSort(nums)
	fmt.Println(nums)
}
```

<!-- REGISTRY_PATH: lcci_10_11_peaks_and_valleys.languages.python -->
### python

```python
from typing import List


def wiggle_sort(nums: List[int]) -> None:
    nums.sort()
    for index in range(0, len(nums) - 1, 2):
        nums[index], nums[index + 1] = nums[index + 1], nums[index]


def main() -> None:
    nums = [5, 3, 1, 2, 3]
    wiggle_sort(nums)
    print(nums)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_10_11_peaks_and_valleys.languages.scala -->
### scala

```scala
object Lcci1011PeaksAndValleys {
    def wiggleSort(nums: Array[Int]): Unit = {
        scala.util.Sorting.quickSort(nums)
        var index = 0
        while (index + 1 < nums.length) {
            val tmp = nums(index)
            nums(index) = nums(index + 1)
            nums(index + 1) = tmp
            index += 2
        }
    }

    def main(args: Array[String]): Unit = {
        val nums = Array(5, 3, 1, 2, 3)
        wiggleSort(nums)
        println(nums.mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_10_11_peaks_and_valleys.languages.typescript -->
### typescript

```typescript
function wiggleSort(nums: number[]): void {
    nums.sort((a, b) => a - b);
    for (let index = 0; index + 1 < nums.length; index += 2) {
        [nums[index], nums[index + 1]] = [nums[index + 1], nums[index]];
    }
}

const demoValues = [5, 3, 1, 2, 3];
wiggleSort(demoValues);
console.log(demoValues);
```

## lcci_16_01_swap_numbers

<!-- REGISTRY_PATH: lcci_16_01_swap_numbers.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> swapNumbers(vector<int> numbers) {
    return {numbers[1], numbers[0]};
}

int main() {
    vector<int> numbers = {1, 2};
    vector<int> ans = swapNumbers(numbers);
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_01_swap_numbers.languages.go -->
### go

```go
package main

import "fmt"

func swapNumbers(numbers []int) []int {
	return []int{numbers[1], numbers[0]}
}

func main() {
	fmt.Println(swapNumbers([]int{1, 2}))
}
```

<!-- REGISTRY_PATH: lcci_16_01_swap_numbers.languages.python -->
### python

```python
from typing import List


def swap_numbers(numbers: List[int]) -> List[int]:
    return [numbers[1], numbers[0]]


def main() -> None:
    print(swap_numbers([1, 2]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_01_swap_numbers.languages.scala -->
### scala

```scala
object Lcci1601SwapNumbers {
    def swapNumbers(numbers: Array[Int]): Array[Int] = Array(numbers(1), numbers(0))

    def main(args: Array[String]): Unit = {
        println(swapNumbers(Array(1, 2)).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_01_swap_numbers.languages.typescript -->
### typescript

```typescript
function swapNumbers(numbers: number[]): number[] {
    return [numbers[1], numbers[0]];
}

console.log(swapNumbers([1, 2]));
```

## lcci_16_02_words_frequency

<!-- REGISTRY_PATH: lcci_16_02_words_frequency.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;

class WordsFrequency {
public:
    explicit WordsFrequency(const vector<string>& book) {
        for (const string& word : book) {
            ++counter[word];
        }
    }

    int get(const string& word) const {
        auto it = counter.find(word);
        return it == counter.end() ? 0 : it->second;
    }

private:
    unordered_map<string, int> counter;
};

int main() {
    vector<string> book = {"i", "have", "an", "apple", "he", "have", "a", "pen"};
    WordsFrequency wf(book);
    cout << wf.get("have") << endl;
    cout << wf.get("you") << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_02_words_frequency.languages.go -->
### go

```go
package main

import "fmt"

type WordsFrequency struct {
	counter map[string]int
}

func Constructor(book []string) WordsFrequency {
	counter := map[string]int{}
	for _, word := range book {
		counter[word]++
	}
	return WordsFrequency{counter: counter}
}

func (w *WordsFrequency) Get(word string) int {
	return w.counter[word]
}

func main() {
	wf := Constructor([]string{"i", "have", "an", "apple", "he", "have", "a", "pen"})
	fmt.Println(wf.Get("have"))
	fmt.Println(wf.Get("you"))
}
```

<!-- REGISTRY_PATH: lcci_16_02_words_frequency.languages.python -->
### python

```python
from collections import Counter
from typing import List


class WordsFrequency:
    def __init__(self, book: List[str]):
        self.counter = Counter(book)

    def get(self, word: str) -> int:
        return self.counter.get(word, 0)


def main() -> None:
    wf = WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"])
    print(wf.get("have"))
    print(wf.get("you"))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_02_words_frequency.languages.scala -->
### scala

```scala
object Lcci1602WordsFrequency {
    final class WordsFrequency(book: Array[String]) {
        private val counter = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
        book.foreach(word => counter(word) = counter(word) + 1)

        def get(word: String): Int = counter(word)
    }

    def main(args: Array[String]): Unit = {
        val wf = new WordsFrequency(Array("i", "have", "an", "apple", "he", "have", "a", "pen"))
        println(wf.get("have"))
        println(wf.get("you"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_02_words_frequency.languages.typescript -->
### typescript

```typescript
class WordsFrequency {
    private readonly counter = new Map<string, number>();

    constructor(book: string[]) {
        for (const word of book) {
            this.counter.set(word, (this.counter.get(word) ?? 0) + 1);
        }
    }

    get(word: string): number {
        return this.counter.get(word) ?? 0;
    }
}

const wf = new WordsFrequency(["i", "have", "an", "apple", "he", "have", "a", "pen"]);
console.log(wf.get("have"));
console.log(wf.get("you"));
```

## lcci_16_03_intersection

<!-- REGISTRY_PATH: lcci_16_03_intersection.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

const double EPS = 1e-9;

bool lessPoint(const vector<double>& a, const vector<double>& b) {
    if (fabs(a[0] - b[0]) > EPS) return a[0] < b[0];
    return a[1] < b[1] - EPS;
}

double cross(const vector<double>& a, const vector<double>& b, const vector<double>& c) {
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
}

bool onSegment(const vector<double>& a, const vector<double>& b, const vector<double>& p) {
    return fabs(cross(a, b, p)) < EPS &&
           min(a[0], b[0]) - EPS <= p[0] && p[0] <= max(a[0], b[0]) + EPS &&
           min(a[1], b[1]) - EPS <= p[1] && p[1] <= max(a[1], b[1]) + EPS;
}

vector<double> intersection(vector<double> start1, vector<double> end1, vector<double> start2, vector<double> end2) {
    if (lessPoint(end1, start1)) swap(start1, end1);
    if (lessPoint(end2, start2)) swap(start2, end2);

    double d1 = cross(start1, end1, start2);
    double d2 = cross(start1, end1, end2);
    double d3 = cross(start2, end2, start1);
    double d4 = cross(start2, end2, end1);

    if (((d1 > EPS && d2 > EPS) || (d1 < -EPS && d2 < -EPS)) ||
        ((d3 > EPS && d4 > EPS) || (d3 < -EPS && d4 < -EPS))) {
        return {};
    }

    double a1 = end1[1] - start1[1];
    double b1 = start1[0] - end1[0];
    double c1 = a1 * start1[0] + b1 * start1[1];

    double a2 = end2[1] - start2[1];
    double b2 = start2[0] - end2[0];
    double c2 = a2 * start2[0] + b2 * start2[1];

    double det = a1 * b2 - a2 * b1;
    if (fabs(det) < EPS) {
        vector<vector<double>> candidates;
        if (onSegment(start1, end1, start2)) candidates.push_back(start2);
        if (onSegment(start1, end1, end2)) candidates.push_back(end2);
        if (onSegment(start2, end2, start1)) candidates.push_back(start1);
        if (onSegment(start2, end2, end1)) candidates.push_back(end1);
        if (candidates.empty()) return {};
        sort(candidates.begin(), candidates.end(), lessPoint);
        return candidates[0];
    }

    double x = (b2 * c1 - b1 * c2) / det;
    double y = (a1 * c2 - a2 * c1) / det;
    vector<double> p = {x, y};
    if (onSegment(start1, end1, p) && onSegment(start2, end2, p)) return p;
    return {};
}

int main() {
    vector<double> ans = intersection({0, 0}, {1, 0}, {1, 1}, {0, -1});
    if (ans.empty()) {
        cout << "[]" << endl;
    } else {
        cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_03_intersection.languages.go -->
### go

```go
package main

import (
	"fmt"
	"math"
	"sort"
)

const eps = 1e-9

func lessPoint(a, b []float64) bool {
	if math.Abs(a[0]-b[0]) > eps {
		return a[0] < b[0]
	}
	return a[1] < b[1]-eps
}

func cross(a, b, c []float64) float64 {
	return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
}

func onSegment(a, b, p []float64) bool {
	return math.Abs(cross(a, b, p)) < eps &&
		math.Min(a[0], b[0])-eps <= p[0] && p[0] <= math.Max(a[0], b[0])+eps &&
		math.Min(a[1], b[1])-eps <= p[1] && p[1] <= math.Max(a[1], b[1])+eps
}

func intersection(start1, end1, start2, end2 []float64) []float64 {
	if lessPoint(end1, start1) {
		start1, end1 = end1, start1
	}
	if lessPoint(end2, start2) {
		start2, end2 = end2, start2
	}

	d1 := cross(start1, end1, start2)
	d2 := cross(start1, end1, end2)
	d3 := cross(start2, end2, start1)
	d4 := cross(start2, end2, end1)

	if ((d1 > eps && d2 > eps) || (d1 < -eps && d2 < -eps)) ||
		((d3 > eps && d4 > eps) || (d3 < -eps && d4 < -eps)) {
		return []float64{}
	}

	a1 := end1[1] - start1[1]
	b1 := start1[0] - end1[0]
	c1 := a1*start1[0] + b1*start1[1]

	a2 := end2[1] - start2[1]
	b2 := start2[0] - end2[0]
	c2 := a2*start2[0] + b2*start2[1]

	det := a1*b2 - a2*b1
	if math.Abs(det) < eps {
		candidates := make([][]float64, 0, 4)
		if onSegment(start1, end1, start2) {
			candidates = append(candidates, start2)
		}
		if onSegment(start1, end1, end2) {
			candidates = append(candidates, end2)
		}
		if onSegment(start2, end2, start1) {
			candidates = append(candidates, start1)
		}
		if onSegment(start2, end2, end1) {
			candidates = append(candidates, end1)
		}
		if len(candidates) == 0 {
			return []float64{}
		}
		sort.Slice(candidates, func(i, j int) bool {
			if math.Abs(candidates[i][0]-candidates[j][0]) > eps {
				return candidates[i][0] < candidates[j][0]
			}
			return candidates[i][1] < candidates[j][1]-eps
		})
		return candidates[0]
	}

	x := (b2*c1 - b1*c2) / det
	y := (a1*c2 - a2*c1) / det
	p := []float64{x, y}
	if onSegment(start1, end1, p) && onSegment(start2, end2, p) {
		return p
	}
	return []float64{}
}

func main() {
	fmt.Println(intersection([]float64{0, 0}, []float64{1, 0}, []float64{1, 1}, []float64{0, -1}))
}
```

<!-- REGISTRY_PATH: lcci_16_03_intersection.languages.python -->
### python

```python
from typing import List

EPS = 1e-9


def less_point(a: List[float], b: List[float]) -> bool:
    if abs(a[0] - b[0]) > EPS:
        return a[0] < b[0]
    return a[1] < b[1] - EPS


def cross(a: List[float], b: List[float], c: List[float]) -> float:
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])


def on_segment(a: List[float], b: List[float], p: List[float]) -> bool:
    return (
        abs(cross(a, b, p)) < EPS
        and min(a[0], b[0]) - EPS <= p[0] <= max(a[0], b[0]) + EPS
        and min(a[1], b[1]) - EPS <= p[1] <= max(a[1], b[1]) + EPS
    )


def intersection(start1: List[float], end1: List[float], start2: List[float], end2: List[float]) -> List[float]:
    if less_point(end1, start1):
        start1, end1 = end1, start1
    if less_point(end2, start2):
        start2, end2 = end2, start2

    d1 = cross(start1, end1, start2)
    d2 = cross(start1, end1, end2)
    d3 = cross(start2, end2, start1)
    d4 = cross(start2, end2, end1)

    if ((d1 > EPS and d2 > EPS) or (d1 < -EPS and d2 < -EPS) or
            (d3 > EPS and d4 > EPS) or (d3 < -EPS and d4 < -EPS)):
        return []

    a1 = end1[1] - start1[1]
    b1 = start1[0] - end1[0]
    c1 = a1 * start1[0] + b1 * start1[1]

    a2 = end2[1] - start2[1]
    b2 = start2[0] - end2[0]
    c2 = a2 * start2[0] + b2 * start2[1]

    det = a1 * b2 - a2 * b1
    if abs(det) < EPS:
        candidates = []
        if on_segment(start1, end1, start2):
            candidates.append(start2)
        if on_segment(start1, end1, end2):
            candidates.append(end2)
        if on_segment(start2, end2, start1):
            candidates.append(start1)
        if on_segment(start2, end2, end1):
            candidates.append(end1)
        if not candidates:
            return []
        candidates.sort(key=lambda p: (p[0], p[1]))
        return candidates[0]

    x = (b2 * c1 - b1 * c2) / det
    y = (a1 * c2 - a2 * c1) / det
    p = [x, y]
    return p if on_segment(start1, end1, p) and on_segment(start2, end2, p) else []


def main() -> None:
    print(intersection([0, 0], [1, 0], [1, 1], [0, -1]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_03_intersection.languages.scala -->
### scala

```scala
object Lcci1603Intersection {
    private val EPS = 1e-9

    private def lessPoint(a: Array[Double], b: Array[Double]): Boolean = {
        if (math.abs(a(0) - b(0)) > EPS) a(0) < b(0) else a(1) < b(1) - EPS
    }

    private def cross(a: Array[Double], b: Array[Double], c: Array[Double]): Double = {
        (b(0) - a(0)) * (c(1) - a(1)) - (b(1) - a(1)) * (c(0) - a(0))
    }

    private def onSegment(a: Array[Double], b: Array[Double], p: Array[Double]): Boolean = {
        math.abs(cross(a, b, p)) < EPS &&
        math.min(a(0), b(0)) - EPS <= p(0) && p(0) <= math.max(a(0), b(0)) + EPS &&
        math.min(a(1), b(1)) - EPS <= p(1) && p(1) <= math.max(a(1), b(1)) + EPS
    }

    def intersection(start1: Array[Double], end1: Array[Double], start2: Array[Double], end2: Array[Double]): Array[Double] = {
        var s1 = start1.clone()
        var e1 = end1.clone()
        var s2 = start2.clone()
        var e2 = end2.clone()

        if (lessPoint(e1, s1)) {
            val t = s1; s1 = e1; e1 = t
        }
        if (lessPoint(e2, s2)) {
            val t = s2; s2 = e2; e2 = t
        }

        val d1 = cross(s1, e1, s2)
        val d2 = cross(s1, e1, e2)
        val d3 = cross(s2, e2, s1)
        val d4 = cross(s2, e2, e1)

        if (((d1 > EPS && d2 > EPS) || (d1 < -EPS && d2 < -EPS)) ||
            ((d3 > EPS && d4 > EPS) || (d3 < -EPS && d4 < -EPS))) {
            return Array.emptyDoubleArray
        }

        val a1 = e1(1) - s1(1)
        val b1 = s1(0) - e1(0)
        val c1 = a1 * s1(0) + b1 * s1(1)

        val a2 = e2(1) - s2(1)
        val b2 = s2(0) - e2(0)
        val c2 = a2 * s2(0) + b2 * s2(1)

        val det = a1 * b2 - a2 * b1
        if (math.abs(det) < EPS) {
            val candidates = scala.collection.mutable.ArrayBuffer[Array[Double]]()
            if (onSegment(s1, e1, s2)) candidates += s2
            if (onSegment(s1, e1, e2)) candidates += e2
            if (onSegment(s2, e2, s1)) candidates += s1
            if (onSegment(s2, e2, e1)) candidates += e1
            if (candidates.isEmpty) return Array.emptyDoubleArray
            val sorted = candidates.sortBy(p => (p(0), p(1)))
            return sorted.head
        }

        val x = (b2 * c1 - b1 * c2) / det
        val y = (a1 * c2 - a2 * c1) / det
        val p = Array(x, y)
        if (onSegment(s1, e1, p) && onSegment(s2, e2, p)) p else Array.emptyDoubleArray
    }

    def main(args: Array[String]): Unit = {
        val ans = intersection(Array(0, 0), Array(1, 0), Array(1, 1), Array(0, -1))
        println(ans.mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_03_intersection.languages.typescript -->
### typescript

```typescript
const EPS = 1e-9;

function lessPoint(a: number[], b: number[]): boolean {
    if (Math.abs(a[0] - b[0]) > EPS) {
        return a[0] < b[0];
    }
    return a[1] < b[1] - EPS;
}

function cross(a: number[], b: number[], c: number[]): number {
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0]);
}

function onSegment(a: number[], b: number[], p: number[]): boolean {
    return Math.abs(cross(a, b, p)) < EPS &&
        Math.min(a[0], b[0]) - EPS <= p[0] && p[0] <= Math.max(a[0], b[0]) + EPS &&
        Math.min(a[1], b[1]) - EPS <= p[1] && p[1] <= Math.max(a[1], b[1]) + EPS;
}

function intersection(start1: number[], end1: number[], start2: number[], end2: number[]): number[] {
    if (lessPoint(end1, start1)) {
        [start1, end1] = [end1, start1];
    }
    if (lessPoint(end2, start2)) {
        [start2, end2] = [end2, start2];
    }

    const d1 = cross(start1, end1, start2);
    const d2 = cross(start1, end1, end2);
    const d3 = cross(start2, end2, start1);
    const d4 = cross(start2, end2, end1);

    if (((d1 > EPS && d2 > EPS) || (d1 < -EPS && d2 < -EPS)) ||
        ((d3 > EPS && d4 > EPS) || (d3 < -EPS && d4 < -EPS))) {
        return [];
    }

    const a1 = end1[1] - start1[1];
    const b1 = start1[0] - end1[0];
    const c1 = a1 * start1[0] + b1 * start1[1];

    const a2 = end2[1] - start2[1];
    const b2 = start2[0] - end2[0];
    const c2 = a2 * start2[0] + b2 * start2[1];

    const det = a1 * b2 - a2 * b1;
    if (Math.abs(det) < EPS) {
        const candidates: number[][] = [];
        if (onSegment(start1, end1, start2)) candidates.push(start2);
        if (onSegment(start1, end1, end2)) candidates.push(end2);
        if (onSegment(start2, end2, start1)) candidates.push(start1);
        if (onSegment(start2, end2, end1)) candidates.push(end1);
        if (candidates.length === 0) return [];
        candidates.sort((p, q) => p[0] !== q[0] ? p[0] - q[0] : p[1] - q[1]);
        return candidates[0];
    }

    const x = (b2 * c1 - b1 * c2) / det;
    const y = (a1 * c2 - a2 * c1) / det;
    const p = [x, y];
    return onSegment(start1, end1, p) && onSegment(start2, end2, p) ? p : [];
}

console.log(intersection([0, 0], [1, 0], [1, 1], [0, -1]));
```

## lcci_16_04_tic_tac_toe

<!-- REGISTRY_PATH: lcci_16_04_tic_tac_toe.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string tictactoe(const vector<string>& board) {
    int n = board.size();
    auto winner = [&](char c) {
        for (int i = 0; i < n; ++i) {
            bool row = true, col = true;
            for (int j = 0; j < n; ++j) {
                row = row && board[i][j] == c;
                col = col && board[j][i] == c;
            }
            if (row || col) return true;
        }
        bool diag1 = true, diag2 = true;
        for (int i = 0; i < n; ++i) {
            diag1 = diag1 && board[i][i] == c;
            diag2 = diag2 && board[i][n - 1 - i] == c;
        }
        return diag1 || diag2;
    };

    if (winner('X')) return "X";
    if (winner('O')) return "O";
    for (const string& row : board) {
        for (char ch : row) {
            if (ch == ' ') return "Pending";
        }
    }
    return "Draw";
}

int main() {
    cout << tictactoe({"O X", " XO", "X O"}) << endl;
    cout << tictactoe({"OOX", "XXO", "OXO"}) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_04_tic_tac_toe.languages.go -->
### go

```go
package main

import "fmt"

func tictactoe(board []string) string {
	n := len(board)
	winner := func(c byte) bool {
		for i := 0; i < n; i++ {
			row, col := true, true
			for j := 0; j < n; j++ {
				row = row && board[i][j] == c
				col = col && board[j][i] == c
			}
			if row || col {
				return true
			}
		}
		diag1, diag2 := true, true
		for i := 0; i < n; i++ {
			diag1 = diag1 && board[i][i] == c
			diag2 = diag2 && board[i][n-1-i] == c
		}
		return diag1 || diag2
	}

	if winner('X') {
		return "X"
	}
	if winner('O') {
		return "O"
	}
	for _, row := range board {
		for i := 0; i < len(row); i++ {
			if row[i] == ' ' {
				return "Pending"
			}
		}
	}
	return "Draw"
}

func main() {
	fmt.Println(tictactoe([]string{"O X", " XO", "X O"}))
	fmt.Println(tictactoe([]string{"OOX", "XXO", "OXO"}))
}
```

<!-- REGISTRY_PATH: lcci_16_04_tic_tac_toe.languages.python -->
### python

```python
from typing import List


def tictactoe(board: List[str]) -> str:
    n = len(board)

    def winner(c: str) -> bool:
        for i in range(n):
            if all(board[i][j] == c for j in range(n)):
                return True
            if all(board[j][i] == c for j in range(n)):
                return True
        if all(board[i][i] == c for i in range(n)):
            return True
        if all(board[i][n - 1 - i] == c for i in range(n)):
            return True
        return False

    if winner("X"):
        return "X"
    if winner("O"):
        return "O"
    if any(ch == " " for row in board for ch in row):
        return "Pending"
    return "Draw"


def main() -> None:
    print(tictactoe(["O X", " XO", "X O"]))
    print(tictactoe(["OOX", "XXO", "OXO"]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_04_tic_tac_toe.languages.scala -->
### scala

```scala
object Lcci1604TicTacToe {
    def tictactoe(board: Array[String]): String = {
        val n = board.length

        def winner(c: Char): Boolean = {
            for (i <- 0 until n) {
                var row = true
                var col = true
                for (j <- 0 until n) {
                    row = row && board(i)(j) == c
                    col = col && board(j)(i) == c
                }
                if (row || col) return true
            }
            var diag1 = true
            var diag2 = true
            for (i <- 0 until n) {
                diag1 = diag1 && board(i)(i) == c
                diag2 = diag2 && board(i)(n - 1 - i) == c
            }
            diag1 || diag2
        }

        if (winner('X')) return "X"
        if (winner('O')) return "O"
        if (board.exists(_.contains(' '))) return "Pending"
        "Draw"
    }

    def main(args: Array[String]): Unit = {
        println(tictactoe(Array("O X", " XO", "X O")))
        println(tictactoe(Array("OOX", "XXO", "OXO")))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_04_tic_tac_toe.languages.typescript -->
### typescript

```typescript
function tictactoe(board: string[]): string {
    const n = board.length;

    const winner = (c: string): boolean => {
        for (let i = 0; i < n; i++) {
            let row = true;
            let col = true;
            for (let j = 0; j < n; j++) {
                row = row && board[i][j] === c;
                col = col && board[j][i] === c;
            }
            if (row || col) return true;
        }
        let diag1 = true;
        let diag2 = true;
        for (let i = 0; i < n; i++) {
            diag1 = diag1 && board[i][i] === c;
            diag2 = diag2 && board[i][n - 1 - i] === c;
        }
        return diag1 || diag2;
    };

    if (winner("X")) return "X";
    if (winner("O")) return "O";
    for (const row of board) {
        for (const ch of row) {
            if (ch === " ") return "Pending";
        }
    }
    return "Draw";
}

console.log(tictactoe(["O X", " XO", "X O"]));
console.log(tictactoe(["OOX", "XXO", "OXO"]));
```

## lcci_16_05_factorial_zeros

<!-- REGISTRY_PATH: lcci_16_05_factorial_zeros.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

int trailingZeroes(int n) {
    int ans = 0;
    while (n > 0) {
        n /= 5;
        ans += n;
    }
    return ans;
}

int main() {
    cout << trailingZeroes(3) << endl;
    cout << trailingZeroes(5) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_05_factorial_zeros.languages.go -->
### go

```go
package main

import "fmt"

func trailingZeroes(n int) int {
	ans := 0
	for n > 0 {
		n /= 5
		ans += n
	}
	return ans
}

func main() {
	fmt.Println(trailingZeroes(3))
	fmt.Println(trailingZeroes(5))
}
```

<!-- REGISTRY_PATH: lcci_16_05_factorial_zeros.languages.python -->
### python

```python
def trailing_zeroes(n: int) -> int:
    ans = 0
    while n > 0:
        n //= 5
        ans += n
    return ans


def main() -> None:
    print(trailing_zeroes(3))
    print(trailing_zeroes(5))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_05_factorial_zeros.languages.scala -->
### scala

```scala
object Lcci1605FactorialZeros {
    def trailingZeroes(n0: Int): Int = {
        var n = n0
        var ans = 0
        while (n > 0) {
            n /= 5
            ans += n
        }
        ans
    }

    def main(args: Array[String]): Unit = {
        println(trailingZeroes(3))
        println(trailingZeroes(5))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_05_factorial_zeros.languages.typescript -->
### typescript

```typescript
function trailingZeroes(n: number): number {
    let ans = 0;
    while (n > 0) {
        n = Math.floor(n / 5);
        ans += n;
    }
    return ans;
}

console.log(trailingZeroes(3));
console.log(trailingZeroes(5));
```

## lcci_16_06_smallest_difference

<!-- REGISTRY_PATH: lcci_16_06_smallest_difference.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

int smallestDifference(vector<int> a, vector<int> b) {
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());
    long long ans = LLONG_MAX;
    int i = 0, j = 0;
    while (i < static_cast<int>(a.size()) && j < static_cast<int>(b.size())) {
        long long x = a[i], y = b[j];
        ans = min(ans, llabs(x - y));
        if (x < y) ++i;
        else ++j;
    }
    return static_cast<int>(ans);
}

int main() {
    cout << smallestDifference({1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_06_smallest_difference.languages.go -->
### go

```go
package main

import (
	"fmt"
	"math"
	"sort"
)

func smallestDifference(a []int, b []int) int {
	sort.Ints(a)
	sort.Ints(b)
	i, j := 0, 0
	ans := int64(math.MaxInt64)
	for i < len(a) && j < len(b) {
		diff := int64(a[i]) - int64(b[j])
		if diff < 0 {
			diff = -diff
		}
		if diff < ans {
			ans = diff
		}
		if a[i] < b[j] {
			i++
		} else {
			j++
		}
	}
	return int(ans)
}

func main() {
	fmt.Println(smallestDifference([]int{1, 3, 15, 11, 2}, []int{23, 127, 235, 19, 8}))
}
```

<!-- REGISTRY_PATH: lcci_16_06_smallest_difference.languages.python -->
### python

```python
from typing import List


def smallest_difference(a: List[int], b: List[int]) -> int:
    a.sort()
    b.sort()
    i = j = 0
    ans = 1 << 63
    while i < len(a) and j < len(b):
        ans = min(ans, abs(a[i] - b[j]))
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans


def main() -> None:
    print(smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_06_smallest_difference.languages.scala -->
### scala

```scala
object Lcci1606SmallestDifference {
    def smallestDifference(a: Array[Int], b: Array[Int]): Int = {
        val x = a.sorted
        val y = b.sorted
        var i = 0
        var j = 0
        var ans = Long.MaxValue
        while (i < x.length && j < y.length) {
            ans = math.min(ans, math.abs(x(i).toLong - y(j).toLong))
            if (x(i) < y(j)) i += 1 else j += 1
        }
        ans.toInt
    }

    def main(args: Array[String]): Unit = {
        println(smallestDifference(Array(1, 3, 15, 11, 2), Array(23, 127, 235, 19, 8)))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_06_smallest_difference.languages.typescript -->
### typescript

```typescript
function smallestDifference(a: number[], b: number[]): number {
    a.sort((x, y) => x - y);
    b.sort((x, y) => x - y);
    let i = 0;
    let j = 0;
    let ans = Number.MAX_SAFE_INTEGER;
    while (i < a.length && j < b.length) {
        ans = Math.min(ans, Math.abs(a[i] - b[j]));
        if (a[i] < b[j]) {
            i += 1;
        } else {
            j += 1;
        }
    }
    return ans;
}

console.log(smallestDifference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]));
```

## lcci_16_07_maximum

<!-- REGISTRY_PATH: lcci_16_07_maximum.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

int maximum(int a, int b) {
    return a > b ? a : b;
}

int main() {
    cout << maximum(1, 2) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_07_maximum.languages.go -->
### go

```go
package main

import "fmt"

func maximum(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

func main() {
	fmt.Println(maximum(1, 2))
}
```

<!-- REGISTRY_PATH: lcci_16_07_maximum.languages.python -->
### python

```python
def maximum(a: int, b: int) -> int:
    return a if a > b else b


def main() -> None:
    print(maximum(1, 2))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_07_maximum.languages.scala -->
### scala

```scala
object Lcci1607Maximum {
    def maximum(a: Int, b: Int): Int = if (a > b) a else b

    def main(args: Array[String]): Unit = {
        println(maximum(1, 2))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_07_maximum.languages.typescript -->
### typescript

```typescript
function maximum(a: number, b: number): number {
    return a > b ? a : b;
}

console.log(maximum(1, 2));
```

## lcci_16_08_english_int

<!-- REGISTRY_PATH: lcci_16_08_english_int.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

string below1000(int n) {
    vector<string> ones = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
    vector<string> teens = {"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    vector<string> tens = {"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};

    string s;
    if (n >= 100) {
        s += ones[n / 100] + " Hundred";
        n %= 100;
        if (n) s += " ";
    }
    if (n >= 20) {
        s += tens[n / 10];
        if (n % 10) s += " " + ones[n % 10];
    } else if (n >= 10) {
        s += teens[n - 10];
    } else if (n > 0) {
        s += ones[n];
    }
    return s;
}

string numberToWords(int num) {
    if (num == 0) return "Zero";
    if (num < 0) return "Negative " + numberToWords(-num);

    vector<string> units = {"", "Thousand", "Million", "Billion"};
    vector<string> parts;
    int unit = 0;
    while (num > 0) {
        int chunk = num % 1000;
        if (chunk > 0) {
            string piece = below1000(chunk);
            if (!units[unit].empty()) piece += " " + units[unit];
            parts.push_back(piece);
        }
        num /= 1000;
        ++unit;
    }

    string ans;
    for (int i = static_cast<int>(parts.size()) - 1; i >= 0; --i) {
        if (!ans.empty()) ans += " ";
        ans += parts[i];
    }
    return ans;
}

int main() {
    cout << numberToWords(123) << endl;
    cout << numberToWords(12345) << endl;
    cout << numberToWords(-1000010) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_08_english_int.languages.go -->
### go

```go
package main

import "fmt"

var ones = []string{"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"}
var teens = []string{"Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"}
var tens = []string{"", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"}
var units = []string{"", "Thousand", "Million", "Billion"}

func below1000(n int) string {
	parts := make([]string, 0)
	if n >= 100 {
		parts = append(parts, ones[n/100], "Hundred")
		n %= 100
	}
	if n >= 20 {
		parts = append(parts, tens[n/10])
		if n%10 != 0 {
			parts = append(parts, ones[n%10])
		}
	} else if n >= 10 {
		parts = append(parts, teens[n-10])
	} else if n > 0 {
		parts = append(parts, ones[n])
	}
	ans := ""
	for i, p := range parts {
		if i > 0 {
			ans += " "
		}
		ans += p
	}
	return ans
}

func numberToWords(num int) string {
	if num == 0 {
		return "Zero"
	}
	if num < 0 {
		return "Negative " + numberToWords(-num)
	}

	parts := make([]string, 0)
	unit := 0
	for num > 0 {
		chunk := num % 1000
		if chunk > 0 {
			piece := below1000(chunk)
			if units[unit] != "" {
				piece += " " + units[unit]
			}
			parts = append(parts, piece)
		}
		num /= 1000
		unit++
	}

	ans := ""
	for i := len(parts) - 1; i >= 0; i-- {
		if ans != "" {
			ans += " "
		}
		ans += parts[i]
	}
	return ans
}

func main() {
	fmt.Println(numberToWords(123))
	fmt.Println(numberToWords(12345))
	fmt.Println(numberToWords(-1000010))
}
```

<!-- REGISTRY_PATH: lcci_16_08_english_int.languages.python -->
### python

```python
ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
UNITS = ["", "Thousand", "Million", "Billion"]


def below_1000(n: int) -> str:
    parts = []
    if n >= 100:
        parts.append(ONES[n // 100])
        parts.append("Hundred")
        n %= 100
    if n >= 20:
        parts.append(TENS[n // 10])
        if n % 10:
            parts.append(ONES[n % 10])
    elif n >= 10:
        parts.append(TEENS[n - 10])
    elif n > 0:
        parts.append(ONES[n])
    return " ".join(parts)


def number_to_words(num: int) -> str:
    if num == 0:
        return "Zero"
    if num < 0:
        return "Negative " + number_to_words(-num)

    parts = []
    unit = 0
    while num > 0:
        chunk = num % 1000
        if chunk:
            piece = below_1000(chunk)
            if UNITS[unit]:
                piece += f" {UNITS[unit]}"
            parts.append(piece)
        num //= 1000
        unit += 1
    return " ".join(reversed(parts))


def main() -> None:
    print(number_to_words(123))
    print(number_to_words(12345))
    print(number_to_words(-1000010))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_08_english_int.languages.scala -->
### scala

```scala
object Lcci1608EnglishInt {
    private val ones = Array("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine")
    private val teens = Array("Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
    private val tens = Array("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
    private val units = Array("", "Thousand", "Million", "Billion")

    private def below1000(n0: Int): String = {
        var n = n0
        val parts = scala.collection.mutable.ArrayBuffer[String]()
        if (n >= 100) {
            parts += ones(n / 100)
            parts += "Hundred"
            n %= 100
        }
        if (n >= 20) {
            parts += tens(n / 10)
            if (n % 10 != 0) parts += ones(n % 10)
        } else if (n >= 10) {
            parts += teens(n - 10)
        } else if (n > 0) {
            parts += ones(n)
        }
        parts.mkString(" ")
    }

    def numberToWords(num0: Int): String = {
        if (num0 == 0) return "Zero"
        if (num0 < 0) return "Negative " + numberToWords(-num0)

        var num = num0
        val parts = scala.collection.mutable.ArrayBuffer[String]()
        var unit = 0
        while (num > 0) {
            val chunk = num % 1000
            if (chunk > 0) {
                var piece = below1000(chunk)
                if (units(unit).nonEmpty) piece += " " + units(unit)
                parts += piece
            }
            num /= 1000
            unit += 1
        }
        parts.reverse.mkString(" ")
    }

    def main(args: Array[String]): Unit = {
        println(numberToWords(123))
        println(numberToWords(12345))
        println(numberToWords(-1000010))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_08_english_int.languages.typescript -->
### typescript

```typescript
const ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"];
const TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"];
const TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"];
const UNITS = ["", "Thousand", "Million", "Billion"];

function below1000(n: number): string {
    const parts: string[] = [];
    if (n >= 100) {
        parts.push(ONES[Math.floor(n / 100)]);
        parts.push("Hundred");
        n %= 100;
    }
    if (n >= 20) {
        parts.push(TENS[Math.floor(n / 10)]);
        if (n % 10) parts.push(ONES[n % 10]);
    } else if (n >= 10) {
        parts.push(TEENS[n - 10]);
    } else if (n > 0) {
        parts.push(ONES[n]);
    }
    return parts.join(" ");
}

function numberToWords(num: number): string {
    if (num === 0) return "Zero";
    if (num < 0) return "Negative " + numberToWords(-num);

    const parts: string[] = [];
    let unit = 0;
    while (num > 0) {
        const chunk = num % 1000;
        if (chunk > 0) {
            let piece = below1000(chunk);
            if (UNITS[unit] !== "") piece += " " + UNITS[unit];
            parts.push(piece);
        }
        num = Math.floor(num / 1000);
        unit += 1;
    }
    return parts.reverse().join(" ");
}

console.log(numberToWords(123));
console.log(numberToWords(12345));
console.log(numberToWords(-1000010));
```

## lcci_16_09_operations

<!-- REGISTRY_PATH: lcci_16_09_operations.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

class Operations {
public:
    int minus(int a, int b) {
        return a - b;
    }

    int multiply(int a, int b) {
        return a * b;
    }

    int divide(int a, int b) {
        return a / b;
    }
};

int main() {
    Operations ops;
    cout << ops.minus(10, 3) << endl;
    cout << ops.multiply(6, -4) << endl;
    cout << ops.divide(20, 5) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_09_operations.languages.go -->
### go

```go
package main

import "fmt"

type Operations struct{}

func (Operations) Minus(a int, b int) int {
	return a - b
}

func (Operations) Multiply(a int, b int) int {
	return a * b
}

func (Operations) Divide(a int, b int) int {
	return a / b
}

func main() {
	ops := Operations{}
	fmt.Println(ops.Minus(10, 3))
	fmt.Println(ops.Multiply(6, -4))
	fmt.Println(ops.Divide(20, 5))
}
```

<!-- REGISTRY_PATH: lcci_16_09_operations.languages.python -->
### python

```python
class Operations:
    def minus(self, a: int, b: int) -> int:
        return a - b

    def multiply(self, a: int, b: int) -> int:
        return a * b

    def divide(self, a: int, b: int) -> int:
        return int(a / b)


def main() -> None:
    ops = Operations()
    print(ops.minus(10, 3))
    print(ops.multiply(6, -4))
    print(ops.divide(20, 5))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_09_operations.languages.scala -->
### scala

```scala
object Lcci1609Operations {
    final class Operations {
        def minus(a: Int, b: Int): Int = a - b
        def multiply(a: Int, b: Int): Int = a * b
        def divide(a: Int, b: Int): Int = a / b
    }

    def main(args: Array[String]): Unit = {
        val ops = new Operations
        println(ops.minus(10, 3))
        println(ops.multiply(6, -4))
        println(ops.divide(20, 5))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_09_operations.languages.typescript -->
### typescript

```typescript
class Operations {
    minus(a: number, b: number): number {
        return a - b;
    }

    multiply(a: number, b: number): number {
        return a * b;
    }

    divide(a: number, b: number): number {
        return Math.trunc(a / b);
    }
}

const ops = new Operations();
console.log(ops.minus(10, 3));
console.log(ops.multiply(6, -4));
console.log(ops.divide(20, 5));
```

## lcci_16_10_living_people

<!-- REGISTRY_PATH: lcci_16_10_living_people.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxAliveYear(const vector<int>& birth, const vector<int>& death) {
    vector<int> diff(102, 0);
    for (int i = 0; i < static_cast<int>(birth.size()); ++i) {
        ++diff[birth[i] - 1900];
        if (death[i] + 1 <= 2000) {
            --diff[death[i] + 1 - 1900];
        }
    }
    int bestYear = 1900;
    int alive = 0;
    int bestAlive = -1;
    for (int i = 0; i <= 100; ++i) {
        alive += diff[i];
        if (alive > bestAlive) {
            bestAlive = alive;
            bestYear = 1900 + i;
        }
    }
    return bestYear;
}

int main() {
    cout << maxAliveYear({1900, 1901, 1950}, {1948, 1951, 2000}) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_10_living_people.languages.go -->
### go

```go
package main

import "fmt"

func maxAliveYear(birth []int, death []int) int {
	diff := make([]int, 102)
	for i := 0; i < len(birth); i++ {
		diff[birth[i]-1900]++
		if death[i]+1 <= 2000 {
			diff[death[i]+1-1900]--
		}
	}

	bestYear := 1900
	alive := 0
	bestAlive := -1
	for i := 0; i <= 100; i++ {
		alive += diff[i]
		if alive > bestAlive {
			bestAlive = alive
			bestYear = 1900 + i
		}
	}
	return bestYear
}

func main() {
	fmt.Println(maxAliveYear([]int{1900, 1901, 1950}, []int{1948, 1951, 2000}))
}
```

<!-- REGISTRY_PATH: lcci_16_10_living_people.languages.python -->
### python

```python
from typing import List


def max_alive_year(birth: List[int], death: List[int]) -> int:
    diff = [0] * 102
    for b, d in zip(birth, death):
        diff[b - 1900] += 1
        if d + 1 <= 2000:
            diff[d + 1 - 1900] -= 1

    best_year = 1900
    alive = 0
    best_alive = -1
    for i in range(101):
        alive += diff[i]
        if alive > best_alive:
            best_alive = alive
            best_year = 1900 + i
    return best_year


def main() -> None:
    print(max_alive_year([1900, 1901, 1950], [1948, 1951, 2000]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_10_living_people.languages.scala -->
### scala

```scala
object Lcci1610LivingPeople {
    def maxAliveYear(birth: Array[Int], death: Array[Int]): Int = {
        val diff = Array.fill(102)(0)
        for (i <- birth.indices) {
            diff(birth(i) - 1900) += 1
            if (death(i) + 1 <= 2000) {
                diff(death(i) + 1 - 1900) -= 1
            }
        }

        var bestYear = 1900
        var alive = 0
        var bestAlive = -1
        for (i <- 0 to 100) {
            alive += diff(i)
            if (alive > bestAlive) {
                bestAlive = alive
                bestYear = 1900 + i
            }
        }
        bestYear
    }

    def main(args: Array[String]): Unit = {
        println(maxAliveYear(Array(1900, 1901, 1950), Array(1948, 1951, 2000)))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_10_living_people.languages.typescript -->
### typescript

```typescript
function maxAliveYear(birth: number[], death: number[]): number {
    const diff = new Array<number>(102).fill(0);
    for (let i = 0; i < birth.length; i++) {
        diff[birth[i] - 1900] += 1;
        if (death[i] + 1 <= 2000) {
            diff[death[i] + 1 - 1900] -= 1;
        }
    }

    let bestYear = 1900;
    let alive = 0;
    let bestAlive = -1;
    for (let i = 0; i <= 100; i++) {
        alive += diff[i];
        if (alive > bestAlive) {
            bestAlive = alive;
            bestYear = 1900 + i;
        }
    }
    return bestYear;
}

console.log(maxAliveYear([1900, 1901, 1950], [1948, 1951, 2000]));
```

## lcci_16_11_diving_board

<!-- REGISTRY_PATH: lcci_16_11_diving_board.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

vector<int> divingBoard(int shorter, int longer, int k) {
    if (k == 0) return {};
    if (shorter == longer) return {shorter * k};
    vector<int> ans;
    for (int i = 0; i <= k; ++i) {
        ans.push_back(shorter * (k - i) + longer * i);
    }
    return ans;
}

int main() {
    vector<int> ans = divingBoard(1, 2, 3);
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << ans[i];
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_11_diving_board.languages.go -->
### go

```go
package main

import "fmt"

func divingBoard(shorter int, longer int, k int) []int {
	if k == 0 {
		return []int{}
	}
	if shorter == longer {
		return []int{shorter * k}
	}
	ans := make([]int, 0, k+1)
	for i := 0; i <= k; i++ {
		ans = append(ans, shorter*(k-i)+longer*i)
	}
	return ans
}

func main() {
	fmt.Println(divingBoard(1, 2, 3))
}
```

<!-- REGISTRY_PATH: lcci_16_11_diving_board.languages.python -->
### python

```python
from typing import List


def diving_board(shorter: int, longer: int, k: int) -> List[int]:
    if k == 0:
        return []
    if shorter == longer:
        return [shorter * k]
    return [shorter * (k - i) + longer * i for i in range(k + 1)]


def main() -> None:
    print(diving_board(1, 2, 3))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_11_diving_board.languages.scala -->
### scala

```scala
object Lcci1611DivingBoard {
    def divingBoard(shorter: Int, longer: Int, k: Int): Array[Int] = {
        if (k == 0) return Array.emptyIntArray
        if (shorter == longer) return Array(shorter * k)
        Array.tabulate(k + 1)(i => shorter * (k - i) + longer * i)
    }

    def main(args: Array[String]): Unit = {
        println(divingBoard(1, 2, 3).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_11_diving_board.languages.typescript -->
### typescript

```typescript
function divingBoard(shorter: number, longer: number, k: number): number[] {
    if (k === 0) return [];
    if (shorter === longer) return [shorter * k];
    const ans: number[] = [];
    for (let i = 0; i <= k; i++) {
        ans.push(shorter * (k - i) + longer * i);
    }
    return ans;
}

console.log(divingBoard(1, 2, 3));
```

## lcci_16_13_bisect_squares

<!-- REGISTRY_PATH: lcci_16_13_bisect_squares.languages.cpp -->
### cpp

```cpp
#include <cmath>
#include <iostream>
#include <vector>
using namespace std;

vector<double> cutSquares(const vector<int>& square1, const vector<int>& square2) {
    double x1 = square1[0], y1 = square1[1], s1 = square1[2];
    double x2 = square2[0], y2 = square2[1], s2 = square2[2];

    double cx1 = x1 + s1 / 2.0, cy1 = y1 + s1 / 2.0;
    double cx2 = x2 + s2 / 2.0, cy2 = y2 + s2 / 2.0;

    const double eps = 1e-9;
    if (fabs(cx1 - cx2) < eps) {
        double x = cx1;
        double yBottom = min(y1, y2);
        double yTop = max(y1 + s1, y2 + s2);
        return {x, yBottom, x, yTop};
    }

    double k = (cy2 - cy1) / (cx2 - cx1);
    double b = cy1 - k * cx1;

    double px1, py1, px2, py2;
    if (fabs(k) <= 1) {
        px1 = min(x1, x2);
        px2 = max(x1 + s1, x2 + s2);
        py1 = k * px1 + b;
        py2 = k * px2 + b;
    } else {
        py1 = min(y1, y2);
        py2 = max(y1 + s1, y2 + s2);
        px1 = (py1 - b) / k;
        px2 = (py2 - b) / k;
    }

    if (px1 > px2 || (fabs(px1 - px2) < eps && py1 > py2)) {
        swap(px1, px2);
        swap(py1, py2);
    }
    return {px1, py1, px2, py2};
}

int main() {
    vector<double> ans = cutSquares({-1, -1, 2}, {0, -1, 2});
    cout << "[" << ans[0] << ", " << ans[1] << ", " << ans[2] << ", " << ans[3] << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_13_bisect_squares.languages.go -->
### go

```go
package main

import (
	"fmt"
	"math"
)

func cutSquares(square1 []int, square2 []int) []float64 {
	x1, y1, s1 := float64(square1[0]), float64(square1[1]), float64(square1[2])
	x2, y2, s2 := float64(square2[0]), float64(square2[1]), float64(square2[2])

	cx1, cy1 := x1+s1/2.0, y1+s1/2.0
	cx2, cy2 := x2+s2/2.0, y2+s2/2.0

	if math.Abs(cx1-cx2) < 1e-9 {
		x := cx1
		yBottom := math.Min(y1, y2)
		yTop := math.Max(y1+s1, y2+s2)
		return []float64{x, yBottom, x, yTop}
	}

	k := (cy2 - cy1) / (cx2 - cx1)
	b := cy1 - k*cx1

	var px1, py1, px2, py2 float64
	if math.Abs(k) <= 1 {
		px1 = math.Min(x1, x2)
		px2 = math.Max(x1+s1, x2+s2)
		py1 = k*px1 + b
		py2 = k*px2 + b
	} else {
		py1 = math.Min(y1, y2)
		py2 = math.Max(y1+s1, y2+s2)
		px1 = (py1 - b) / k
		px2 = (py2 - b) / k
	}

	if px1 > px2 || (math.Abs(px1-px2) < 1e-9 && py1 > py2) {
		px1, px2 = px2, px1
		py1, py2 = py2, py1
	}
	return []float64{px1, py1, px2, py2}
}

func main() {
	fmt.Println(cutSquares([]int{-1, -1, 2}, []int{0, -1, 2}))
}
```

<!-- REGISTRY_PATH: lcci_16_13_bisect_squares.languages.python -->
### python

```python
from typing import List


def cut_squares(square1: List[int], square2: List[int]) -> List[float]:
    x1, y1, s1 = square1
    x2, y2, s2 = square2

    cx1, cy1 = x1 + s1 / 2.0, y1 + s1 / 2.0
    cx2, cy2 = x2 + s2 / 2.0, y2 + s2 / 2.0

    eps = 1e-9
    if abs(cx1 - cx2) < eps:
        x = cx1
        y_bottom = min(y1, y2)
        y_top = max(y1 + s1, y2 + s2)
        return [x, y_bottom, x, y_top]

    k = (cy2 - cy1) / (cx2 - cx1)
    b = cy1 - k * cx1

    if abs(k) <= 1:
        px1 = min(x1, x2)
        px2 = max(x1 + s1, x2 + s2)
        py1 = k * px1 + b
        py2 = k * px2 + b
    else:
        py1 = min(y1, y2)
        py2 = max(y1 + s1, y2 + s2)
        px1 = (py1 - b) / k
        px2 = (py2 - b) / k

    if px1 > px2 or (abs(px1 - px2) < eps and py1 > py2):
        px1, px2 = px2, px1
        py1, py2 = py2, py1

    return [px1, py1, px2, py2]


def main() -> None:
    print(cut_squares([-1, -1, 2], [0, -1, 2]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_13_bisect_squares.languages.scala -->
### scala

```scala
object Lcci1613BisectSquares {
    def cutSquares(square1: Array[Int], square2: Array[Int]): Array[Double] = {
        val x1 = square1(0).toDouble
        val y1 = square1(1).toDouble
        val s1 = square1(2).toDouble
        val x2 = square2(0).toDouble
        val y2 = square2(1).toDouble
        val s2 = square2(2).toDouble

        val cx1 = x1 + s1 / 2.0
        val cy1 = y1 + s1 / 2.0
        val cx2 = x2 + s2 / 2.0
        val cy2 = y2 + s2 / 2.0

        if (math.abs(cx1 - cx2) < 1e-9) {
            val x = cx1
            val yBottom = math.min(y1, y2)
            val yTop = math.max(y1 + s1, y2 + s2)
            return Array(x, yBottom, x, yTop)
        }

        val k = (cy2 - cy1) / (cx2 - cx1)
        val b = cy1 - k * cx1

        var px1 = 0.0
        var py1 = 0.0
        var px2 = 0.0
        var py2 = 0.0

        if (math.abs(k) <= 1) {
            px1 = math.min(x1, x2)
            px2 = math.max(x1 + s1, x2 + s2)
            py1 = k * px1 + b
            py2 = k * px2 + b
        } else {
            py1 = math.min(y1, y2)
            py2 = math.max(y1 + s1, y2 + s2)
            px1 = (py1 - b) / k
            px2 = (py2 - b) / k
        }

        if (px1 > px2 || (math.abs(px1 - px2) < 1e-9 && py1 > py2)) {
            val tx = px1
            px1 = px2
            px2 = tx
            val ty = py1
            py1 = py2
            py2 = ty
        }

        Array(px1, py1, px2, py2)
    }

    def main(args: Array[String]): Unit = {
        println(cutSquares(Array(-1, -1, 2), Array(0, -1, 2)).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_13_bisect_squares.languages.typescript -->
### typescript

```typescript
function cutSquares(square1: number[], square2: number[]): number[] {
    const [x1, y1, s1] = square1;
    const [x2, y2, s2] = square2;

    const cx1 = x1 + s1 / 2;
    const cy1 = y1 + s1 / 2;
    const cx2 = x2 + s2 / 2;
    const cy2 = y2 + s2 / 2;

    if (Math.abs(cx1 - cx2) < 1e-9) {
        const x = cx1;
        const yBottom = Math.min(y1, y2);
        const yTop = Math.max(y1 + s1, y2 + s2);
        return [x, yBottom, x, yTop];
    }

    const k = (cy2 - cy1) / (cx2 - cx1);
    const b = cy1 - k * cx1;

    let px1: number;
    let py1: number;
    let px2: number;
    let py2: number;

    if (Math.abs(k) <= 1) {
        px1 = Math.min(x1, x2);
        px2 = Math.max(x1 + s1, x2 + s2);
        py1 = k * px1 + b;
        py2 = k * px2 + b;
    } else {
        py1 = Math.min(y1, y2);
        py2 = Math.max(y1 + s1, y2 + s2);
        px1 = (py1 - b) / k;
        px2 = (py2 - b) / k;
    }

    if (px1 > px2 || (Math.abs(px1 - px2) < 1e-9 && py1 > py2)) {
        [px1, px2] = [px2, px1];
        [py1, py2] = [py2, py1];
    }

    return [px1, py1, px2, py2];
}

console.log(cutSquares([-1, -1, 2], [0, -1, 2]));
```

## lcci_16_14_best_line

<!-- REGISTRY_PATH: lcci_16_14_best_line.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool collinear(const vector<int>& a, const vector<int>& b, const vector<int>& c) {
    long long x1 = b[0] - a[0], y1 = b[1] - a[1];
    long long x2 = c[0] - a[0], y2 = c[1] - a[1];
    return x1 * y2 == x2 * y1;
}

vector<int> bestLine(const vector<vector<int>>& points) {
    int n = points.size();
    int bestI = 0, bestJ = 1, bestCount = 2;
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int count = 2;
            for (int k = j + 1; k < n; ++k) {
                if (collinear(points[i], points[j], points[k])) {
                    ++count;
                }
            }
            if (count > bestCount || (count == bestCount && (i < bestI || (i == bestI && j < bestJ)))) {
                bestCount = count;
                bestI = i;
                bestJ = j;
            }
        }
    }
    return {bestI, bestJ};
}

int main() {
    vector<int> ans = bestLine({{0, 0}, {1, 1}, {1, 0}, {2, 2}});
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_14_best_line.languages.go -->
### go

```go
package main

import "fmt"

func collinear(a, b, c []int) bool {
	x1, y1 := int64(b[0]-a[0]), int64(b[1]-a[1])
	x2, y2 := int64(c[0]-a[0]), int64(c[1]-a[1])
	return x1*y2 == x2*y1
}

func bestLine(points [][]int) []int {
	n := len(points)
	bestI, bestJ, bestCount := 0, 1, 2
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			count := 2
			for k := j + 1; k < n; k++ {
				if collinear(points[i], points[j], points[k]) {
					count++
				}
			}
			if count > bestCount || (count == bestCount && (i < bestI || (i == bestI && j < bestJ))) {
				bestI, bestJ, bestCount = i, j, count
			}
		}
	}
	return []int{bestI, bestJ}
}

func main() {
	fmt.Println(bestLine([][]int{{0, 0}, {1, 1}, {1, 0}, {2, 2}}))
}
```

<!-- REGISTRY_PATH: lcci_16_14_best_line.languages.python -->
### python

```python
from typing import List


def collinear(a: List[int], b: List[int], c: List[int]) -> bool:
    x1, y1 = b[0] - a[0], b[1] - a[1]
    x2, y2 = c[0] - a[0], c[1] - a[1]
    return x1 * y2 == x2 * y1


def best_line(points: List[List[int]]) -> List[int]:
    n = len(points)
    best_i, best_j, best_count = 0, 1, 2
    for i in range(n):
        for j in range(i + 1, n):
            count = 2
            for k in range(j + 1, n):
                if collinear(points[i], points[j], points[k]):
                    count += 1
            if count > best_count or (count == best_count and (i < best_i or (i == best_i and j < best_j))):
                best_i, best_j, best_count = i, j, count
    return [best_i, best_j]


def main() -> None:
    print(best_line([[0, 0], [1, 1], [1, 0], [2, 2]]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_14_best_line.languages.scala -->
### scala

```scala
object Lcci1614BestLine {
    private def collinear(a: Array[Int], b: Array[Int], c: Array[Int]): Boolean = {
        val x1 = b(0).toLong - a(0).toLong
        val y1 = b(1).toLong - a(1).toLong
        val x2 = c(0).toLong - a(0).toLong
        val y2 = c(1).toLong - a(1).toLong
        x1 * y2 == x2 * y1
    }

    def bestLine(points: Array[Array[Int]]): Array[Int] = {
        val n = points.length
        var bestI = 0
        var bestJ = 1
        var bestCount = 2
        for (i <- 0 until n) {
            for (j <- i + 1 until n) {
                var count = 2
                for (k <- j + 1 until n) {
                    if (collinear(points(i), points(j), points(k))) count += 1
                }
                if (count > bestCount || (count == bestCount && (i < bestI || (i == bestI && j < bestJ)))) {
                    bestI = i
                    bestJ = j
                    bestCount = count
                }
            }
        }
        Array(bestI, bestJ)
    }

    def main(args: Array[String]): Unit = {
        println(bestLine(Array(Array(0, 0), Array(1, 1), Array(1, 0), Array(2, 2))).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_14_best_line.languages.typescript -->
### typescript

```typescript
function collinear(a: number[], b: number[], c: number[]): boolean {
    const x1 = b[0] - a[0];
    const y1 = b[1] - a[1];
    const x2 = c[0] - a[0];
    const y2 = c[1] - a[1];
    return x1 * y2 === x2 * y1;
}

function bestLine(points: number[][]): number[] {
    const n = points.length;
    let bestI = 0;
    let bestJ = 1;
    let bestCount = 2;
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let count = 2;
            for (let k = j + 1; k < n; k++) {
                if (collinear(points[i], points[j], points[k])) {
                    count += 1;
                }
            }
            if (count > bestCount || (count === bestCount && (i < bestI || (i === bestI && j < bestJ)))) {
                bestI = i;
                bestJ = j;
                bestCount = count;
            }
        }
    }
    return [bestI, bestJ];
}

console.log(bestLine([[0, 0], [1, 1], [1, 0], [2, 2]]));
```

## lcci_16_15_master_mind

<!-- REGISTRY_PATH: lcci_16_15_master_mind.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<int> masterMind(const string& solution, const string& guess) {
    int hits = 0;
    vector<int> cs(26, 0), cg(26, 0);
    for (int i = 0; i < 4; ++i) {
        if (solution[i] == guess[i]) {
            ++hits;
        } else {
            ++cs[solution[i] - 'A'];
            ++cg[guess[i] - 'A'];
        }
    }
    int pseudo = 0;
    for (int i = 0; i < 26; ++i) {
        pseudo += min(cs[i], cg[i]);
    }
    return {hits, pseudo};
}

int main() {
    vector<int> ans = masterMind("RGBY", "GGRR");
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_15_master_mind.languages.go -->
### go

```go
package main

import "fmt"

func masterMind(solution string, guess string) []int {
	hits := 0
	cs := make([]int, 26)
	cg := make([]int, 26)
	for i := 0; i < 4; i++ {
		if solution[i] == guess[i] {
			hits++
		} else {
			cs[solution[i]-'A']++
			cg[guess[i]-'A']++
		}
	}
	pseudo := 0
	for i := 0; i < 26; i++ {
		if cs[i] < cg[i] {
			pseudo += cs[i]
		} else {
			pseudo += cg[i]
		}
	}
	return []int{hits, pseudo}
}

func main() {
	fmt.Println(masterMind("RGBY", "GGRR"))
}
```

<!-- REGISTRY_PATH: lcci_16_15_master_mind.languages.python -->
### python

```python
from typing import List


def master_mind(solution: str, guess: str) -> List[int]:
    hits = 0
    cs = [0] * 26
    cg = [0] * 26
    for s, g in zip(solution, guess):
        if s == g:
            hits += 1
        else:
            cs[ord(s) - ord("A")] += 1
            cg[ord(g) - ord("A")] += 1
    pseudo = sum(min(cs[i], cg[i]) for i in range(26))
    return [hits, pseudo]


def main() -> None:
    print(master_mind("RGBY", "GGRR"))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_15_master_mind.languages.scala -->
### scala

```scala
object Lcci1615MasterMind {
    def masterMind(solution: String, guess: String): Array[Int] = {
        var hits = 0
        val cs = Array.fill(26)(0)
        val cg = Array.fill(26)(0)
        for (i <- 0 until 4) {
            if (solution(i) == guess(i)) {
                hits += 1
            } else {
                cs(solution(i) - 'A') += 1
                cg(guess(i) - 'A') += 1
            }
        }
        var pseudo = 0
        for (i <- 0 until 26) {
            pseudo += math.min(cs(i), cg(i))
        }
        Array(hits, pseudo)
    }

    def main(args: Array[String]): Unit = {
        println(masterMind("RGBY", "GGRR").mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_15_master_mind.languages.typescript -->
### typescript

```typescript
function masterMind(solution: string, guess: string): number[] {
    let hits = 0;
    const cs = new Array<number>(26).fill(0);
    const cg = new Array<number>(26).fill(0);
    for (let i = 0; i < 4; i++) {
        if (solution[i] === guess[i]) {
            hits += 1;
        } else {
            cs[solution.charCodeAt(i) - 65] += 1;
            cg[guess.charCodeAt(i) - 65] += 1;
        }
    }
    let pseudo = 0;
    for (let i = 0; i < 26; i++) {
        pseudo += Math.min(cs[i], cg[i]);
    }
    return [hits, pseudo];
}

console.log(masterMind("RGBY", "GGRR"));
```

## lcci_16_16_sub_sort

<!-- REGISTRY_PATH: lcci_16_16_sub_sort.languages.cpp -->
### cpp

```cpp
#include <climits>
#include <iostream>
#include <vector>
using namespace std;

vector<int> subSort(const vector<int>& array) {
    int n = array.size();
    int left = -1, right = -1;

    int maxSeen = INT_MIN;
    for (int i = 0; i < n; ++i) {
        if (array[i] < maxSeen) right = i;
        else maxSeen = array[i];
    }

    int minSeen = INT_MAX;
    for (int i = n - 1; i >= 0; --i) {
        if (array[i] > minSeen) left = i;
        else minSeen = array[i];
    }

    if (left == -1) return {-1, -1};
    return {left, right};
}

int main() {
    vector<int> ans = subSort({1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19});
    cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_16_sub_sort.languages.go -->
### go

```go
package main

import (
	"fmt"
	"math"
)

func subSort(array []int) []int {
	n := len(array)
	left, right := -1, -1

	maxSeen := math.MinInt
	for i := 0; i < n; i++ {
		if array[i] < maxSeen {
			right = i
		} else {
			maxSeen = array[i]
		}
	}

	minSeen := math.MaxInt
	for i := n - 1; i >= 0; i-- {
		if array[i] > minSeen {
			left = i
		} else {
			minSeen = array[i]
		}
	}

	if left == -1 {
		return []int{-1, -1}
	}
	return []int{left, right}
}

func main() {
	fmt.Println(subSort([]int{1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19}))
}
```

<!-- REGISTRY_PATH: lcci_16_16_sub_sort.languages.python -->
### python

```python
from typing import List


def sub_sort(array: List[int]) -> List[int]:
    n = len(array)
    left = right = -1

    max_seen = -10**18
    for i, value in enumerate(array):
        if value < max_seen:
            right = i
        else:
            max_seen = value

    min_seen = 10**18
    for i in range(n - 1, -1, -1):
        if array[i] > min_seen:
            left = i
        else:
            min_seen = array[i]

    return [left, right] if left != -1 else [-1, -1]


def main() -> None:
    print(sub_sort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_16_sub_sort.languages.scala -->
### scala

```scala
object Lcci1616SubSort {
    def subSort(array: Array[Int]): Array[Int] = {
        val n = array.length
        var left = -1
        var right = -1

        var maxSeen = Int.MinValue
        for (i <- 0 until n) {
            if (array(i) < maxSeen) right = i else maxSeen = array(i)
        }

        var minSeen = Int.MaxValue
        for (i <- (0 until n).reverse) {
            if (array(i) > minSeen) left = i else minSeen = array(i)
        }

        if (left == -1) Array(-1, -1) else Array(left, right)
    }

    def main(args: Array[String]): Unit = {
        println(subSort(Array(1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19)).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_16_sub_sort.languages.typescript -->
### typescript

```typescript
function subSort(array: number[]): number[] {
    const n = array.length;
    let left = -1;
    let right = -1;

    let maxSeen = Number.NEGATIVE_INFINITY;
    for (let i = 0; i < n; i++) {
        if (array[i] < maxSeen) {
            right = i;
        } else {
            maxSeen = array[i];
        }
    }

    let minSeen = Number.POSITIVE_INFINITY;
    for (let i = n - 1; i >= 0; i--) {
        if (array[i] > minSeen) {
            left = i;
        } else {
            minSeen = array[i];
        }
    }

    return left === -1 ? [-1, -1] : [left, right];
}

console.log(subSort([1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19]));
```

## lcci_16_17_contiguous_sequence

<!-- REGISTRY_PATH: lcci_16_17_contiguous_sequence.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxSubArray(const vector<int>& nums) {
    int best = nums[0];
    int cur = nums[0];
    for (int i = 1; i < static_cast<int>(nums.size()); ++i) {
        cur = max(nums[i], cur + nums[i]);
        best = max(best, cur);
    }
    return best;
}

int main() {
    cout << maxSubArray({-2, 1, -3, 4, -1, 2, 1, -5, 4}) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_17_contiguous_sequence.languages.go -->
### go

```go
package main

import "fmt"

func maxSubArray(nums []int) int {
	best, cur := nums[0], nums[0]
	for i := 1; i < len(nums); i++ {
		if cur+nums[i] > nums[i] {
			cur = cur + nums[i]
		} else {
			cur = nums[i]
		}
		if cur > best {
			best = cur
		}
	}
	return best
}

func main() {
	fmt.Println(maxSubArray([]int{-2, 1, -3, 4, -1, 2, 1, -5, 4}))
}
```

<!-- REGISTRY_PATH: lcci_16_17_contiguous_sequence.languages.python -->
### python

```python
from typing import List


def max_sub_array(nums: List[int]) -> int:
    best = cur = nums[0]
    for value in nums[1:]:
        cur = max(value, cur + value)
        best = max(best, cur)
    return best


def main() -> None:
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_17_contiguous_sequence.languages.scala -->
### scala

```scala
object Lcci1617ContiguousSequence {
    def maxSubArray(nums: Array[Int]): Int = {
        var best = nums(0)
        var cur = nums(0)
        for (i <- 1 until nums.length) {
            cur = math.max(nums(i), cur + nums(i))
            best = math.max(best, cur)
        }
        best
    }

    def main(args: Array[String]): Unit = {
        println(maxSubArray(Array(-2, 1, -3, 4, -1, 2, 1, -5, 4)))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_17_contiguous_sequence.languages.typescript -->
### typescript

```typescript
function maxSubArray(nums: number[]): number {
    let best = nums[0];
    let cur = nums[0];
    for (let i = 1; i < nums.length; i++) {
        cur = Math.max(nums[i], cur + nums[i]);
        best = Math.max(best, cur);
    }
    return best;
}

console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]));
```

## lcci_16_18_pattern_matching

<!-- REGISTRY_PATH: lcci_16_18_pattern_matching.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
using namespace std;

bool patternMatching(const string& pattern, const string& value) {
    if (pattern.empty()) return value.empty();

    int countA = 0, countB = 0;
    for (char ch : pattern) {
        if (ch == 'a') ++countA;
        else ++countB;
    }

    if (countA < countB) {
        string swapped = pattern;
        for (char& ch : swapped) ch = (ch == 'a' ? 'b' : 'a');
        return patternMatching(swapped, value);
    }

    if (value.empty()) return countB == 0;

    int n = value.size();
    for (int lenA = 0; countA * lenA <= n; ++lenA) {
        int rest = n - countA * lenA;
        if (countB == 0) {
            if (rest != 0) continue;
        } else if (rest % countB != 0) {
            continue;
        }
        int lenB = (countB == 0 ? 0 : rest / countB);

        int pos = 0;
        string a = "#", b = "#";
        bool ok = true;
        for (char ch : pattern) {
            if (ch == 'a') {
                string sub = value.substr(pos, lenA);
                if (a == "#") a = sub;
                else if (a != sub) { ok = false; break; }
                pos += lenA;
            } else {
                string sub = value.substr(pos, lenB);
                if (b == "#") b = sub;
                else if (b != sub) { ok = false; break; }
                pos += lenB;
            }
        }
        if (ok && a != b) return true;
    }
    return false;
}

int main() {
    cout << boolalpha << patternMatching("abba", "dogcatcatdog") << endl;
    cout << boolalpha << patternMatching("abba", "dogcatcatfish") << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_18_pattern_matching.languages.go -->
### go

```go
package main

import "fmt"

func patternMatching(pattern string, value string) bool {
	if pattern == "" {
		return value == ""
	}

	countA, countB := 0, 0
	for i := 0; i < len(pattern); i++ {
		if pattern[i] == 'a' {
			countA++
		} else {
			countB++
		}
	}

	if countA < countB {
		swapped := make([]byte, len(pattern))
		for i := 0; i < len(pattern); i++ {
			if pattern[i] == 'a' {
				swapped[i] = 'b'
			} else {
				swapped[i] = 'a'
			}
		}
		return patternMatching(string(swapped), value)
	}

	if value == "" {
		return countB == 0
	}

	n := len(value)
	for lenA := 0; countA*lenA <= n; lenA++ {
		rest := n - countA*lenA
		lenB := 0
		if countB == 0 {
			if rest != 0 {
				continue
			}
		} else {
			if rest%countB != 0 {
				continue
			}
			lenB = rest / countB
		}

		pos := 0
		a, b := "", ""
		hasA, hasB := false, false
		ok := true
		for i := 0; i < len(pattern); i++ {
			if pattern[i] == 'a' {
				sub := value[pos : pos+lenA]
				if !hasA {
					a = sub
					hasA = true
				} else if a != sub {
					ok = false
					break
				}
				pos += lenA
			} else {
				sub := value[pos : pos+lenB]
				if !hasB {
					b = sub
					hasB = true
				} else if b != sub {
					ok = false
					break
				}
				pos += lenB
			}
		}
		if ok && a != b {
			return true
		}
	}
	return false
}

func main() {
	fmt.Println(patternMatching("abba", "dogcatcatdog"))
	fmt.Println(patternMatching("abba", "dogcatcatfish"))
}
```

<!-- REGISTRY_PATH: lcci_16_18_pattern_matching.languages.python -->
### python

```python
def pattern_matching(pattern: str, value: str) -> bool:
    if not pattern:
        return value == ""

    count_a = pattern.count("a")
    count_b = pattern.count("b")

    if count_a < count_b:
        swapped = "".join("b" if c == "a" else "a" for c in pattern)
        return pattern_matching(swapped, value)

    if value == "":
        return count_b == 0

    n = len(value)
    for len_a in range(0, n // count_a + 1):
        rest = n - count_a * len_a
        if count_b == 0:
            if rest != 0:
                continue
            len_b = 0
        else:
            if rest % count_b != 0:
                continue
            len_b = rest // count_b

        pos = 0
        a = None
        b = None
        ok = True
        for ch in pattern:
            if ch == "a":
                sub = value[pos:pos + len_a]
                if a is None:
                    a = sub
                elif a != sub:
                    ok = False
                    break
                pos += len_a
            else:
                sub = value[pos:pos + len_b]
                if b is None:
                    b = sub
                elif b != sub:
                    ok = False
                    break
                pos += len_b
        if ok and a != b:
            return True
    return False


def main() -> None:
    print(pattern_matching("abba", "dogcatcatdog"))
    print(pattern_matching("abba", "dogcatcatfish"))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_18_pattern_matching.languages.scala -->
### scala

```scala
object Lcci1618PatternMatching {
    def patternMatching(pattern: String, value: String): Boolean = {
        if (pattern.isEmpty) return value.isEmpty

        var countA = 0
        var countB = 0
        pattern.foreach(ch => if (ch == 'a') countA += 1 else countB += 1)

        if (countA < countB) {
            val swapped = pattern.map(ch => if (ch == 'a') 'b' else 'a')
            return patternMatching(swapped, value)
        }

        if (value.isEmpty) return countB == 0

        val n = value.length
        var lenA = 0
        while (countA * lenA <= n) {
            val rest = n - countA * lenA
            var lenB = 0
            var valid = true
            if (countB == 0) {
                if (rest != 0) valid = false
            } else {
                if (rest % countB != 0) valid = false
                else lenB = rest / countB
            }

            if (valid) {
                var pos = 0
                var a: String = null
                var b: String = null
                var ok = true
                pattern.foreach { ch =>
                    if (ok && ch == 'a') {
                        val sub = value.substring(pos, pos + lenA)
                        if (a == null) a = sub
                        else if (a != sub) ok = false
                        pos += lenA
                    } else if (ok) {
                        val sub = value.substring(pos, pos + lenB)
                        if (b == null) b = sub
                        else if (b != sub) ok = false
                        pos += lenB
                    }
                }
                if (ok && a != b) return true
            }
            lenA += 1
        }
        false
    }

    def main(args: Array[String]): Unit = {
        println(patternMatching("abba", "dogcatcatdog"))
        println(patternMatching("abba", "dogcatcatfish"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_18_pattern_matching.languages.typescript -->
### typescript

```typescript
function patternMatching(pattern: string, value: string): boolean {
    if (pattern.length === 0) return value.length === 0;

    let countA = 0;
    let countB = 0;
    for (const ch of pattern) {
        if (ch === "a") countA += 1;
        else countB += 1;
    }

    if (countA < countB) {
        const swapped = [...pattern].map((ch) => (ch === "a" ? "b" : "a")).join("");
        return patternMatching(swapped, value);
    }

    if (value.length === 0) return countB === 0;

    const n = value.length;
    for (let lenA = 0; countA * lenA <= n; lenA++) {
        const rest = n - countA * lenA;
        let lenB = 0;
        if (countB === 0) {
            if (rest !== 0) continue;
        } else {
            if (rest % countB !== 0) continue;
            lenB = rest / countB;
        }

        let pos = 0;
        let a: string | null = null;
        let b: string | null = null;
        let ok = true;
        for (const ch of pattern) {
            if (ch === "a") {
                const sub = value.slice(pos, pos + lenA);
                if (a === null) a = sub;
                else if (a !== sub) {
                    ok = false;
                    break;
                }
                pos += lenA;
            } else {
                const sub = value.slice(pos, pos + lenB);
                if (b === null) b = sub;
                else if (b !== sub) {
                    ok = false;
                    break;
                }
                pos += lenB;
            }
        }
        if (ok && a !== b) return true;
    }
    return false;
}

console.log(patternMatching("abba", "dogcatcatdog"));
console.log(patternMatching("abba", "dogcatcatfish"));
```

## lcci_16_19_pond_sizes

<!-- REGISTRY_PATH: lcci_16_19_pond_sizes.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int dfs(vector<vector<int>>& land, int r, int c) {
    int m = land.size(), n = land[0].size();
    if (r < 0 || r >= m || c < 0 || c >= n || land[r][c] != 0) return 0;
    land[r][c] = -1;
    int size = 1;
    for (int dr = -1; dr <= 1; ++dr) {
        for (int dc = -1; dc <= 1; ++dc) {
            if (dr != 0 || dc != 0) size += dfs(land, r + dr, c + dc);
        }
    }
    return size;
}

vector<int> pondSizes(vector<vector<int>> land) {
    vector<int> ans;
    int m = land.size(), n = land[0].size();
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (land[i][j] == 0) ans.push_back(dfs(land, i, j));
        }
    }
    sort(ans.begin(), ans.end());
    return ans;
}

int main() {
    vector<int> ans = pondSizes({{0, 2, 1, 0}, {0, 1, 0, 1}, {1, 1, 0, 1}, {0, 1, 0, 1}});
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << ans[i];
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_19_pond_sizes.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func pondSizes(land [][]int) []int {
	m, n := len(land), len(land[0])
	var dfs func(int, int) int
	dfs = func(r int, c int) int {
		if r < 0 || r >= m || c < 0 || c >= n || land[r][c] != 0 {
			return 0
		}
		land[r][c] = -1
		size := 1
		for dr := -1; dr <= 1; dr++ {
			for dc := -1; dc <= 1; dc++ {
				if dr != 0 || dc != 0 {
					size += dfs(r+dr, c+dc)
				}
			}
		}
		return size
	}

	ans := make([]int, 0)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if land[i][j] == 0 {
				ans = append(ans, dfs(i, j))
			}
		}
	}
	sort.Ints(ans)
	return ans
}

func main() {
	fmt.Println(pondSizes([][]int{{0, 2, 1, 0}, {0, 1, 0, 1}, {1, 1, 0, 1}, {0, 1, 0, 1}}))
}
```

<!-- REGISTRY_PATH: lcci_16_19_pond_sizes.languages.python -->
### python

```python
from typing import List


def pond_sizes(land: List[List[int]]) -> List[int]:
    m, n = len(land), len(land[0])

    def dfs(r: int, c: int) -> int:
        if r < 0 or r >= m or c < 0 or c >= n or land[r][c] != 0:
            return 0
        land[r][c] = -1
        size = 1
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr != 0 or dc != 0:
                    size += dfs(r + dr, c + dc)
        return size

    ans = []
    for i in range(m):
        for j in range(n):
            if land[i][j] == 0:
                ans.append(dfs(i, j))
    ans.sort()
    return ans


def main() -> None:
    print(pond_sizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_19_pond_sizes.languages.scala -->
### scala

```scala
object Lcci1619PondSizes {
    def pondSizes(land: Array[Array[Int]]): Array[Int] = {
        val m = land.length
        val n = land(0).length

        def dfs(r: Int, c: Int): Int = {
            if (r < 0 || r >= m || c < 0 || c >= n || land(r)(c) != 0) return 0
            land(r)(c) = -1
            var size = 1
            for (dr <- -1 to 1) {
                for (dc <- -1 to 1) {
                    if (dr != 0 || dc != 0) size += dfs(r + dr, c + dc)
                }
            }
            size
        }

        val ans = scala.collection.mutable.ArrayBuffer[Int]()
        for (i <- 0 until m; j <- 0 until n) {
            if (land(i)(j) == 0) ans += dfs(i, j)
        }
        ans.sorted.toArray
    }

    def main(args: Array[String]): Unit = {
        val land = Array(Array(0, 2, 1, 0), Array(0, 1, 0, 1), Array(1, 1, 0, 1), Array(0, 1, 0, 1))
        println(pondSizes(land).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_19_pond_sizes.languages.typescript -->
### typescript

```typescript
function pondSizes(land: number[][]): number[] {
    const m = land.length;
    const n = land[0].length;

    const dfs = (r: number, c: number): number => {
        if (r < 0 || r >= m || c < 0 || c >= n || land[r][c] !== 0) return 0;
        land[r][c] = -1;
        let size = 1;
        for (let dr = -1; dr <= 1; dr++) {
            for (let dc = -1; dc <= 1; dc++) {
                if (dr !== 0 || dc !== 0) size += dfs(r + dr, c + dc);
            }
        }
        return size;
    };

    const ans: number[] = [];
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (land[i][j] === 0) ans.push(dfs(i, j));
        }
    }
    ans.sort((a, b) => a - b);
    return ans;
}

console.log(pondSizes([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]));
```

## lcci_16_20_t9

<!-- REGISTRY_PATH: lcci_16_20_t9.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

char mapDigit(char ch) {
    if (ch <= 'c') return '2';
    if (ch <= 'f') return '3';
    if (ch <= 'i') return '4';
    if (ch <= 'l') return '5';
    if (ch <= 'o') return '6';
    if (ch <= 's') return '7';
    if (ch <= 'v') return '8';
    return '9';
}

vector<string> getValidT9Words(const string& num, const vector<string>& words) {
    vector<string> ans;
    for (const string& word : words) {
        if (word.size() != num.size()) continue;
        bool ok = true;
        for (int i = 0; i < static_cast<int>(word.size()); ++i) {
            if (mapDigit(word[i]) != num[i]) {
                ok = false;
                break;
            }
        }
        if (ok) ans.push_back(word);
    }
    return ans;
}

int main() {
    vector<string> ans = getValidT9Words("8733", {"tree", "used", "true"});
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << ans[i];
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_20_t9.languages.go -->
### go

```go
package main

import "fmt"

func mapDigit(ch byte) byte {
	switch {
	case ch <= 'c':
		return '2'
	case ch <= 'f':
		return '3'
	case ch <= 'i':
		return '4'
	case ch <= 'l':
		return '5'
	case ch <= 'o':
		return '6'
	case ch <= 's':
		return '7'
	case ch <= 'v':
		return '8'
	default:
		return '9'
	}
}

func getValidT9Words(num string, words []string) []string {
	ans := make([]string, 0)
	for _, word := range words {
		if len(word) != len(num) {
			continue
		}
		ok := true
		for i := 0; i < len(word); i++ {
			if mapDigit(word[i]) != num[i] {
				ok = false
				break
			}
		}
		if ok {
			ans = append(ans, word)
		}
	}
	return ans
}

func main() {
	fmt.Println(getValidT9Words("8733", []string{"tree", "used", "true"}))
}
```

<!-- REGISTRY_PATH: lcci_16_20_t9.languages.python -->
### python

```python
from typing import List


def map_digit(ch: str) -> str:
    if ch <= "c":
        return "2"
    if ch <= "f":
        return "3"
    if ch <= "i":
        return "4"
    if ch <= "l":
        return "5"
    if ch <= "o":
        return "6"
    if ch <= "s":
        return "7"
    if ch <= "v":
        return "8"
    return "9"


def get_valid_t9_words(num: str, words: List[str]) -> List[str]:
    ans = []
    for word in words:
        if len(word) != len(num):
            continue
        if all(map_digit(word[i]) == num[i] for i in range(len(word))):
            ans.append(word)
    return ans


def main() -> None:
    print(get_valid_t9_words("8733", ["tree", "used", "true"]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_20_t9.languages.scala -->
### scala

```scala
object Lcci1620T9 {
    private def mapDigit(ch: Char): Char = {
        if (ch <= 'c') '2'
        else if (ch <= 'f') '3'
        else if (ch <= 'i') '4'
        else if (ch <= 'l') '5'
        else if (ch <= 'o') '6'
        else if (ch <= 's') '7'
        else if (ch <= 'v') '8'
        else '9'
    }

    def getValidT9Words(num: String, words: Array[String]): Array[String] = {
        words.filter { word =>
            word.length == num.length && word.indices.forall(i => mapDigit(word(i)) == num(i))
        }
    }

    def main(args: Array[String]): Unit = {
        println(getValidT9Words("8733", Array("tree", "used", "true")).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_20_t9.languages.typescript -->
### typescript

```typescript
function mapDigit(ch: string): string {
    if (ch <= "c") return "2";
    if (ch <= "f") return "3";
    if (ch <= "i") return "4";
    if (ch <= "l") return "5";
    if (ch <= "o") return "6";
    if (ch <= "s") return "7";
    if (ch <= "v") return "8";
    return "9";
}

function getValidT9Words(num: string, words: string[]): string[] {
    const ans: string[] = [];
    for (const word of words) {
        if (word.length !== num.length) continue;
        let ok = true;
        for (let i = 0; i < word.length; i++) {
            if (mapDigit(word[i]) !== num[i]) {
                ok = false;
                break;
            }
        }
        if (ok) ans.push(word);
    }
    return ans;
}

console.log(getValidT9Words("8733", ["tree", "used", "true"]));
```

## lcci_16_21_sum_swap

<!-- REGISTRY_PATH: lcci_16_21_sum_swap.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

vector<int> findSwapValues(const vector<int>& array1, const vector<int>& array2) {
    long long sum1 = 0, sum2 = 0;
    for (int x : array1) sum1 += x;
    for (int x : array2) sum2 += x;

    long long diff = sum1 - sum2;
    if (diff % 2 != 0) return {};
    long long target = diff / 2;

    unordered_set<long long> set2;
    for (int y : array2) set2.insert(y);

    for (int x : array1) {
        long long y = x - target;
        if (set2.count(y)) return {x, static_cast<int>(y)};
    }
    return {};
}

int main() {
    vector<int> ans = findSwapValues({4, 1, 2, 1, 1, 2}, {3, 6, 3, 3});
    if (ans.empty()) cout << "[]" << endl;
    else cout << "[" << ans[0] << ", " << ans[1] << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_21_sum_swap.languages.go -->
### go

```go
package main

import "fmt"

func findSwapValues(array1 []int, array2 []int) []int {
	sum1, sum2 := 0, 0
	for _, x := range array1 {
		sum1 += x
	}
	for _, y := range array2 {
		sum2 += y
	}
	diff := sum1 - sum2
	if diff%2 != 0 {
		return []int{}
	}
	target := diff / 2

	set2 := map[int]bool{}
	for _, y := range array2 {
		set2[y] = true
	}
	for _, x := range array1 {
		y := x - target
		if set2[y] {
			return []int{x, y}
		}
	}
	return []int{}
}

func main() {
	fmt.Println(findSwapValues([]int{4, 1, 2, 1, 1, 2}, []int{3, 6, 3, 3}))
}
```

<!-- REGISTRY_PATH: lcci_16_21_sum_swap.languages.python -->
### python

```python
from typing import List


def find_swap_values(array1: List[int], array2: List[int]) -> List[int]:
    diff = sum(array1) - sum(array2)
    if diff % 2 != 0:
        return []
    target = diff // 2
    set2 = set(array2)
    for x in array1:
        y = x - target
        if y in set2:
            return [x, y]
    return []


def main() -> None:
    print(find_swap_values([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_21_sum_swap.languages.scala -->
### scala

```scala
object Lcci1621SumSwap {
    def findSwapValues(array1: Array[Int], array2: Array[Int]): Array[Int] = {
        val diff = array1.sum - array2.sum
        if (diff % 2 != 0) return Array.emptyIntArray
        val target = diff / 2
        val set2 = array2.toSet
        array1.foreach { x =>
            val y = x - target
            if (set2.contains(y)) return Array(x, y)
        }
        Array.emptyIntArray
    }

    def main(args: Array[String]): Unit = {
        println(findSwapValues(Array(4, 1, 2, 1, 1, 2), Array(3, 6, 3, 3)).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_21_sum_swap.languages.typescript -->
### typescript

```typescript
function findSwapValues(array1: number[], array2: number[]): number[] {
    const sum1 = array1.reduce((a, b) => a + b, 0);
    const sum2 = array2.reduce((a, b) => a + b, 0);
    const diff = sum1 - sum2;
    if (diff % 2 !== 0) return [];
    const target = diff / 2;

    const set2 = new Set(array2);
    for (const x of array1) {
        const y = x - target;
        if (set2.has(y)) return [x, y];
    }
    return [];
}

console.log(findSwapValues([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]));
```

## lcci_16_22_langtons_ant

<!-- REGISTRY_PATH: lcci_16_22_langtons_ant.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;

string key(int r, int c) {
    return to_string(r) + "#" + to_string(c);
}

vector<string> printKMoves(int k) {
    int r = 0, c = 0, dir = 0;
    vector<int> dr = {0, 1, 0, -1};
    vector<int> dc = {1, 0, -1, 0};
    string dirs = "RDLU";

    unordered_set<string> black;
    int minR = 0, maxR = 0, minC = 0, maxC = 0;

    for (int step = 0; step < k; ++step) {
        string cur = key(r, c);
        if (black.count(cur)) {
            black.erase(cur);
            dir = (dir + 3) % 4;
        } else {
            black.insert(cur);
            dir = (dir + 1) % 4;
        }
        r += dr[dir];
        c += dc[dir];
        minR = min(minR, r);
        maxR = max(maxR, r);
        minC = min(minC, c);
        maxC = max(maxC, c);
    }

    for (const string& p : black) {
        size_t pos = p.find('#');
        int br = stoi(p.substr(0, pos));
        int bc = stoi(p.substr(pos + 1));
        minR = min(minR, br);
        maxR = max(maxR, br);
        minC = min(minC, bc);
        maxC = max(maxC, bc);
    }

    vector<string> board;
    for (int i = minR; i <= maxR; ++i) {
        string row;
        for (int j = minC; j <= maxC; ++j) {
            if (i == r && j == c) row.push_back(dirs[dir]);
            else if (black.count(key(i, j))) row.push_back('X');
            else row.push_back('_');
        }
        board.push_back(row);
    }
    return board;
}

int main() {
    vector<string> board = printKMoves(2);
    cout << "[";
    for (int i = 0; i < static_cast<int>(board.size()); ++i) {
        if (i) cout << ", ";
        cout << board[i];
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_22_langtons_ant.languages.go -->
### go

```go
package main

import "fmt"

func key(r int, c int) string {
	return fmt.Sprintf("%d#%d", r, c)
}

func printKMoves(k int) []string {
	r, c, dir := 0, 0, 0
	dr := []int{0, 1, 0, -1}
	dc := []int{1, 0, -1, 0}
	dirs := "RDLU"

	black := map[string]bool{}
	minR, maxR, minC, maxC := 0, 0, 0, 0

	for step := 0; step < k; step++ {
		cur := key(r, c)
		if black[cur] {
			delete(black, cur)
			dir = (dir + 3) % 4
		} else {
			black[cur] = true
			dir = (dir + 1) % 4
		}
		r += dr[dir]
		c += dc[dir]
		if r < minR {
			minR = r
		}
		if r > maxR {
			maxR = r
		}
		if c < minC {
			minC = c
		}
		if c > maxC {
			maxC = c
		}
	}

	for p := range black {
		var br, bc int
		fmt.Sscanf(p, "%d#%d", &br, &bc)
		if br < minR {
			minR = br
		}
		if br > maxR {
			maxR = br
		}
		if bc < minC {
			minC = bc
		}
		if bc > maxC {
			maxC = bc
		}
	}

	board := make([]string, 0, maxR-minR+1)
	for i := minR; i <= maxR; i++ {
		row := make([]byte, 0, maxC-minC+1)
		for j := minC; j <= maxC; j++ {
			if i == r && j == c {
				row = append(row, dirs[dir])
			} else if black[key(i, j)] {
				row = append(row, 'X')
			} else {
				row = append(row, '_')
			}
		}
		board = append(board, string(row))
	}
	return board
}

func main() {
	fmt.Println(printKMoves(2))
}
```

<!-- REGISTRY_PATH: lcci_16_22_langtons_ant.languages.python -->
### python

```python
from typing import List, Set, Tuple


def print_k_moves(k: int) -> List[str]:
    r = c = 0
    dir_idx = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    dirs = "RDLU"

    black: Set[Tuple[int, int]] = set()
    min_r = max_r = 0
    min_c = max_c = 0

    for _ in range(k):
        cur = (r, c)
        if cur in black:
            black.remove(cur)
            dir_idx = (dir_idx + 3) % 4
        else:
            black.add(cur)
            dir_idx = (dir_idx + 1) % 4
        r += dr[dir_idx]
        c += dc[dir_idx]
        min_r = min(min_r, r)
        max_r = max(max_r, r)
        min_c = min(min_c, c)
        max_c = max(max_c, c)

    for br, bc in black:
        min_r = min(min_r, br)
        max_r = max(max_r, br)
        min_c = min(min_c, bc)
        max_c = max(max_c, bc)

    board = []
    for i in range(min_r, max_r + 1):
        row = []
        for j in range(min_c, max_c + 1):
            if (i, j) == (r, c):
                row.append(dirs[dir_idx])
            elif (i, j) in black:
                row.append("X")
            else:
                row.append("_")
        board.append("".join(row))
    return board


def main() -> None:
    print(print_k_moves(2))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_22_langtons_ant.languages.scala -->
### scala

```scala
object Lcci1622LangtonsAnt {
    private def key(r: Int, c: Int): String = s"$r#$c"

    def printKMoves(k: Int): Array[String] = {
        var r = 0
        var c = 0
        var dir = 0
        val dr = Array(0, 1, 0, -1)
        val dc = Array(1, 0, -1, 0)
        val dirs = "RDLU"

        val black = scala.collection.mutable.Set[String]()
        var minR = 0
        var maxR = 0
        var minC = 0
        var maxC = 0

        for (_ <- 0 until k) {
            val cur = key(r, c)
            if (black.contains(cur)) {
                black -= cur
                dir = (dir + 3) % 4
            } else {
                black += cur
                dir = (dir + 1) % 4
            }
            r += dr(dir)
            c += dc(dir)
            minR = math.min(minR, r)
            maxR = math.max(maxR, r)
            minC = math.min(minC, c)
            maxC = math.max(maxC, c)
        }

        black.foreach { p =>
            val parts = p.split("#")
            val br = parts(0).toInt
            val bc = parts(1).toInt
            minR = math.min(minR, br)
            maxR = math.max(maxR, br)
            minC = math.min(minC, bc)
            maxC = math.max(maxC, bc)
        }

        val board = scala.collection.mutable.ArrayBuffer[String]()
        for (i <- minR to maxR) {
            val row = new StringBuilder
            for (j <- minC to maxC) {
                if (i == r && j == c) row += dirs(dir)
                else if (black.contains(key(i, j))) row += 'X'
                else row += '_'
            }
            board += row.toString
        }
        board.toArray
    }

    def main(args: Array[String]): Unit = {
        println(printKMoves(2).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_22_langtons_ant.languages.typescript -->
### typescript

```typescript
function key(r: number, c: number): string {
    return `${r}#${c}`;
}

function printKMoves(k: number): string[] {
    let r = 0;
    let c = 0;
    let dir = 0;
    const dr = [0, 1, 0, -1];
    const dc = [1, 0, -1, 0];
    const dirs = "RDLU";

    const black = new Set<string>();
    let minR = 0;
    let maxR = 0;
    let minC = 0;
    let maxC = 0;

    for (let step = 0; step < k; step++) {
        const cur = key(r, c);
        if (black.has(cur)) {
            black.delete(cur);
            dir = (dir + 3) % 4;
        } else {
            black.add(cur);
            dir = (dir + 1) % 4;
        }
        r += dr[dir];
        c += dc[dir];
        minR = Math.min(minR, r);
        maxR = Math.max(maxR, r);
        minC = Math.min(minC, c);
        maxC = Math.max(maxC, c);
    }

    for (const p of black) {
        const [br, bc] = p.split("#").map(Number);
        minR = Math.min(minR, br);
        maxR = Math.max(maxR, br);
        minC = Math.min(minC, bc);
        maxC = Math.max(maxC, bc);
    }

    const board: string[] = [];
    for (let i = minR; i <= maxR; i++) {
        let row = "";
        for (let j = minC; j <= maxC; j++) {
            if (i === r && j === c) row += dirs[dir];
            else if (black.has(key(i, j))) row += "X";
            else row += "_";
        }
        board.push(row);
    }
    return board;
}

console.log(printKMoves(2));
```

## lcci_16_24_pairs_with_sum

<!-- REGISTRY_PATH: lcci_16_24_pairs_with_sum.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

vector<vector<int>> pairSums(const vector<int>& nums, int target) {
    unordered_map<int, int> freq;
    vector<vector<int>> ans;
    for (int x : nums) {
        int y = target - x;
        if (freq[y] > 0) {
            --freq[y];
            ans.push_back({min(x, y), max(x, y)});
        } else {
            ++freq[x];
        }
    }
    return ans;
}

int main() {
    vector<vector<int>> ans = pairSums({5, 6, 5}, 11);
    cout << "[";
    for (int i = 0; i < static_cast<int>(ans.size()); ++i) {
        if (i) cout << ", ";
        cout << "[" << ans[i][0] << ", " << ans[i][1] << "]";
    }
    cout << "]" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_24_pairs_with_sum.languages.go -->
### go

```go
package main

import "fmt"

func pairSums(nums []int, target int) [][]int {
	freq := map[int]int{}
	ans := make([][]int, 0)
	for _, x := range nums {
		y := target - x
		if freq[y] > 0 {
			freq[y]--
			a, b := x, y
			if a > b {
				a, b = b, a
			}
			ans = append(ans, []int{a, b})
		} else {
			freq[x]++
		}
	}
	return ans
}

func main() {
	fmt.Println(pairSums([]int{5, 6, 5}, 11))
}
```

<!-- REGISTRY_PATH: lcci_16_24_pairs_with_sum.languages.python -->
### python

```python
from collections import defaultdict
from typing import List


def pair_sums(nums: List[int], target: int) -> List[List[int]]:
    freq: dict[int, int] = defaultdict(int)
    ans = []
    for x in nums:
        y = target - x
        if freq[y] > 0:
            freq[y] -= 1
            ans.append([min(x, y), max(x, y)])
        else:
            freq[x] += 1
    return ans


def main() -> None:
    print(pair_sums([5, 6, 5], 11))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_24_pairs_with_sum.languages.scala -->
### scala

```scala
object Lcci1624PairsWithSum {
    def pairSums(nums: Array[Int], target: Int): Array[Array[Int]] = {
        val freq = scala.collection.mutable.Map[Int, Int]().withDefaultValue(0)
        val ans = scala.collection.mutable.ArrayBuffer[Array[Int]]()
        nums.foreach { x =>
            val y = target - x
            if (freq(y) > 0) {
                freq(y) = freq(y) - 1
                ans += Array(math.min(x, y), math.max(x, y))
            } else {
                freq(x) = freq(x) + 1
            }
        }
        ans.toArray
    }

    def main(args: Array[String]): Unit = {
        println(pairSums(Array(5, 6, 5), 11).map(_.mkString("[", ", ", "]")).mkString("[", ", ", "]"))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_24_pairs_with_sum.languages.typescript -->
### typescript

```typescript
function pairSums(nums: number[], target: number): number[][] {
    const freq = new Map<number, number>();
    const ans: number[][] = [];
    for (const x of nums) {
        const y = target - x;
        const cnt = freq.get(y) ?? 0;
        if (cnt > 0) {
            freq.set(y, cnt - 1);
            ans.push([Math.min(x, y), Math.max(x, y)]);
        } else {
            freq.set(x, (freq.get(x) ?? 0) + 1);
        }
    }
    return ans;
}

console.log(pairSums([5, 6, 5], 11));
```

## lcci_16_25_lru_cache

<!-- REGISTRY_PATH: lcci_16_25_lru_cache.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <list>
#include <unordered_map>
using namespace std;

class LRUCache {
public:
    explicit LRUCache(int capacity) : cap(capacity) {}

    int get(int key) {
        auto it = pos.find(key);
        if (it == pos.end()) return -1;
        items.splice(items.begin(), items, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = pos.find(key);
        if (it != pos.end()) {
            it->second->second = value;
            items.splice(items.begin(), items, it->second);
            return;
        }
        if (static_cast<int>(items.size()) == cap) {
            int old = items.back().first;
            items.pop_back();
            pos.erase(old);
        }
        items.push_front({key, value});
        pos[key] = items.begin();
    }

private:
    int cap;
    list<pair<int, int>> items;
    unordered_map<int, list<pair<int, int>>::iterator> pos;
};

int main() {
    LRUCache cache(2);
    cache.put(1, 1);
    cache.put(2, 2);
    cout << cache.get(1) << endl;
    cache.put(3, 3);
    cout << cache.get(2) << endl;
    cache.put(4, 4);
    cout << cache.get(1) << endl;
    cout << cache.get(3) << endl;
    cout << cache.get(4) << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_25_lru_cache.languages.go -->
### go

```go
package main

import (
	"container/list"
	"fmt"
)

type node struct {
	key int
	val int
}

type LRUCache struct {
	cap  int
	list *list.List
	pos  map[int]*list.Element
}

func Constructor(capacity int) LRUCache {
	return LRUCache{cap: capacity, list: list.New(), pos: map[int]*list.Element{}}
}

func (c *LRUCache) Get(key int) int {
	if e, ok := c.pos[key]; ok {
		c.list.MoveToFront(e)
		return e.Value.(node).val
	}
	return -1
}

func (c *LRUCache) Put(key int, value int) {
	if e, ok := c.pos[key]; ok {
		e.Value = node{key: key, val: value}
		c.list.MoveToFront(e)
		return
	}
	if c.list.Len() == c.cap {
		tail := c.list.Back()
		delete(c.pos, tail.Value.(node).key)
		c.list.Remove(tail)
	}
	e := c.list.PushFront(node{key: key, val: value})
	c.pos[key] = e
}

func main() {
	cache := Constructor(2)
	cache.Put(1, 1)
	cache.Put(2, 2)
	fmt.Println(cache.Get(1))
	cache.Put(3, 3)
	fmt.Println(cache.Get(2))
	cache.Put(4, 4)
	fmt.Println(cache.Get(1))
	fmt.Println(cache.Get(3))
	fmt.Println(cache.Get(4))
}
```

<!-- REGISTRY_PATH: lcci_16_25_lru_cache.languages.python -->
### python

```python
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data: OrderedDict[int, int] = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value
        if len(self.data) > self.capacity:
            self.data.popitem(last=False)


def main() -> None:
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_25_lru_cache.languages.scala -->
### scala

```scala
object Lcci1625LruCache {
    final class LRUCache(capacity: Int) {
        private val data = scala.collection.mutable.LinkedHashMap[Int, Int]()

        def get(key: Int): Int = {
            data.get(key) match {
                case None => -1
                case Some(v) =>
                    data -= key
                    data += (key -> v)
                    v
            }
        }

        def put(key: Int, value: Int): Unit = {
            if (data.contains(key)) data -= key
            data += (key -> value)
            if (data.size > capacity) {
                val oldest = data.head._1
                data -= oldest
            }
        }
    }

    def main(args: Array[String]): Unit = {
        val cache = new LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        println(cache.get(1))
        cache.put(3, 3)
        println(cache.get(2))
        cache.put(4, 4)
        println(cache.get(1))
        println(cache.get(3))
        println(cache.get(4))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_25_lru_cache.languages.typescript -->
### typescript

```typescript
class DLinkedNode {
    key: number;
    val: number;
    prev: DLinkedNode | null = null;
    next: DLinkedNode | null = null;

    constructor(key: number, val: number) {
        this.key = key;
        this.val = val;
    }
}

class LRUCache {
    private readonly capacity: number;
    private readonly map = new Map<number, DLinkedNode>();
    private readonly head = new DLinkedNode(0, 0);
    private readonly tail = new DLinkedNode(0, 0);

    constructor(capacity: number) {
        this.capacity = capacity;
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    private remove(node: DLinkedNode): void {
        node.prev!.next = node.next;
        node.next!.prev = node.prev;
    }

    private addFront(node: DLinkedNode): void {
        node.next = this.head.next;
        node.prev = this.head;
        this.head.next!.prev = node;
        this.head.next = node;
    }

    get(key: number): number {
        const node = this.map.get(key);
        if (!node) return -1;
        this.remove(node);
        this.addFront(node);
        return node.val;
    }

    put(key: number, value: number): void {
        const node = this.map.get(key);
        if (node) {
            node.val = value;
            this.remove(node);
            this.addFront(node);
            return;
        }
        if (this.map.size === this.capacity) {
            const lru = this.tail.prev!;
            this.remove(lru);
            this.map.delete(lru.key);
        }
        const fresh = new DLinkedNode(key, value);
        this.addFront(fresh);
        this.map.set(key, fresh);
    }
}

const cache = new LRUCache(2);
cache.put(1, 1);
cache.put(2, 2);
console.log(cache.get(1));
cache.put(3, 3);
console.log(cache.get(2));
cache.put(4, 4);
console.log(cache.get(1));
console.log(cache.get(3));
console.log(cache.get(4));
```

## lcci_16_26_calculator

<!-- REGISTRY_PATH: lcci_16_26_calculator.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int calculate(const string& s) {
    vector<int> st;
    int n = s.size();
    long long num = 0;
    char op = '+';
    for (int i = 0; i <= n; ++i) {
        char ch = (i < n ? s[i] : '+');
        if (ch == ' ') continue;
        if (isdigit(ch)) {
            num = num * 10 + (ch - '0');
            continue;
        }
        if (op == '+') st.push_back(static_cast<int>(num));
        else if (op == '-') st.push_back(static_cast<int>(-num));
        else if (op == '*') {
            int v = st.back(); st.pop_back();
            st.push_back(v * static_cast<int>(num));
        } else {
            int v = st.back(); st.pop_back();
            st.push_back(v / static_cast<int>(num));
        }
        op = ch;
        num = 0;
    }
    int ans = 0;
    for (int v : st) ans += v;
    return ans;
}

int main() {
    cout << calculate("3+2*2") << endl;
    cout << calculate(" 3/2 ") << endl;
    cout << calculate(" 3+5 / 2 ") << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_16_26_calculator.languages.go -->
### go

```go
package main

import "fmt"

func calculate(s string) int {
	st := make([]int, 0)
	num := 0
	op := byte('+')
	for i := 0; i <= len(s); i++ {
		ch := byte('+')
		if i < len(s) {
			ch = s[i]
		}
		if ch == ' ' {
			continue
		}
		if ch >= '0' && ch <= '9' {
			num = num*10 + int(ch-'0')
			continue
		}
		switch op {
		case '+':
			st = append(st, num)
		case '-':
			st = append(st, -num)
		case '*':
			st[len(st)-1] = st[len(st)-1] * num
		case '/':
			st[len(st)-1] = st[len(st)-1] / num
		}
		op = ch
		num = 0
	}
	ans := 0
	for _, v := range st {
		ans += v
	}
	return ans
}

func main() {
	fmt.Println(calculate("3+2*2"))
	fmt.Println(calculate(" 3/2 "))
	fmt.Println(calculate(" 3+5 / 2 "))
}
```

<!-- REGISTRY_PATH: lcci_16_26_calculator.languages.python -->
### python

```python
def calculate(s: str) -> int:
    st = []
    num = 0
    op = "+"
    for ch in s + "+":
        if ch == " ":
            continue
        if ch.isdigit():
            num = num * 10 + int(ch)
            continue
        if op == "+":
            st.append(num)
        elif op == "-":
            st.append(-num)
        elif op == "*":
            st.append(st.pop() * num)
        else:
            st.append(int(st.pop() / num))
        op = ch
        num = 0
    return sum(st)


def main() -> None:
    print(calculate("3+2*2"))
    print(calculate(" 3/2 "))
    print(calculate(" 3+5 / 2 "))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_16_26_calculator.languages.scala -->
### scala

```scala
object Lcci1626Calculator {
    def calculate(s: String): Int = {
        val st = scala.collection.mutable.ArrayBuffer[Int]()
        var num = 0
        var op = '+'
        val str = s + "+"
        str.foreach { ch =>
            if (ch != ' ') {
                if (ch.isDigit) {
                    num = num * 10 + (ch - '0')
                } else {
                    op match {
                        case '+' => st += num
                        case '-' => st += -num
                        case '*' => st(st.length - 1) = st.last * num
                        case '/' => st(st.length - 1) = st.last / num
                    }
                    op = ch
                    num = 0
                }
            }
        }
        st.sum
    }

    def main(args: Array[String]): Unit = {
        println(calculate("3+2*2"))
        println(calculate(" 3/2 "))
        println(calculate(" 3+5 / 2 "))
    }
}
```

<!-- REGISTRY_PATH: lcci_16_26_calculator.languages.typescript -->
### typescript

```typescript
function calculate(s: string): number {
    const st: number[] = [];
    let num = 0;
    let op = "+";
    for (let i = 0; i <= s.length; i++) {
        const ch = i < s.length ? s[i] : "+";
        if (ch === " ") continue;
        if (ch >= "0" && ch <= "9") {
            num = num * 10 + Number(ch);
            continue;
        }
        if (op === "+") st.push(num);
        else if (op === "-") st.push(-num);
        else if (op === "*") st.push(st.pop()! * num);
        else st.push(Math.trunc(st.pop()! / num));
        op = ch;
        num = 0;
    }
    return st.reduce((a, b) => a + b, 0);
}

console.log(calculate("3+2*2"));
console.log(calculate(" 3/2 "));
console.log(calculate(" 3+5 / 2 "));
```

## lcci_17_01_add_without_plus

<!-- REGISTRY_PATH: lcci_17_01_add_without_plus.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int add(int a, int b) {
        while (b != 0) {
            unsigned int carry = (unsigned int)(a & b) << 1;
            a = a ^ b;
            b = (int)carry;
        }
        return a;
    }
};

int main() {
    Solution sol;
    cout << sol.add(1, 2) << endl;    // 3
    cout << sol.add(3, -2) << endl;   // 1
    cout << sol.add(-1, -2) << endl;  // -3
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_01_add_without_plus.languages.go -->
### go

```go
package main

import "fmt"

func add(a int, b int) int {
	for b != 0 {
		carry := uint(a&b) << 1
		a = a ^ b
		b = int(carry)
	}
	return a
}

func main() {
	fmt.Println(add(1, 2))   // 3
	fmt.Println(add(3, -2))  // 1
	fmt.Println(add(-1, -2)) // -3
}
```

<!-- REGISTRY_PATH: lcci_17_01_add_without_plus.languages.python -->
### python

```python
class Solution:
    def add(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        while b & mask:
            carry = ((a & b) & mask) << 1
            a = (a ^ b) & mask
            b = carry
        return a if b == 0 else a | ~mask


def main():
    sol = Solution()
    print(sol.add(1, 2))    # 3
    print(sol.add(3, -2))   # 1
    print(sol.add(-1, -2))  # -3


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_01_add_without_plus.languages.scala -->
### scala

```scala
object Lcci1701AddWithoutPlus {
  def add(a: Int, b: Int): Int = {
    var x = a
    var y = b
    while (y != 0) {
      val carry = (x & y) << 1
      x = x ^ y
      y = carry
    }
    x
  }

  def main(args: Array[String]): Unit = {
    println(add(1, 2))    // 3
    println(add(3, -2))   // 1
    println(add(-1, -2))  // -3
  }
}
```

<!-- REGISTRY_PATH: lcci_17_01_add_without_plus.languages.typescript -->
### typescript

```typescript
function add(a: number, b: number): number {
    while (b !== 0) {
        const carry = (a & b) << 1;
        a = a ^ b;
        b = carry;
    }
    return a;
}

console.log(add(1, 2));    // 3
console.log(add(3, -2));   // 1
console.log(add(-1, -2));  // -3
```

## lcci_17_04_missing_number

<!-- REGISTRY_PATH: lcci_17_04_missing_number.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int ans = 0;
        for (int i = 1; i <= (int)nums.size(); i++) {
            ans ^= i;
        }
        for (int x : nums) {
            ans ^= x;
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {3, 0, 1};
    cout << sol.missingNumber(nums1) << endl;  // 2

    vector<int> nums2 = {9, 6, 4, 2, 3, 5, 7, 0, 1};
    cout << sol.missingNumber(nums2) << endl;  // 8
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_04_missing_number.languages.go -->
### go

```go
package main

import "fmt"

func missingNumber(nums []int) int {
	ans := 0
	for i, x := range nums {
		ans ^= (i + 1) ^ x
	}
	return ans
}

func main() {
	fmt.Println(missingNumber([]int{3, 0, 1}))                   // 2
	fmt.Println(missingNumber([]int{9, 6, 4, 2, 3, 5, 7, 0, 1})) // 8
}
```

<!-- REGISTRY_PATH: lcci_17_04_missing_number.languages.python -->
### python

```python
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0
        for i, x in enumerate(nums, 1):
            ans ^= i ^ x
        return ans


def main():
    sol = Solution()
    print(sol.missingNumber([3, 0, 1]))              # 2
    print(sol.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_04_missing_number.languages.scala -->
### scala

```scala
object Lcci1704MissingNumber {
  def missingNumber(nums: Array[Int]): Int = {
    var ans = 0
    for (i <- 1 to nums.length) ans ^= i
    for (x <- nums) ans ^= x
    ans
  }

  def main(args: Array[String]): Unit = {
    println(missingNumber(Array(3, 0, 1)))                   // 2
    println(missingNumber(Array(9, 6, 4, 2, 3, 5, 7, 0, 1))) // 8
  }
}
```

<!-- REGISTRY_PATH: lcci_17_04_missing_number.languages.typescript -->
### typescript

```typescript
function missingNumber(nums: number[]): number {
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        ans ^= (i + 1) ^ nums[i];
    }
    return ans;
}

console.log(missingNumber([3, 0, 1]));                   // 2
console.log(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1])); // 8
```

## lcci_17_05_find_longest_subarray

<!-- REGISTRY_PATH: lcci_17_05_find_longest_subarray.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<string> findLongestSubarray(vector<string>& array) {
        unordered_map<int, int> first;
        first[0] = -1;
        int s = 0, maxLen = 0, start = 0;
        for (int i = 0; i < (int)array.size(); i++) {
            s += isalpha(array[i][0]) ? 1 : -1;
            if (first.count(s)) {
                int len = i - first[s];
                if (len > maxLen) {
                    maxLen = len;
                    start = first[s] + 1;
                }
            } else {
                first[s] = i;
            }
        }
        return vector<string>(array.begin() + start, array.begin() + start + maxLen);
    }
};

int main() {
    Solution sol;
    vector<string> arr1 = {"A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"};
    auto res1 = sol.findLongestSubarray(arr1);
    for (auto& s : res1) cout << s << " ";
    cout << endl;

    vector<string> arr2 = {"A","A"};
    auto res2 = sol.findLongestSubarray(arr2);
    if (res2.empty()) cout << "(empty)" << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_05_find_longest_subarray.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func findLongestSubarray(array []string) []string {
	first := map[int]int{0: -1}
	s, maxLen, start := 0, 0, 0
	for i, x := range array {
		if unicode.IsLetter(rune(x[0])) {
			s++
		} else {
			s--
		}
		if idx, ok := first[s]; ok {
			if length := i - idx; length > maxLen {
				maxLen = length
				start = idx + 1
			}
		} else {
			first[s] = i
		}
	}
	return array[start : start+maxLen]
}

func main() {
	arr1 := []string{"A", "1", "B", "C", "D", "2", "3", "4", "E", "5", "F", "G", "6", "7", "H", "I", "J", "K", "L", "M"}
	fmt.Println(strings.Join(findLongestSubarray(arr1), " ")) // A 1 B C D 2 3 4 E 5 F G 6 7

	arr2 := []string{"A", "A"}
	res2 := findLongestSubarray(arr2)
	if len(res2) == 0 {
		fmt.Println("(empty)")
	} else {
		fmt.Println(strings.Join(res2, " "))
	}
}
```

<!-- REGISTRY_PATH: lcci_17_05_find_longest_subarray.languages.python -->
### python

```python
from typing import List


class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        first = {0: -1}
        s = 0
        max_len = 0
        start = 0
        for i, x in enumerate(array):
            s += 1 if x[0].isalpha() else -1
            if s in first:
                length = i - first[s]
                if length > max_len:
                    max_len = length
                    start = first[s] + 1
            else:
                first[s] = i
        return array[start:start + max_len]


def main():
    sol = Solution()
    arr1 = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"]
    print(' '.join(sol.findLongestSubarray(arr1)))  # A 1 B C D 2 3 4 E 5 F G 6 7

    arr2 = ["A", "A"]
    res2 = sol.findLongestSubarray(arr2)
    print("(empty)" if not res2 else ' '.join(res2))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_05_find_longest_subarray.languages.scala -->
### scala

```scala
object Lcci1705FindLongestSubarray {
  def findLongestSubarray(array: Array[String]): Array[String] = {
    val first = scala.collection.mutable.Map(0 -> -1)
    var s = 0
    var maxLen = 0
    var start = 0
    for (i <- array.indices) {
      s += (if (array(i)(0).isLetter) 1 else -1)
      if (first.contains(s)) {
        val length = i - first(s)
        if (length > maxLen) {
          maxLen = length
          start = first(s) + 1
        }
      } else {
        first(s) = i
      }
    }
    array.slice(start, start + maxLen)
  }

  def main(args: Array[String]): Unit = {
    val arr1 = Array("A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M")
    println(findLongestSubarray(arr1).mkString(" ")) // A 1 B C D 2 3 4 E 5 F G 6 7

    val arr2 = Array("A", "A")
    val res2 = findLongestSubarray(arr2)
    println(if (res2.isEmpty) "(empty)" else res2.mkString(" "))
  }
}
```

<!-- REGISTRY_PATH: lcci_17_05_find_longest_subarray.languages.typescript -->
### typescript

```typescript
function findLongestSubarray(array: string[]): string[] {
    const first = new Map<number, number>();
    first.set(0, -1);
    let s = 0, maxLen = 0, start = 0;
    for (let i = 0; i < array.length; i++) {
        s += /[a-zA-Z]/.test(array[i]) ? 1 : -1;
        if (first.has(s)) {
            const length = i - first.get(s)!;
            if (length > maxLen) {
                maxLen = length;
                start = first.get(s)! + 1;
            }
        } else {
            first.set(s, i);
        }
    }
    return array.slice(start, start + maxLen);
}

const arr1 = ["A","1","B","C","D","2","3","4","E","5","F","G","6","7","H","I","J","K","L","M"];
console.log(findLongestSubarray(arr1).join(' ')); // A 1 B C D 2 3 4 E 5 F G 6 7

const arr2 = ["A", "A"];
const res2 = findLongestSubarray(arr2);
console.log(res2.length === 0 ? "(empty)" : res2.join(' '));
```

## lcci_17_06_number_of_2s_in_range

<!-- REGISTRY_PATH: lcci_17_06_number_of_2s_in_range.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

class Solution {
public:
    int numberOf2sInRange(int n) {
        int count = 0;
        for (long long m = 1; m <= n; m *= 10) {
            long long a = n / m, b = n % m;
            if (a % 10 > 2) {
                count += (int)((a / 10 + 1) * m);
            } else if (a % 10 == 2) {
                count += (int)((a / 10) * m + b + 1);
            } else {
                count += (int)((a / 10) * m);
            }
        }
        return count;
    }
};

int main() {
    Solution sol;
    cout << sol.numberOf2sInRange(25) << endl;  // 9
    cout << sol.numberOf2sInRange(20) << endl;  // 2
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_06_number_of_2s_in_range.languages.go -->
### go

```go
package main

import "fmt"

func numberOf2sInRange(n int) int {
	count := 0
	for m := 1; m <= n; m *= 10 {
		a, b := n/m, n%m
		digit := (a % 10)
		if digit > 2 {
			count += (a/10 + 1) * m
		} else if digit == 2 {
			count += (a/10)*m + b + 1
		} else {
			count += (a / 10) * m
		}
	}
	return count
}

func main() {
	fmt.Println(numberOf2sInRange(25)) // 9
	fmt.Println(numberOf2sInRange(20)) // 2
}
```

<!-- REGISTRY_PATH: lcci_17_06_number_of_2s_in_range.languages.python -->
### python

```python
class Solution:
    def numberOf2sInRange(self, n: int) -> int:
        count = 0
        m = 1
        while m <= n:
            a, b = n // m, n % m
            digit = a % 10
            if digit > 2:
                count += (a // 10 + 1) * m
            elif digit == 2:
                count += (a // 10) * m + b + 1
            else:
                count += (a // 10) * m
            m *= 10
        return count


def main():
    sol = Solution()
    print(sol.numberOf2sInRange(25))  # 9
    print(sol.numberOf2sInRange(20))  # 2


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_06_number_of_2s_in_range.languages.scala -->
### scala

```scala
object Lcci1706NumberOf2sInRange {
  def numberOf2sInRange(n: Int): Int = {
    var count = 0
    var m = 1
    while (m <= n) {
      val a = n / m
      val b = n % m
      val digit = a % 10
      if (digit > 2) count += (a / 10 + 1) * m
      else if (digit == 2) count += (a / 10) * m + b + 1
      else count += (a / 10) * m
      m *= 10
    }
    count
  }

  def main(args: Array[String]): Unit = {
    println(numberOf2sInRange(25)) // 9
    println(numberOf2sInRange(20)) // 2
  }
}
```

<!-- REGISTRY_PATH: lcci_17_06_number_of_2s_in_range.languages.typescript -->
### typescript

```typescript
function numberOf2sInRange(n: number): number {
    let count = 0;
    for (let m = 1; m <= n; m *= 10) {
        const a = Math.trunc(n / m);
        const b = n % m;
        const digit = a % 10;
        if (digit > 2) {
            count += (Math.trunc(a / 10) + 1) * m;
        } else if (digit === 2) {
            count += Math.trunc(a / 10) * m + b + 1;
        } else {
            count += Math.trunc(a / 10) * m;
        }
    }
    return count;
}

console.log(numberOf2sInRange(25)); // 9
console.log(numberOf2sInRange(20)); // 2
```

## lcci_17_07_baby_names

<!-- REGISTRY_PATH: lcci_17_07_baby_names.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
    unordered_map<string, string> parent;

    string find(const string& x) {
        if (parent.find(x) == parent.end()) parent[x] = x;
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    void unite(const string& a, const string& b) {
        string pa = find(a), pb = find(b);
        if (pa != pb) {
            if (pa < pb) parent[pb] = pa;
            else parent[pa] = pb;
        }
    }

public:
    vector<string> trulyMostPopular(vector<string>& names, vector<string>& synonyms) {
        unordered_map<string, int> freq;
        for (auto& s : names) {
            size_t paren = s.find('(');
            string name = s.substr(0, paren);
            int count = stoi(s.substr(paren + 1, s.size() - paren - 2));
            freq[name] = count;
        }
        for (auto& syn : synonyms) {
            string s = syn.substr(1, syn.size() - 2);
            size_t comma = s.find(',');
            unite(s.substr(0, comma), s.substr(comma + 1));
        }
        unordered_map<string, int> result;
        for (auto& [name, cnt] : freq) {
            result[find(name)] += cnt;
        }
        vector<string> ans;
        for (auto& [name, cnt] : result) {
            ans.push_back(name + "(" + to_string(cnt) + ")");
        }
        sort(ans.begin(), ans.end());
        return ans;
    }
};

int main() {
    Solution sol;
    vector<string> names = {"John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"};
    vector<string> synonyms = {"(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"};
    auto res = sol.trulyMostPopular(names, synonyms);
    for (auto& s : res) cout << s << " ";
    cout << endl;
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_07_baby_names.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

var parent map[string]string

func find(x string) string {
	if _, ok := parent[x]; !ok {
		parent[x] = x
	}
	if parent[x] != x {
		parent[x] = find(parent[x])
	}
	return parent[x]
}

func unite(a, b string) {
	pa, pb := find(a), find(b)
	if pa != pb {
		if pa < pb {
			parent[pb] = pa
		} else {
			parent[pa] = pb
		}
	}
}

func trulyMostPopular(names []string, synonyms []string) []string {
	parent = make(map[string]string)
	freq := make(map[string]int)
	for _, s := range names {
		paren := strings.Index(s, "(")
		name := s[:paren]
		count, _ := strconv.Atoi(s[paren+1 : len(s)-1])
		freq[name] = count
	}
	for _, syn := range synonyms {
		s := syn[1 : len(syn)-1]
		comma := strings.Index(s, ",")
		unite(s[:comma], s[comma+1:])
	}
	result := make(map[string]int)
	for name, cnt := range freq {
		result[find(name)] += cnt
	}
	ans := make([]string, 0, len(result))
	for name, cnt := range result {
		ans = append(ans, name+"("+strconv.Itoa(cnt)+")")
	}
	sort.Strings(ans)
	return ans
}

func main() {
	names := []string{"John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"}
	synonyms := []string{"(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"}
	fmt.Println(strings.Join(trulyMostPopular(names, synonyms), " ")) // Chris(36) John(27)
}
```

<!-- REGISTRY_PATH: lcci_17_07_baby_names.languages.python -->
### python

```python
from typing import List
from collections import defaultdict


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        parent: dict = {}

        def find(x: str) -> str:
            if x not in parent:
                parent[x] = x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def unite(a: str, b: str) -> None:
            pa, pb = find(a), find(b)
            if pa != pb:
                if pa < pb:
                    parent[pb] = pa
                else:
                    parent[pa] = pb

        freq: dict = {}
        for s in names:
            paren = s.index('(')
            name = s[:paren]
            count = int(s[paren + 1:-1])
            freq[name] = count

        for syn in synonyms:
            s = syn[1:-1]
            comma = s.index(',')
            unite(s[:comma], s[comma + 1:])

        result: dict = defaultdict(int)
        for name, cnt in freq.items():
            result[find(name)] += cnt

        return sorted(f"{name}({cnt})" for name, cnt in result.items())


def main():
    sol = Solution()
    names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"]
    synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"]
    print(' '.join(sol.trulyMostPopular(names, synonyms)))  # Chris(36) John(27)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_07_baby_names.languages.scala -->
### scala

```scala
object Lcci1707BabyNames {
  def trulyMostPopular(names: Array[String], synonyms: Array[String]): Array[String] = {
    val parent = scala.collection.mutable.Map[String, String]()

    def find(x: String): String = {
      if (!parent.contains(x)) parent(x) = x
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    def unite(a: String, b: String): Unit = {
      val pa = find(a)
      val pb = find(b)
      if (pa != pb) {
        if (pa < pb) parent(pb) = pa
        else parent(pa) = pb
      }
    }

    val freq = scala.collection.mutable.Map[String, Int]()
    for (s <- names) {
      val idx = s.indexOf('(')
      val name = s.substring(0, idx)
      val count = s.substring(idx + 1, s.length - 1).toInt
      freq(name) = count
    }

    for (syn <- synonyms) {
      val s = syn.substring(1, syn.length - 1)
      val comma = s.indexOf(',')
      unite(s.substring(0, comma), s.substring(comma + 1))
    }

    val result = scala.collection.mutable.Map[String, Int]().withDefaultValue(0)
    for ((name, cnt) <- freq) result(find(name)) += cnt

    result.toArray.sortBy(_._1).map { case (name, cnt) => s"$name($cnt)" }
  }

  def main(args: Array[String]): Unit = {
    val names = Array("John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)")
    val synonyms = Array("(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)")
    println(trulyMostPopular(names, synonyms).mkString(" ")) // Chris(36) John(27)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_07_baby_names.languages.typescript -->
### typescript

```typescript
function trulyMostPopular(names: string[], synonyms: string[]): string[] {
    const parent = new Map<string, string>();

    const find = (x: string): string => {
        if (!parent.has(x)) parent.set(x, x);
        if (parent.get(x)! !== x) parent.set(x, find(parent.get(x)!));
        return parent.get(x)!;
    };

    const unite = (a: string, b: string): void => {
        const pa = find(a);
        const pb = find(b);
        if (pa !== pb) {
            if (pa < pb) parent.set(pb, pa);
            else parent.set(pa, pb);
        }
    };

    const freq = new Map<string, number>();
    for (const s of names) {
        const idx = s.indexOf('(');
        const name = s.slice(0, idx);
        const count = Number(s.slice(idx + 1, -1));
        freq.set(name, count);
    }

    for (const syn of synonyms) {
        const s = syn.slice(1, -1);
        const comma = s.indexOf(',');
        unite(s.slice(0, comma), s.slice(comma + 1));
    }

    const result = new Map<string, number>();
    for (const [name, cnt] of freq) {
        const root = find(name);
        result.set(root, (result.get(root) ?? 0) + cnt);
    }

    return [...result.entries()]
        .sort((a, b) => a[0].localeCompare(b[0]))
        .map(([name, cnt]) => `${name}(${cnt})`);
}

const names = ["John(15)", "Jon(12)", "Chris(13)", "Kris(4)", "Christopher(19)"];
const synonyms = ["(Jon,John)", "(John,Johnny)", "(Chris,Kris)", "(Chris,Christopher)"];
console.log(trulyMostPopular(names, synonyms).join(' ')); // Chris(36) John(27)
```

## lcci_17_08_circus_tower

<!-- REGISTRY_PATH: lcci_17_08_circus_tower.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int bestSeqAtIndex(vector<int>& height, vector<int>& weight) {
        vector<pair<int, int>> people;
        for (int i = 0; i < (int)height.size(); i++) {
            people.push_back({height[i], weight[i]});
        }
        sort(people.begin(), people.end(), [](const auto& a, const auto& b) {
            if (a.first != b.first) return a.first < b.first;
            return a.second > b.second;
        });

        vector<int> lis;
        for (auto& p : people) {
            int w = p.second;
            auto it = lower_bound(lis.begin(), lis.end(), w);
            if (it == lis.end()) lis.push_back(w);
            else *it = w;
        }
        return (int)lis.size();
    }
};

int main() {
    Solution sol;
    vector<int> h1 = {65, 70, 56, 75, 60, 68};
    vector<int> w1 = {100, 150, 90, 190, 95, 110};
    cout << sol.bestSeqAtIndex(h1, w1) << endl; // 6

    vector<int> h2 = {65, 70, 56, 75};
    vector<int> w2 = {100, 150, 90, 190};
    cout << sol.bestSeqAtIndex(h2, w2) << endl; // 4
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_08_circus_tower.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func bestSeqAtIndex(height []int, weight []int) int {
	type pair struct{ h, w int }
	people := make([]pair, len(height))
	for i := range height {
		people[i] = pair{height[i], weight[i]}
	}
	sort.Slice(people, func(i, j int) bool {
		if people[i].h != people[j].h {
			return people[i].h < people[j].h
		}
		return people[i].w > people[j].w
	})

	lis := []int{}
	for _, p := range people {
		i := sort.SearchInts(lis, p.w)
		if i == len(lis) {
			lis = append(lis, p.w)
		} else {
			lis[i] = p.w
		}
	}
	return len(lis)
}

func main() {
	fmt.Println(bestSeqAtIndex([]int{65, 70, 56, 75, 60, 68}, []int{100, 150, 90, 190, 95, 110})) // 6
	fmt.Println(bestSeqAtIndex([]int{65, 70, 56, 75}, []int{100, 150, 90, 190}))                  // 4
}
```

<!-- REGISTRY_PATH: lcci_17_08_circus_tower.languages.python -->
### python

```python
from bisect import bisect_left
from typing import List


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        people = sorted(zip(height, weight), key=lambda x: (x[0], -x[1]))
        lis: List[int] = []
        for _, w in people:
            i = bisect_left(lis, w)
            if i == len(lis):
                lis.append(w)
            else:
                lis[i] = w
        return len(lis)


def main():
    sol = Solution()
    print(sol.bestSeqAtIndex([65, 70, 56, 75, 60, 68], [100, 150, 90, 190, 95, 110]))  # 6
    print(sol.bestSeqAtIndex([65, 70, 56, 75], [100, 150, 90, 190]))  # 4


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_08_circus_tower.languages.scala -->
### scala

```scala
object Lcci1708CircusTower {
  def bestSeqAtIndex(height: Array[Int], weight: Array[Int]): Int = {
    val people = height.indices.map(i => (height(i), weight(i))).sortBy(x => (x._1, -x._2))
    val lis = scala.collection.mutable.ArrayBuffer[Int]()

    for ((_, w) <- people) {
      var l = 0
      var r = lis.length
      while (l < r) {
        val m = (l + r) / 2
        if (lis(m) < w) l = m + 1
        else r = m
      }
      if (l == lis.length) lis += w
      else lis(l) = w
    }
    lis.length
  }

  def main(args: Array[String]): Unit = {
    println(bestSeqAtIndex(Array(65, 70, 56, 75, 60, 68), Array(100, 150, 90, 190, 95, 110))) // 6
    println(bestSeqAtIndex(Array(65, 70, 56, 75), Array(100, 150, 90, 190))) // 4
  }
}
```

<!-- REGISTRY_PATH: lcci_17_08_circus_tower.languages.typescript -->
### typescript

```typescript
function bestSeqAtIndex(height: number[], weight: number[]): number {
    const people: Array<[number, number]> = [];
    for (let i = 0; i < height.length; i++) {
        people.push([height[i], weight[i]]);
    }
    people.sort((a, b) => a[0] - b[0] || b[1] - a[1]);

    const lis: number[] = [];
    for (const [, w] of people) {
        let l = 0, r = lis.length;
        while (l < r) {
            const m = (l + r) >> 1;
            if (lis[m] < w) l = m + 1;
            else r = m;
        }
        if (l === lis.length) lis.push(w);
        else lis[l] = w;
    }
    return lis.length;
}

console.log(bestSeqAtIndex([65, 70, 56, 75, 60, 68], [100, 150, 90, 190, 95, 110])); // 6
console.log(bestSeqAtIndex([65, 70, 56, 75], [100, 150, 90, 190])); // 4
```

## lcci_17_09_get_kth_magic_number

<!-- REGISTRY_PATH: lcci_17_09_get_kth_magic_number.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int getKthMagicNumber(int k) {
        vector<long long> dp(k + 1);
        dp[1] = 1;
        int i3 = 1, i5 = 1, i7 = 1;
        for (int i = 2; i <= k; i++) {
            long long a = dp[i3] * 3;
            long long b = dp[i5] * 5;
            long long c = dp[i7] * 7;
            dp[i] = min(a, min(b, c));
            if (dp[i] == a) i3++;
            if (dp[i] == b) i5++;
            if (dp[i] == c) i7++;
        }
        return (int)dp[k];
    }
};

int main() {
    Solution sol;
    cout << sol.getKthMagicNumber(5) << endl; // 9
    cout << sol.getKthMagicNumber(1) << endl; // 1
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_09_get_kth_magic_number.languages.go -->
### go

```go
package main

import "fmt"

func getKthMagicNumber(k int) int {
	dp := make([]int, k+1)
	dp[1] = 1
	i3, i5, i7 := 1, 1, 1
	for i := 2; i <= k; i++ {
		a := dp[i3] * 3
		b := dp[i5] * 5
		c := dp[i7] * 7
		dp[i] = a
		if b < dp[i] {
			dp[i] = b
		}
		if c < dp[i] {
			dp[i] = c
		}
		if dp[i] == a {
			i3++
		}
		if dp[i] == b {
			i5++
		}
		if dp[i] == c {
			i7++
		}
	}
	return dp[k]
}

func main() {
	fmt.Println(getKthMagicNumber(5)) // 9
	fmt.Println(getKthMagicNumber(1)) // 1
}
```

<!-- REGISTRY_PATH: lcci_17_09_get_kth_magic_number.languages.python -->
### python

```python
class Solution:
    def getKthMagicNumber(self, k: int) -> int:
        dp = [0] * (k + 1)
        dp[1] = 1
        i3 = i5 = i7 = 1
        for i in range(2, k + 1):
            a = dp[i3] * 3
            b = dp[i5] * 5
            c = dp[i7] * 7
            dp[i] = min(a, b, c)
            if dp[i] == a:
                i3 += 1
            if dp[i] == b:
                i5 += 1
            if dp[i] == c:
                i7 += 1
        return dp[k]


def main():
    sol = Solution()
    print(sol.getKthMagicNumber(5))  # 9
    print(sol.getKthMagicNumber(1))  # 1


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_09_get_kth_magic_number.languages.scala -->
### scala

```scala
object Lcci1709GetKthMagicNumber {
  def getKthMagicNumber(k: Int): Int = {
    val dp = Array.fill(k + 1)(0)
    dp(1) = 1
    var i3 = 1
    var i5 = 1
    var i7 = 1
    for (i <- 2 to k) {
      val a = dp(i3) * 3
      val b = dp(i5) * 5
      val c = dp(i7) * 7
      dp(i) = math.min(a, math.min(b, c))
      if (dp(i) == a) i3 += 1
      if (dp(i) == b) i5 += 1
      if (dp(i) == c) i7 += 1
    }
    dp(k)
  }

  def main(args: Array[String]): Unit = {
    println(getKthMagicNumber(5)) // 9
    println(getKthMagicNumber(1)) // 1
  }
}
```

<!-- REGISTRY_PATH: lcci_17_09_get_kth_magic_number.languages.typescript -->
### typescript

```typescript
function getKthMagicNumber(k: number): number {
    const dp: number[] = Array(k + 1).fill(0);
    dp[1] = 1;
    let i3 = 1, i5 = 1, i7 = 1;
    for (let i = 2; i <= k; i++) {
        const a = dp[i3] * 3;
        const b = dp[i5] * 5;
        const c = dp[i7] * 7;
        dp[i] = Math.min(a, b, c);
        if (dp[i] === a) i3++;
        if (dp[i] === b) i5++;
        if (dp[i] === c) i7++;
    }
    return dp[k];
}

console.log(getKthMagicNumber(5)); // 9
console.log(getKthMagicNumber(1)); // 1
```

## lcci_17_10_find_majority_element

<!-- REGISTRY_PATH: lcci_17_10_find_majority_element.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int candidate = 0, count = 0;
        for (int x : nums) {
            if (count == 0) candidate = x;
            count += (x == candidate) ? 1 : -1;
        }
        count = 0;
        for (int x : nums) {
            if (x == candidate) count++;
        }
        return count > (int)nums.size() / 2 ? candidate : -1;
    }
};

int main() {
    Solution sol;
    vector<int> nums1 = {1, 2, 5, 9, 5, 9, 5, 5, 5};
    cout << sol.majorityElement(nums1) << endl; // 5

    vector<int> nums2 = {3, 2};
    cout << sol.majorityElement(nums2) << endl; // -1
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_10_find_majority_element.languages.go -->
### go

```go
package main

import "fmt"

func majorityElement(nums []int) int {
	candidate, count := 0, 0
	for _, x := range nums {
		if count == 0 {
			candidate = x
		}
		if x == candidate {
			count++
		} else {
			count--
		}
	}

	count = 0
	for _, x := range nums {
		if x == candidate {
			count++
		}
	}
	if count > len(nums)/2 {
		return candidate
	}
	return -1
}

func main() {
	fmt.Println(majorityElement([]int{1, 2, 5, 9, 5, 9, 5, 5, 5})) // 5
	fmt.Println(majorityElement([]int{3, 2}))                      // -1
}
```

<!-- REGISTRY_PATH: lcci_17_10_find_majority_element.languages.python -->
### python

```python
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            count += 1 if x == candidate else -1
        return candidate if nums.count(candidate) > len(nums) // 2 else -1


def main():
    sol = Solution()
    print(sol.majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5]))  # 5
    print(sol.majorityElement([3, 2]))  # -1


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_10_find_majority_element.languages.scala -->
### scala

```scala
object Lcci1710FindMajorityElement {
  def majorityElement(nums: Array[Int]): Int = {
    var candidate = 0
    var count = 0
    for (x <- nums) {
      if (count == 0) candidate = x
      count += (if (x == candidate) 1 else -1)
    }
    if (nums.count(_ == candidate) > nums.length / 2) candidate else -1
  }

  def main(args: Array[String]): Unit = {
    println(majorityElement(Array(1, 2, 5, 9, 5, 9, 5, 5, 5))) // 5
    println(majorityElement(Array(3, 2))) // -1
  }
}
```

<!-- REGISTRY_PATH: lcci_17_10_find_majority_element.languages.typescript -->
### typescript

```typescript
function majorityElement(nums: number[]): number {
    let candidate = 0;
    let count = 0;
    for (const x of nums) {
        if (count === 0) candidate = x;
        count += (x === candidate ? 1 : -1);
    }
    let c = 0;
    for (const x of nums) {
        if (x === candidate) c++;
    }
    return c > Math.floor(nums.length / 2) ? candidate : -1;
}

console.log(majorityElement([1, 2, 5, 9, 5, 9, 5, 5, 5])); // 5
console.log(majorityElement([3, 2])); // -1
```

## lcci_17_11_find_closest

<!-- REGISTRY_PATH: lcci_17_11_find_closest.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <climits>
using namespace std;

class Solution {
public:
    int findClosest(vector<string>& words, string word1, string word2) {
        int i1 = -1, i2 = -1, ans = INT_MAX;
        for (int i = 0; i < (int)words.size(); i++) {
            if (words[i] == word1) i1 = i;
            if (words[i] == word2) i2 = i;
            if (i1 != -1 && i2 != -1) ans = min(ans, abs(i1 - i2));
        }
        return ans;
    }
};

int main() {
    Solution sol;
    vector<string> w1 = {"I","am","a","student","from","a","university","in","a","city"};
    cout << sol.findClosest(w1, "a", "student") << endl; // 1

    vector<string> w2 = {"aa", "bb"};
    cout << sol.findClosest(w2, "aa", "bb") << endl; // 1
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_11_find_closest.languages.go -->
### go

```go
package main

import "fmt"

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

func findClosest(words []string, word1 string, word2 string) int {
	i1, i2, ans := -1, -1, 1<<30
	for i, w := range words {
		if w == word1 {
			i1 = i
		}
		if w == word2 {
			i2 = i
		}
		if i1 != -1 && i2 != -1 {
			d := abs(i1 - i2)
			if d < ans {
				ans = d
			}
		}
	}
	return ans
}

func main() {
	fmt.Println(findClosest([]string{"I", "am", "a", "student", "from", "a", "university", "in", "a", "city"}, "a", "student")) // 1
	fmt.Println(findClosest([]string{"aa", "bb"}, "aa", "bb"))                                                                  // 1
}
```

<!-- REGISTRY_PATH: lcci_17_11_find_closest.languages.python -->
### python

```python
from typing import List


class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        i1 = i2 = -1
        ans = float('inf')
        for i, w in enumerate(words):
            if w == word1:
                i1 = i
            if w == word2:
                i2 = i
            if i1 != -1 and i2 != -1:
                ans = min(ans, abs(i1 - i2))
        return int(ans)


def main():
    sol = Solution()
    print(sol.findClosest(["I","am","a","student","from","a","university","in","a","city"], "a", "student"))  # 1
    print(sol.findClosest(["aa", "bb"], "aa", "bb"))  # 1


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_11_find_closest.languages.scala -->
### scala

```scala
object Lcci1711FindClosest {
  def findClosest(words: Array[String], word1: String, word2: String): Int = {
    var i1 = -1
    var i2 = -1
    var ans = Int.MaxValue
    for (i <- words.indices) {
      if (words(i) == word1) i1 = i
      if (words(i) == word2) i2 = i
      if (i1 != -1 && i2 != -1) ans = math.min(ans, math.abs(i1 - i2))
    }
    ans
  }

  def main(args: Array[String]): Unit = {
    println(findClosest(Array("I", "am", "a", "student", "from", "a", "university", "in", "a", "city"), "a", "student")) // 1
    println(findClosest(Array("aa", "bb"), "aa", "bb")) // 1
  }
}
```

<!-- REGISTRY_PATH: lcci_17_11_find_closest.languages.typescript -->
### typescript

```typescript
function findClosest(words: string[], word1: string, word2: string): number {
    let i1 = -1, i2 = -1;
    let ans = Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < words.length; i++) {
        if (words[i] === word1) i1 = i;
        if (words[i] === word2) i2 = i;
        if (i1 !== -1 && i2 !== -1) {
            ans = Math.min(ans, Math.abs(i1 - i2));
        }
    }
    return ans;
}

console.log(findClosest(["I","am","a","student","from","a","university","in","a","city"], "a", "student")); // 1
console.log(findClosest(["aa", "bb"], "aa", "bb")); // 1
```

## lcci_17_12_binode

<!-- REGISTRY_PATH: lcci_17_12_binode.languages.cpp -->
### cpp

```cpp
#include <iostream>
using namespace std;

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
};

class Solution {
    TreeNode* prev = nullptr;

    void inorder(TreeNode* root) {
        if (!root) return;
        inorder(root->left);
        root->left = nullptr;
        prev->right = root;
        prev = root;
        inorder(root->right);
    }

public:
    TreeNode* convertBiNode(TreeNode* root) {
        TreeNode dummy(0);
        prev = &dummy;
        inorder(root);
        return dummy.right;
    }
};

int main() {
    TreeNode* root = new TreeNode(4);
    root->left = new TreeNode(2);
    root->right = new TreeNode(5);
    root->left->left = new TreeNode(1);
    root->left->right = new TreeNode(3);
    root->right->right = new TreeNode(6);
    root->left->left->left = new TreeNode(0);

    Solution sol;
    TreeNode* head = sol.convertBiNode(root);
    while (head) {
        cout << head->val << (head->right ? ' ' : '\n');
        head = head->right;
    }
    return 0;
}
```

<!-- REGISTRY_PATH: lcci_17_12_binode.languages.go -->
### go

```go
package main

import "fmt"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

var prev *TreeNode

func inorder(root *TreeNode) {
	if root == nil {
		return
	}
	inorder(root.Left)
	root.Left = nil
	prev.Right = root
	prev = root
	inorder(root.Right)
}

func convertBiNode(root *TreeNode) *TreeNode {
	dummy := &TreeNode{}
	prev = dummy
	inorder(root)
	return dummy.Right
}

func main() {
	root := &TreeNode{Val: 4}
	root.Left = &TreeNode{Val: 2}
	root.Right = &TreeNode{Val: 5}
	root.Left.Left = &TreeNode{Val: 1}
	root.Left.Right = &TreeNode{Val: 3}
	root.Right.Right = &TreeNode{Val: 6}
	root.Left.Left.Left = &TreeNode{Val: 0}

	head := convertBiNode(root)
	for head != nil {
		if head.Right != nil {
			fmt.Printf("%d ", head.Val)
		} else {
			fmt.Printf("%d\n", head.Val)
		}
		head = head.Right
	}
}
```

<!-- REGISTRY_PATH: lcci_17_12_binode.languages.python -->
### python

```python
from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, x: int):
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Solution:
    def __init__(self) -> None:
        self.prev: Optional[TreeNode] = None

    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(0)
        self.prev = dummy

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            node.left = None
            self.prev.right = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        return dummy.right


def main():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(0)

    head = Solution().convertBiNode(root)
    out = []
    while head:
        out.append(str(head.val))
        head = head.right
    print(' '.join(out))  # 0 1 2 3 4 5 6


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: lcci_17_12_binode.languages.scala -->
### scala

```scala
class TreeNode(var value: Int, var left: TreeNode = null, var right: TreeNode = null)

object Lcci1712BiNode {
  private var prev: TreeNode = _

  private def inorder(root: TreeNode): Unit = {
    if (root == null) return
    inorder(root.left)
    root.left = null
    prev.right = root
    prev = root
    inorder(root.right)
  }

  def convertBiNode(root: TreeNode): TreeNode = {
    val dummy = new TreeNode(0)
    prev = dummy
    inorder(root)
    dummy.right
  }

  def main(args: Array[String]): Unit = {
    val root = new TreeNode(4)
    root.left = new TreeNode(2)
    root.right = new TreeNode(5)
    root.left.left = new TreeNode(1)
    root.left.right = new TreeNode(3)
    root.right.right = new TreeNode(6)
    root.left.left.left = new TreeNode(0)

    var head = convertBiNode(root)
    val out = scala.collection.mutable.ArrayBuffer[Int]()
    while (head != null) {
      out += head.value
      head = head.right
    }
    println(out.mkString(" ")) // 0 1 2 3 4 5 6
  }
}
```

<!-- REGISTRY_PATH: lcci_17_12_binode.languages.typescript -->
### typescript

```typescript
class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function convertBiNode(root: TreeNode | null): TreeNode | null {
    const dummy = new TreeNode(0);
    let prev = dummy;

    const inorder = (node: TreeNode | null): void => {
        if (!node) return;
        inorder(node.left);
        node.left = null;
        prev.right = node;
        prev = node;
        inorder(node.right);
    };

    inorder(root);
    return dummy.right;
}

const root = new TreeNode(4);
root.left = new TreeNode(2);
root.right = new TreeNode(5);
root.left.left = new TreeNode(1);
root.left.right = new TreeNode(3);
root.right.right = new TreeNode(6);
root.left.left.left = new TreeNode(0);

let head = convertBiNode(root);
const out: number[] = [];
while (head) {
    out.push(head.val);
    head = head.right;
}
console.log(out.join(' ')); // 0 1 2 3 4 5 6
```

## lcci_17_13_re_space

<!-- REGISTRY_PATH: lcci_17_13_re_space.languages.cpp -->
### cpp

```cpp
#include <string>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:
    int respace(vector<string>& dictionary, string sentence) {
        unordered_set<string> s(dictionary.begin(), dictionary.end());
        int n = sentence.size();
        vector<int> dp(n + 1, 0);
        for (int i = 1; i <= n; ++i) {
            dp[i] = dp[i - 1] + 1;
            for (int j = 0; j < i; ++j) {
                if (s.count(sentence.substr(j, i - j))) {
                    dp[i] = min(dp[i], dp[j]);
                }
            }
        }
        return dp[n];
    }
};
```

<!-- REGISTRY_PATH: lcci_17_13_re_space.languages.go -->
### go

```go
package main

func respace(dictionary []string, sentence string) int {
	s := make(map[string]bool)
	for _, w := range dictionary {
		s[w] = true
	}
	n := len(sentence)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = dp[i-1] + 1
		for j := 0; j < i; j++ {
			if s[sentence[j:i]] {
				if dp[j] < dp[i] {
					dp[i] = dp[j]
				}
			}
		}
	}
	return dp[n]
}
```

<!-- REGISTRY_PATH: lcci_17_13_re_space.languages.python -->
### python

```python
from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        s = set(dictionary)
        n = len(sentence)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1
            for j in range(i):
                if sentence[j:i] in s:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
```

<!-- REGISTRY_PATH: lcci_17_13_re_space.languages.scala -->
### scala

```scala
object Solution {
  def respace(dictionary: Array[String], sentence: String): Int = {
    val s = dictionary.toSet
    val n = sentence.length
    val dp = Array.fill(n + 1)(0)
    for (i <- 1 to n) {
      dp(i) = dp(i - 1) + 1
      for (j <- 0 until i) {
        if (s.contains(sentence.substring(j, i))) {
          dp(i) = dp(i).min(dp(j))
        }
      }
    }
    dp(n)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_13_re_space.languages.typescript -->
### typescript

```typescript
function respace(dictionary: string[], sentence: string): number {
    const s = new Set(dictionary);
    const n = sentence.length;
    const dp = new Array(n + 1).fill(0);
    for (let i = 1; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;
        for (let j = 0; j < i; j++) {
            if (s.has(sentence.slice(j, i))) {
                dp[i] = Math.min(dp[i], dp[j]);
            }
        }
    }
    return dp[n];
}
```

## lcci_17_14_smallest_k

<!-- REGISTRY_PATH: lcci_17_14_smallest_k.languages.cpp -->
### cpp

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> smallestK(vector<int>& arr, int k) {
        sort(arr.begin(), arr.end());
        return vector<int>(arr.begin(), arr.begin() + k);
    }
};
```

<!-- REGISTRY_PATH: lcci_17_14_smallest_k.languages.go -->
### go

```go
package main

import "sort"

func smallestK(arr []int, k int) []int {
	sort.Ints(arr)
	return arr[:k]
}
```

<!-- REGISTRY_PATH: lcci_17_14_smallest_k.languages.python -->
### python

```python
from typing import List
import heapq


class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        h = []
        for x in arr:
            heapq.heappush(h, -x)
            if len(h) > k:
                heapq.heappop(h)
        return [-x for x in h]
```

<!-- REGISTRY_PATH: lcci_17_14_smallest_k.languages.scala -->
### scala

```scala
object Solution {
  def smallestK(arr: Array[Int], k: Int): Array[Int] = {
    arr.sorted.take(k)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_14_smallest_k.languages.typescript -->
### typescript

```typescript
function smallestK(arr: number[], k: number): number[] {
    arr.sort((a, b) => a - b);
    return arr.slice(0, k);
}
```

## lcci_17_15_longest_word

<!-- REGISTRY_PATH: lcci_17_15_longest_word.languages.cpp -->
### cpp

```cpp
#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
    unordered_set<string> wordSet;

    bool canBuild(const string& w) {
        if (w.empty()) return true;
        for (int i = 1; i <= (int)w.size(); ++i) {
            if (wordSet.count(w.substr(0, i)) && canBuild(w.substr(i))) {
                return true;
            }
        }
        return false;
    }

public:
    string longestWord(vector<string>& words) {
        for (auto& w : words) wordSet.insert(w);
        sort(words.begin(), words.end(), [](const string& a, const string& b) {
            return a.size() != b.size() ? a.size() > b.size() : a < b;
        });
        for (auto& w : words) {
            wordSet.erase(w);
            if (canBuild(w)) return w;
            wordSet.insert(w);
        }
        return "";
    }
};
```

<!-- REGISTRY_PATH: lcci_17_15_longest_word.languages.go -->
### go

```go
package main

import "sort"

func longestWord(words []string) string {
	wordSet := make(map[string]bool)
	for _, w := range words {
		wordSet[w] = true
	}

	var canBuild func(w string) bool
	canBuild = func(w string) bool {
		if w == "" {
			return true
		}
		for i := 1; i <= len(w); i++ {
			if wordSet[w[:i]] && canBuild(w[i:]) {
				return true
			}
		}
		return false
	}

	sort.Slice(words, func(i, j int) bool {
		if len(words[i]) != len(words[j]) {
			return len(words[i]) > len(words[j])
		}
		return words[i] < words[j]
	})

	for _, w := range words {
		delete(wordSet, w)
		if canBuild(w) {
			return w
		}
		wordSet[w] = true
	}
	return ""
}
```

<!-- REGISTRY_PATH: lcci_17_15_longest_word.languages.python -->
### python

```python
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)

        def can_build(w: str) -> bool:
            if not w:
                return True
            for i in range(1, len(w) + 1):
                if w[:i] in word_set and can_build(w[i:]):
                    return True
            return False

        words.sort(key=lambda x: (-len(x), x))
        for w in words:
            word_set.discard(w)
            if can_build(w):
                return w
            word_set.add(w)
        return ""
```

<!-- REGISTRY_PATH: lcci_17_15_longest_word.languages.scala -->
### scala

```scala
object Solution {
  def longestWord(words: Array[String]): String = {
    val wordSet = scala.collection.mutable.Set(words: _*)

    def canBuild(w: String): Boolean = {
      if (w.isEmpty) return true
      (1 to w.length).exists(i => wordSet.contains(w.take(i)) && canBuild(w.drop(i)))
    }

    val sorted = words.sortWith((a, b) => if (a.length != b.length) a.length > b.length else a < b)
    for (w <- sorted) {
      wordSet.remove(w)
      if (canBuild(w)) return w
      wordSet.add(w)
    }
    ""
  }
}
```

<!-- REGISTRY_PATH: lcci_17_15_longest_word.languages.typescript -->
### typescript

```typescript
function longestWord(words: string[]): string {
    const wordSet = new Set(words);

    function canBuild(w: string): boolean {
        if (w === '') return true;
        for (let i = 1; i <= w.length; i++) {
            if (wordSet.has(w.slice(0, i)) && canBuild(w.slice(i))) {
                return true;
            }
        }
        return false;
    }

    words.sort((a, b) => b.length - a.length || a.localeCompare(b));

    for (const w of words) {
        wordSet.delete(w);
        if (canBuild(w)) return w;
        wordSet.add(w);
    }
    return '';
}
```

## lcci_17_16_the_masseuse

<!-- REGISTRY_PATH: lcci_17_16_the_masseuse.languages.cpp -->
### cpp

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int massage(vector<int>& nums) {
        int f = 0, g = 0;
        for (int x : nums) {
            int nf = g + x;
            int ng = max(f, g);
            f = nf;
            g = ng;
        }
        return max(f, g);
    }
};
```

<!-- REGISTRY_PATH: lcci_17_16_the_masseuse.languages.go -->
### go

```go
package main

func massage(nums []int) int {
	f, g := 0, 0
	for _, x := range nums {
		f, g = g+x, max(f, g)
	}
	return max(f, g)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
```

<!-- REGISTRY_PATH: lcci_17_16_the_masseuse.languages.python -->
### python

```python
from typing import List


class Solution:
    def massage(self, nums: List[int]) -> int:
        f = g = 0
        for x in nums:
            f, g = g + x, max(f, g)
        return max(f, g)
```

<!-- REGISTRY_PATH: lcci_17_16_the_masseuse.languages.scala -->
### scala

```scala
object Solution {
  def massage(nums: Array[Int]): Int = {
    var f = 0
    var g = 0
    for (x <- nums) {
      val nf = g + x
      val ng = f.max(g)
      f = nf
      g = ng
    }
    f.max(g)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_16_the_masseuse.languages.typescript -->
### typescript

```typescript
function massage(nums: number[]): number {
    let f = 0, g = 0;
    for (const x of nums) {
        [f, g] = [g + x, Math.max(f, g)];
    }
    return Math.max(f, g);
}
```

## lcci_17_17_multi_search

<!-- REGISTRY_PATH: lcci_17_17_multi_search.languages.cpp -->
### cpp

```cpp
#include <string>
#include <vector>
using namespace std;

struct Trie {
    Trie* children[26] = {};
    int idx = -1;

    void insert(const string& word, int i) {
        Trie* node = this;
        for (char c : word) {
            int j = c - 'a';
            if (!node->children[j]) node->children[j] = new Trie();
            node = node->children[j];
        }
        node->idx = i;
    }
};

class Solution {
public:
    vector<vector<int>> multiSearch(string big, vector<string>& smalls) {
        Trie* trie = new Trie();
        for (int i = 0; i < (int)smalls.size(); ++i) {
            if (!smalls[i].empty()) trie->insert(smalls[i], i);
        }
        int n = big.size();
        vector<vector<int>> ans(smalls.size());
        for (int i = 0; i < n; ++i) {
            Trie* node = trie;
            for (int j = i; j < n; ++j) {
                int k = big[j] - 'a';
                if (!node->children[k]) break;
                node = node->children[k];
                if (node->idx != -1) ans[node->idx].push_back(i);
            }
        }
        return ans;
    }
};
```

<!-- REGISTRY_PATH: lcci_17_17_multi_search.languages.go -->
### go

```go
package main

type Trie struct {
	children [26]*Trie
	idx      int
}

func newTrie() *Trie {
	return &Trie{idx: -1}
}

func (t *Trie) insert(word string, i int) {
	node := t
	for _, c := range word {
		j := c - 'a'
		if node.children[j] == nil {
			node.children[j] = newTrie()
		}
		node = node.children[j]
	}
	node.idx = i
}

func multiSearch(big string, smalls []string) [][]int {
	trie := newTrie()
	for i, s := range smalls {
		if s != "" {
			trie.insert(s, i)
		}
	}

	ans := make([][]int, len(smalls))
	for i := range ans {
		ans[i] = []int{}
	}

	for i := range big {
		node := trie
		for j := i; j < len(big); j++ {
			k := big[j] - 'a'
			if node.children[k] == nil {
				break
			}
			node = node.children[k]
			if node.idx != -1 {
				ans[node.idx] = append(ans[node.idx], i)
			}
		}
	}
	return ans
}
```

<!-- REGISTRY_PATH: lcci_17_17_multi_search.languages.python -->
### python

```python
from typing import List


class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.idx = -1

    def insert(self, word: str, i: int):
        node = self
        for c in word:
            j = ord(c) - ord('a')
            if node.children[j] is None:
                node.children[j] = Trie()
            node = node.children[j]
        node.idx = i


class Solution:
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        trie = Trie()
        for i, s in enumerate(smalls):
            if s:
                trie.insert(s, i)

        ans = [[] for _ in smalls]
        for i in range(len(big)):
            node = trie
            for j in range(i, len(big)):
                k = ord(big[j]) - ord('a')
                if node.children[k] is None:
                    break
                node = node.children[k]
                if node.idx != -1:
                    ans[node.idx].append(i)
        return ans
```

<!-- REGISTRY_PATH: lcci_17_17_multi_search.languages.scala -->
### scala

```scala
import scala.collection.mutable

object Solution {
  class TrieNode {
    val children: Array[TrieNode] = new Array[TrieNode](26)
    var idx: Int = -1
  }

  def multiSearch(big: String, smalls: Array[String]): Array[Array[Int]] = {
    val root = new TrieNode()
    for ((s, i) <- smalls.zipWithIndex if s.nonEmpty) {
      var node = root
      for (c <- s) {
        val j = c - 'a'
        if (node.children(j) == null) node.children(j) = new TrieNode()
        node = node.children(j)
      }
      node.idx = i
    }
    val ans = Array.fill(smalls.length)(mutable.ArrayBuffer[Int]())
    for (i <- big.indices) {
      var node = root
      var j = i
      var stop = false
      while (j < big.length && !stop) {
        val k = big(j) - 'a'
        if (node.children(k) == null) stop = true
        else {
          node = node.children(k)
          if (node.idx != -1) ans(node.idx) += i
          j += 1
        }
      }
    }
    ans.map(_.toArray)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_17_multi_search.languages.typescript -->
### typescript

```typescript
class TrieNode {
    children: (TrieNode | null)[] = new Array(26).fill(null);
    idx: number = -1;
}

function multiSearch(big: string, smalls: string[]): number[][] {
    const root = new TrieNode();
    const insert = (word: string, i: number) => {
        let node = root;
        for (const c of word) {
            const j = c.charCodeAt(0) - 97;
            if (!node.children[j]) node.children[j] = new TrieNode();
            node = node.children[j]!;
        }
        node.idx = i;
    };
    for (let i = 0; i < smalls.length; i++) {
        if (smalls[i]) insert(smalls[i], i);
    }
    const ans: number[][] = smalls.map(() => []);
    for (let i = 0; i < big.length; i++) {
        let node = root;
        for (let j = i; j < big.length; j++) {
            const k = big.charCodeAt(j) - 97;
            if (!node.children[k]) break;
            node = node.children[k]!;
            if (node.idx !== -1) ans[node.idx].push(i);
        }
    }
    return ans;
}
```

## lcci_17_18_shortest_supersequence

<!-- REGISTRY_PATH: lcci_17_18_shortest_supersequence.languages.cpp -->
### cpp

```cpp
#include <vector>
#include <unordered_map>
#include <climits>
using namespace std;

class Solution {
public:
    vector<int> shortestSeq(vector<int>& big, vector<int>& small) {
        unordered_map<int, int> need;
        for (int x : small) need[x]++;
        unordered_map<int, int> window;
        int cnt = small.size();
        int j = 0, k = -1, mi = INT_MAX;
        for (int i = 0; i < (int)big.size(); ++i) {
            window[big[i]]++;
            if (need[big[i]] >= window[big[i]]) cnt--;
            while (cnt == 0) {
                if (i - j + 1 < mi) { mi = i - j + 1; k = j; }
                if (need[big[j]] >= window[big[j]]) cnt++;
                window[big[j]]--;
                j++;
            }
        }
        if (k == -1) return {};
        return {k, k + mi - 1};
    }
};
```

<!-- REGISTRY_PATH: lcci_17_18_shortest_supersequence.languages.go -->
### go

```go
package main

func shortestSeq(big []int, small []int) []int {
	need := make(map[int]int)
	for _, x := range small {
		need[x]++
	}
	window := make(map[int]int)
	cnt := len(small)
	j, k, mi := 0, -1, len(big)+1

	for i, x := range big {
		window[x]++
		if need[x] >= window[x] {
			cnt--
		}
		for cnt == 0 {
			if i-j+1 < mi {
				mi = i - j + 1
				k = j
			}
			if need[big[j]] >= window[big[j]] {
				cnt++
			}
			window[big[j]]--
			j++
		}
	}
	if k == -1 {
		return []int{}
	}
	return []int{k, k + mi - 1}
}
```

<!-- REGISTRY_PATH: lcci_17_18_shortest_supersequence.languages.python -->
### python

```python
from typing import List
from collections import Counter


class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        need = Counter(small)
        window = Counter()
        cnt = len(small)
        j = 0
        k = -1
        mi = float('inf')
        for i, x in enumerate(big):
            window[x] += 1
            if need[x] >= window[x]:
                cnt -= 1
            while cnt == 0:
                if i - j + 1 < mi:
                    mi = i - j + 1
                    k = j
                if need[big[j]] >= window[big[j]]:
                    cnt += 1
                window[big[j]] -= 1
                j += 1
        return [] if k == -1 else [k, k + mi - 1]
```

<!-- REGISTRY_PATH: lcci_17_18_shortest_supersequence.languages.scala -->
### scala

```scala
object Solution {
  def shortestSeq(big: Array[Int], small: Array[Int]): Array[Int] = {
    val need = scala.collection.mutable.Map[Int, Int]()
    for (x <- small) need(x) = need.getOrElse(x, 0) + 1
    val window = scala.collection.mutable.Map[Int, Int]()
    var cnt = small.length
    var j = 0; var k = -1; var mi = Int.MaxValue

    for (i <- big.indices) {
      val x = big(i)
      window(x) = window.getOrElse(x, 0) + 1
      if (need.getOrElse(x, 0) >= window(x)) cnt -= 1
      while (cnt == 0) {
        if (i - j + 1 < mi) { mi = i - j + 1; k = j }
        val lx = big(j)
        if (need.getOrElse(lx, 0) >= window.getOrElse(lx, 0)) cnt += 1
        window(lx) = window.getOrElse(lx, 0) - 1
        j += 1
      }
    }
    if (k == -1) Array() else Array(k, k + mi - 1)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_18_shortest_supersequence.languages.typescript -->
### typescript

```typescript
function shortestSeq(big: number[], small: number[]): number[] {
    const need = new Map<number, number>();
    for (const x of small) need.set(x, (need.get(x) ?? 0) + 1);
    const window = new Map<number, number>();
    let cnt = small.length;
    let j = 0, k = -1, mi = Infinity;
    for (let i = 0; i < big.length; i++) {
        const x = big[i];
        window.set(x, (window.get(x) ?? 0) + 1);
        if ((need.get(x) ?? 0) >= (window.get(x) ?? 0)) cnt--;
        while (cnt === 0) {
            if (i - j + 1 < mi) { mi = i - j + 1; k = j; }
            const lx = big[j];
            if ((need.get(lx) ?? 0) >= (window.get(lx) ?? 0)) cnt++;
            window.set(lx, (window.get(lx) ?? 0) - 1);
            j++;
        }
    }
    return k === -1 ? [] : [k, k + mi - 1];
}
```

## lcci_17_19_missing_two

<!-- REGISTRY_PATH: lcci_17_19_missing_two.languages.cpp -->
### cpp

```cpp
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> missingTwo(vector<int>& nums) {
        int n = nums.size() + 2;
        int xorVal = 0;
        for (int v : nums) xorVal ^= v;
        for (int i = 1; i <= n; ++i) xorVal ^= i;
        int diff = xorVal & (-xorVal);
        int a = 0;
        for (int v : nums) if (v & diff) a ^= v;
        for (int i = 1; i <= n; ++i) if (i & diff) a ^= i;
        int b = xorVal ^ a;
        return {a, b};
    }
};
```

<!-- REGISTRY_PATH: lcci_17_19_missing_two.languages.go -->
### go

```go
package main

func missingTwo(nums []int) []int {
	n := len(nums) + 2
	xor := 0
	for _, v := range nums {
		xor ^= v
	}
	for i := 1; i <= n; i++ {
		xor ^= i
	}
	diff := xor & (-xor)
	a := 0
	for _, v := range nums {
		if v&diff != 0 {
			a ^= v
		}
	}
	for i := 1; i <= n; i++ {
		if i&diff != 0 {
			a ^= i
		}
	}
	b := xor ^ a
	return []int{a, b}
}
```

<!-- REGISTRY_PATH: lcci_17_19_missing_two.languages.python -->
### python

```python
from typing import List


class Solution:
    def missingTwo(self, nums: List[int]) -> List[int]:
        n = len(nums) + 2
        xor = 0
        for v in nums:
            xor ^= v
        for i in range(1, n + 1):
            xor ^= i
        diff = xor & (-xor)
        a = 0
        for v in nums:
            if v & diff:
                a ^= v
        for i in range(1, n + 1):
            if i & diff:
                a ^= i
        b = xor ^ a
        return [a, b]
```

<!-- REGISTRY_PATH: lcci_17_19_missing_two.languages.scala -->
### scala

```scala
object Solution {
  def missingTwo(nums: Array[Int]): Array[Int] = {
    val n = nums.length + 2
    var xor = 0
    for (v <- nums) xor ^= v
    for (i <- 1 to n) xor ^= i
    val diff = xor & (-xor)
    var a = 0
    for (v <- nums) if ((v & diff) != 0) a ^= v
    for (i <- 1 to n) if ((i & diff) != 0) a ^= i
    val b = xor ^ a
    Array(a, b)
  }
}
```

<!-- REGISTRY_PATH: lcci_17_19_missing_two.languages.typescript -->
### typescript

```typescript
function missingTwo(nums: number[]): number[] {
    const n = nums.length + 2;
    let xor = 0;
    for (const v of nums) xor ^= v;
    for (let i = 1; i <= n; i++) xor ^= i;
    const diff = xor & (-xor);
    let a = 0;
    for (const v of nums) if (v & diff) a ^= v;
    for (let i = 1; i <= n; i++) if (i & diff) a ^= i;
    const b = xor ^ a;
    return [a, b];
}
```

## lcci_17_20_continuous_median

<!-- REGISTRY_PATH: lcci_17_20_continuous_median.languages.cpp -->
### cpp

```cpp
#include <queue>
using namespace std;

class MedianFinder {
    priority_queue<int> lo;                          // max-heap
    priority_queue<int, vector<int>, greater<int>> hi; // min-heap
public:
    void addNum(int num) {
        lo.push(num);
        hi.push(lo.top()); lo.pop();
        if (hi.size() > lo.size()) {
            lo.push(hi.top()); hi.pop();
        }
    }

    double findMedian() {
        if (lo.size() > hi.size()) return lo.top();
        return (lo.top() + hi.top()) / 2.0;
    }
};
```

<!-- REGISTRY_PATH: lcci_17_20_continuous_median.languages.go -->
### go

```go
package main

import "container/heap"

type MaxHeap []int

func (h MaxHeap) Len() int           { return len(h) }
func (h MaxHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h MaxHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MaxHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MaxHeap) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }
func (h *MinHeap) Push(x any)        { *h = append(*h, x.(int)) }
func (h *MinHeap) Pop() any          { old := *h; n := len(old); x := old[n-1]; *h = old[:n-1]; return x }

type MedianFinder struct {
	lo *MaxHeap
	hi *MinHeap
}

func Constructor() MedianFinder {
	lo, hi := &MaxHeap{}, &MinHeap{}
	heap.Init(lo)
	heap.Init(hi)
	return MedianFinder{lo, hi}
}

func (mf *MedianFinder) AddNum(num int) {
	heap.Push(mf.lo, num)
	heap.Push(mf.hi, heap.Pop(mf.lo))
	if mf.hi.Len() > mf.lo.Len() {
		heap.Push(mf.lo, heap.Pop(mf.hi))
	}
}

func (mf *MedianFinder) FindMedian() float64 {
	if mf.lo.Len() > mf.hi.Len() {
		return float64((*mf.lo)[0])
	}
	return float64((*mf.lo)[0]+(*mf.hi)[0]) / 2.0
}
```

<!-- REGISTRY_PATH: lcci_17_20_continuous_median.languages.python -->
### python

```python
import heapq


class MedianFinder:
    def __init__(self):
        # lo is a max-heap (negate values), hi is a min-heap
        self.lo: list = []  # max-heap
        self.hi: list = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.lo, -num)
        heapq.heappush(self.hi, -heapq.heappop(self.lo))
        if len(self.hi) > len(self.lo):
            heapq.heappush(self.lo, -heapq.heappop(self.hi))

    def findMedian(self) -> float:
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2.0
```

<!-- REGISTRY_PATH: lcci_17_20_continuous_median.languages.scala -->
### scala

```scala
import scala.collection.mutable

class MedianFinder {
  // lo: max-heap, hi: min-heap
  private val lo = mutable.PriorityQueue[Int]()        // max-heap
  private val hi = mutable.PriorityQueue[Int]()(Ordering[Int].reverse) // min-heap

  def addNum(num: Int): Unit = {
    lo.enqueue(num)
    hi.enqueue(lo.dequeue())
    if (hi.size > lo.size) lo.enqueue(hi.dequeue())
  }

  def findMedian(): Double = {
    if (lo.size > hi.size) lo.head.toDouble
    else (lo.head + hi.head) / 2.0
  }
}
```

<!-- REGISTRY_PATH: lcci_17_20_continuous_median.languages.typescript -->
### typescript

```typescript
class MedianFinder {
    // lo: max-heap (negated), hi: min-heap
    private lo: number[] = [];
    private hi: number[] = [];

    addNum(num: number): void {
        this.heapPush(this.lo, -num, true);
        this.heapPush(this.hi, -this.heapPop(this.lo, true), false);
        if (this.hi.length > this.lo.length) {
            this.heapPush(this.lo, -this.heapPop(this.hi, false), true);
        }
    }

    findMedian(): number {
        if (this.lo.length > this.hi.length) return -this.lo[0];
        return (-this.lo[0] + this.hi[0]) / 2;
    }

    private heapPush(h: number[], val: number, isMax: boolean): void {
        h.push(val);
        let i = h.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (isMax ? h[p] >= h[i] : h[p] <= h[i]) break;
            [h[p], h[i]] = [h[i], h[p]];
            i = p;
        }
    }

    private heapPop(h: number[], isMax: boolean): number {
        const top = h[0];
        const last = h.pop()!;
        if (h.length > 0) {
            h[0] = last;
            let i = 0;
            while (true) {
                let best = i;
                const l = 2 * i + 1, r = 2 * i + 2;
                if (l < h.length && (isMax ? h[l] > h[best] : h[l] < h[best])) best = l;
                if (r < h.length && (isMax ? h[r] > h[best] : h[r] < h[best])) best = r;
                if (best === i) break;
                [h[i], h[best]] = [h[best], h[i]];
                i = best;
            }
        }
        return top;
    }
}
```

## lcci_17_21_volume_of_histogram

<!-- REGISTRY_PATH: lcci_17_21_volume_of_histogram.languages.cpp -->
### cpp

```cpp
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        int left = 0, right = (int)height.size() - 1;
        int leftMax = 0, rightMax = 0, ans = 0;
        while (left < right) {
            if (height[left] < height[right]) {
                if (height[left] >= leftMax) leftMax = height[left];
                else ans += leftMax - height[left];
                left++;
            } else {
                if (height[right] >= rightMax) rightMax = height[right];
                else ans += rightMax - height[right];
                right--;
            }
        }
        return ans;
    }
};
```

<!-- REGISTRY_PATH: lcci_17_21_volume_of_histogram.languages.go -->
### go

```go
package main

func trap(height []int) int {
	left, right := 0, len(height)-1
	leftMax, rightMax := 0, 0
	ans := 0
	for left < right {
		if height[left] < height[right] {
			if height[left] >= leftMax {
				leftMax = height[left]
			} else {
				ans += leftMax - height[left]
			}
			left++
		} else {
			if height[right] >= rightMax {
				rightMax = height[right]
			} else {
				ans += rightMax - height[right]
			}
			right--
		}
	}
	return ans
}
```

<!-- REGISTRY_PATH: lcci_17_21_volume_of_histogram.languages.python -->
### python

```python
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    ans += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    ans += right_max - height[right]
                right -= 1
        return ans
```

<!-- REGISTRY_PATH: lcci_17_21_volume_of_histogram.languages.scala -->
### scala

```scala
object Solution {
  def trap(height: Array[Int]): Int = {
    var left = 0; var right = height.length - 1
    var leftMax = 0; var rightMax = 0; var ans = 0
    while (left < right) {
      if (height(left) < height(right)) {
        if (height(left) >= leftMax) leftMax = height(left)
        else ans += leftMax - height(left)
        left += 1
      } else {
        if (height(right) >= rightMax) rightMax = height(right)
        else ans += rightMax - height(right)
        right -= 1
      }
    }
    ans
  }
}
```

<!-- REGISTRY_PATH: lcci_17_21_volume_of_histogram.languages.typescript -->
### typescript

```typescript
function trap(height: number[]): number {
    let left = 0, right = height.length - 1;
    let leftMax = 0, rightMax = 0, ans = 0;
    while (left < right) {
        if (height[left] < height[right]) {
            if (height[left] >= leftMax) leftMax = height[left];
            else ans += leftMax - height[left];
            left++;
        } else {
            if (height[right] >= rightMax) rightMax = height[right];
            else ans += rightMax - height[right];
            right--;
        }
    }
    return ans;
}
```

## lcci_17_22_word_transformer

<!-- REGISTRY_PATH: lcci_17_22_word_transformer.languages.cpp -->
### cpp

```cpp
#include <string>
#include <vector>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
public:
    vector<string> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        if (!wordSet.count(endWord)) return {};

        queue<vector<string>> q;
        q.push({beginWord});
        unordered_set<string> visited = {beginWord};

        while (!q.empty()) {
            auto path = q.front(); q.pop();
            string cur = path.back();
            for (int i = 0; i < (int)cur.size(); ++i) {
                char orig = cur[i];
                for (char c = 'a'; c <= 'z'; ++c) {
                    if (c == orig) continue;
                    cur[i] = c;
                    auto newPath = path;
                    newPath.push_back(cur);
                    if (cur == endWord) return newPath;
                    if (wordSet.count(cur) && !visited.count(cur)) {
                        visited.insert(cur);
                        q.push(newPath);
                    }
                    cur[i] = orig;
                }
            }
        }
        return {};
    }
};
```

<!-- REGISTRY_PATH: lcci_17_22_word_transformer.languages.go -->
### go

```go
package main

func findLadders(beginWord string, endWord string, wordList []string) []string {
	wordSet := make(map[string]bool)
	for _, w := range wordList {
		wordSet[w] = true
	}
	if !wordSet[endWord] {
		return []string{}
	}

	type State struct {
		path []string
	}
	queue := []State{{[]string{beginWord}}}
	visited := map[string]bool{beginWord: true}

	for len(queue) > 0 {
		st := queue[0]
		queue = queue[1:]
		cur := st.path[len(st.path)-1]
		bs := []byte(cur)
		for i := 0; i < len(bs); i++ {
			orig := bs[i]
			for c := byte('a'); c <= byte('z'); c++ {
				if c == orig {
					continue
				}
				bs[i] = c
				nxt := string(bs)
				newPath := append(append([]string{}, st.path...), nxt)
				if nxt == endWord {
					return newPath
				}
				if wordSet[nxt] && !visited[nxt] {
					visited[nxt] = true
					queue = append(queue, State{newPath})
				}
				bs[i] = orig
			}
		}
	}
	return []string{}
}
```

<!-- REGISTRY_PATH: lcci_17_22_word_transformer.languages.python -->
### python

```python
from typing import List
from collections import deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        queue = deque([[beginWord]])
        visited = {beginWord}
        while queue:
            path = queue.popleft()
            cur = path[-1]
            for i in range(len(cur)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = cur[:i] + c + cur[i+1:]
                    if nxt == endWord:
                        return path + [endWord]
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        queue.append(path + [nxt])
        return []
```

<!-- REGISTRY_PATH: lcci_17_22_word_transformer.languages.scala -->
### scala

```scala
import scala.collection.mutable

object Solution {
  def findLadders(beginWord: String, endWord: String, wordList: Array[String]): Array[String] = {
    val wordSet = wordList.toSet
    if (!wordSet.contains(endWord)) return Array()

    val queue = mutable.Queue[List[String]](List(beginWord))
    val visited = mutable.Set[String](beginWord)

    while (queue.nonEmpty) {
      val path = queue.dequeue()
      val cur = path.last
      for (i <- cur.indices) {
        for (c <- 'a' to 'z') {
          if (c != cur(i)) {
            val nxt = cur.updated(i, c)
            if (nxt == endWord) return (path :+ nxt).toArray
            if (wordSet.contains(nxt) && !visited.contains(nxt)) {
              visited.add(nxt)
              queue.enqueue(path :+ nxt)
            }
          }
        }
      }
    }
    Array()
  }
}
```

<!-- REGISTRY_PATH: lcci_17_22_word_transformer.languages.typescript -->
### typescript

```typescript
function findLadders(beginWord: string, endWord: string, wordList: string[]): string[] {
    const wordSet = new Set(wordList);
    if (!wordSet.has(endWord)) return [];

    const queue: string[][] = [[beginWord]];
    const visited = new Set([beginWord]);

    while (queue.length > 0) {
        const path = queue.shift()!;
        const cur = path[path.length - 1];
        const arr = cur.split('');
        for (let i = 0; i < arr.length; i++) {
            const orig = arr[i];
            for (let c = 0; c < 26; c++) {
                const ch = String.fromCharCode(97 + c);
                if (ch === orig) continue;
                arr[i] = ch;
                const nxt = arr.join('');
                if (nxt === endWord) return [...path, nxt];
                if (wordSet.has(nxt) && !visited.has(nxt)) {
                    visited.add(nxt);
                    queue.push([...path, nxt]);
                }
                arr[i] = orig;
            }
        }
    }
    return [];
}
```

## linked_lists

- Docs: /content/docs/linked_lists/README.md

<!-- REGISTRY_PATH: linked_lists.languages.cpp -->
### cpp

```cpp
#include <iostream>

struct Node {
    int value;
    Node* next;
    explicit Node(int v) : value(v), next(nullptr) {}
};

void printList(Node* head) {
    for (Node* cur = head; cur; cur = cur->next) {
        std::cout << cur->value;
        if (cur->next) std::cout << " -> ";
    }
    std::cout << "\n";
}

Node* prepend(Node* head, int value) {
    Node* node = new Node(value);
    node->next = head;
    return node;
}

Node* removeValue(Node* head, int value) {
    if (!head) return nullptr;
    if (head->value == value) {
        Node* next = head->next;
        delete head;
        return next;
    }
    head->next = removeValue(head->next, value);
    return head;
}

int main() {
    Node* head = nullptr;
    for (int v : {3, 2, 1}) head = prepend(head, v);  // 1 -> 2 -> 3
    printList(head);
    head = removeValue(head, 2);
    printList(head);  // 1 -> 3
    while (head) { Node* next = head->next; delete head; head = next; }
    return 0;
}
```

<!-- REGISTRY_PATH: linked_lists.languages.go -->
### go

```go
package main

import "fmt"

type Node struct {
	value int
	next  *Node
}

func printList(head *Node) {
	for cur := head; cur != nil; cur = cur.next {
		fmt.Print(cur.value)
		if cur.next != nil {
			fmt.Print(" -> ")
		}
	}
	fmt.Println()
}

func prepend(head *Node, value int) *Node {
	return &Node{value: value, next: head}
}

func removeValue(head *Node, value int) *Node {
	if head == nil {
		return nil
	}
	if head.value == value {
		return head.next
	}
	head.next = removeValue(head.next, value)
	return head
}

func main() {
	var head *Node
	for _, v := range []int{3, 2, 1} {
		head = prepend(head, v) // 1 -> 2 -> 3
	}
	printList(head)
	head = removeValue(head, 2)
	printList(head) // 1 -> 3
}
```

<!-- REGISTRY_PATH: linked_lists.languages.python -->
### python

```python
#!/usr/bin/env python3
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Node:
    value: int
    next: Optional[Node] = field(default=None, repr=False)


def print_list(head: Optional[Node]) -> None:
    parts: list[str] = []
    cur = head
    while cur:
        parts.append(str(cur.value))
        cur = cur.next
    print(" -> ".join(parts))


def prepend(head: Optional[Node], value: int) -> Node:
    return Node(value=value, next=head)


def remove_value(head: Optional[Node], value: int) -> Optional[Node]:
    if head is None:
        return None
    if head.value == value:
        return head.next
    head.next = remove_value(head.next, value)
    return head


def main() -> None:
    head: Optional[Node] = None
    for v in [3, 2, 1]:
        head = prepend(head, v)  # 1 -> 2 -> 3
    print_list(head)
    head = remove_value(head, 2)
    print_list(head)  # 1 -> 3


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: linked_lists.languages.scala -->
### scala

```scala
object LinkedListBasics {
  case class Node(value: Int, next: Option[Node] = None)

  def printList(head: Option[Node]): Unit = {
    val parts = Iterator.unfold(head) {
      case None       => None
      case Some(node) => Some((node.value.toString, node.next))
    }
    println(parts.mkString(" -> "))
  }

  def prepend(head: Option[Node], value: Int): Node = Node(value, head)

  def removeValue(head: Option[Node], value: Int): Option[Node] = head match {
    case None                              => None
    case Some(node) if node.value == value => node.next
    case Some(node)                        => Some(node.copy(next = removeValue(node.next, value)))
  }

  def main(args: Array[String]): Unit = {
    var head: Option[Node] = None
    for (v <- List(3, 2, 1)) head = Some(prepend(head, v))  // 1 -> 2 -> 3
    printList(head)
    head = removeValue(head, 2)
    printList(head)  // 1 -> 3
  }
}
```

<!-- REGISTRY_PATH: linked_lists.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

interface Node {
  value: number;
  next: Node | null;
}

function makeNode(value: number, next: Node | null = null): Node {
  return { value, next };
}

function printList(head: Node | null): void {
  const parts: string[] = [];
  for (let cur = head; cur !== null; cur = cur.next) {
    parts.push(String(cur.value));
  }
  console.log(parts.join(" -> "));
}

function prepend(head: Node | null, value: number): Node {
  return makeNode(value, head);
}

function removeValue(head: Node | null, value: number): Node | null {
  if (head === null) return null;
  if (head.value === value) return head.next;
  head.next = removeValue(head.next, value);
  return head;
}

function main(): void {
  let head: Node | null = null;
  for (const v of [3, 2, 1]) head = prepend(head, v);  // 1 -> 2 -> 3
  printList(head);
  head = removeValue(head, 2);
  printList(head);  // 1 -> 3
}

main();
```

## loops

- Docs: /content/docs/loops/README.md

<!-- REGISTRY_PATH: loops.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5};

    for (size_t i = 0; i < values.size(); ++i) {
        std::cout << "for index: " << i << " -> " << values[i] << "\n";
    }

    for (int v : values) {
        if (v == 3) {
            continue;
        }
        std::cout << "range for: " << v << "\n";
    }

    int i = 0;
    while (i < static_cast<int>(values.size())) {
        if (values[i] == 4) {
            break;
        }
        std::cout << "while: " << values[i] << "\n";
        ++i;
    }

    int c = 0;
    do {
        std::cout << "do-while iteration: " << c << "\n";
        ++c;
    } while (c < 2);

    return 0;
}
```

<!-- REGISTRY_PATH: loops.languages.go -->
### go

```go
package main

import "fmt"

func main() {
	values := []int{1, 2, 3, 4, 5}

	for i := 0; i < len(values); i++ {
		fmt.Println("for index:", i, "->", values[i])
	}

	for _, v := range values {
		if v == 3 {
			continue
		}
		fmt.Println("range:", v)
	}

	i := 0
	for i < len(values) {
		if values[i] == 4 {
			break
		}
		fmt.Println("while-style:", values[i])
		i++
	}

	c := 0
	for {
		fmt.Println("infinite-loop iteration:", c)
		c++
		if c >= 2 {
			break
		}
	}
}
```

<!-- REGISTRY_PATH: loops.languages.python -->
### python

```python
#!/usr/bin/env python3

def main() -> None:
    values = [1, 2, 3, 4, 5]

    for i in range(len(values)):
        print("for index:", i, "->", values[i])

    for v in values:
        if v == 3:
            continue
        print("for each:", v)

    i = 0
    while i < len(values):
        if values[i] == 4:
            break
        print("while:", values[i])
        i += 1

    c = 0
    while True:
        print("do-while style iteration:", c)
        c += 1
        if c >= 2:
            break


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: loops.languages.scala -->
### scala

```scala
object LoopsBasics {
  def main(args: Array[String]): Unit = {
    val values = Vector(1, 2, 3, 4, 5)

    for (i <- values.indices) {
      println(s"for index: $i -> ${values(i)}")
    }

    for (v <- values) {
      if (v != 3) println(s"for each: $v")
    }

    var i = 0
    while (i < values.length && values(i) != 4) {
      println(s"while: ${values(i)}")
      i += 1
    }

    var c = 0
    do {
      println(s"do-while iteration: $c")
      c += 1
    } while (c < 2)
  }
}
```

<!-- REGISTRY_PATH: loops.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const values = [1, 2, 3, 4, 5];

  for (let i = 0; i < values.length; i++) {
    console.log("for index:", i, "->", values[i]);
  }

  for (const v of values) {
    if (v === 3) {
      continue;
    }
    console.log("for...of:", v);
  }

  let i = 0;
  while (i < values.length) {
    if (values[i] === 4) {
      break;
    }
    console.log("while:", values[i]);
    i++;
  }

  let c = 0;
  do {
    console.log("do...while iteration:", c);
    c++;
  } while (c < 2);
}

main();
setImmediate(() => {});
```

## maps_and_sets

- Docs: /content/docs/maps_and_sets/README.md

<!-- REGISTRY_PATH: maps_and_sets.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <map>
#include <set>
#include <string>

int main() {
    std::map<std::string, int> counts;
    counts["apple"] = 2;
    counts["banana"] = 1;
    counts["apple"] += 3;

    std::set<std::string> tags{"fruit", "food"};
    tags.insert("fresh");

    std::cout << "apple count: " << counts["apple"] << "\n";

    std::cout << "all map entries: ";
    for (const auto& p : counts) {
        std::cout << "(" << p.first << "," << p.second << ") ";
    }
    std::cout << "\n";

    std::cout << "all set entries: ";
    for (const auto& t : tags) {
        std::cout << t << ' ';
    }
    std::cout << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: maps_and_sets.languages.go -->
### go

```go
package main

import "fmt"

func main() {
	counts := map[string]int{
		"apple":  2,
		"banana": 1,
	}
	counts["apple"] += 3

	tags := map[string]struct{}{
		"fruit": {},
		"food":  {},
	}
	tags["fresh"] = struct{}{}

	fmt.Println("apple count:", counts["apple"])
	fmt.Println("all map entries:")
	for k, v := range counts {
		fmt.Printf("(%s,%d) ", k, v)
	}
	fmt.Println()

	fmt.Println("all set entries:")
	for t := range tags {
		fmt.Printf("%s ", t)
	}
	fmt.Println()
}
```

<!-- REGISTRY_PATH: maps_and_sets.languages.python -->
### python

```python
#!/usr/bin/env python3

def main() -> None:
    counts = {"apple": 2, "banana": 1}
    counts["apple"] += 3

    tags = {"fruit", "food"}
    tags.add("fresh")

    print("apple count:", counts["apple"])
    print("all map entries:", sorted(counts.items()))
    print("all set entries:", sorted(tags))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: maps_and_sets.languages.scala -->
### scala

```scala
object MapsAndSetsBasics {
  def main(args: Array[String]): Unit = {
    val counts = scala.collection.mutable.Map("apple" -> 2, "banana" -> 1)
    counts("apple") = counts("apple") + 3

    val tags = scala.collection.mutable.Set("fruit", "food")
    tags += "fresh"

    println(s"apple count: ${counts("apple")}")
    println(s"all map entries: ${counts.toSeq.sortBy(_._1)}")
    println(s"all set entries: ${tags.toSeq.sorted}")
  }
}
```

<!-- REGISTRY_PATH: maps_and_sets.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const counts = new Map<string, number>([
    ["apple", 2],
    ["banana", 1],
  ]);
  counts.set("apple", (counts.get("apple") ?? 0) + 3);

  const tags = new Set<string>(["fruit", "food"]);
  tags.add("fresh");

  console.log("apple count:", counts.get("apple"));
  console.log("all map entries:", Array.from(counts.entries()));
  console.log("all set entries:", Array.from(tags.values()));
}

main();
setImmediate(() => {});
```

## memory_layout

- Docs: /content/docs/memory_layout/README.md

<!-- REGISTRY_PATH: memory_layout.languages.cpp -->
### cpp

```cpp
// Common baseline
int stack = 7;
int* p = &stack;
std::unique_ptr<int> sp = std::make_unique<int>(42);
```

<!-- REGISTRY_PATH: memory_layout.languages.go -->
### go

```go
// Common baseline
v := 7
```

<!-- REGISTRY_PATH: memory_layout.languages.python -->
### python

```python
# Common baseline
x = [1,2,3]
y = x
```

<!-- REGISTRY_PATH: memory_layout.languages.scala -->
### scala

```scala
object MemoryLayout {
  def main(args: Array[String]): Unit = {
    // primitive on the stack-like area (JVM may optimize, but conceptually a value)
    val x: Int = 7

    // arrays/objects are allocated on the heap and referenced
    val arr = Array(1, 2, 3)
    val alias = arr

    // mutating via alias affects original reference
    alias(0) = 42

    println(s"x = $x")
    println(s"arr = ${arr.mkString(",")}")
  }
}
```

<!-- REGISTRY_PATH: memory_layout.languages.typescript -->
### typescript

```typescript
// Common baseline
const user = { score: 1 }
```

## nullable_optional_values

- Docs: /content/docs/nullable_optional_values/README.md

<!-- REGISTRY_PATH: nullable_optional_values.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <optional>
#include <string>

std::optional<int> parse_age(const std::string& text) {
    if (text.empty()) {
        return std::nullopt;
    }
    return std::stoi(text);
}

int main() {
    auto age = parse_age("29");
    auto missing = parse_age("");

    std::cout << "age present: " << age.has_value() << "\n";
    std::cout << "missing default: " << missing.value_or(0) << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: nullable_optional_values.languages.go -->
### go

```go
package main

import "fmt"

func parseAge(text string) *int {
	if text == "" {
		return nil
	}

	age := 29
	return &age
}

func main() {
	age := parseAge("29")
	missing := parseAge("")

	fmt.Println("age present:", age != nil)
	if missing == nil {
		fmt.Println("missing default:", 0)
	} else {
		fmt.Println("missing default:", *missing)
	}
}
```

<!-- REGISTRY_PATH: nullable_optional_values.languages.python -->
### python

```python
#!/usr/bin/env python3
from typing import Optional


def parse_age(text: str) -> Optional[int]:
    if not text:
        return None
    return int(text)


def main() -> None:
    age = parse_age("29")
    missing = parse_age("")

    print("age present:", age is not None)
    print("missing default:", missing or 0)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: nullable_optional_values.languages.scala -->
### scala

```scala
object NullableOptionalValuesBasics {
  def parseAge(text: String): Option[Int] = {
    if (text.isEmpty) None else Some(text.toInt)
  }

  def main(args: Array[String]): Unit = {
    val age = parseAge("29")
    val missing = parseAge("")

    println(s"age present: ${age.isDefined}")
    println(s"missing default: ${missing.getOrElse(0)}")
  }
}
```

<!-- REGISTRY_PATH: nullable_optional_values.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function parseAge(text: string): number | null {
  if (text === "") {
    return null;
  }
  return Number(text);
}

function main(): void {
  const age = parseAge("29");
  const missing = parseAge("");

  console.log("age present:", age !== null);
  console.log("missing default:", missing ?? 0);
}

main();
setImmediate(() => {});
```

## problems

- Docs: /content/docs/problems/README.md

<!-- REGISTRY_PATH: problems.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

bool isBalanced(const std::string& s) {
    static const std::unordered_map<char, char> closeToOpen = {
        {')', '('},
        {']', '['},
        {'}', '{'}
    };

    std::vector<char> st;
    st.reserve(s.size());

    for (char ch : s) {
        if (ch == '(' || ch == '[' || ch == '{') {
            st.push_back(ch);
        } else if (closeToOpen.count(ch)) {
            if (st.empty() || st.back() != closeToOpen.at(ch)) {
                return false;
            }
            st.pop_back();
        }
    }

    return st.empty();
}

int main() {
    const std::string input1 = "([{}])(()[]){}";
    const std::string input2 = "([)]";

    std::cout << std::boolalpha;
    std::cout << "input_1 valid: " << isBalanced(input1) << '\n';
    std::cout << "input_2 valid: " << isBalanced(input2) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: problems.languages.go -->
### go

```go
package main

import "fmt"

func isBalanced(s string) bool {
	closeToOpen := map[rune]rune{
		')': '(',
		']': '[',
		'}': '{',
	}

	stack := make([]rune, 0, len(s))
	for _, ch := range s {
		switch ch {
		case '(', '[', '{':
			stack = append(stack, ch)
		case ')', ']', '}':
			if len(stack) == 0 || stack[len(stack)-1] != closeToOpen[ch] {
				return false
			}
			stack = stack[:len(stack)-1]
		}
	}

	return len(stack) == 0
}

func main() {
	input1 := "([{}])(()[]){}"
	input2 := "([)]"

	fmt.Printf("input_1 valid: %v\n", isBalanced(input1))
	fmt.Printf("input_2 valid: %v\n", isBalanced(input2))
}
```

<!-- REGISTRY_PATH: problems.languages.python -->
### python

```python
def is_balanced(s: str) -> bool:
    close_to_open = {")": "(", "]": "[", "}": "{"}
    stack: list[str] = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in close_to_open:
            if not stack or stack[-1] != close_to_open[ch]:
                return False
            stack.pop()

    return not stack


def main() -> None:
    input_1 = "([{}])(()[]){}"
    input_2 = "([)]"

    print(f"input_1 valid: {str(is_balanced(input_1)).lower()}")
    print(f"input_2 valid: {str(is_balanced(input_2)).lower()}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: problems.languages.scala -->
### scala

```scala
object BalancedBrackets {
  def isBalanced(s: String): Boolean = {
    val closeToOpen = Map(
      ')' -> '(',
      ']' -> '[',
      '}' -> '{'
    )

    val st = scala.collection.mutable.ArrayBuffer.empty[Char]
    s.foreach { ch =>
      ch match {
        case '(' | '[' | '{' => st += ch
        case ')' | ']' | '}' =>
          if (st.isEmpty || st.last != closeToOpen(ch)) return false
          st.remove(st.size - 1)
        case _ =>
      }
    }
    st.isEmpty
  }

  def main(args: Array[String]): Unit = {
    val input1 = "([{}])(()[]){}"
    val input2 = "([)]"

    println(s"input_1 valid: ${isBalanced(input1)}")
    println(s"input_2 valid: ${isBalanced(input2)}")
  }
}
```

<!-- REGISTRY_PATH: problems.languages.typescript -->
### typescript

```typescript
import { setImmediate } from "node:timers";

function isBalanced(s: string): boolean {
  const closeToOpen: Record<string, string> = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  const stack: string[] = [];
  for (const ch of s) {
    if (ch === "(" || ch === "[" || ch === "{") {
      stack.push(ch);
    } else if (ch in closeToOpen) {
      if (stack.length === 0 || stack[stack.length - 1] !== closeToOpen[ch]) {
        return false;
      }
      stack.pop();
    }
  }

  return stack.length === 0;
}

function main(): void {
  const input1 = "([{}])(()[]){}";
  const input2 = "([)]";

  console.log(`input_1 valid: ${isBalanced(input1)}`);
  console.log(`input_2 valid: ${isBalanced(input2)}`);
}

main();
setImmediate(() => {});
```

## random_numbers

- Docs: /content/docs/random_numbers/README.md

<!-- REGISTRY_PATH: random_numbers.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <random>

int main() {
    std::mt19937 generator(42);
    std::uniform_int_distribution<int> dist(1, 10);

    std::cout << "draws: ";
    for (int i = 0; i < 3; ++i) {
        std::cout << dist(generator) << ' ';
    }
    std::cout << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: random_numbers.languages.go -->
### go

```go
package main

import (
	"fmt"
	"math/rand"
)

func main() {
	generator := rand.New(rand.NewSource(42))
	draws := []int{
		generator.Intn(10) + 1,
		generator.Intn(10) + 1,
		generator.Intn(10) + 1,
	}
	fmt.Println("draws:", draws)
}
```

<!-- REGISTRY_PATH: random_numbers.languages.python -->
### python

```python
#!/usr/bin/env python3
import random


def main() -> None:
    generator = random.Random(42)
    draws = [generator.randint(1, 10) for _ in range(3)]
    print("draws:", draws)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: random_numbers.languages.scala -->
### scala

```scala
import scala.util.Random

object RandomNumbersBasics {
  def main(args: Array[String]): Unit = {
    val generator = new Random(42)
    val draws = Seq.fill(3)(generator.between(1, 11))
    println(s"draws: $draws")
  }
}
```

<!-- REGISTRY_PATH: random_numbers.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function makeGenerator(seed: number): () => number {
  let state = seed;
  return () => {
    state = (state * 1664525 + 1013904223) % 4294967296;
    return state / 4294967296;
  };
}

function main(): void {
  const next = makeGenerator(42);
  const draws = Array.from({ length: 3 }, () => Math.floor(next() * 10) + 1);
  console.log("draws:", draws);
}

main();
setImmediate(() => {});
```

## recursion

- Docs: /content/docs/recursion/README.md

<!-- REGISTRY_PATH: recursion.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>

int factorial(int n) {
    if (n <= 1) {
        return 1;
    }
    return n * factorial(n - 1);
}

int sum_recursive(const std::vector<int>& values, size_t index = 0) {
    if (index >= values.size()) {
        return 0;
    }
    return values[index] + sum_recursive(values, index + 1);
}

int main() {
    std::vector<int> values{1, 2, 3, 4};
    std::cout << "factorial(5): " << factorial(5) << "\n";
    std::cout << "sum_recursive(values): " << sum_recursive(values) << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: recursion.languages.go -->
### go

```go
package main

import "fmt"

func factorial(n int) int {
	if n <= 1 {
		return 1
	}
	return n * factorial(n-1)
}

func sumRecursive(values []int, index int) int {
	if index >= len(values) {
		return 0
	}
	return values[index] + sumRecursive(values, index+1)
}

func main() {
	values := []int{1, 2, 3, 4}
	fmt.Println("factorial(5):", factorial(5))
	fmt.Println("sumRecursive(values):", sumRecursive(values, 0))
}
```

<!-- REGISTRY_PATH: recursion.languages.python -->
### python

```python
#!/usr/bin/env python3

def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_recursive(values: list[int], index: int = 0) -> int:
    if index >= len(values):
        return 0
    return values[index] + sum_recursive(values, index + 1)


def main() -> None:
    values = [1, 2, 3, 4]
    print("factorial(5):", factorial(5))
    print("sum_recursive(values):", sum_recursive(values))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: recursion.languages.scala -->
### scala

```scala
object RecursionBasics {
  def factorial(n: Int): Int = {
    if (n <= 1) 1 else n * factorial(n - 1)
  }

  def sumRecursive(values: Vector[Int], index: Int = 0): Int = {
    if (index >= values.length) 0
    else values(index) + sumRecursive(values, index + 1)
  }

  def main(args: Array[String]): Unit = {
    val values = Vector(1, 2, 3, 4)
    println(s"factorial(5): ${factorial(5)}")
    println(s"sumRecursive(values): ${sumRecursive(values)}")
  }
}
```

<!-- REGISTRY_PATH: recursion.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function factorial(n: number): number {
  if (n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

function sumRecursive(values: number[], index = 0): number {
  if (index >= values.length) {
    return 0;
  }
  return values[index] + sumRecursive(values, index + 1);
}

function main(): void {
  const values = [1, 2, 3, 4];
  console.log("factorial(5):", factorial(5));
  console.log("sumRecursive(values):", sumRecursive(values));
}

main();
setImmediate(() => {});
```

## sorting_and_searching

- Docs: /content/docs/sorting_and_searching/README.md

<!-- REGISTRY_PATH: sorting_and_searching.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{9, 3, 7, 1, 5};
    std::sort(values.begin(), values.end());

    bool has_seven = std::binary_search(values.begin(), values.end(), 7);
    auto it = std::lower_bound(values.begin(), values.end(), 7);
    int index = (it != values.end() && *it == 7) ? static_cast<int>(it - values.begin()) : -1;

    std::cout << "sorted: ";
    for (int v : values) {
        std::cout << v << ' ';
    }
    std::cout << "\ncontains 7: " << has_seven << "\nindex of 7: " << index << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: sorting_and_searching.languages.go -->
### go

```go
package main

import (
	"fmt"
	"sort"
)

func main() {
	values := []int{9, 3, 7, 1, 5}
	sort.Ints(values)

	index := sort.SearchInts(values, 7)
	foundIndex := -1
	if index < len(values) && values[index] == 7 {
		foundIndex = index
	}

	fmt.Println("sorted:", values)
	fmt.Println("contains 7:", foundIndex >= 0)
	fmt.Println("index of 7:", foundIndex)
}
```

<!-- REGISTRY_PATH: sorting_and_searching.languages.python -->
### python

```python
#!/usr/bin/env python3
from bisect import bisect_left


def main() -> None:
    values = [9, 3, 7, 1, 5]
    ordered = sorted(values)

    index = bisect_left(ordered, 7)
    found_index = index if index < len(ordered) and ordered[index] == 7 else -1

    print("sorted:", ordered)
    print("contains 7:", 7 in ordered)
    print("index of 7:", found_index)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: sorting_and_searching.languages.scala -->
### scala

```scala
object SortingAndSearchingBasics {
  def main(args: Array[String]): Unit = {
    val values = Vector(9, 3, 7, 1, 5).sorted
    val index = values.indexOf(7)

    println(s"sorted: $values")
    println(s"contains 7: ${index >= 0}")
    println(s"index of 7: $index")
  }
}
```

<!-- REGISTRY_PATH: sorting_and_searching.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function binarySearch(values: number[], target: number): number {
  let left = 0;
  let right = values.length - 1;

  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (values[mid] === target) {
      return mid;
    }
    if (values[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  return -1;
}

function main(): void {
  const values = [9, 3, 7, 1, 5].sort((a, b) => a - b);
  const index = binarySearch(values, 7);

  console.log("sorted:", values);
  console.log("contains 7:", index >= 0);
  console.log("index of 7:", index);
}

main();
setImmediate(() => {});
```

## stacks_and_queues

- Docs: /content/docs/stacks_and_queues/README.md

<!-- REGISTRY_PATH: stacks_and_queues.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <queue>
#include <stack>

int main() {
    std::stack<int> stk;
    for (int v : {1, 2, 3}) stk.push(v);
    std::cout << "stack top: " << stk.top() << "\n";  // 3 (LIFO)
    stk.pop();
    std::cout << "after pop: " << stk.top() << "\n";  // 2

    std::queue<int> q;
    for (int v : {1, 2, 3}) q.push(v);
    std::cout << "queue front: " << q.front() << "\n";  // 1 (FIFO)
    q.pop();
    std::cout << "after dequeue: " << q.front() << "\n";  // 2
    return 0;
}
```

<!-- REGISTRY_PATH: stacks_and_queues.languages.go -->
### go

```go
package main

import "fmt"

func main() {
	// Stack: slice used as LIFO
	stack := []int{}
	for _, v := range []int{1, 2, 3} {
		stack = append(stack, v)
	}
	fmt.Println("stack top:", stack[len(stack)-1]) // 3
	stack = stack[:len(stack)-1]
	fmt.Println("after pop:", stack[len(stack)-1]) // 2

	// Queue: slice used as FIFO
	queue := []int{}
	for _, v := range []int{1, 2, 3} {
		queue = append(queue, v)
	}
	fmt.Println("queue front:", queue[0]) // 1
	queue = queue[1:]
	fmt.Println("after dequeue:", queue[0]) // 2
}
```

<!-- REGISTRY_PATH: stacks_and_queues.languages.python -->
### python

```python
#!/usr/bin/env python3
from collections import deque


def main() -> None:
    # Stack: list used as LIFO
    stack: list[int] = []
    for v in [1, 2, 3]:
        stack.append(v)
    print("stack top:", stack[-1])  # 3
    stack.pop()
    print("after pop:", stack[-1])  # 2

    # Queue: deque used as FIFO
    queue: deque[int] = deque()
    for v in [1, 2, 3]:
        queue.append(v)
    print("queue front:", queue[0])  # 1
    queue.popleft()
    print("after dequeue:", queue[0])  # 2


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: stacks_and_queues.languages.scala -->
### scala

```scala
import scala.collection.mutable

object StacksAndQueues {
  def main(args: Array[String]): Unit = {
    val stack = mutable.Stack[Int]()
    List(1, 2, 3).foreach(stack.push)
    println(s"stack top: ${stack.top}")  // 3 (LIFO)
    stack.pop()
    println(s"after pop: ${stack.top}")  // 2

    val queue = mutable.Queue[Int]()
    List(1, 2, 3).foreach(queue.enqueue)
    println(s"queue front: ${queue.front}")  // 1 (FIFO)
    queue.dequeue()
    println(s"after dequeue: ${queue.front}")  // 2
  }
}
```

<!-- REGISTRY_PATH: stacks_and_queues.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

class Stack<T> {
  private items: T[] = [];
  push(v: T): void { this.items.push(v); }
  pop(): void { this.items.pop(); }
  top(): T { return this.items[this.items.length - 1]; }
  isEmpty(): boolean { return this.items.length === 0; }
}

class Queue<T> {
  private items: T[] = [];
  enqueue(v: T): void { this.items.push(v); }
  dequeue(): void { this.items.shift(); }
  front(): T { return this.items[0]; }
  isEmpty(): boolean { return this.items.length === 0; }
}

function main(): void {
  const stk = new Stack<number>();
  for (const v of [1, 2, 3]) stk.push(v);
  console.log("stack top:", stk.top());  // 3 (LIFO)
  stk.pop();
  console.log("after pop:", stk.top());  // 2

  const q = new Queue<number>();
  for (const v of [1, 2, 3]) q.enqueue(v);
  console.log("queue front:", q.front());  // 1 (FIFO)
  q.dequeue();
  console.log("after dequeue:", q.front());  // 2
}

main();
```

## strings

- Docs: /content/docs/strings/README.md

<!-- REGISTRY_PATH: strings.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

int main() {
    std::string first = "hello";
    std::string second = "world";
    std::string joined = first + " " + second;

    std::string part = joined.substr(0, 5);
    std::string replaced = joined;
    replaced.replace(0, 5, "hi");

    std::vector<std::string> words;
    std::istringstream iss(joined);
    for (std::string token; iss >> token;) {
        words.push_back(token);
    }

    std::cout << "joined: " << joined << "\n";
    std::cout << "part: " << part << "\n";
    std::cout << "replaced: " << replaced << "\n";
    std::cout << "tokens: ";
    for (const auto& w : words) {
        std::cout << w << ' ';
    }
    std::cout << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: strings.languages.go -->
### go

```go
package main

import (
	"fmt"
	"strings"
)

func main() {
	first := "hello"
	second := "world"
	joined := first + " " + second

	part := joined[:5]
	replaced := strings.Replace(joined, "hello", "hi", 1)
	words := strings.Fields(joined)

	fmt.Println("joined:", joined)
	fmt.Println("part:", part)
	fmt.Println("replaced:", replaced)
	fmt.Println("tokens:", words)
}
```

<!-- REGISTRY_PATH: strings.languages.python -->
### python

```python
#!/usr/bin/env python3

def main() -> None:
    first = "hello"
    second = "world"
    joined = first + " " + second

    part = joined[:5]
    replaced = joined.replace("hello", "hi", 1)
    words = joined.split()

    print("joined:", joined)
    print("part:", part)
    print("replaced:", replaced)
    print("tokens:", words)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: strings.languages.scala -->
### scala

```scala
object StringsBasics {
  def main(args: Array[String]): Unit = {
    val first = "hello"
    val second = "world"
    val joined = s"$first $second"

    val part = joined.substring(0, 5)
    val replaced = joined.replace("hello", "hi")
    val words = joined.split("\\s+").toSeq

    println(s"joined: $joined")
    println(s"part: $part")
    println(s"replaced: $replaced")
    println(s"tokens: $words")
  }
}
```

<!-- REGISTRY_PATH: strings.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const first = "hello";
  const second = "world";
  const joined = `${first} ${second}`;

  const part = joined.slice(0, 5);
  const replaced = joined.replace("hello", "hi");
  const words = joined.split(/\s+/);

  console.log("joined:", joined);
  console.log("part:", part);
  console.log("replaced:", replaced);
  console.log("tokens:", words);
}

main();
setImmediate(() => {});
```

## trees_and_graphs

- Docs: /content/docs/trees_and_graphs/README.md

<!-- REGISTRY_PATH: trees_and_graphs.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <queue>

struct TreeNode {
    int value;
    TreeNode* left;
    TreeNode* right;
    explicit TreeNode(int v) : value(v), left(nullptr), right(nullptr) {}
};

TreeNode* insert(TreeNode* root, int value) {
    if (!root) return new TreeNode(value);
    if (value < root->value) root->left  = insert(root->left,  value);
    else                     root->right = insert(root->right, value);
    return root;
}

void inOrder(TreeNode* root) {
    if (!root) return;
    inOrder(root->left);
    std::cout << root->value << ' ';
    inOrder(root->right);
}

void bfs(TreeNode* root) {
    if (!root) return;
    std::queue<TreeNode*> q;
    q.push(root);
    while (!q.empty()) {
        TreeNode* node = q.front(); q.pop();
        std::cout << node->value << ' ';
        if (node->left)  q.push(node->left);
        if (node->right) q.push(node->right);
    }
}

int main() {
    TreeNode* root = nullptr;
    for (int v : {5, 3, 7, 1, 4}) root = insert(root, v);
    std::cout << "in-order: "; inOrder(root); std::cout << "\n";  // 1 3 4 5 7
    std::cout << "bfs:      "; bfs(root);     std::cout << "\n";  // 5 3 7 1 4
    return 0;
}
```

<!-- REGISTRY_PATH: trees_and_graphs.languages.go -->
### go

```go
package main

import "fmt"

type TreeNode struct {
	value       int
	left, right *TreeNode
}

func insert(root *TreeNode, value int) *TreeNode {
	if root == nil {
		return &TreeNode{value: value}
	}
	if value < root.value {
		root.left = insert(root.left, value)
	} else {
		root.right = insert(root.right, value)
	}
	return root
}

func inOrder(root *TreeNode) {
	if root == nil {
		return
	}
	inOrder(root.left)
	fmt.Print(root.value, " ")
	inOrder(root.right)
}

func bfs(root *TreeNode) {
	if root == nil {
		return
	}
	queue := []*TreeNode{root}
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		fmt.Print(node.value, " ")
		if node.left != nil {
			queue = append(queue, node.left)
		}
		if node.right != nil {
			queue = append(queue, node.right)
		}
	}
}

func main() {
	var root *TreeNode
	for _, v := range []int{5, 3, 7, 1, 4} {
		root = insert(root, v)
	}
	fmt.Print("in-order: ")
	inOrder(root)
	fmt.Println() // 1 3 4 5 7
	fmt.Print("bfs:      ")
	bfs(root)
	fmt.Println() // 5 3 7 1 4
}
```

<!-- REGISTRY_PATH: trees_and_graphs.languages.python -->
### python

```python
#!/usr/bin/env python3
from __future__ import annotations
from collections import deque
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class TreeNode:
    value: int
    left: Optional[TreeNode] = field(default=None, repr=False)
    right: Optional[TreeNode] = field(default=None, repr=False)


def insert(root: Optional[TreeNode], value: int) -> TreeNode:
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root


def in_order(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    return in_order(root.left) + [root.value] + in_order(root.right)


def bfs(root: Optional[TreeNode]) -> list[int]:
    if root is None:
        return []
    result: list[int] = []
    queue: deque[TreeNode] = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:  queue.append(node.left)
        if node.right: queue.append(node.right)
    return result


def main() -> None:
    root: Optional[TreeNode] = None
    for v in [5, 3, 7, 1, 4]:
        root = insert(root, v)
    print("in-order:", in_order(root))  # [1, 3, 4, 5, 7]
    print("bfs:     ", bfs(root))       # [5, 3, 7, 1, 4]


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: trees_and_graphs.languages.scala -->
### scala

```scala
import scala.collection.mutable

object TreesAndGraphs {
  case class TreeNode(value: Int, var left: Option[TreeNode] = None, var right: Option[TreeNode] = None)

  def insert(root: Option[TreeNode], value: Int): TreeNode = root match {
    case None => TreeNode(value)
    case Some(node) =>
      if (value < node.value) node.left  = Some(insert(node.left,  value))
      else                    node.right = Some(insert(node.right, value))
      node
  }

  def inOrder(root: Option[TreeNode]): List[Int] = root match {
    case None       => Nil
    case Some(node) => inOrder(node.left) ::: node.value :: inOrder(node.right)
  }

  def bfs(root: Option[TreeNode]): List[Int] = {
    val queue  = mutable.Queue[TreeNode]()
    val result = mutable.ListBuffer[Int]()
    root.foreach(queue.enqueue)
    while (queue.nonEmpty) {
      val node = queue.dequeue()
      result += node.value
      node.left.foreach(queue.enqueue)
      node.right.foreach(queue.enqueue)
    }
    result.toList
  }

  def main(args: Array[String]): Unit = {
    var root: Option[TreeNode] = None
    for (v <- List(5, 3, 7, 1, 4)) root = Some(insert(root, v))
    println(s"in-order: ${inOrder(root)}")  // List(1, 3, 4, 5, 7)
    println(s"bfs:      ${bfs(root)}")      // List(5, 3, 7, 1, 4)
  }
}
```

<!-- REGISTRY_PATH: trees_and_graphs.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

interface TreeNode {
  value: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

function makeNode(value: number): TreeNode {
  return { value, left: null, right: null };
}

function insert(root: TreeNode | null, value: number): TreeNode {
  if (root === null) return makeNode(value);
  if (value < root.value) root.left  = insert(root.left,  value);
  else                    root.right = insert(root.right, value);
  return root;
}

function inOrder(root: TreeNode | null): number[] {
  if (root === null) return [];
  return [...inOrder(root.left), root.value, ...inOrder(root.right)];
}

function bfs(root: TreeNode | null): number[] {
  if (root === null) return [];
  const result: number[] = [];
  const queue: TreeNode[] = [root];
  while (queue.length > 0) {
    const node = queue.shift()!;
    result.push(node.value);
    if (node.left)  queue.push(node.left);
    if (node.right) queue.push(node.right);
  }
  return result;
}

function main(): void {
  let root: TreeNode | null = null;
  for (const v of [5, 3, 7, 1, 4]) root = insert(root, v);
  console.log("in-order:", inOrder(root));  // [1, 3, 4, 5, 7]
  console.log("bfs:     ", bfs(root));      // [5, 3, 7, 1, 4]
}

main();
```

## type_system_comparison

- Docs: /content/docs/type_system_comparison/README.md

<!-- REGISTRY_PATH: type_system_comparison.languages.cpp -->
### cpp

```cpp
// C++: static + nominal
constexpr int a = 2;
```

<!-- REGISTRY_PATH: type_system_comparison.languages.go -->
### go

```go
// Go: static + structural (interfaces are satisfied implicitly)
package main

import "fmt"

type N int

func (n N) Double() int { return int(n) * 2 }

type Doubler interface {
  Double() int
}

func twiceInt(x int) int { return x * 2 }

func main() {
  fmt.Println(twiceInt(4))
  var d Doubler = N(3)
  fmt.Println(d.Double())
}
```

<!-- REGISTRY_PATH: type_system_comparison.languages.python -->
### python

```python
# Python: dynamic duck typing
def twice(x): return x * 2
```

<!-- REGISTRY_PATH: type_system_comparison.languages.scala -->
### scala

```scala
// Scala: static + nominal (type inference + explicit types when desired)
object TypeSystemComparison {
  def twice(x: Int): Int = x * 2

  def main(args: Array[String]): Unit = {
    println(twice(3))
    // Scala is statically typed; mismatched types are a compile error
    // val s: String = 5 // would not compile
  }
}
```

<!-- REGISTRY_PATH: type_system_comparison.languages.typescript -->
### typescript

```typescript
// TypeScript: static + structural (interfaces are structural)
interface HasValue { value: number }

function twice(x: HasValue) {
  return x.value * 2
}

const a = { value: 3, extra: 'ok' }
console.log(twice(a))
```

