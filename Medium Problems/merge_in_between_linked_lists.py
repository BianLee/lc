# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        masterDummy = ListNode()
        masterDummy.next = list1
        currOne = list1
        insertSpot = currOne
        secondSpot = ListNode()
        for i in range(a-1):
            currOne=currOne.next
            insertSpot = currOne
        
        for i in range(b-a+2):
            currOne=currOne.next
            secondSpot=currOne
        
        insertSpot.next = list2

        dummy = ListNode()
        dummy.next = list2
        while list2:
            list2=list2.next
            dummy=dummy.next
        dummy.next = secondSpot
        return masterDummy.next
