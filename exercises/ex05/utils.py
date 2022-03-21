"""EX 05 homework."""
__author__ = 730530918


def only_evens(xs: list[int]) -> list[int]:
    """Creates a list of only even numbers."""
    op_list: list[int] = list()
    for item in xs:
        if item % 2 == 0:
            op_list.append(item)
    return op_list


def sub(xs: list[int], a: int, b: int) -> list[int]:
    """Creates a list of only two desired numbers."""
    op_list: list[int] = []
    if a < 0:
        a = 0
    if b > len(xs):
        b = len(xs)
    if a > len(xs) or b <= 0:
        return op_list
    i: int = a
    while i < b:
        op_list.append(xs[i])
        i += 1
    return op_list


def concat(first: list[int], second: list[int]) -> list[int]:
    """Adds one list to the end of another."""
    for item in second:
        first.append(item)
    return first
