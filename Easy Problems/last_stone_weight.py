class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 0:
            return 0
        
        customHeap = []
        for c in stones:
            customHeap.append(c * -1)
        heapq.heapify(customHeap)
        print(customHeap)
        
        while len(customHeap) > 1:
            y = customHeap[0]
            heapq.heappop(customHeap)
            heapq.heapify(customHeap)
            x = customHeap[0]
            print(y,x)
            
            if x == y:
                heapq.heappop(customHeap)
            else:
                heapq.heappop(customHeap)
                heapq.heappush(customHeap, -((-y)-(-x)))
                heapq.heapify(customHeap)
        
        if len(customHeap) == 0:
            return 0
        return -1 * customHeap[0]

