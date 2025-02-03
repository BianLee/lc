class Solution:
    def check(self, nums: List[int]) -> bool:
    
        for i in range(len(nums)):
            if i+1<len(nums) and nums[i] <= nums[i+1]:
                continue
            else:
                break
        
        if i == len(nums)-1:
            return True
        else:
            print(i)
            for j in range(0, i):
                if nums[j] <= nums[j+1]:
                    continue
                else:
                    return False
            for j in range(i+1, len(nums)-1):
                print(nums[j], nums[j+1])
                if nums[j] <= nums[j+1]:
                    continue
                else:
                    return False
    
            if nums[0:i+1][0] >= nums[i+1:len(nums)][0]:
                if nums[0:i+1][0] >= nums[i+1:len(nums)][-1]:
                    return True
                return False
            else:
                if nums[0:i+1][-1] < nums[i+1:len(nums)][-1]:
                    return True
                return False
