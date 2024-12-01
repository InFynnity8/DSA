# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # two pointer 
    def removeNthFromEnd1(self, head, n: int):
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
    
    def removeNthFromEnd2(self, head, n: int):
        # two pass
        curr = head
        length = 1
        while curr.next:
            curr = curr.next
            length += 1
        if length == n:
            return head.next

        curr = head
        for _ in range(length-n-1):
            curr = curr.next
        curr.next = curr.next.next
        return head
