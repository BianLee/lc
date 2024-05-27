class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited=set()
        q=deque()

        def bfs():
            while q:
                a=q.popleft()
                for j in rooms[a]:
                    if j not in visited and j not in q:
                        q.append(j)
                visited.add(a)

        q.append(0)
        bfs()
        return len(visited) == len(rooms)

        
