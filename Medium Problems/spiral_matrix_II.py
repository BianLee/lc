class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        result = [[0] * n for _ in range(n)]
        
        directions = [[0,1],[1,0],[0,-1],[-1,0]]
        i=0
        visited=set()
        r,c = 0,0
        count=1

        result[r][c] = count
        visited.add((r,c))
        count+=1

        for j in range(n*n):
            i = i % len(directions)
            dr, dc = directions[i]
   
            while r+dr in range(n) and c+dc in range(n) and (r+dr, c+dc) not in visited:
                r+=dr
                c+=dc
                print(r,c,count)
                result[r][c] = count
                count+=1
                visited.add((r,c))
                
            i+=1
            
        print(result)
        return result
