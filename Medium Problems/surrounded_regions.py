class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
    
        def dfs(r,c):
            directions = [[-1,0], [1,0], [0,1], [0,-1]]
            for dr, dc in directions:
                if dr+r in range(len(board)) and dc+c in range(len(board[0])) and board[r+dr][c+dc] == "O":
                    board[r+dr][c+dc] = "T"
                    dfs(r+dr, c+dc)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r != 0 and r != len(board)-1 and c != 0 and c != len(board[0])-1:
                    continue
                if board[r][c] == "O":
                    board[r][c] = "T"
                    dfs(r,c)
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "T":
                    board[r][c] = "O"
        

