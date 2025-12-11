from collections import deque 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0]*len(rooms)
        visited[0] = 1
        queue = deque()
        queue.append(0)
        while queue:
            size = len(queue)
            for i in range (size):
                node = queue.popleft()
                for nei in rooms[node]:
                    if visited[nei] == 0:
                        queue.append(nei)
                        visited[nei] = 1
        return sum(visited) == len(rooms)
        