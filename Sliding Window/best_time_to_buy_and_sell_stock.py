class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow, fast = 0, 1
        maxProfit = 0
        while slow < fast and fast < len(prices):
            if prices[fast] < prices[slow]:
                slow = fast
            else:
                maxProfit = max(maxProfit, prices[fast] - prices[slow])
            fast+=1
        return maxProfit