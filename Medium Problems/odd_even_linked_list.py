# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        first,second=head,head.next
        copied=head.next
        while first and first.next and second and second.next:
            first.next=first.next.next
            first=first.next
            second.next=second.next.next
            second=second.next
        first.next=copied
        return head
