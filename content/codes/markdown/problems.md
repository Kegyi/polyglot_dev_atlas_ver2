# Codes registry — problems

This file contains code snippets exported from content/codes_registry.json.
Edit this file and run `scripts/update_registry_from_md.py` to push changes back.

## arrays_and_collections

- Docs: /content/docs/arrays_and_collections/README.md

<!-- REGISTRY_PATH: arrays_and_collections.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <numeric>
#include <vector>

int main() {
    std::vector<int> values{1, 2, 3, 4, 5};

    std::cout << "original: ";
    for (int v : values) {
        std::cout << v << ' ';
    }
    std::cout << "\n";

    std::vector<int> doubled(values.size());
    std::transform(values.begin(), values.end(), doubled.begin(), [](int x) {
        return x * 2;
    });

    std::vector<int> evens;
    std::copy_if(doubled.begin(), doubled.end(), std::back_inserter(evens), [](int x) {
        return x % 2 == 0;
    });

    int total = std::accumulate(evens.begin(), evens.end(), 0);
    std::cout << "sum of evens in doubled: " << total << "\n";
    return 0;
}
```

<!-- REGISTRY_PATH: arrays_and_collections.languages.go -->
### go

```go
package main

import "fmt"

func main() {
	values := []int{1, 2, 3, 4, 5}
	fmt.Println("original:", values)

	doubled := make([]int, 0, len(values))
	for _, v := range values {
		doubled = append(doubled, v*2)
	}

	evens := make([]int, 0, len(doubled))
	total := 0
	for _, v := range doubled {
		if v%2 == 0 {
			evens = append(evens, v)
			total += v
		}
	}

	fmt.Println("doubled:", doubled)
	fmt.Println("evens:", evens)
	fmt.Println("sum of evens in doubled:", total)
}
```

<!-- REGISTRY_PATH: arrays_and_collections.languages.python -->
### python

```python
#!/usr/bin/env python3

def main() -> None:
    values = [1, 2, 3, 4, 5]
    print("original:", values)

    doubled = [x * 2 for x in values]
    evens = [x for x in doubled if x % 2 == 0]

    print("doubled:", doubled)
    print("evens:", evens)
    print("sum of evens in doubled:", sum(evens))


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: arrays_and_collections.languages.scala -->
### scala

```scala
object ArraysAndCollectionsBasics {
  def main(args: Array[String]): Unit = {
    val values = Vector(1, 2, 3, 4, 5)
    println(s"original: $values")

    val doubled = values.map(_ * 2)
    val evens = doubled.filter(_ % 2 == 0)
    val total = evens.sum

    println(s"doubled: $doubled")
    println(s"evens: $evens")
    println(s"sum of evens in doubled: $total")
  }
}
```

<!-- REGISTRY_PATH: arrays_and_collections.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function main(): void {
  const values = [1, 2, 3, 4, 5];
  console.log("original:", values);

  const doubled = values.map((x) => x * 2);
  const evens = doubled.filter((x) => x % 2 === 0);
  const total = evens.reduce((sum, x) => sum + x, 0);

  console.log("doubled:", doubled);
  console.log("evens:", evens);
  console.log("sum of evens in doubled:", total);
}

main();
setImmediate(() => {});
```

## balanced_brackets

- Docs: /content/docs/balanced_brackets/README.md

<!-- REGISTRY_PATH: balanced_brackets.languages.cpp -->
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

<!-- REGISTRY_PATH: balanced_brackets.languages.go -->
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

<!-- REGISTRY_PATH: balanced_brackets.languages.python -->
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

<!-- REGISTRY_PATH: balanced_brackets.languages.scala -->
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

<!-- REGISTRY_PATH: balanced_brackets.languages.typescript -->
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

## bit_manipulation

- Docs: /content/docs/bit_manipulation/README.md

<!-- REGISTRY_PATH: bit_manipulation.languages.cpp -->
### cpp

```cpp
#include <bitset>
#include <iostream>

int countBits(int n) {
    int count = 0;
    while (n) { count += n & 1; n >>= 1; }
    return count;
}

int main() {
    int a = 0b1010, b = 0b1100;  // 10, 12
    std::cout << "a & b:  " << std::bitset<4>(a & b) << "\n";  // 1000
    std::cout << "a | b:  " << std::bitset<4>(a | b) << "\n";  // 1110
    std::cout << "a ^ b:  " << std::bitset<4>(a ^ b) << "\n";  // 0110

    int n = 0b0101;
    std::cout << "bit 1 set? " << ((n >> 1) & 1) << "\n";  // check -> 0
    n |= (1 << 2);                                          // set bit 2
    n &= ~(1 << 0);                                         // clear bit 0
    std::cout << "after set/clear: " << std::bitset<4>(n) << "\n";  // 0100

    std::cout << "count bits in 7: " << countBits(7) << "\n";  // 3
    return 0;
}
```

<!-- REGISTRY_PATH: bit_manipulation.languages.go -->
### go

```go
package main

import "fmt"

func countBits(n int) int {
	count := 0
	for n != 0 {
		count += n & 1
		n >>= 1
	}
	return count
}

func main() {
	a, b := 0b1010, 0b1100            // 10, 12
	fmt.Printf("a & b:  %04b\n", a&b) // 1000
	fmt.Printf("a | b:  %04b\n", a|b) // 1110
	fmt.Printf("a ^ b:  %04b\n", a^b) // 0110

	n := 0b0101
	fmt.Printf("bit 1 set? %d\n", (n>>1)&1)  // check -> 0
	n |= (1 << 2)                            // set bit 2
	n &^= (1 << 0)                           // clear bit 0
	fmt.Printf("after set/clear: %04b\n", n) // 0100

	fmt.Println("count bits in 7:", countBits(7)) // 3
}
```

<!-- REGISTRY_PATH: bit_manipulation.languages.python -->
### python

```python
#!/usr/bin/env python3


def count_bits(n: int) -> int:
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def main() -> None:
    a, b = 0b1010, 0b1100  # 10, 12
    print(f"a & b:  {a & b:04b}")  # 1000
    print(f"a | b:  {a | b:04b}")  # 1110
    print(f"a ^ b:  {a ^ b:04b}")  # 0110

    n = 0b0101
    print(f"bit 1 set? {(n >> 1) & 1}")  # check -> 0
    n |= (1 << 2)   # set bit 2
    n &= ~(1 << 0)  # clear bit 0
    print(f"after set/clear: {n:04b}")   # 0100

    print(f"count bits in 7: {count_bits(7)}")  # 3


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: bit_manipulation.languages.scala -->
### scala

```scala
object BitManipulation {
  def countBits(n: Int): Int = {
    var count = 0
    var x = n
    while (x != 0) { count += x & 1; x >>= 1 }
    count
  }

  def main(args: Array[String]): Unit = {
    val a = 10  // 1010 in binary
    val b = 12  // 1100 in binary
    println(s"a & b:  ${(a & b).toBinaryString}")  // 1000
    println(s"a | b:  ${(a | b).toBinaryString}")  // 1110
    println(s"a ^ b:  ${(a ^ b).toBinaryString}")  // 110

    var n = 5   // 0101 in binary
    println(s"bit 1 set? ${(n >> 1) & 1}")  // check -> 0
    n |= (1 << 2)    // set bit 2
    n &= ~(1 << 0)   // clear bit 0
    println(s"after set/clear: ${n.toBinaryString}")  // 100

    println(s"count bits in 7: ${countBits(7)}")  // 3
  }
}
```

<!-- REGISTRY_PATH: bit_manipulation.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

function countBits(n: number): number {
  let count = 0;
  while (n !== 0) {
    count += n & 1;
    n >>>= 1;
  }
  return count;
}

function main(): void {
  const a = 0b1010;  // 10
  const b = 0b1100;  // 12
  console.log("a & b: ", (a & b).toString(2).padStart(4, "0"));  // 1000
  console.log("a | b: ", (a | b).toString(2).padStart(4, "0"));  // 1110
  console.log("a ^ b: ", (a ^ b).toString(2).padStart(4, "0"));  // 0110

  let n = 0b0101;
  console.log("bit 1 set?", (n >> 1) & 1);  // check -> 0
  n |= (1 << 2);   // set bit 2
  n &= ~(1 << 0);  // clear bit 0
  console.log("after set/clear:", n.toString(2).padStart(4, "0"));  // 0100

  console.log("count bits in 7:", countBits(7));  // 3
}

main();
```

## concurrency_demo

- Docs: /content/docs/concurrency_demo/README.md

<!-- REGISTRY_PATH: concurrency_demo.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <numeric>
#include <future>
#include <thread>
#include <algorithm>

int partial_sum(const std::vector<int>& v, size_t start, size_t len) {
    return std::accumulate(v.begin() + start, v.begin() + start + len, 0);
}

int main() {
    const size_t N = 1000;
    std::vector<int> data(N);
    std::iota(data.begin(), data.end(), 1);
    size_t threads = std::thread::hardware_concurrency();
    if (threads == 0) threads = 4;
    size_t block = data.size() / threads;
    std::vector<std::future<int>> futs;
    for (size_t i = 0; i < threads; ++i) {
        size_t s = i * block;
        size_t len = (i + 1 == threads) ? data.size() - s : block;
        futs.push_back(std::async(std::launch::async, [s, len, &data]() {
            return partial_sum(data, s, len);
        }));
    }
    int total = 0;
    for (auto &f : futs) total += f.get();
    std::cout << "Total: " << total << std::endl;
    return 0;
}
```

<!-- REGISTRY_PATH: concurrency_demo.languages.go -->
### go

```go
package main

import (
    "fmt"
    "runtime"
    "sync"
)

func main() {
    n := 1000
    data := make([]int, n)
    for i := 0; i < n; i++ { data[i] = i + 1 }
    threads := runtime.NumCPU()
    if threads < 1 { threads = 4 }
    block := n / threads
    var wg sync.WaitGroup
    ch := make(chan int, threads)
    for i := 0; i < threads; i++ {
        s := i * block
        end := (i+1) * block
        if i == threads-1 { end = n }
        wg.Add(1)
        go func(start, end int) {
            defer wg.Done()
            sum := 0
            for j := start; j < end; j++ { sum += data[j] }
            ch <- sum
        }(s, end)
    }
    wg.Wait()
    close(ch)
    total := 0
    for v := range ch { total += v }
    fmt.Println("Total:", total)
}
```

<!-- REGISTRY_PATH: concurrency_demo.languages.python -->
### python

```python
#!/usr/bin/env python3
from concurrent.futures import ThreadPoolExecutor

def partial_sum(slice_data):
    return sum(slice_data)

def main():
    n = 1000
    data = list(range(1, n+1))
    threads = min(8, max(1, len(data) // 100))
    chunk = len(data) // threads
    chunks = [data[i*chunk:(i+1)*chunk] for i in range(threads-1)]
    chunks.append(data[(threads-1)*chunk:])
    with ThreadPoolExecutor(max_workers=threads) as ex:
        results = list(ex.map(partial_sum, chunks))
    print("Total:", sum(results))

if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: concurrency_demo.languages.scala -->
### scala

```scala
import scala.concurrent.{Future, Await}
import scala.concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.Duration

object ConcurrencyDemo {
  def main(args: Array[String]): Unit = {
  val n = 1000
  val data = (1 to n).toArray
  val threads = Runtime.getRuntime.availableProcessors()
  val block = n / threads
  val futures = (0 until threads).map { i =>
    Future {
      val s = i * block
      val e = if (i == threads - 1) n else (i + 1) * block
      (s until e).map(j => data(j)).sum
    }
  }
  val results = Await.result(Future.sequence(futures), Duration.Inf)
  println("Total: " + results.sum)
  }
}
```

<!-- REGISTRY_PATH: concurrency_demo.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node

import { setImmediate } from "node:timers";

function partialSum(arr: number[]): Promise<number> {
  return new Promise((resolve) => {
    setImmediate(() => {
      resolve(arr.reduce((a, b) => a + b, 0));
    });
  });
}

async function main() {
  const n = 1000;
  const data = Array.from({ length: n }, (_, i) => i + 1);
  const workers = Math.min(8, Math.max(1, Math.floor(n / 100)));
  const chunk = Math.floor(n / workers);
  const chunks: number[][] = [];

  for (let i = 0; i < workers; i++) {
    const start = i * chunk;
    const end = i + 1 === workers ? n : (i + 1) * chunk;
    chunks.push(data.slice(start, end));
  }

  const results = await Promise.all(chunks.map((values) => partialSum(values)));
  console.log("Total:", results.reduce((a, b) => a + b, 0));
}

main().catch((err) => {
  console.error("Error:", err);
  process.exit(1);
});
```

## grid_shortest_path

- Docs: /content/docs/grid_shortest_path/README.md

<!-- REGISTRY_PATH: grid_shortest_path.languages.cpp -->
### cpp

```cpp
#include <array>
#include <iostream>
#include <queue>
#include <utility>
#include <vector>

int shortestPathSteps(const std::vector<std::vector<int>>& grid) {
    const int rows = static_cast<int>(grid.size());
    const int cols = static_cast<int>(grid[0].size());
    if (grid[0][0] == 1 || grid[rows - 1][cols - 1] == 1) {
        return -1;
    }

    std::vector<std::vector<int>> dist(rows, std::vector<int>(cols, -1));
    std::queue<std::pair<int, int>> q;
    q.push({0, 0});
    dist[0][0] = 0;

    const std::array<std::pair<int, int>, 4> dirs = {{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}};

    while (!q.empty()) {
        auto [r, c] = q.front();
        q.pop();

        if (r == rows - 1 && c == cols - 1) {
            return dist[r][c];
        }

        for (auto [dr, dc] : dirs) {
            int nr = r + dr;
            int nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
                continue;
            }
            if (grid[nr][nc] == 1 || dist[nr][nc] != -1) {
                continue;
            }
            dist[nr][nc] = dist[r][c] + 1;
            q.push({nr, nc});
        }
    }

    return -1;
}

int main() {
    const std::vector<std::vector<int>> grid = {
        {0, 0, 1, 0, 0},
        {1, 0, 1, 0, 1},
        {0, 0, 0, 0, 0},
        {0, 1, 1, 1, 0},
        {0, 0, 0, 1, 0}
    };

    std::cout << "shortest steps: " << shortestPathSteps(grid) << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: grid_shortest_path.languages.go -->
### go

```go
package main

import "fmt"

type point struct {
	r int
	c int
}

func shortestPathSteps(grid [][]int) int {
	rows := len(grid)
	cols := len(grid[0])
	if grid[0][0] == 1 || grid[rows-1][cols-1] == 1 {
		return -1
	}

	dist := make([][]int, rows)
	for r := 0; r < rows; r++ {
		dist[r] = make([]int, cols)
		for c := 0; c < cols; c++ {
			dist[r][c] = -1
		}
	}

	dirs := []point{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	queue := []point{{0, 0}}
	dist[0][0] = 0

	for len(queue) > 0 {
		cur := queue[0]
		queue = queue[1:]

		if cur.r == rows-1 && cur.c == cols-1 {
			return dist[cur.r][cur.c]
		}

		for _, d := range dirs {
			nr := cur.r + d.r
			nc := cur.c + d.c
			if nr < 0 || nr >= rows || nc < 0 || nc >= cols {
				continue
			}
			if grid[nr][nc] == 1 || dist[nr][nc] != -1 {
				continue
			}
			dist[nr][nc] = dist[cur.r][cur.c] + 1
			queue = append(queue, point{nr, nc})
		}
	}

	return -1
}

func main() {
	grid := [][]int{
		{0, 0, 1, 0, 0},
		{1, 0, 1, 0, 1},
		{0, 0, 0, 0, 0},
		{0, 1, 1, 1, 0},
		{0, 0, 0, 1, 0},
	}

	fmt.Printf("shortest steps: %d\n", shortestPathSteps(grid))
}
```

<!-- REGISTRY_PATH: grid_shortest_path.languages.python -->
### python

```python
from collections import deque


def shortest_path_steps(grid: list[list[int]]) -> int:
    rows = len(grid)
    cols = len(grid[0])

    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    dist = [[-1] * cols for _ in range(rows)]
    q: deque[tuple[int, int]] = deque([(0, 0)])
    dist[0][0] = 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while q:
        r, c = q.popleft()
        if r == rows - 1 and c == cols - 1:
            return dist[r][c]

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue
            if grid[nr][nc] == 1 or dist[nr][nc] != -1:
                continue
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

    return -1


def main() -> None:
    grid = [
        [0, 0, 1, 0, 0],
        [1, 0, 1, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
    ]

    print(f"shortest steps: {shortest_path_steps(grid)}")


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: grid_shortest_path.languages.scala -->
### scala

```scala
object GridShortestPath {
  private val dirs = List((1, 0), (-1, 0), (0, 1), (0, -1))

  def shortestPathSteps(grid: Vector[Vector[Int]]): Int = {
    val rows = grid.length
    val cols = grid.head.length

    if (grid(0)(0) == 1 || grid(rows - 1)(cols - 1) == 1) {
      return -1
    }

    val dist = Array.fill(rows, cols)(-1)
    val q = scala.collection.mutable.Queue[(Int, Int)]()
    q.enqueue((0, 0))
    dist(0)(0) = 0

    while (q.nonEmpty) {
      val (r, c) = q.dequeue()
      if (r == rows - 1 && c == cols - 1) {
        return dist(r)(c)
      }

      dirs.foreach { case (dr, dc) =>
        val nr = r + dr
        val nc = c + dc
        val inBounds = nr >= 0 && nr < rows && nc >= 0 && nc < cols
        if (inBounds && grid(nr)(nc) == 0 && dist(nr)(nc) == -1) {
          dist(nr)(nc) = dist(r)(c) + 1
          q.enqueue((nr, nc))
        }
      }
    }

    -1
  }

  def main(args: Array[String]): Unit = {
    val grid = Vector(
      Vector(0, 0, 1, 0, 0),
      Vector(1, 0, 1, 0, 1),
      Vector(0, 0, 0, 0, 0),
      Vector(0, 1, 1, 1, 0),
      Vector(0, 0, 0, 1, 0)
    )

    println(s"shortest steps: ${shortestPathSteps(grid)}")
  }
}
```

<!-- REGISTRY_PATH: grid_shortest_path.languages.typescript -->
### typescript

```typescript
type Point = { r: number; c: number };

function shortestPathSteps(grid: number[][]): number {
  const rows = grid.length;
  const cols = grid[0].length;

  if (grid[0][0] === 1 || grid[rows - 1][cols - 1] === 1) {
    return -1;
  }

  const dist = Array.from({ length: rows }, () => Array(cols).fill(-1));
  const queue: Point[] = [{ r: 0, c: 0 }];
  dist[0][0] = 0;

  const dirs: Point[] = [
    { r: 1, c: 0 },
    { r: -1, c: 0 },
    { r: 0, c: 1 },
    { r: 0, c: -1 },
  ];

  for (let head = 0; head < queue.length; head++) {
    const { r, c } = queue[head];

    if (r === rows - 1 && c === cols - 1) {
      return dist[r][c];
    }

    for (const d of dirs) {
      const nr = r + d.r;
      const nc = c + d.c;
      if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) {
        continue;
      }
      if (grid[nr][nc] === 1 || dist[nr][nc] !== -1) {
        continue;
      }

      dist[nr][nc] = dist[r][c] + 1;
      queue.push({ r: nr, c: nc });
    }
  }

  return -1;
}

function main(): void {
  const grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
  ];

  console.log(`shortest steps: ${shortestPathSteps(grid)}`);
}

main();
```

## matrix_mul

- Docs: /content/docs/matrix_mul/README.md

<!-- REGISTRY_PATH: matrix_mul.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <vector>
#include <numeric>

int main() {
    const int N = 200;
    std::vector<std::vector<int>> A(N, std::vector<int>(N)), B(N, std::vector<int>(N)), C(N, std::vector<int>(N, 0));
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) {
            A[i][j] = i + j;
            B[i][j] = i - j;
        }
    for (int i = 0; i < N; ++i)
        for (int k = 0; k < N; ++k)
            for (int j = 0; j < N; ++j)
                C[i][j] += A[i][k] * B[k][j];
    std::cout << C[0][0] << std::endl;
    return 0;
}
```

<!-- REGISTRY_PATH: matrix_mul.languages.go -->
### go

```go
package main

import "fmt"

func main() {
    const N = 200
    A := make([][]int, N)
    B := make([][]int, N)
    C := make([][]int, N)
    for i := 0; i < N; i++ {
        A[i] = make([]int, N)
        B[i] = make([]int, N)
        C[i] = make([]int, N)
        for j := 0; j < N; j++ {
            A[i][j] = i + j
            B[i][j] = i - j
        }
    }
    for i := 0; i < N; i++ {
        for k := 0; k < N; k++ {
            for j := 0; j < N; j++ {
                C[i][j] += A[i][k] * B[k][j]
            }
        }
    }
    fmt.Println(C[0][0])
}
```

<!-- REGISTRY_PATH: matrix_mul.languages.python -->
### python

```python
def make_matrix(n, init):
    return [[init(i, j) for j in range(n)] for i in range(n)]


def main():
    N = 200
    A = make_matrix(N, lambda i, j: i + j)
    B = make_matrix(N, lambda i, j: i - j)
    C = [[0] * N for _ in range(N)]
    for i in range(N):
        for k in range(N):
            aik = A[i][k]
            for j in range(N):
                C[i][j] += aik * B[k][j]
    print(C[0][0])


if __name__ == '__main__':
    main()
```

<!-- REGISTRY_PATH: matrix_mul.languages.scala -->
### scala

```scala
object MatrixMul {
  def main(args: Array[String]): Unit = {
    val N = 200
    val A = Array.tabulate(N, N)((i, j) => i + j)
    val B = Array.tabulate(N, N)((i, j) => i - j)
    val C = Array.ofDim[Int](N, N)
    for (i <- 0 until N)
      for (k <- 0 until N)
        for (j <- 0 until N)
          C(i)(j) += A(i)(k) * B(k)(j)
    println(C(0)(0))
  }
}
```

<!-- REGISTRY_PATH: matrix_mul.languages.typescript -->
### typescript

```typescript
import { setImmediate } from "node:timers";

function makeMatrix(n: number, fn: (i: number, j: number) => number): number[][] {
  const M: number[][] = []
  for (let i = 0; i < n; i++) {
    M[i] = []
    for (let j = 0; j < n; j++) M[i][j] = fn(i, j)
  }
  return M
}

async function main() {
  const N = 200
  const A = makeMatrix(N, (i, j) => i + j)
  const B = makeMatrix(N, (i, j) => i - j)
  const C: number[][] = Array.from({ length: N }, () => Array(N).fill(0))
  for (let i = 0; i < N; i++) {
    for (let k = 0; k < N; k++) {
      const aik = A[i][k]
      for (let j = 0; j < N; j++) C[i][j] += aik * B[k][j]
    }
  }
  await new Promise<void>((resolve) => setImmediate(resolve))
  console.log(C[0][0])
}

main().catch((err) => {
  console.error("Error:", err)
  process.exit(1)
})
```

## top_k_frequent

- Docs: /content/docs/top_k_frequent/README.md

<!-- REGISTRY_PATH: top_k_frequent.languages.cpp -->
### cpp

```cpp
#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <utility>
#include <vector>

std::vector<int> topKFrequent(const std::vector<int>& nums, int k) {
    std::unordered_map<int, int> freq;
    for (int n : nums) {
        ++freq[n];
    }

    using Entry = std::pair<int, int>;  // (frequency, value)
    auto cmp = [](const Entry& a, const Entry& b) { return a.first > b.first; };
    std::priority_queue<Entry, std::vector<Entry>, decltype(cmp)> minHeap(cmp);

    for (const auto& [value, count] : freq) {
        minHeap.push({count, value});
        if (static_cast<int>(minHeap.size()) > k) {
            minHeap.pop();
        }
    }

    std::vector<int> result;
    while (!minHeap.empty()) {
        result.push_back(minHeap.top().second);
        minHeap.pop();
    }
    std::reverse(result.begin(), result.end());
    return result;
}

int main() {
    const std::vector<int> nums = {1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5};
    const int k = 2;

    const auto result = topKFrequent(nums, k);
    std::cout << "top k frequent:";
    for (int n : result) {
        std::cout << ' ' << n;
    }
    std::cout << '\n';
    return 0;
}
```

<!-- REGISTRY_PATH: top_k_frequent.languages.go -->
### go

```go
package main

import (
	"container/heap"
	"fmt"
)

type entry struct {
	count int
	value int
}

type minHeap []entry

func (h minHeap) Len() int { return len(h) }

func (h minHeap) Less(i, j int) bool { return h[i].count < h[j].count }

func (h minHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *minHeap) Push(x any) {
	*h = append(*h, x.(entry))
}

func (h *minHeap) Pop() any {
	old := *h
	n := len(old)
	out := old[n-1]
	*h = old[:n-1]
	return out
}

func topKFrequent(nums []int, k int) []int {
	freq := map[int]int{}
	for _, n := range nums {
		freq[n]++
	}

	h := &minHeap{}
	heap.Init(h)

	for value, count := range freq {
		heap.Push(h, entry{count: count, value: value})
		if h.Len() > k {
			heap.Pop(h)
		}
	}

	result := make([]int, h.Len())
	for i := len(result) - 1; i >= 0; i-- {
		result[i] = heap.Pop(h).(entry).value
	}
	return result
}

func main() {
	nums := []int{1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5}
	k := 2
	result := topKFrequent(nums, k)

	fmt.Print("top k frequent:")
	for _, v := range result {
		fmt.Printf(" %d", v)
	}
	fmt.Println()
}
```

<!-- REGISTRY_PATH: top_k_frequent.languages.python -->
### python

```python
from collections import Counter
import heapq


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    heap: list[tuple[int, int]] = []

    for value, count in freq.items():
        heapq.heappush(heap, (count, value))
        if len(heap) > k:
            heapq.heappop(heap)

    # Highest-frequency values should be first in the final output.
    return [value for _, value in sorted(heap, reverse=True)]


def main() -> None:
    nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5]
    k = 2
    result = top_k_frequent(nums, k)
    print("top k frequent:", *result)


if __name__ == "__main__":
    main()
```

<!-- REGISTRY_PATH: top_k_frequent.languages.scala -->
### scala

```scala
object TopKFrequent {
  def topKFrequent(nums: Vector[Int], k: Int): Vector[Int] = {
    nums
      .groupBy(identity)
      .view
      .mapValues(_.length)
      .toVector
      .sortBy { case (_, count) => -count }
      .take(k)
      .map { case (value, _) => value }
  }

  def main(args: Array[String]): Unit = {
    val nums = Vector(1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5)
    val k = 2
    val result = topKFrequent(nums, k)

    println("top k frequent: " + result.mkString(" "))
  }
}
```

<!-- REGISTRY_PATH: top_k_frequent.languages.typescript -->
### typescript

```typescript
function topKFrequent(nums: number[], k: number): number[] {
  const freq = new Map<number, number>();
  for (const n of nums) {
    freq.set(n, (freq.get(n) ?? 0) + 1);
  }

  const pairs = Array.from(freq.entries()).map(([value, count]) => ({ value, count }));
  pairs.sort((a, b) => b.count - a.count);

  return pairs.slice(0, k).map((p) => p.value);
}

function main(): void {
  const nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5];
  const k = 2;
  const result = topKFrequent(nums, k);

  console.log("top k frequent:", ...result);
}

main();
```

## word_count

- Docs: /content/docs/word_count/README.md

<!-- REGISTRY_PATH: word_count.languages.cpp -->
### cpp

```cpp
#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>
#include <cctype>

int main(int argc, char** argv) {
    std::string path = (argc > 1) ? argv[1] : "data.txt";
    std::ifstream in(path);
    if (!in) { std::cerr << "Cannot open " << path << std::endl; return 1; }
    std::unordered_map<std::string,int> counts;
    std::string token;
    while (in >> token) {
        std::string w;
        for (char ch : token) {
            if (std::isalpha(static_cast<unsigned char>(ch))) w.push_back(std::tolower(static_cast<unsigned char>(ch)));
        }
        if (!w.empty()) ++counts[w];
    }
    std::vector<std::pair<std::string,int>> vec(counts.begin(), counts.end());
    std::sort(vec.begin(), vec.end(), [](const auto& a, const auto& b){ return a.second > b.second; });
    for (const auto& p : vec) std::cout << p.first << ": " << p.second << std::endl;
    return 0;
}
```

<!-- REGISTRY_PATH: word_count.languages.go -->
### go

```go
package main

import (
    "bufio"
    "fmt"
    "os"
    "sort"
    "strings"
)

func main() {
    path := "data.txt"
    if len(os.Args) > 1 { path = os.Args[1] }
    f, err := os.Open(path)
    if err != nil { fmt.Println("Error:", err); os.Exit(1) }
    defer f.Close()
    scanner := bufio.NewScanner(f)
    scanner.Split(bufio.ScanWords)
    counts := map[string]int{}
    for scanner.Scan() {
        w := strings.ToLower(scanner.Text())
        // keep only letters
        filtered := ""
        for _, r := range w { if (r >= 'a' && r <= 'z') || (r >= '0' && r <= '9') { filtered += string(r) } }
        if filtered != "" { counts[filtered]++ }
    }
    type P struct{ K string; V int }
    arr := make([]P, 0, len(counts))
    for k, v := range counts { arr = append(arr, P{k, v}) }
    sort.Slice(arr, func(i, j int) bool { return arr[i].V > arr[j].V })
    for _, p := range arr { fmt.Printf("%s: %d\n", p.K, p.V) }
}
```

<!-- REGISTRY_PATH: word_count.languages.python -->
### python

```python
#!/usr/bin/env python3
from collections import Counter
import re
import sys

def word_count(path='data.txt'):
    with open(path, 'r', encoding='utf-8') as fh:
        text = fh.read().lower()
    words = re.findall(r"\b\w+\b", text)
    return Counter(words)

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else 'data.txt'
    cnt = word_count(path)
    for w, c in cnt.most_common():
        print(f"{w}: {c}")

if __name__ == '__main__':
    main()
```

<!-- REGISTRY_PATH: word_count.languages.scala -->
### scala

```scala
import scala.io.Source

object WordCount {
  def main(args: Array[String]): Unit = {
    val path = if (args.nonEmpty) args(0) else "data.txt"

    val source = Source.fromFile(path)
    val text = try source.mkString.toLowerCase finally source.close()

    val words = "\\w+".r.findAllIn(text).toList
    val counts = words.groupBy(identity).view.mapValues(_.size).toSeq.sortBy(-_._2)
    counts.foreach { case (w, c) => println(s"$w: $c") }
  }
}
```

<!-- REGISTRY_PATH: word_count.languages.typescript -->
### typescript

```typescript
#!/usr/bin/env ts-node
import { promises as fs } from 'fs';

async function main() {
    const path = process.argv[2] || 'data.txt';
    const text = await fs.readFile(path, 'utf8');
    const words = text.toLowerCase().match(/\b\w+\b/g) || [];
    const m = new Map<string, number>();
    for (const w of words) m.set(w, (m.get(w) || 0) + 1);
    const arr = Array.from(m.entries()).sort((a,b) => b[1] - a[1]);
    for (const [k,v] of arr) console.log(`${k}: ${v}`);
}

main().catch(e => { console.error('Error:', e); process.exit(1); });
```

