class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    
        maxHeap = []
        for n in nums:
            maxHeap.append(n*-1)
        heapq.heapify(maxHeap)

        for i in range(k-1):
            heapq.heappop(maxHeap)
        
        return -1*maxHeap[0]
