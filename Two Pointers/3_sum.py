class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # [-1, 0, 1, 2, -1, -4] --> [-4, -1, -1, 0, 1, 2]

        res = [] # result (answer)
        nums.sort() # sort the array
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r=len(nums)-1
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -=1
                elif threeSum <0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
        return res