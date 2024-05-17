class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        memo = dict()
        def dp(numRows):
            if numRows in memo:
                return memo[numRows]
            if numRows == 1:
                return [[1]]
            if numRows == 2:
                return [[1], [1, 1]]
            newArr = list()
            newArr.append(1)
            lastArr = dp(numRows-1)
            for i in range(len(lastArr[-1])):
                if i+1<len(lastArr[-1]):
                    newArr.append(lastArr[-1][i] + lastArr[-1][i+1])
            newArr.append(1)
            memo[numRows] = lastArr + [newArr]
            return memo[numRows]
        return dp(numRows)
