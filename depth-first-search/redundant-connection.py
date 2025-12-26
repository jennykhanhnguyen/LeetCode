from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges):
        graph = defaultdict(list)              # adjacency list
        ans = None                             # store last redundant edge

        def has_path_dfs(src, target):
            stack = [src]                      # DFS stack
            seen = set([src])                  # visited set

            while stack:                       # standard DFS loop
                node = stack.pop()
                if node == target:             # found a path src -> target
                    return True
                for nei in graph[node]:        # explore neighbors
                    if nei not in seen:
                        seen.add(nei)
                        stack.append(nei)
            return False                        # no path exists

        for u, v in edges:                     # process edges in given order
            # If u and v are already connected, this edge creates a cycle
            if u in graph and v in graph and has_path_dfs(u, v):
                ans = [u, v]                   # record it (keep last one)
            else:
                graph[u].append(v)             # add edge to graph
                graph[v].append(u)

        return ans

        