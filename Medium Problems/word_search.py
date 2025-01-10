class Solution:
    
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        #[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]

        self.status = False
        self.visited = set()

        def dfs(r,c,index) -> bool:
            #print(self.visited)
            #rint(index)
            if index == len(word):
                self.status = True
                return
            directions = [[0,1],[1,0],[-1,0],[0,-1]]
            self.visited.add((r,c))
            for dr, dc in directions:
                #print("here, ", index, word[index])
                
                if r+dr in range(len(board)) and c+dc in range(len(board[0])) and board[r+dr][c+dc] == word[index] and (r+dr, c+dc) not in self.visited:
                    dfs(r+dr, c+dc, index+1)

            self.visited.remove((r,c))
                    

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    # self.visited.add((r,c))
                    self.visited = set()
                    dfs(r,c,1)
                    

        if self.status == True:
            return True
        
        return False
