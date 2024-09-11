class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        
        for course, prereq in prerequisites:
            graph[prereq].append(course) # prereq -> course
            indegree[course]+=1
        
        print(graph)
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0: #
                q.append(i)
            
        ans = []
        coursesTaken = 0
        while q:
            node = q.popleft()
            ans.append(node)
            coursesTaken+=1

        
            for neighbor in graph[node]:
                indegree[neighbor]-=1

                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        if coursesTaken == numCourses:
            return ans
        return []



        
