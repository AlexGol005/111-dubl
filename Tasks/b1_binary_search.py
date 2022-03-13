from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left_index = 0
    right_index = len(arr) - 1
    while left_index <= right_index:
        middle_index = left_index + (right_index - left_index) // 2
        middle_value = arr[middle_index]
        if middle_value == elem:
            return middle_index
        elif middle_value < elem:
            left_index = middle_index + 1
        elif middle_value > elem:
            right_index = middle_index - 1
    return None

print(binary_search(2, [0, 1, 2, 3, 4, 5, 6, 7]))







