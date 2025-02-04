class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
    
        running = nums[0]
        ans = nums[0]
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i] < nums[i+1]:
                running += nums[i+1]
                ans = max(running, ans)
            else:
                if i+1<len(nums):
                    running = nums[i+1]
                    ans = max(running, ans)

            print(running)

        return ans
