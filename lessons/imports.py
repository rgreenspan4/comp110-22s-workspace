"""Examples of importing in python."""

from lessons import helpers

# imports with alias
# from lessons import helpers as hp

# imports names defined globally in a module
# from lessons.helpers import powerful


def main() -> None:
    """Entrypoint of program."""
    print(helpers.powerful(2, 4))


if __name__ == "__main__":
    main()