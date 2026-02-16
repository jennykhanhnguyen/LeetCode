class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algo with no heap
        n = len(points)        
        visited = [False] * n
        min_dist = [float('inf')] * n
        
        min_dist[0] = 0
        total_cost = 0
        
        for i in range(n):
            u = -1
            for j in range(n):
                if not visited[j] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i

            visited[u] = True
            total_cost += min_dist[u]
            
            for v in range(n):
                if not visited[v]:
                    dist = abs(points[u][0] - points[v][0]) + \
                           abs(points[u][1] - points[v][1])
                    
                    if dist < min_dist[v]:
                        min_dist[v] = dist
        
        return total_cost
