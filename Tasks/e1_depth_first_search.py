from typing import Hashable, List
from collections import deque

import networkx as nx


# def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
#     """
#     Do an depth-first search and returns list of nodes in the visited order
#
#     :param g: input graph
#     :param start_node: starting node of search
#     :return: list of nodes in the visited order
#     """
#     path_nodes = []
#     visited_nodes = {node: False for node in g.nodes}
#     wait_nodes = [] #стек
#     visited_nodes[start_node] = True
#
#     while wait_nodes:

def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
    ...
