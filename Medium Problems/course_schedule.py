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
