class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = {}
        def dp(numRows):
            if numRows in memo:
                return memo[numRows]
            if numRows == 1:
                memo[numRows] = [[1]]
                return memo[numRows]
            if numRows == 2:
                memo[numRows] = [[1], [1, 1]]
                return memo[numRows]
            lastArr = dp(numRows - 1)
            newArr = [1]
            for i in range(len(lastArr[-1]) - 1):
                newArr.append(lastArr[-1][i] + lastArr[-1][i + 1])
            newArr.append(1)
            memo[numRows] = lastArr + [newArr]
            return memo[numRows]
        return dp(numRows)
