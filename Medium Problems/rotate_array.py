class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums.reverse()
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        if k>len(nums):
            k = k % len(nums)
        memory = []
        for i in range(len(nums)-k):
            memory.append(nums[i])
        index = 0
        for i in range(len(nums)-k, len(nums)):
            nums[index] = nums[i]
            index+=1
        for i in range(len(memory)):
            nums[index] = memory[i]
            index+=1

    
