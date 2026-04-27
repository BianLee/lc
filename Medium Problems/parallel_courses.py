class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        
        indegrees = dict()
        for i in range(n):
            indegrees[i+1] = 0
        for prev, next in relations:
            indegrees[next] += 1

        print(indegrees)

        graph = defaultdict(list)

        for prev, next in relations:
            graph[prev].append(next)
        
        print(graph)

        q = deque()
        for key, value in indegrees.items():
            if value == 0:
                q.append(key)

        print(q)

        
        semester, taken = 0, 0
        while q:
            semester+=1
            for i in range(len(q)):
                course = q.popleft()
                taken += 1
                for unlocked in graph[course]:
                    indegrees[unlocked] -= 1
                    if indegrees[unlocked] == 0:
                        q.append(unlocked)

        if taken == n:
         
            return semester

        return -1
                
