class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        largestKeyVal = 0
        index = 0
        for i in range(len(releaseTimes)):
            if i != 0:
                if releaseTimes[i] - releaseTimes[i-1] == largestKeyVal:
                    if ord(keysPressed[i])-ord('a') > ord(keysPressed[index])-ord('a'):
                        index = i  
                elif releaseTimes[i] - releaseTimes[i-1] > largestKeyVal:
                    largestKeyVal = releaseTimes[i] - releaseTimes[i-1]
                    index = i
            else:
                largestKeyVal = releaseTimes[i]
            print(largestKeyVal, index)
          
        return keysPressed[index]