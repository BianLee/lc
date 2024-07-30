class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        mapped = dict()
        for i in range(len(nums)):
            if nums[i] in self.mapped:
                self.mapped[nums[i]].append(i)
            else:
                self.mapped[nums[i]] = [i]

    def pick(self, target: int) -> int:
        return self.mapped[target][random.randrange(0, len(self.mapped[target]))]
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
