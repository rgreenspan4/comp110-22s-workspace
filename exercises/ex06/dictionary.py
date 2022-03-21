"""Exercise 06 on dictionary functions."""
__author__ = 730530918


def invert(a: dict[str, str]) -> dict[str, str]:
    """This function inverts the key and value in a dictionary."""
    invert_dic: dict[str, str] = dict()
    for item in a:
        if a[item] in invert_dic:
            raise KeyError
        else:
            invert_dic[a[item]] = item 
    return invert_dic


def favorite_color(a: dict[str, str]) -> str:
    """This function finds the most common color and returns it."""
    color_count: dict[str, int] = {}
    pop_color: str = ""
    for key in a:
        if a[key] in color_count:
            color_count[a[key]] += 1
        else:
            color_count[a[key]] = 1
    # print(color_count)
    max: int = 0
    for key in color_count:
        if color_count[key] > max:
            max = color_count[key]
            pop_color = key
            # print(pop_color)
    return pop_color  


def count(a: list[str]) -> dict[str, int]:
    """This function takes a list of strings and counts how many times a string is on that list."""
    result: dict[str, int] = dict()
    x: int = 0
    i: int = 0
    for item in a:
        i = 0
        while i < len(a):
            if item == a[i]:
                x += 1
            i += 1
        result[item] = x
        x = 0
    return result