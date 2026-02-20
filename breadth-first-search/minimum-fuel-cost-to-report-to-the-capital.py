from collections import defaultdict, deque
import math
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = defaultdict(list)
        for left, right in roads:
            graph[left].append(right)
            graph[right].append(left)
        fuel = 0

        def dfs(node, parent):
            people = 1
            nonlocal fuel
            for nei in graph[node]:
                if nei == parent:
                    continue
                child_people = dfs(nei, node)
                people += child_people
                fuel += math.ceil(child_people/seats)
            return people
        dfs(0, -1)
        return fuel

        