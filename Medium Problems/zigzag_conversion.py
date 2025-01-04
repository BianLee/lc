class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # numRows + (numRows-2) + numRows

        rowStr = [[] for i in range(numRows)]
        print(rowStr)
        # 0,1,2,1,0
        rowCount = 0
        direction = "forward"
        for i in range(len(s)):
            rowStr[rowCount].append(s[i])
            print(rowCount)
            if rowCount+1 < numRows and direction=="forward":
                rowCount+=1
            elif rowCount-1 > -1 and direction=="backward":
                rowCount-=1
            
            if rowCount == numRows-1:
                direction = "backward"
            if rowCount == 0:
                direction = "forward"
        ans=""
        for i in range(len(rowStr)):
            for j in rowStr[i]:
                ans+=str(j)
        return ans


    
