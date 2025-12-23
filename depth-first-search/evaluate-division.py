from collections import defaultdict
class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(list)
        for i in range(len(equations)): # a/b = 2.5 --> a = 2.5b
            graph[equations[i][0]].append((equations[i][1], values[i]))
            graph[equations[i][1]].append((equations[i][0], 1.0/values[i]))
        visited = set()
        def dfs(abv,blw, val):
            if abv == blw:
                return val
            for nei,wei in graph[abv]:
                if nei not in visited:
                    visited.add(nei)
                    res = dfs(nei, blw, val*wei)
                    if res != -1.0:
                        return res
            return -1.0
        ans = []
        for left, right in queries:
            if left not in graph or right not in graph:
                ans.append(-1.0)
            else:
                visited = set([left])
                ans.append(dfs(left,right,1))

        return ans