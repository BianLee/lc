# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        fast=head
        stack=[]
        while fast:
            stack.append(fast.val)
            fast=fast.next
        i = 0
        ans = 0
        while stack:
            value = stack.pop()
            ans += value * pow(2, i)
            i+=1
        return ans

