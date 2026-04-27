from collections import defaultdict

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
    
        indegree=dict()
        
        for i in range(n):
            indegree[i+1] = 0

        for prev, next in relations:
            indegree[next] += 1
        
        # print(indegree)
    
        graph = defaultdict(list)
        
        for prev, next in relations:
            graph[prev].append(next)
    
        print(graph)

        queue = deque()
        for course in indegree:
            if indegree[course] == 0: 
                queue.append(course) #add the course without prereqs into the queue

        semesters, taken = 0,0
        while queue:
            semesters += 1
            for i in range(len(queue)):
                course = queue.popleft()
                taken += 1
                for neighbor in graph[course]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)

        if taken == n:
            return semesters
        else:
            return -1


        


