from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for l, r, w in flights:
            graph[l].append((r,w))
        total_price = float("inf")
        visited = set()
        visited.add(src)
        memo = {}
        def dfs(node, price, stop):
            nonlocal total_price
            if stop > k +1:
                return
            elif node == dst:
                total_price = min(total_price, price)
                return 
            if (node, stop) in memo and memo[(node, stop)] <= cost:
                return
            memo[(node, stop)] = price
            for nei, wei in graph[node]:
                if nei not in visited and price + wei < total_price:
                    visited.add(nei)
                    dfs(nei, price + wei, stop + 1)
                    visited.remove(nei)                
        dfs(src, 0, 0)
        return total_price if total_price != float("inf") else -1