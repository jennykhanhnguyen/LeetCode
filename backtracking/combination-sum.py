class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        final = []
        path = []
        def backtrack(i, s):
            if s >= target:
                if s == target:
                    final.append(path[:])
                return
            for j, num in enumerate(candidates[i:]):
                path.append(num)
                backtrack(i+j, s+num)
                path.pop()
        backtrack(0,0)
        return final