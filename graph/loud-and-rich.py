from collections import defaultdict, deque
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # topo sort
        n = len(quiet)
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for left, right in richer:
            graph[left].append(right)
            indegree[right] += 1
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
        ans = list(range(n))
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                for nei in graph[node]:
                    indegree[nei] -= 1
                    if quiet[ans[node]] < quiet[ans[nei]]:
                            ans[nei] = ans[node]
                    if indegree[nei] == 0:                       
                        queue.append(nei)
        return ans