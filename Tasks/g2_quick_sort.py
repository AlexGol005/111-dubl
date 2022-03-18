from typing import List
from random import choice


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if not container:
        return container

    pivot = choice(container)

    return sort([v for v in container if v < pivot]) \
                + [v for v in container if v == pivot] \
                + sort([v for v in container if v > pivot])