from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = [0]*len(graph)
        red = set()
        blue = set()
        red.add(0)
        queue = deque()
        queue.append(0)
        while queue:
            size = len(queue)
            for k in range(size):
                node = queue.popleft()
                visited[node] = 1
                if node in red:
                    for z in range(len(graph[node])):      
                        if graph[node][z] in red: 
                            return False           
                        if visited[graph[node][z]] == 0:
                            queue.append(graph[node][z])
                            blue.add(graph[node][z])
                            # visited[graph[node][z]] = 1
                elif node in blue:
                    for z in range(len(graph[node])):   
                        if graph[node][z] in blue: 
                            return False       
                        if visited[graph[node][z]] == 0:
                            queue.append(graph[node][z])
                            red.add(graph[node][z])
                            # visited[graph[node][z]] = 1
        return True