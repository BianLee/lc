# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
        numInStr = ""
        numInStrTwo = ""
        while l1:
            numInStr += str(l1.val)
            l1 = l1.next
        while l2:
            numInStrTwo += str(l2.val)
            l2 = l2.next

        numInStr = numInStr[::-1]
        numInStrTwo = numInStrTwo[::-1]
        n1,n2 = int(numInStr), int(numInStrTwo)
        result = n1+n2
        resultStr = str(result)[::-1]
        dummy = ListNode()
        curr = dummy
        for i in range(len(resultStr)):
            new = ListNode(resultStr[i])
            curr.next = new
            curr = curr.next
        return dummy.next
