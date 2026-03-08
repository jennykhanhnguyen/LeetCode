from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # build graph
        graph = defaultdict(list)
        for left, right in adjacentPairs:
            graph[left].append(right)
            graph[right].append(left)
        for node in graph:
            if len(graph[node]) == 1:
                start_node = node
                break
        visited = set()
        visited.add(start_node)
        path = [start_node]
        def dfs(node):
            for nei in graph[node]:
                if nei not in visited:
                    path.append(nei)
                    visited.add(nei)
                    dfs(nei)

        dfs(start_node)
        return path