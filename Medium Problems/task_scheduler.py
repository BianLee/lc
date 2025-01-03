class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = dict()
        for i in range(len(tasks)):
            if tasks[i] in count:
                count[tasks[i]]+=1
            else:
                count[tasks[i]]=1

        maxHeap = []
        for key,value in count.items():
            maxHeap.append(-1 * value)
        heapq.heapify(maxHeap)
        print(maxHeap)
        q = deque()
        timer = 0
        while len(maxHeap) > 0 or q:    
            timer+=1
            if len(maxHeap)>0:     
                popped = heapq.heappop(maxHeap)
            
                if popped+1 < 0:
                    q.append((popped+1, timer+n))
            
            if q and q[0][1] == timer:
                heapq.heappush(maxHeap, q.popleft()[0])

        return timer
