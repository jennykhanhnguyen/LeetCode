from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = set()
        final = 0
        def bfs(x,y):
            maxx = 0
            queue = deque()
            queue.append((x,y))
            visited.add((x,y))
            dirx = [-1, 0, 0, 1]
            diry = [0, -1, 1, 0]
            while queue:
                size = len(queue)
                for i in range(size):
                    row, col = queue.popleft()
                    maxx += 1
                    for j in range(4):
                        newrow = row + dirx[j]
                        newcol = col + diry[j]
                        if newrow >= 0 and newrow < len(grid) and newcol >= 0 and newcol < len(grid[newrow]):
                            if grid[newrow][newcol] == 1 and (newrow,newcol) not in visited:
                                queue.append((newrow, newcol))
                                visited.add((newrow, newcol))
            nonlocal final
            final = max(final, maxx)


        for row in range(len(grid)):
            for col in range (len(grid[row])):
                if grid[row][col] == 1 and (row,col) not in visited:
                    bfs(row,col)
        return final
        
