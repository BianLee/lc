class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        row=dict()
        col=dict()
        for i,j in indices:
            if i in row:
                row[i]+=1
            else:
                row[i]=1
            if j in col:
                col[j]+=1
            else:
                col[j]=1
        print(row, col)
        sim = [[0 for i in range(n)] for i in range(m)]
        print(sim)
        for key,value in row.items():
            x=0
            while x<n:
                sim[key][x] += value
                x+=1
        print(sim)
        for key,value in col.items():
            x=0
            while x<m:
                sim[x][key] += value
                x+=1
        ans=0
        for i in range(m):
            for j in range(n):
                if (sim[i][j]) % 2 == 1:
                    ans+=1
        return ans
