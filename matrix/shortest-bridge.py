from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        group1 = set()
        n = len(grid)
        found1 = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    startr = r
                    startc = c
                    found1 = True
                    break
            if found1 == True:
                break
        group1.add((startr, startc))
        dirr = [0, 0, 1, -1]
        dirc = [-1, 1, 0, 0]
        def dfs(row, col):
            for i in range(4):
                newr = row + dirr[i]
                newc = col + dirc[i]
                if newr >= 0 and newr < n and newc >= 0 and newc < n and (newr,newc) not in group1:
                    if grid[newr][newc] == 1:
                        group1.add((newr, newc))
                        dfs(newr, newc)
        dfs(startr, startc)
        queue = deque(group1)
        visited = group1

        # bfs
        lv = -1
        while queue:
            lv += 1
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for i in range(4):
                    newr = row + dirr[i]
                    newc = col + dirc[i]
                    if newr >= 0 and newr < n and newc >= 0 and newc < n and (newr,newc) not in visited:
                        if grid[newr][newc] == 0:
                            visited.add((newr, newc))
                            queue.append((newr, newc))
                        else:
                            return lv
                                           


