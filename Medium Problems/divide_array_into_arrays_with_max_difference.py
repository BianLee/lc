class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans=[]
        temp=list()
        for i in range(len(nums)):
            #print(temp)
            if len(temp)<3:
                temp.append(nums[i])
            if len(temp)==3:
                ans.append(temp)
                temp=list()
        print(ans)
        for i in ans:
            if i[2]-i[0]>k:
                return []       
        return ans
