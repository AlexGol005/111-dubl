"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priorityQueue = [] # todo для очереди можно использовать python dict


    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        insert_item = {
            'elem': elem,
            'priority': priority
        }

        for index, current_item in enumerate(self.priorityQueue):
            if insert_item['priority'] >= current_item['priority']:
                self.priorityQueue.insert(index, insert_item)
                break
        else:
            self.priorityQueue.append(insert_item)

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if not self.priorityQueue:
            return None
        return self.priorityQueue.pop()['elem']

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        if not self.priorityQueue or ind < 0 or ind > len(self.priorityQueue):
            return None
        return self.priorityQueue[-(ind + 1)]['elem']

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        return self.priorityQueue.clear()
