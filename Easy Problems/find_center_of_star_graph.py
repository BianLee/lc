class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        memo=dict()
        for a,b in edges:
            if a in memo:
                memo[a]+=1
            else:
                memo[a]=1
            
            if b in memo:
                memo[b]+=1
            else:
                memo[b]=1
        for key, value in memo.items():
            if value == len(edges):
                return key
