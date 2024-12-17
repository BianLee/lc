import math

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:

        newArr = []
        countDict = dict()
        for i in range(len(time)):
            if time[i]%60 in countDict:
                countDict[time[i]%60]+=1
            else:
                countDict[time[i]%60]=1
        
        print(countDict)
        count = 0
        special_case = 0
        ans = 0
        
        for key,value in countDict.items():
            print(key,value)
            if key == 0:
                special_case += math.comb(value, 2)
            elif key == 30:
                special_case += math.comb(value, 2)
            else:
                if 60-key in countDict:
                    count += countDict[60-key] * value
            
        return (count//2) + special_case


                
