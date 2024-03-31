class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        curr = 1
        for i in range(len(nums)):
            curr *= nums[i]
            prefix[i] *= curr
        curr = 1
        for i in range(len(nums)):
            curr *= nums[len(nums)-1-i]
            postfix[len(nums)-1-i] *= curr
        
        res = [1] * len(nums)
        for i in range(len(nums)):
            if i == 0: # first 
                res[i] = postfix[i+1]
            elif i == len(nums)-1: # last
                res[i] = prefix[i-1]
            else: #everything else
                res[i] = prefix[i-1] * postfix[i+1]

        return res