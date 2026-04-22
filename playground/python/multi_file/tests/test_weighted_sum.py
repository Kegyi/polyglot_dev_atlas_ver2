from weighted_sum_playground.core import weighted_sum


def test_weighted_sum_basic() -> None:
    assert weighted_sum([2, 4, 8], [1, 2, 1]) == 18
