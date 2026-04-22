# Python Playground

Create mini projects as subfolders under this folder.

## Create Your Own Mini Project

Example folder:

```text
playground/python/my_project/
  pyproject.toml
  src/
	my_project/
	  __init__.py
	  __main__.py
	  calc.py
  tests/
	test_calc.py
```

Minimal `src/my_project/__main__.py`:

```python
from my_project.calc import add


def main() -> None:
	print(add(2, 3))


if __name__ == "__main__":
	main()
```

Run with the playground runner from repository root:

```powershell
go run tools/run_playground.go -l python -p my_project
```

Run tests with the playground test runner from repository root:

```powershell
go run tools/test_playground.go -l python -p my_project
```

Note: Python tool-based run/test requires a `.venv` in the project folder or workspace root.

If defaults are not enough, add `playground.json` in the mini project folder.

## Testing Guide (Beginner)

You can start with built-in `unittest` (no extra package needed), then move to `pytest` later.

Example `src/my_project/calc.py`:

```python
def add(a: int, b: int) -> int:
	return a + b
```

Example `tests/test_calc.py` using `unittest`:

```python
import unittest

from my_project.calc import add


class TestCalc(unittest.TestCase):
	def test_add(self) -> None:
		self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
	unittest.main()
```

Run tests:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -q
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Optional `pytest` flow:

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest -q
```

Testing checklist:

- Name test files as `test_*.py` for easy discovery.
- Keep each test focused on one behavior.
- Add edge-case tests (empty strings, zero, None handling) early.

Recommended real-life project layout:

- `pyproject.toml`
- `src/<package_name>/__main__.py`
- `src/<package_name>/...`
- `tests/...`

Default runner behavior:

- If `pyproject.toml` exists and a `src` package contains `__main__.py`, runs it as a module.
- Otherwise falls back to `main.py`, `app.py`, `run.py`, or `__main__.py`.
- If only one Python file exists, runs that file.

Use `playground.json` when you want custom commands.

Test runner behavior:

- `tools/test_playground.go` runs `python -m pytest <project_dir>`.
- If `pytest` is not installed in `.venv`, tool-based testing fails.

## Manual Build Guidance

From a mini project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
.\.venv\Scripts\python.exe -m <package_name>
```

Run tests (if present):

```powershell
.\.venv\Scripts\python.exe -m pip install pytest
.\.venv\Scripts\python.exe -m pytest <test dir> -q
```
