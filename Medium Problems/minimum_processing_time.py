class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        i = len(tasks)-1
        arr=list()
        l=0
        while i > -1:
            temp=list()
            for j in range(4):
                temp.append(tasks[i]+processorTime[l])
                i-=1
            arr.append(max(temp))
            l+=1
        print(arr)
        return max(arr)
