'''
visted[node] = true /false 
visited[node] = true 
def dfs(node) : 
    for neigbor in adj[node] : 
        if not visited[neighbor] : 
            visited[neigbor] = true 
            dfs(neighbor)
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        visited = [0]*(n)
        visited[0] = 1
        path = [0]
        final = []
        def dfs(node):
            print(path,node)
            if node == n-1:
                final.append(path.copy())
                return
            
            for nei in graph[node]:
                if visited[nei] == 0:
                    visited[nei] = 1
                    path.append(nei)
                    dfs(nei)   
                    visited[nei] = 0        
                    path.pop()
        dfs(0)
        return final
               