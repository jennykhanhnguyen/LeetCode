class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        path = []
        final = []

        def backtrack(start,ind):
            if ind == k:
                final.append(path[:])
                return
            for i in range(start+1,n+1):
               path.append(i)
               backtrack(i,ind+1)
               path.pop()
        backtrack(0,0)
        return final