class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
            
        visited = set()
        def dfs(crs):
            if crs in visited: #if it has already been visited
                return False
            if preMap[crs] == []: #if it encounters a case where there is no dependencies 
                return True

            visited.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            visited.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):
            
            if dfs(c) == False: 
                return False
        
        return True


#alternative topological sort
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course]+=1

        #initialize queue with all courses that have no prereqs
        
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        taken_courses = 0
        while queue:
            course = queue.popleft()
            taken_courses += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return taken_courses == numCourses
