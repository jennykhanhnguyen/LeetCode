class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range (9):
            seenr = set()
            seenc = set()
            for c in range (9):
                if board[r][c] != '.': 
                    if board[r][c] in seenr:
                        return False
                    seenr.add(board[r][c])

                if board[c][r] != '.':
                    if board[c][r] in seenc:
                        return False
                    seenc.add(board[c][r])
        r = 0
        c = 0
        dr = (0, 1, 2, 0, 1, 2, 0, 1, 2)
        dc = (0,0,0,1,1,1,2,2,2)
        for r in range (0,9,3):
            for c in range (0,9,3):
                seen = set()
                for i in range (9):
                    newr = r + dr[i]
                    newc = c + dc[i]
                    if board[newr][newc] != '.': 
                        if board[newr][newc] in seen:
                            return False
                        seen.add(board[newr][newc])
        return True

