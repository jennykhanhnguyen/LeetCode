from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # dijkstra
        graph = defaultdict(list)
        for left, right, weight in times:
            graph[left].append((right, weight))
        heap = [(0, k)]
        dist = {k: 0}
        while heap:
            curr_dist, node = heapq.heappop(heap)
            if curr_dist > dist[node]:
                continue
            for nei, wei in graph[node]:
                new_dist = curr_dist + wei
                if nei not in dist or new_dist < dist[nei]:
                    dist[nei] = new_dist
                    heapq.heappush(heap,(new_dist,nei))
        return max(dist.values()) if len(dist.keys()) == n else -1