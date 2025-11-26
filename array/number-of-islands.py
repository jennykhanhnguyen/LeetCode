from collections import deque
# Time complexity: n^2 + n^2
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid) # number of rows
        n = len(grid[0]) # number of cols
        visited = []
        res = 0
        for i in range(m):
            visited.append([0]*n)
        queue = deque()
        dirx = [-1,0,1,0]
        diry = [0,-1,0,1]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and visited[i][j] == 0:
                    # print(i,j,res)
                    queue.append((i,j))
                    visited[i][j] = 1
                    while queue:
                        size = len(queue)
                        for k in range(size):
                            x,y = queue.popleft()
                            for l in range(4):
                                newx = x + dirx[l]
                                newy = y + diry[l]                              
                                if newx >= 0 and newx <= m-1 and newy >= 0 and newy <= n-1:
                                    # print(newx, newy)
                                    if grid[newx][newy] == "1" and visited[newx][newy] == 0:
                                        queue.append((newx,newy))
                                        visited[newx][newy] = 1
                    res += 1
        return res



