class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        while l < r:
            m = l + ((r-l)//2)
            print(m)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]



# one that uses (l+r)//2 to calculate midpoint

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        while l<r:
            m = (l+r)//2
            #compare mid element with the rightmost element

            # if the mid element is greater than the rightmost
            if nums[m] > nums[r]: 
                l = m+1
            else:
                r = m
        return nums[l]
