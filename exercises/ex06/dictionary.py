"""EX06 - Dictionary Function - practice with some dictionary functions."""

__author__ = "730365499"


def invert(a: dict[str, str]) -> dict[str, str]:
    """This function is to switch key and value in given dictionary and return a new one."""
    invert_result: dict[str, str] = {}
    for i in a:
        if a[i] in invert_result:
            raise KeyError("The invert result has repeated key")
        else:
            invert_result[a[i]] = i
    return invert_result


def favorite_color(a: dict[str, str]) -> str:
    """This funciton is to find the most frequent value in dict, and return that value."""
    color: dict[str, int] = {}
    for i in a:
        if a[i] not in color:
            color[a[i]] = 1
        elif a[i] in color:
            color[a[i]] += 1
    most_color: str = max(color, key=color.get)
    return most_color


def count(xs: list[str]) -> dict[str, int]:
    """This function is to count different value in a list and count its corresponded times."""
    result: dict[str, int] = {}
    for item in xs:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result 
