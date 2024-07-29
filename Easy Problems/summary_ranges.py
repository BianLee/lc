class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output=[]
        i=0
        while i<len(nums):
            initial = i
            while i+1 < len(nums) and nums[i+1] - nums[i] == 1:
                i+=1
            if initial != i:
                strSample = ""
                strSample+=str(nums[initial]) + "->" + str(nums[i])
                output.append(strSample)
            else:
                output.append(str(nums[initial]))
            i+=1
        return output


#another solution
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = 0
        r = 0
        ans = []
        while r<len(nums):
            while r+1<len(nums) and nums[r+1] - nums[r] == 1:
                r+=1
            if nums[l] != nums[r]:
                ans.append(str(nums[l]) + "->" + str(nums[r]))
            else:
                ans.append(str(nums[l]))
            l = r+1
            r+=1
        return ans
            
