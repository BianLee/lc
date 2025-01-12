class Solution:
    def validStrings(self, n: int) -> List[str]:
        
        self.ans = []
        def dfs(build):
            
            for i in range(len(build)):
                if i+1<len(build) and build[i] == build[i+1] == 0:
                    return

            if len(build) == n:
                self.ans.append(build.copy())
                return

            build.append(0)
            dfs(build)

            build.pop()

            build.append(1)
            dfs(build)
            build.pop()
                

        dfs([])

        final = []
        for i in range(len(self.ans)):
            temp = ""
            for c in self.ans[i]:
                temp+=str(c)
            final.append(temp)
        return final
                
