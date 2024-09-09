class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        newArray = list()
        for s in timePoints:
            value = int(s[0:2]) * 60 + int(s[3:])
            newArray.append(value)
        #[23:59, 00:02] --> [1439, ]
        
        newArray.sort() #[0, 1439, 1440]
        newArray.append(newArray[0] + 1440)
        minDiff = float('inf')
        for i in range(len(newArray)):
            if i+1 < len(newArray):
                minDiff = min(newArray[i+1] - newArray[i], minDiff)
        
        return minDiff
