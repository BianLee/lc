class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l+=1
        return l


# Another solution
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        numSet = set()
        for j in range(len(nums)):
            if nums[j] not in numSet:
                numSet.add(nums[j])
                nums[i] = nums[j]
                i+=1
            
        return i
