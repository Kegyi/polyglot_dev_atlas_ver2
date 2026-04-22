from typing import Iterable


def weighted_sum(values: Iterable[int], weights: Iterable[int]) -> int:
    return sum(v * w for v, w in zip(values, weights))
