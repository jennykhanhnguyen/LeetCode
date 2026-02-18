from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for left, right in redEdges:
            graph[left].append((right, "red"))
        for left, right in blueEdges:
            graph[left].append((right, "blue"))
        queue = deque()
        queue.append((0, ""))
        ans = [-1]*n
        ans[0] = 0
        level = 0
        while queue:
            level += 1
            size = len(queue)
            for i in range(size):
                node, last_color = queue.popleft()
                for neighbor, color in graph[node]:
                    if color != last_color:
                        if ans[neighbor] == -1:
                            ans[neighbor] = level
                        queue.append((neighbor, color))
        return ans


