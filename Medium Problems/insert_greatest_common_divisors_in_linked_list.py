# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next
        while fast:
            newNode = ListNode()
            newNode.val = gcd(slow.val, fast.val)
            slow.next = newNode
            newNode.next = fast
            slow = slow.next.next
            fast=fast.next
        return head
            
