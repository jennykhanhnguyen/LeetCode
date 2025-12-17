from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights) # rows
        n = len(heights[0]) # cols
        pacific_heads = deque()
        atlantic_heads = deque()
        for i in range(n):
            pacific_heads.append((0,i))
        for j in range(1,m):
            pacific_heads.append((j,0))
        for i in range(0,m-1): 
            atlantic_heads.append((m-1, i)) 
        for j in range(n):             
            atlantic_heads.append((j, n-1))  
        # bfs 
        dirx = [-1, 0, 0, 1]
        diry = [0, -1, 1, 0]
        def bfs(queue):
            lstres =[]
            visited = {}
            while queue:
                size = len(queue)
                for i in range(size):
                    curx,cury = queue.popleft()
                    lstres.append((curx,cury))
                    for j in range(4):
                        newx = curx + dirx[j]
                        newy = cury + diry[j]
                        if newx >= 0 and newx <= m-1 and newy >= 0 and newy <= n-1 and (newx, newy) not in visited and heights[newx][newy] >= heights[curx][cury]:
                            visited[(newx, newy)] = 1
                            queue.append((newx,newy))
            return lstres
        pacific_res = bfs(pacific_heads)
        atlantic_res = bfs(atlantic_heads)
        final_res = []
        for tple in pacific_res:
            if tple in pacific_res and tple in atlantic_res and tple not in final_res:
                final_res.append(tple)
        for tple in atlantic_res:
            if tple in pacific_res and tple in atlantic_res and tple not in final_res:
                final_res.append(tple)
        return final_res


