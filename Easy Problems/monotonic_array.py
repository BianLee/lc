class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i] == nums[i+1]:
                continue
            if i+1<len(nums) and nums[i]<nums[i+1]:
                direction = 1
                break
            elif i+1<len(nums) and nums[i]>nums[i+1]:
                direction = -1
                break
        for j in range(i, len(nums)):
            if j+1<len(nums) and nums[j]>nums[j+1] and direction == 1:
                return False
            elif j+1<len(nums) and nums[j]<nums[j+1] and direction == -1:
                return False
        return True
