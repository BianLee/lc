class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        memo=dict()
        for i in range(len(groupSizes)):
            if groupSizes[i] in memo:
                memo[groupSizes[i]].append(i)
            else:
                memo[groupSizes[i]] = [i]
        ans=list()
        for key,value in memo.items():
            temp=list()
            for i in range(len(value)):
                temp.append(value[i])
                if (i+1)%key == 0:
                    ans.append(temp)
                    temp=list()
                
        return ans
