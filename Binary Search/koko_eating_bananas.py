class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1, max(piles)
        while l<=r:
            mid=(l+r)//2
            count=0
            for i in range(len(piles)):
                count+=math.ceil(piles[i]/mid)
            if count > h:
                l=mid+1
            else:
                r=mid-1
        return l
