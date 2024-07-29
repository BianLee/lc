class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        l,r = 0, len(nums)-1
        while l<=r:
            m= (l+r)//2
            if m-1 >= 0 and nums[m-1] > nums[m]: #left is greater
                r = m-1
            elif m+1 <= len(nums)-1 and nums[m+1] > nums[m]: #right is greater
                l = m+1
            else: #if neither neighbor is greater, current element is the peak
                return m
