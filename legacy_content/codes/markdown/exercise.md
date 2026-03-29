# Codes registry — exercise

This file contains code snippets exported from legacy_content/codes_registry.json.
Edit this file and run `scripts/update_registry_from_md.py` to push changes back.

## array_reverse

<!-- REGISTRY_PATH: array_reverse.languages.cpp -->
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

<!-- REGISTRY_PATH: array_reverse.languages.go -->
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

<!-- REGISTRY_PATH: array_reverse.languages.python -->
### python

```python
arr = [1, 2, 3, 4, 5]
arr.reverse()  # or arr = arr[::-1]
print(arr)
```

<!-- REGISTRY_PATH: array_reverse.languages.scala2 -->
### scala2

```scala2
val arr = List(1, 2, 3, 4, 5)
val reversed = arr.reverse
println(reversed)
```

<!-- REGISTRY_PATH: array_reverse.languages.scala3 -->
### scala3

```scala3
val arr = List(1, 2, 3, 4, 5)
val reversed = arr.reverse
println(reversed)
```

<!-- REGISTRY_PATH: array_reverse.languages.typescript -->
### typescript

```typescript
const arr = [1, 2, 3, 4, 5];
arr.reverse();
console.log(arr);
```

## even_odd

<!-- REGISTRY_PATH: even_odd.languages.cpp -->
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

<!-- REGISTRY_PATH: even_odd.languages.go -->
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

<!-- REGISTRY_PATH: even_odd.languages.python -->
### python

```python
n = int(input("Enter a number: "))
if n % 2 == 0:
    print(f"{n} is even")
else:
    print(f"{n} is odd")
```

<!-- REGISTRY_PATH: even_odd.languages.scala2 -->
### scala2

```scala2
val n = scala.io.StdIn.readInt()
if (n % 2 == 0) println(s"$n is even")
else println(s"$n is odd")
```

<!-- REGISTRY_PATH: even_odd.languages.scala3 -->
### scala3

```scala3
val n = scala.io.StdIn.readInt()
if n % 2 == 0 then println(s"$n is even")
else println(s"$n is odd")
```

<!-- REGISTRY_PATH: even_odd.languages.typescript -->
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

## fibonacci

<!-- REGISTRY_PATH: fibonacci.languages.cpp -->
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

<!-- REGISTRY_PATH: fibonacci.languages.go -->
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

<!-- REGISTRY_PATH: fibonacci.languages.python -->
### python

```python
n = int(input("Enter number of terms: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
```

<!-- REGISTRY_PATH: fibonacci.languages.scala2 -->
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

<!-- REGISTRY_PATH: fibonacci.languages.scala3 -->
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

<!-- REGISTRY_PATH: fibonacci.languages.typescript -->
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

## fizzbuzz

<!-- REGISTRY_PATH: fizzbuzz.languages.cpp -->
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

<!-- REGISTRY_PATH: fizzbuzz.languages.go -->
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

<!-- REGISTRY_PATH: fizzbuzz.languages.python -->
### python

```python
for i in range(1, 101):
    if i % 15 == 0: print("FizzBuzz")
    elif i % 3 == 0: print("Fizz")
    elif i % 5 == 0: print("Buzz")
    else: print(i)
```

<!-- REGISTRY_PATH: fizzbuzz.languages.scala2 -->
### scala2

```scala2
(1 to 100).foreach { i =>
  if (i % 15 == 0) println("FizzBuzz")
  else if (i % 3 == 0) println("Fizz")
  else if (i % 5 == 0) println("Buzz")
  else println(i)
}
```

<!-- REGISTRY_PATH: fizzbuzz.languages.scala3 -->
### scala3

```scala3
(1 to 100).foreach { i =>
  if i % 15 == 0 then println("FizzBuzz")
  else if i % 3 == 0 then println("Fizz")
  else if i % 5 == 0 then println("Buzz")
  else println(i)
}
```

<!-- REGISTRY_PATH: fizzbuzz.languages.typescript -->
### typescript

```typescript
for (let i = 1; i <= 100; i++) {
  if (i % 15 === 0) console.log("FizzBuzz");
  else if (i % 3 === 0) console.log("Fizz");
  else if (i % 5 === 0) console.log("Buzz");
  else console.log(i);
}
```

## hello_world

<!-- REGISTRY_PATH: hello_world.languages.cpp -->
### cpp

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!\
";
    return 0;
}
```

<!-- REGISTRY_PATH: hello_world.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

<!-- REGISTRY_PATH: hello_world.languages.python -->
### python

```python
print("Hello, World!")
```

<!-- REGISTRY_PATH: hello_world.languages.scala2 -->
### scala2

```scala2
object Main extends App {
  println("Hello, World!")
}
```

<!-- REGISTRY_PATH: hello_world.languages.scala3 -->
### scala3

```scala3
@main def hello(): Unit =
  println("Hello, World!")
```

<!-- REGISTRY_PATH: hello_world.languages.typescript -->
### typescript

```typescript
console.log("Hello, World!");
```

## palindrome

<!-- REGISTRY_PATH: palindrome.languages.cpp -->
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

<!-- REGISTRY_PATH: palindrome.languages.go -->
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

<!-- REGISTRY_PATH: palindrome.languages.python -->
### python

```python
s = "A man, a plan, a canal: Panama"
cleaned = "".join(c.lower() for c in s if c.isalnum())
is_palin = cleaned == cleaned[::-1]
print("Palindrome" if is_palin else "Not a palindrome")
```

<!-- REGISTRY_PATH: palindrome.languages.scala2 -->
### scala2

```scala2
val s = "A man, a plan, a canal: Panama"
val cleaned = s.filter(_.isLetterOrDigit).toLowerCase
val isPalin = cleaned == cleaned.reverse
println(if (isPalin) "Palindrome" else "Not a palindrome")
```

<!-- REGISTRY_PATH: palindrome.languages.scala3 -->
### scala3

```scala3
val s = "A man, a plan, a canal: Panama"
val cleaned = s.filter(_.isLetterOrDigit).toLowerCase
val isPalin = cleaned == cleaned.reverse
println(if isPalin then "Palindrome" else "Not a palindrome")
```

<!-- REGISTRY_PATH: palindrome.languages.typescript -->
### typescript

```typescript
const s = "A man, a plan, a canal: Panama";
const cleaned = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
const isPalin = cleaned === cleaned.split("").reverse().join("");
console.log(isPalin ? "Palindrome" : "Not a palindrome");
```

## parallel_aggregator

<!-- REGISTRY_PATH: parallel_aggregator.languages.cpp -->
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

<!-- REGISTRY_PATH: parallel_aggregator.languages.go -->
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

<!-- REGISTRY_PATH: parallel_aggregator.languages.python -->
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

<!-- REGISTRY_PATH: parallel_aggregator.languages.scala2 -->
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

<!-- REGISTRY_PATH: parallel_aggregator.languages.scala3 -->
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

<!-- REGISTRY_PATH: parallel_aggregator.languages.typescript -->
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

## stream_processor

<!-- REGISTRY_PATH: stream_processor.languages.cpp -->
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

<!-- REGISTRY_PATH: stream_processor.languages.go -->
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

<!-- REGISTRY_PATH: stream_processor.languages.python -->
### python

```python
nums = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum(n**2 for n in nums if n % 2 == 0)
print(f"Sum of squares of even numbers: {result}")
```

<!-- REGISTRY_PATH: stream_processor.languages.scala2 -->
### scala2

```scala2
val nums = List(1, 2, 3, 4, 5, 6, 7, 8)
val result = nums
  .filter(_ % 2 == 0)
  .map(n => n * n)
  .sum

println(s"Sum of squares of even numbers: $result")
```

<!-- REGISTRY_PATH: stream_processor.languages.scala3 -->
### scala3

```scala3
val nums = List(1, 2, 3, 4, 5, 6, 7, 8)
val result = nums
  .filter(_ % 2 == 0)
  .map(n => n * n)
  .sum

println(s"Sum of squares of even numbers: $result")
```

<!-- REGISTRY_PATH: stream_processor.languages.typescript -->
### typescript

```typescript
const nums = [1, 2, 3, 4, 5, 6, 7, 8];
const result = nums
  .filter(n => n % 2 === 0)
  .map(n => n * n)
  .reduce((a, b) => a + b, 0);

console.log(`Sum of squares of even numbers: ${result}`);
```

## temperature_converter

<!-- REGISTRY_PATH: temperature_converter.languages.cpp -->
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

<!-- REGISTRY_PATH: temperature_converter.languages.go -->
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

<!-- REGISTRY_PATH: temperature_converter.languages.python -->
### python

```python
celsius = 25.0
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"{celsius} deg C = {fahrenheit:.2f} deg F = {kelvin:.2f}K")
```

<!-- REGISTRY_PATH: temperature_converter.languages.scala2 -->
### scala2

```scala2
val celsius = 25.0
val fahrenheit = (celsius * 9/5) + 32
val kelvin = celsius + 273.15

println(f"$celsius deg C = $fahrenheit%.2f deg F = $kelvin%.2f K")
```

<!-- REGISTRY_PATH: temperature_converter.languages.scala3 -->
### scala3

```scala3
val celsius = 25.0
val fahrenheit = (celsius * 9/5) + 32
val kelvin = celsius + 273.15

println(f"$celsius deg C = $fahrenheit%.2f deg F = $kelvin%.2f K")
```

<!-- REGISTRY_PATH: temperature_converter.languages.typescript -->
### typescript

```typescript
const celsius = 25.0;
const fahrenheit = (celsius * 9/5) + 32;
const kelvin = celsius + 273.15;

console.log(`${celsius} deg C = ${fahrenheit.toFixed(2)} deg F = ${kelvin.toFixed(2)}K`);
```

## tree_traversal

<!-- REGISTRY_PATH: tree_traversal.languages.cpp -->
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

<!-- REGISTRY_PATH: tree_traversal.languages.go -->
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

<!-- REGISTRY_PATH: tree_traversal.languages.python -->
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

<!-- REGISTRY_PATH: tree_traversal.languages.scala2 -->
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

<!-- REGISTRY_PATH: tree_traversal.languages.scala3 -->
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

<!-- REGISTRY_PATH: tree_traversal.languages.typescript -->
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

## word_frequency

<!-- REGISTRY_PATH: word_frequency.languages.cpp -->
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

<!-- REGISTRY_PATH: word_frequency.languages.go -->
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

<!-- REGISTRY_PATH: word_frequency.languages.python -->
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

<!-- REGISTRY_PATH: word_frequency.languages.scala2 -->
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

<!-- REGISTRY_PATH: word_frequency.languages.scala3 -->
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

<!-- REGISTRY_PATH: word_frequency.languages.typescript -->
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

