from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        dummy = ListNode(0, head)
        counterNode = dummy.next
        listSize = 0
        while counterNode is not None:
            counterNode = counterNode.next
            listSize += 1
        countRotate = k % listSize
        slow = fast = dummy
        for _ in range(countRotate):
            fast = fast.next
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        while countRotate != 0:
            cur = slow.next
            prev = slow
            while cur.next is not None:
                cur = cur.next
                prev = prev.next
            cur.next = dummy.next
            dummy.next = cur
            prev.next = None
            countRotate -= 1
        return dummy.next


if __name__ == '__main__':
    a = Solution()
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    print(a.rotateRight(head, 4).val)
