class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose matrix, then reverse each row
        for r in range(len(matrix)):
            for c in range(r, len(matrix)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for row in matrix:
            row.reverse()
        
