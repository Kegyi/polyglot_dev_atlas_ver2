from example_project.core import greet


def test_greet_contains_name() -> None:
    assert "Alice" in greet("Alice")


def test_greet_starts_with_hello() -> None:
    assert greet("world").startswith("Hello")


def test_greet_empty_name_non_empty_result() -> None:
    assert greet("") != ""
