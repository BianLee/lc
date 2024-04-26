# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tempSum = 0
        fast = head
        dummy = ListNode()
        tracker = dummy
        while fast:
            if fast.val != 0:
                tempSum += fast.val
            else:
                if tempSum != 0:
                    tracker.next = ListNode(tempSum)
                    tracker = tracker.next
                tempSum = 0
            fast = fast.next
        return dummy.next