class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i == 0 or i == 1 or nums[i-2] != n:
                nums[i] = n
                i+=1
        return i
