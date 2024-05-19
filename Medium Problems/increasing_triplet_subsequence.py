class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        maxVal=0
        maxValIndex=0
        for i in range(len(nums)):
            if i==0 or i==1:
                continue
            if nums[i]>maxVal:
                maxVal=nums[i]
                maxValIndex=i
            
        numSet = set()
       
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>=nums[j]:
                    break
                for k in range(j+1, len(nums)):
                    print(nums[i], nums[j],nums[k])
                    print(maxVal)
                    if nums[j]<maxVal and j<maxValIndex:
                        return True
                    if (tuple([nums[i],nums[j]])) in numSet and i!=0:
                        break
                    numSet.add(tuple([nums[i],nums[j]]))
                    if nums[i]<nums[j]<nums[k]:
                        return True
        return False
