from collections import defaultdict, deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        queue = deque()
        fresh = 0
        dirr = [-1,0,0,1]
        diry = [0,-1,1,0]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    queue.append((row,col))
        rotten = len(queue)
        minutes = 0
        while queue:
            size = len(queue)
            found = False
            for i in range(size):
                row, col = queue.popleft()
                for j in range(4):
                    newr = row + dirr[j]
                    newc = col + diry[j]
                    if newr >= 0 and newr <= len(grid)-1 and newc >= 0 and newc <= len(grid[0])-1:
                        if grid[newr][newc] == 1:
                            fresh -= 1
                            grid[newr][newc] = 2
                            queue.append((newr,newc))
                            found = True
            if found:
                minutes += 1
        return minutes if fresh == 0 else -1

