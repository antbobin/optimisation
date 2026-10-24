"""Fonctions d'optimisation de base."""

from collections.abc import Callable

GOLDEN_RATIO = (5**0.5 - 1) / 2


def minimize_scalar(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-8,
) -> float:
    """Minimise une fonction unimodale sur [a, b] par la méthode du nombre d'or."""
    if a >= b:
        raise ValueError("a doit être strictement inférieur à b")
    c = b - GOLDEN_RATIO * (b - a)
    d = a + GOLDEN_RATIO * (b - a)
    while b - a > tol:
        if f(c) < f(d):
            b = d
        else:
            a = c
        c = b - GOLDEN_RATIO * (b - a)
        d = a + GOLDEN_RATIO * (b - a)
    return (a + b) / 2
