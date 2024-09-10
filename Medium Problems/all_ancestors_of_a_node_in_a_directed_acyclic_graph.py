class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        reversed_mapping = defaultdict(list)
        for parent, child in edges:
            reversed_mapping[child].append(parent)
        
        print(reversed_mapping)

        def dfs(node, visited, parents):
            for parentNode in reversed_mapping[node]:
                if parentNode not in visited:
                    visited.add(parentNode)
                    parents.add(parentNode)
                    dfs(parentNode, visited, parents)
            
        ans=[]
        for i in range(n):
            parents = set()
            visited = set()
            dfs(i, visited, parents)
            ans.append(sorted(parents))
    
        return ans
