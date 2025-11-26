from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)

        # edge case
        if grid[0][0] == 0 and n == 1 and len(grid[0]) == 1:
            return 1
        elif grid[0][0] != 0 or grid[n-1][n-1] != 0:
            return -1
        # print('a')
        visited = []
        for i in range(n):
            visited.append([0]*n)
        visited[0][0] = 1
        queue = deque()
        queue.append((0,0))
        res = 1
        directionx = [-1,-1,-1,0,0,1,1,1]
        directiony = [-1,0,1,-1,1,-1,0,1]
        while queue:           
            res += 1
            size = len(queue)
            for i in range(size):
                x,y = queue.popleft()
                # print(x,y,res)
                for i in range(8):
                    newx = x + directionx[i]
                    newy = y + directiony[i]
                    if newx >= 0 and newx <= n-1 and newy >= 0 and newy <= n-1:   
                        # print(newx, newy, grid[newx][newy], visited[newx][newy])                    
                        if grid[newx][newy] == 0 and visited[newx][newy] == 0:
                            # print(newx,newy)
                            queue.append((newx,newy))
                            visited[newx][newy] = 1
                            #print(1,newx, newy)
                        if newx == n-1 and newy == n-1:
                            return res
            # print(visited)    
        return -1

# [[0,0,0]
# ,[0,1,0]
# ,[0,0,0]]
