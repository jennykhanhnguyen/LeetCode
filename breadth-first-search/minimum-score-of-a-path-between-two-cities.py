from collections import defaultdict
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        adj = defaultdict(list)
        for left, right, weight in roads:
            adj[left].append((right, weight))
            adj[right].append((left, weight))
        res = float("inf")
        visited = set()
        def dfs(node):
            nonlocal res
            for nei, wei in adj[node]:
                res = min(res, wei)
                if nei not in visited:
                    visited.add(nei)
                    dfs(nei)

        # visited = set()
        # def dfs(node, val):
        #     nonlocal res
        #     if node == n:
        #         res = min(res, val)
        #         return
        #     for nei, wei in adj[node]:
        #         if nei not in visited:
        #             visited.add(nei)
        #             newwei = min(val, wei)
        #             dfs(nei, newwei)
                    # visited.remove(nei)
        dfs(1)
        return res

                