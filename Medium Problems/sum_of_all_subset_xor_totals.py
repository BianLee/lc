class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        self.ans = 0
        def dfs(index, build, curr_xor):
            self.ans += curr_xor
            for i in range(index, len(nums)):
                build.append(nums[i])
                dfs(i+1, build, curr_xor^nums[i])
                build.pop()
        


        dfs(0, [], 0)
        return self.ans
