class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        reversed_mapping = defaultdict(list)
        for start, end in edges:
            reversed_mapping[end].append(start)
        print(reversed_mapping)

        def dfs(node, visited, ancestors):
            for parent in reversed_mapping[node]:
                if parent not in visited:
                    visited.add(parent)
                    ancestors.add(parent)
                    dfs(parent, visited, ancestors)

        res = []
        for i in range(n):
            ancestors = set() # for each node, reinitialize the collection of ancestors to empty set
            dfs(i, set(), ancestors)
            res.append(sorted(ancestors))
        
        return res
