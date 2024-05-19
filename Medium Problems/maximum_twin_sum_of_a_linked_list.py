# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        curr=head
        n=0
        maxSum = 0
        while curr:
            n+=1
            curr=curr.next
        curr=head
        for i in range(n//2):
            stack.append(curr.val)
            curr=curr.next
        for i in range(n//2):
            maxSum = max(maxSum, stack.pop()+curr.val)
            curr=curr.next
        return maxSum