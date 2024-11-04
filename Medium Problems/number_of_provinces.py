class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        

        mapping = dict()
        for i in range(len(isConnected)):
            mapping[i+1] = []

        print(isConnected)

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                # print("hello")
                if (isConnected[i][j] == 1):
                    mapping[i+1].append(j+1)
        
        print(mapping)
        q = deque()
        visited = set()
        def bfs(node):
            q.append(node)
            visited.add(node)
            while q:
                current = q.popleft()
                for neighbor in mapping[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
        count= 0
        for key in mapping:
            if key not in visited:
                bfs(key)
                count += 1

        return count
