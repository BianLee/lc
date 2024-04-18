class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = dict()
        for n in nums:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        sum =0 
        for n in nums:
            if count[n] == 1:
                sum+=n
        return sum