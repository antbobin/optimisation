import pytest

from optimisation import minimize_scalar


def test_minimize_scalar_quadratic():
    assert minimize_scalar(lambda x: (x - 2) ** 2, 0, 5) == pytest.approx(2, abs=1e-6)


def test_minimize_scalar_invalid_interval():
    with pytest.raises(ValueError):
        minimize_scalar(lambda x: x, 1, 0)
