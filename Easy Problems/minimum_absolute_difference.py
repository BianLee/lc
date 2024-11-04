class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        arr.sort()
        minDiff = float('inf')
        runningList = list()
        for i in range(len(arr)):
            

            if i+1<len(arr):
                if arr[i+1] - arr[i] < minDiff:
                    minDiff = arr[i+1] - arr[i]
                    runningList = list()
                    runningList.append([arr[i], arr[i+1]])
                elif arr[i+1] - arr[i] == minDiff:
                    runningList.append([arr[i], arr[i+1]])
            
        return runningList
