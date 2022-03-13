"""
Taylor series
"""
from typing import Union
from math import factorial
from itertools import count

Epsilon = 0.0001

def get_item_ex(x, n):
    return (x ** n) / factorial(n)

def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    sum_ = 1
    for i in count(1, 1):
        current_item = get_item_ex(x, i)
        sum_ += current_item
        if current_item <= Epsilon:
            return sum_

def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    n = 1
    sin_elem = ((-1) ** (n - 1) * x ** (2 * n - 1)) / factorial(2 * n - 1)
    while sin_elem > Epsilon:
        sin_elem = ((-1) ** (n - 1) * x ** (2 * n - 1)) / factorial(2 * n - 1)
        sum_ += sin_elem
        n += 1
    return sum_
