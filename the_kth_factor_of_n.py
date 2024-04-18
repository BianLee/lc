class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        for j in range(1, n+1):
            if n % j == 0:
                factors.append(j)
        if k > len(factors):
            return -1
        else:
            return factors[k-1]

