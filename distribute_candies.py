class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        count=dict()
        for n in candyType:
            if n in count:
                count[n]+=1
            else:
                count[n]=1
        threshold = len(candyType)//2
        if len(count) > threshold:
            return threshold
        else:
            return len(count)