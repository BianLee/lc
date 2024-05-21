class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[0]*len(nums)
        postfix=[0]*len(nums)
        prev=0
        for i in range(len(nums)):
            prefix[i]=prev+nums[i]
            prev=prefix[i]
        prev=0
        for i in range(len(nums)):
            postfix[len(nums)-1-i]=prev+nums[len(nums)-1-i]
            prev=postfix[len(nums)-1-i]
        print(prefix)
        print(postfix)
        for i in range(len(nums)):
            if prefix[i]==postfix[i]:
                return i
        return -1
