class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        direction = [1, 1]
        # checking every diagnoal from top row
        for i in range(len(matrix[0])):
            r = 0
            c = i
            prev = matrix[r][c]
            dr, dc = direction
            while r+dr in range(len(matrix)) and c+dc in range(len(matrix[0])):
                if matrix[r+dr][c+dc] != prev:
                    return False
                r = r+dr
                c = c+dc

        # checking every diagonal from left column
        for i in range(len(matrix)):
            r = i
            c = 0
            prev = matrix[r][c]
            dr, dc = direction
            while r+dr in range(len(matrix)) and c+dc in range(len(matrix[0])):
                if matrix[r+dr][c+dc] != prev:
                    return False
                r = r+dr
                c = c+dc


        
        return True


        
