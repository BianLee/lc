class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        for i in range(k):
            first_min = float(inf)
            x_index = 0
            for j in range(len(nums)):
                if nums[j] < first_min:
                    first_min = nums[j]
                    x_index = j
            nums[x_index] *= multiplier
        return nums 
