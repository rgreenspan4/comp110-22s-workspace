"""Adds up items in a list"""


def sum(xs: list[float]) -> float:
    """Adds items"""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total