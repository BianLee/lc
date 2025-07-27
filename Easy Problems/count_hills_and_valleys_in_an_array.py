class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count=0
        used = set()
        for i in range(1, len(nums)-1):
            l, r = i-1, i+1
            while l-1>-1 and nums[l] == nums[i]:
                l-=1
            while r+1<len(nums) and nums[r] == nums[i]:
                r+=1
            


            if ((l,r) not in used) and ((nums[l] < nums[i] and nums[r] < nums[i]) or (nums[l] > nums[i] and nums[r] > nums[i])):
                print(l,r)
                count+=1
                used.add((l,r))
                print(used)
            
        return count
