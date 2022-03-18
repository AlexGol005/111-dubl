from typing import List
from operator import lt, gt


def sort(container: List[int], ascending: bool =True, inplace=True) -> List[int]:
    """
    Sort input container with bubble sort
    :param asc сортировать по возрастанию ли
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    N = len(container)
    if not inplace:
        container = container.copy()
    offset = 1
    compare_operator = gt if ascending else lt
    is_change = False
    for i in range(N - offset):
        for j in range(i + 1, N):
            if container[i] > container[j]: #compare_operator(container[i], container[i + 1]):
                container[j], container[i] = container[i], container[j]
                is_change = True
        if not is_change:
            break
        offset += 1
    return container
