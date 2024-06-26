class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = dict()
        for i in range(len(nums)):
            if nums[i] in hashMap:
                return hashMap[nums[i]], i
            else:
                hashMap[target-nums[i]] = i