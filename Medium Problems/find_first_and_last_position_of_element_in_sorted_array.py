class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        l,r = 0, len(nums)-1
        m=0
        while l<=r:
            m = (l+r)//2
            if nums[m] < target:
                l = m+1
            elif nums[m] > target:
                r = m-1
            else:
                break
        
        print(m)
        start = m
        end = m
        for i in range(m-1, -1, -1):
            if nums[i] == target:
                start = i
            else:
                break
        for i in range(m+1, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break
        return [start,end]
        
