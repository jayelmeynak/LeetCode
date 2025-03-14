# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        number_str_1 = ''
        number_str_2 = ''
        while l1 is not None and l2 is not None:
            if l1:
                number_str_1 += str(l1.val)
                l1 = l1.next
            if l2:
                number_str_2 += str(l2.val)
                l2 = l2.next
        number1 = number_str_1[::-1]
        number2 = number_str_2[::-1]
        total = int(number1) + int(number2)
        ans = ListNode(total % 10)
        current = ans
        while total > 9:
            total = total // 10
            current.next = ListNode(total % 10)
        return ans

if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    ans = Solution().addTwoNumbers(l1, l2)
