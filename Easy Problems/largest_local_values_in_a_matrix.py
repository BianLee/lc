class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        n = len(grid)
        arr = []
        print(arr)
        for a in range(n-2):
            for b in range(n-2):
                localMax = float('-inf')
                for i in range(3):
                    for j in range(3):
                        localMax = max(grid[i+a][j+b], localMax)
                arr.append(localMax)
        
        ans = []

        i= 0
        while i < len(arr):
            temp = []
            for j in range(n-2):
                temp.append(arr[i])
                i+=1
            ans.append(temp)

        return ans
