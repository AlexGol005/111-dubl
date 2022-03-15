"""
Taylor series
"""
from typing import Union
from math import factorial
from itertools import count

Epsilon = 0.0001

def get_item_ex(x, n):
    return (x ** n) / factorial(n)

def get_item_sin(x, n):
    return ((-1) ** (n - 1) * x ** (2 * n - 1)) / factorial(2 * n - 1)

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
        if abs(current_item) <= Epsilon:
            return sum_

def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sum_ = 0
    for i in count(1, 1):
        current_item = get_item_sin(x, i)
        sum_ += current_item
        if abs(current_item) < Epsilon:
            return sum_
