class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numMap = dict()
        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = i
            else:
                if abs(i - numMap[nums[i]]) <= k:
                    return True
                else:
                    numMap[nums[i]] = i
        return False