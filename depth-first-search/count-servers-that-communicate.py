class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = 0
        def dfs(row, col):
            nonlocal communicate
            for r in range(len(grid)):
                if grid[r][col] == 1 and (r,col) not in visited:
                    communicate += 1
                    visited.add((r,col))
                    dfs(r, col)
            for c in range(len(grid[0])):
                if grid[row][c] == 1 and (row,c) not in visited:
                    communicate += 1
                    visited.add((row,c))
                    dfs(row, c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    visited.add((r, c))
                    communicate = 1
                    dfs(r,c)
                    if communicate > 1:
                        ans += communicate

        return ans