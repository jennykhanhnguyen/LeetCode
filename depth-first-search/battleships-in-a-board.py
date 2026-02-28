from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        if not board or not board[0]:
            return 0

        m, n = len(board), len(board[0])
        ships = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'X':
                    continue
                if i > 0 and board[i - 1][j] == 'X':
                    continue
                if j > 0 and board[i][j - 1] == 'X':
                    continue
                ships += 1

        return ships