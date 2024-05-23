class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count=0
        for i in range(len(prices)):
            if i+1<len(prices) and prices[i+1]-prices[i]>0:
                count+=prices[i+1]-prices[i]
        return count
