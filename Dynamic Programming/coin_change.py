class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = dict()
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]
            tempList = list()
            for c in coins:
                tempList.append(1+dp(amount-c))
            memo[amount] = min(tempList)
            return memo[amount]
            
        
        minimum = dp(amount)
        if minimum < float("inf"):
            return minimum
        else:
            return -1
