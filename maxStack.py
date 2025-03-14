class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Solution:
    start = Node(0)
    end = Node(0)
    start.next = end
    end.prev = start

    def push(self, x: int):
        new_node = Node(x)
        new_node.next = self.end
        new_node.prev = self.end.prev
        self.end.prev = new_node

    def pop(self) -> int:
        x = self.end.prev
        self.end.prev = x.prev
        prev = x.prev
        prev.next = self.end
        return x.value

    def top(self) -> int:
        x = self.end.prev
        return x.value

