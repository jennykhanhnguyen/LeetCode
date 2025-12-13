class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = []
        for i in range (n+1):
            adj.append([])
        for left, right, weight in roads:
            adj[left].append((right,weight))
            adj[right].append((left,weight))
        visited = [0]*(n+1)
        visited[1] = 1
        path = [1]
        minans = 999999999999
        # print(adj)
        def dfs(node, minval):
            if node == n:
                nonlocal minans
                minans = min (minans, minval)
            print(path, minans, visited)
            for nei,weight in adj[node]:
                minval = min(weight, minval)
                if visited[nei] == 0:
                    visited[nei] = 1
                    path.append((nei,weight))
                    dfs(nei, minval)   
                    visited[nei] = 0        
                    path.pop()
        dfs(1,9999999) 
        return minans
