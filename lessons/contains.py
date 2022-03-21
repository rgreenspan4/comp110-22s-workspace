"""Writing a function to search a list."""


def contains(needle: str, haystack: list[str]) -> bool:
    """Finding needle in haystack."""
    for item in haystack:
        if item == needle:
            return True
    return False
