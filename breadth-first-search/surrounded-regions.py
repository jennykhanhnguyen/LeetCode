class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dirx = [-1,0,0,1]
        diry = [0,-1,1,0]
        res = 0
        queue = deque()
        for i in range(m):
            if board[i][0] == "O":
                queue.append((i,0))
            if board[i][n-1] == "O":
                queue.append((i,n-1))
        for i in range(1,n-1):
            if board[0][i] == "O":
                queue.append((0,i))
            if board[m-1][i] == "O":     
                queue.append((m-1,i))
        # print(queue)
        while queue:
            size = len(queue)
            for k in range(size):
                x, y = queue.popleft()
                # print(x,y)
                board[x][y] = "S"
                for z in range(len(dirx)):
                    newx = x + dirx[z]
                    newy = y + diry[z]                   
                    if newx >=0 and newx <= m-1 and newy >= 0 and newy <= n-1 and board[newx][newy] == "O":
                        # print(newx,newy)
                        queue.append((newx, newy))
                        # print(newx,newy)
                        board[newx][newy] = "S"
        # for i in range(m):
        #     for j in range(n):
        #         print(board[i][j])
        #     print("\n")
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "S":
                    board[i][j] = "O"
        
        