class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        
        output = []
        for i in range(len(prices)):
            temp = 0
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    output.append(prices[i] - prices[j])
                    temp = 1
                    break
            if temp == 0:
                output.append(prices[i])
            
        return output
