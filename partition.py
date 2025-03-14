from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        right = dummy.next
        prevRight = dummy
        while right and right.val < x:
            prevRight, right = prevRight.next, right.next
        while right:
            if right.val < x:
                tmp = right.next
                right.next = prevRight.next
                prevRight.next = right
                right = tmp
            else:
                right = right.next
        return dummy.next

if __name__ == '__main__':
    s = Solution()
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    print(s.partition(head, 3))
