class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        rowsMin = float('inf')
        rowsMinArr = []
        colsMax = float('-inf')
        colsMaxArr = []
        ans = []

        for r in range(len(matrix)):
            rowsMin = float('inf')
            for c in range(len(matrix[0])):
                rowsMin = min(rowsMin, matrix[r][c])
            rowsMinArr.append(rowsMin)

        for c in range(len(matrix[0])):
            colsMax = float('-inf')
            for r in range(len(matrix)):
                colsMax = max(matrix[r][c], colsMax)
            colsMaxArr.append(colsMax)
        
        print(rowsMinArr)
        print(colsMaxArr)

        if len(rowsMinArr) < len(colsMaxArr):
            for i in range(len(rowsMinArr)):
                if rowsMinArr[i] in colsMaxArr:
                    ans.append(rowsMinArr[i])
        else:
            for i in range(len(colsMaxArr)):
                if colsMaxArr[i] in rowsMinArr:
                    ans.append(colsMaxArr[i])
        return ans
