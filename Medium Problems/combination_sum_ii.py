class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        if len(candidates) == 1 and sum(candidates) == target:
            return [candidates]


        candidates.sort()
        #print(candidates)
        #[1,1,2,5,6,7,10]
        #print(candidates)
        self.ans = []
        def dfs(pointer, build, curr_sum):
            
            if curr_sum == target:
                #print(build)
                temp = build.copy()
                temp.sort()
                if temp not in self.ans:
                    self.ans.append(temp)
            elif curr_sum > target:
                return
            
            for i in range(pointer, len(candidates)):
                if i-1>=pointer and candidates[i] == candidates[i-1]:
                    continue
                build.append(candidates[i])
                dfs(i+1, build, curr_sum+candidates[i])
                build.pop()
                
            
    
        dfs(0, [], 0)
        return self.ans
