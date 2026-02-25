class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        num_row = len(matrix)
        num_col = len(matrix[0])
        left, right = 0, num_row - 1
        while left <= right:
            mid = (left + right) // 2
            row_start = matrix[mid][0]
            row_end = matrix[mid][num_col - 1]
            if target < row_start:
                right = mid -1
            elif target > row_end:
                left = mid + 1
            else:
                left_col, right_col = 0, num_col - 1
                while left_col <= right_col:
                    mid_col = (left_col + right_col) // 2
                    if target < matrix[mid][mid_col]:
                        right_col = mid_col -1
                    elif target > matrix[mid][mid_col]:
                        left_col = mid_col +1
                    else:
                        return True
                return False
        return False