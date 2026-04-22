# Python Playground Setup Guide

This folder is a reference hub — not a runnable project itself.
Copy `example_project/` to start a new mini project, then follow the tiers below to grow it.

---

## Folder layout

```text
.setup/
    README.md                   <- you are here
    example_project/            <- copy this to start a new project
        pyproject.toml
        src/
            example_project/
                __init__.py
                __main__.py
                core.py
        tests/
            test_core.py
```

---

## Prerequisites (important)

Tool-based Python run/test requires a `.venv` in the project folder or workspace root.
The test tool uses `pytest` for Python projects.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -U pip
.\.venv\Scripts\python.exe -m pip install pytest
```

---

## Tier 1 — Single-file scratch pad

Good for quick experiments that fit in one file.

```text
playground/python/my_scratch/
    main.py
```

Minimal `main.py`:

```python
print("hello")
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
python main.py
python -m compileall .
```

Manual test (inside the project folder):

```powershell
# Add test_main.py first, then:
python -m unittest -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l python -p my_scratch
go run tools/test_playground.go -l python -p my_scratch
```

Note: tool-based testing requires `.venv` and `pytest`.

When to move up: when you want reusable functions/modules or repeatable tests.

---

## Tier 2 — Small module with tests

Keep things simple: one entry file, one logic file, one tests folder.

```text
playground/python/my_project/
    main.py
    calc.py
    tests/
        test_calc.py
```

Example `calc.py`:

```python
def add(a: int, b: int) -> int:
    return a + b
```

Example `tests/test_calc.py` (unittest style):

```python
import unittest

from calc import add


class TestCalc(unittest.TestCase):
    def test_add(self) -> None:
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
python main.py
python -m compileall .
```

Manual test (inside the project folder):

```powershell
python -m unittest discover -s tests -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l python -p my_project
go run tools/test_playground.go -l python -p my_project
```

Note: `pytest` runs all `test_*.py` files, including `unittest.TestCase` tests.

When to move up: when you need package imports that scale and cleaner dependency management.

---

## Tier 3 — Real package layout with pyproject (recommended)

Use the `src/` layout with `pyproject.toml` and a package `__main__.py`.
This is the pattern used by `example_project/` and `multi_file/`.

```text
playground/python/my_project/
    pyproject.toml
    src/
        my_project/
            __init__.py
            __main__.py
            core.py
    tests/
        test_core.py
```

`src/my_project/__main__.py`:

```python
from my_project.core import greet


def main() -> None:
    print(greet("world"))


if __name__ == "__main__":
    main()
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m my_project
```

Manual test (inside the project folder):

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest tests -q
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l python -p my_project
go run tools/test_playground.go -l python -p my_project
```

Note: when `pyproject.toml` and `src/<pkg>/__main__.py` exist, `run_playground` uses `python -m <pkg>`.

---

## Tier 4 — Better test quality with pytest patterns

Move from one-off tests to parametrized tests and focused failure messages.

Example `tests/test_core.py`:

```python
import pytest

from my_project.core import greet


@pytest.mark.parametrize(
    "name,expected",
    [
        ("Alice", "Alice"),
        ("world", "Hello"),
        ("", "Hello"),
    ],
)
def test_greet(name: str, expected: str) -> None:
    assert expected in greet(name)
```

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m my_project
```

Manual test (inside the project folder):

```powershell
.\.venv\Scripts\python.exe -m pytest tests -q
.\.venv\Scripts\python.exe -m pytest tests -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l python -p my_project
go run tools/test_playground.go -l python -p my_project
```

---

## Tier 5 — Advanced: custom commands with playground.json

When defaults are not enough (custom entrypoint, custom test arguments, env vars), add
`playground.json` in the mini project folder.

Example `playground.json`:

```json
{
    "workDir": ".",
    "env": {
        "PYTHONPATH": "src"
    },
    "build": [".venv/Scripts/python.exe", "-m", "pip", "install", "-e", "."],
    "run": [".venv/Scripts/python.exe", "-m", "my_project"],
    "test": [".venv/Scripts/python.exe", "-m", "pytest", "tests", "-q"]
}
```

See `tools/run_playground.go` and `tools/test_playground.go` for the full list of supported keys.

### Run/Test at this tier

Manual run/build (inside the project folder):

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m my_project
```

Manual test (inside the project folder):

```powershell
.\.venv\Scripts\python.exe -m pytest tests -q
.\.venv\Scripts\python.exe -m pytest tests -v
```

Tool run/test (from repository root):

```powershell
go run tools/run_playground.go -l python -p my_project
go run tools/test_playground.go -l python -p my_project
```

Note: at this tier, `playground.json` can override both run and test commands.

---

## Quick-start checklist

1. Copy `.setup/example_project/` to `playground/python/<your_name>/`.
2. Rename package folder `src/example_project/` to `src/<your_name>/`.
3. Update imports and module references in `__main__.py` and tests.
4. Create `.venv` and install dependencies.
5. Run: `go run tools/run_playground.go -l python -p <your_name>`
6. Test: `go run tools/test_playground.go -l python -p <your_name>`

---

## Testing checklist

- Name test files `test_*.py` for discovery.
- Keep tests deterministic (no network, no sleep-based timing).
- Cover happy path, at least one boundary, and one failure path.
- Use parametrized tests when inputs vary.
- Add a regression test for each bug fix.
