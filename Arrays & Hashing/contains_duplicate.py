class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueSet = set()
        for i in nums:
            if i in uniqueSet:
                return True
            else:
                uniqueSet.add(i)
        return False