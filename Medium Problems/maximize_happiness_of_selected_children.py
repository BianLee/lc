class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        sum = 0
        for i in range(k):
            sum += max((happiness[len(happiness)-1-i] - i), 0)
        return sum