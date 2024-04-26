class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # [8,1,2,2,3] --> [1,2,2,3,8]
        temp = sorted(nums)
        mapping = dict()
        result = list()
        for i in range(len(temp)):
            if temp[i] not in mapping:
                mapping[temp[i]] = i
        for n in nums:
            result.append(mapping[n])
        return result