class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        final = []
        path = []
        visited = [0]*n
        def backtrack(index):
            if index == n:
                final.append(path[:])
                return
            for i, num in enumerate(nums):
                if visited[i] == 0:
                    visited[i] = 1
                    path.append(num)
                    backtrack(index+1)
                    visited[i] = 0
                    path.pop()
        backtrack(0)
        return final
