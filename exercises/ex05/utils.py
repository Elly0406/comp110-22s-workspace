"""EX05 -- this exercise is to build some list utility function."""

__author__ = "730365499"


def only_evens(xs: list[int]) -> list[int]:
    """This function is to return the even number in the list."""
    even_number: list[int] = list()
    for number in xs:
        if number % 2 == 0:
            even_number.append(number)
    return even_number


def sub(a_list: list[int], a: int, b: int) -> list[int]:
    """This function is to return number in the list between index a and b-1."""
    subset: list[int] = list()
    while a < b:
        if len(a_list) == 0 or a >= len(a_list) or b < 0:
            subset = []
            a += 1
        elif a < 0:
            a = 0
            subset.append(a_list[a])
            a += 1
        elif b > len(a_list):
            b = len(a_list)
            subset.append(a_list[a])
            a += 1
        else:
            subset.append(a_list[a])
            a += 1
    return subset


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """This function is to return each number in two list in order."""
    new_list: list[int] = list()
    i: int = 0
    for i in xs:
        new_list.append(i)
    for j in ys: 
        new_list.append(j)      
    return new_list
