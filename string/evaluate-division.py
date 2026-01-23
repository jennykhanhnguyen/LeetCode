from collections import defaultdict, deque
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # graph
        # bfs + dsu --> connected component
        # look up 
        ans = []
        graph = defaultdict(list)
        for index, tpl in enumerate(equations):
            graph[tpl[0]].append((tpl[1], float(1.0/values[index]))) # tuple: right, edge_val
            graph[tpl[1]].append((tpl[0], values[index]))
        visited = set()
        comp = {}
        dct = {}
        def bfs(node):
            queue = deque()
            queue.append(node)
            visited.add(node)
            comp[node] = node
            dct[node] = 1
            while queue:
                size = len(queue)
                for i in range(size):
                    top = queue.popleft()
                    for nei,wei in graph[top]:
                        if nei not in visited:
                            comp[nei] = node
                            dct[nei] = wei*dct[top]
                            visited.add(nei)
                            queue.append(nei)
        for key, val in graph.items():
            if key not in visited:
                bfs(key)
        print(comp)
        for left, right in queries:
            if left not in comp or right not in comp or comp[left] != comp[right]:
                ans.append(-1.0)
            else:
                ans.append(dct[left]/dct[right])
                
        return ans


            

