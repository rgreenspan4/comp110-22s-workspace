"""Practice for Exam 3."""


def odd_and_even(a: list[int]) -> list[int]:
    """returns list of odd numbers and even indices."""
    i: int = 0
    result: list[int] = []
    while i < len(a):
        if a[i] % 2 != 0:
            result.append(a[i])
        i += 2
    return result


def vowels_and_threes(a: str) -> str:
    """returns every third letter or vowel (not both)."""
    vowel: list[str] = ['a', 'e', 'i', 'o', 'u', 'y']
    i: int = 0
    output: str = ""
    Do_nothing = True
    while i < len(a):
        if a[i] in vowel and i % 3 == 0:
            Do_nothing != Do_nothing
        elif a[i] in vowel:
            output += a[i]
        elif i % 3 == 0:
            output += a[i]
        i += 1
    return output


def average_grades(name_and_grades: dict[str, list[int]]) -> dict[str, float]:
    """Averages peoples grades."""
    avg_score: dict[str, float] = {}
    for student in name_and_grades:
        i: int = 0
        add_list: list[int] = name_and_grades[student]
        total: int = 0
        while i < len(name_and_grades[student]):
            total += add_list[i]
            i += 1
        avg_score[student] = (total / len(name_and_grades[student]))
    return avg_score