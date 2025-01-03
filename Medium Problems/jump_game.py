class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        lastIndex = len(nums)-1
        
        traceback = ["_"] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                traceback[i] = "end"
            else:
                for j in range(1, nums[i]+1):
                    # print(traceback[i+j])
                    #print(i)
                    #print(j)
                    if i+j<len(nums):
                        if (traceback[i+j] == "y" or traceback[i+j] == "end"):
                            traceback[i] = "y"
                            break
                        else:
                            traceback[i] = "n"
                # if traceback[i]
        #print(traceback)
        if traceback[0] == "y":
            return True
        return False
        
