class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        r, c = 0,0 
        visited = set()
        directions = [[0,1], [1,0], [0,-1],[-1,0]]
        output = []
        i = 0
        output.append(matrix[0][0])
        visited.add((0,0))
        while True:
            i = i % len(directions)
            dr, dc = directions[i]
            while r+dr in range(len(matrix)) and c+dc in range(len(matrix[0])) and (r+dr,c+dc) not in visited:
                r += dr
                c += dc
                output.append(matrix[r][c])
                visited.add((r,c))
            print(output)
            i+=1
            
            if len(output) == len(matrix)*len(matrix[0]):
                break
        
        return output
        
