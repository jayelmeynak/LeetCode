# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next


if __name__ == '__main__':
    list1 = ListNode(1)
    list2 = ListNode(1)
    list1.next = ListNode(2)
    list2.next = ListNode(3)
    list1.next.next = ListNode(4)
    list2.next.next = ListNode(4)
    print(Solution().mergeTwoLists(list1, list2))

