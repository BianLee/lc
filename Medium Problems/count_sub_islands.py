class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        visitedTwo = set()

        def dfsTwo(r,c, runningList):
            if r not in range(len(grid2)) or c not in range(len(grid2[0])) or (r,c) in visitedTwo or grid2[r][c] == 0:
                return
            visitedTwo.add((r,c))
            runningList.append((r,c))
            directions = [[-1,0],[1,0],[0,1],[0,-1]]
            for dr, dc in directions:
                dfsTwo(r+dr, c+dc, runningList)
            return runningList

        count = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                tempOne, tempTwo = list(), list()
                if grid2[r][c] == 1 and (r,c) not in visitedTwo:
                    tempTwo = dfsTwo(r,c,[])
                
                status=0
                for cell in tempTwo:
                    a,b=cell
                    if grid1[a][b] == 1:
                        continue
                    else:
                        status=1
                        break
                if status != 1 and len(tempTwo)>0:
                    count+=1

        return count
