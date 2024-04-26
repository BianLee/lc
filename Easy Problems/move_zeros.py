class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[slow] = nums[i]
                slow+=1

        for i in range(slow, len(nums)):
            nums[i] = 0
    