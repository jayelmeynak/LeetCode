from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        set_arr = set()
        curr = head
        while curr is not None:
            if curr in set_arr:
                return True
            set_arr.add(curr)
            curr = curr.next
        return False

if __name__ == '__main__':
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next.next
    print(Solution().hasCycle(head))