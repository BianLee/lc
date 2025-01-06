#this is a pretty bad, not optimal solution (brute force)

class TicTacToe:

    def __init__(self, n: int):
        self.board = [['-' for i in range(n)] for j in range(n)]
        # print(self.board)
        

    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            self.board[row][col] = 'X'
        elif player == 2:
            self.board[row][col] = 'O'
        
        #print(self.board)
    
        for r in range(len(self.board)):
            if "-" not in self.board[r] and "O" not in self.board[r]:
                return 1
            elif "-" not in self.board[r] and "X" not in self.board[r]:
                return 2
        for c in range(len(self.board[0])):
            temp = []
            for r in range(len(self.board)):
                temp.append(self.board[r][c])
            if "-" not in temp and "O" not in temp:
                return 1
            elif "-" not in temp and "X" not in temp:
                return 2
            
        temp = []
        for i in range(len(self.board)):
            temp.append(self.board[i][i])

        #print(temp)
        if "-" not in temp and "O" not in temp:
            return 1
        elif "-" not in temp and "X" not in temp:
            return 2
        
        temp = []
        for i in range(len(self.board)):
            temp.append(self.board[len(self.board)-1-i][i])

        if "-" not in temp and "O" not in temp:
            return 1
        elif "-" not in temp and "X" not in temp:
            return 2
    

        return 0
            


        # print(self.board)

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
