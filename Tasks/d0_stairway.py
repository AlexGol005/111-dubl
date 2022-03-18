from typing import Union, Sequence
# i = min(i - 1, i - 2)

def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    def laizy_stair_way_path(stair_number: int) -> Union[float, int]:
        if stair_number == 0:
            return stairway[stair_number]
        if stair_number == 1:
            return stairway[stair_number]
        current_cost = stairway[stair_number]
        return current_cost + min(laizy_stair_way_path(stair_number - 1),
                                  laizy_stair_way_path(stair_number - 2))
    return laizy_stair_way_path(len(stairway)-1)

def direct_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    # cost of step
    count_stairs = len(stairway)  # количество ступеней
    total_cost = [0] * count_stairs  # стоимость дойти до ступеней
    # изначальные условия 1 и 2 ступень
    # прямой метод обхода i - стоимость = i - цена + min((i - 1) - стоимость, (i - 2) - стоимсоть)
    total_cost[0] = stairway[0]
    total_cost[1] = min(stairway[1], stairway[0] + stairway[1])
    for i in range(2, count_stairs):
        total_cost[i] = stairway[i] + min(total_cost[i - 1], total_cost[i - 2])
    return total_cost[-1]

def reverse_stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    count_stairs = len(stairway)  # количество ступеней
    total_cost = [float('inf')] * count_stairs  # стоимость дойти до ступеней
    total_cost[0] = stairway[0]
    total_cost[1] = min(stairway[1], stairway[0] + stairway[1])
    for i in range(0, count_stairs):
        if i + 1 < count_stairs:
            total_cost[i + 1] = min(total_cost[i] + stairway[i + 1], total_cost[i + 1])
        if i + 2 < count_stairs:
            total_cost[i + 2] = min(total_cost[i] + stairway[i + 2], total_cost[i + 2])
    return total_cost[-1]



