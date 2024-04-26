class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        hashMap = dict()
        for n in nums:
            if n in hashMap:
                hashMap[n]+=1
            else:
                hashMap[n]=1
        count = 0
        leftOver = 0
        numSet = set(nums)
        for n in numSet:
            count += hashMap[n]//2
            leftOver+=hashMap[n]%2
        return count, leftOver