class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pacificGrid = set()
        pacificVisited = set()
        atlanticGrid = set()
        atlanticVisited = set()

        ans = []
        def pacificDfs(r,c):

            pacificGrid.add((r,c))
            pacificVisited.add((r,c))

            directions = [[-1,0],[0,1],[1,0],[0,-1]]
            for dr, dc in directions:
                if r+dr in range(len(heights)) and c+dc in range(len(heights[0])) and heights[r+dr][c+dc] >= heights[r][c] and (r+dr,c+dc) not in pacificVisited:
                    pacificDfs(r+dr, c+dc)
        
        def atlanticDfs(r,c):
            
            atlanticGrid.add((r,c))
            atlanticVisited.add((r,c))

            directions = [[-1,0],[0,1],[1,0],[0,-1]]
            for dr, dc in directions:
                if r+dr in range(len(heights)) and c+dc in range(len(heights[0])) and heights[r+dr][c+dc] >= heights[r][c] and (r+dr,c+dc) not in atlanticVisited: 
                    atlanticDfs(r+dr, c+dc)
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                #check the coasts
                if r == 0 or c == 0:
                    pacificVisited.add((r,c))
                    pacificDfs(r,c)
                    
                if r == len(heights)-1 or c == len(heights[0]) - 1:
                    atlanticVisited.add((r,c))
                    atlanticDfs(r,c)
                    
        
        #print(pacificGrid)
        #print(atlanticGrid)


        for n in pacificGrid:
            if n in atlanticGrid:
                ans.append(n)
        return ans
