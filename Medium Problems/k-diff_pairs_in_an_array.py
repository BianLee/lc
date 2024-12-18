import math

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        numDict = dict()
        for i in range(len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]]+=1
            else:
                numDict[nums[i]]=1
        
        count=0
        print(numDict)
        for key,value in numDict.items():
            if k == 0:
                if value > 1:
                    count += 1
            else:
                if key+k in numDict:
                    count += 1
        return count 

            

