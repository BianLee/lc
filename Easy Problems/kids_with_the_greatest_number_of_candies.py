class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        ans=list()
        for c in candies:
            if c+extraCandies>=maxVal:
                ans.append(True)
            else:
                ans.append(False)
        return ans
