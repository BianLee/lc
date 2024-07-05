# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr=head
        arr=list()
        arr.append(curr.val)
        critical=list()
        minValue = float('inf')
        
        while curr.next:
            curr = curr.next
            arr.append(curr.val)
        print(arr)
        for i in range(len(arr)):
            if i>0 and i<len(arr)-1:
                if arr[i]<arr[i-1] and arr[i]<arr[i+1]:
                    if len(critical)>0:
                        print(i-critical[-1])
                        minValue = min(minValue, i-critical[-1])
                    critical.append(i)
                elif arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                    
                    if len(critical)>0:
                        print(i-critical[-1])
                        minValue = min(minValue, i-critical[-1])
                    critical.append(i)
        
        maxValue = 0
        if len(critical)>0:
            maxValue = critical[-1]-critical[0]
        else:
            return [-1, -1]
        
        if minValue == float('inf') or maxValue == 0:
            return [-1, -1]
        return [minValue, maxValue]
                
