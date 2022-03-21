"""I love functions."""


def love(name: str) -> str:
    """This will tell you it loves you."""
    return f"I love you {name}"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times"""
    i: int = 0
    love_note: str = ""
    while i < n:
        love_note += love(to) + "\n"
        i += 1
    return love_note
