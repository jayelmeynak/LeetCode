from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None
        cur = head
        hash_arr = {}
        while cur:
            new_node = Node(cur.val)
            hash_arr[cur] = new_node
            cur = cur.next
        cur = head
        while cur:
            new_node = hash_arr[cur]
            new_node.next = hash_arr[cur.next] if cur.next else None
            new_node.random = hash_arr[cur.random] if cur.random else None
            cur = cur.next
        return hash_arr[head]
