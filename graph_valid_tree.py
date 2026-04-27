class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        q = deque([(0, -1)]) # have to save the parent (the second element)
        # q.append(edges[0][0])
        visited = set()

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
    

        while q:
            print(q)
            for i in range(len(q)):
                node, parent = q.popleft()
                visited.add(node)
                for unlocked in graph[node]:
                    if unlocked == parent:
                        continue
                    if unlocked in visited:
                        print(unlocked)
                        return False
                    q.append((unlocked, node))
    
        if len(visited) != n:
            return False




        return True
        
