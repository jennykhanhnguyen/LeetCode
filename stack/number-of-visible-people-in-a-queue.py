class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        res =[0]*n
        stack = [] # monotonic decreasing stack
        for i in range(n - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop() # block sight
                res[i] += 1 # the current person is able to see that shorter person but not anyones on the left
            if stack: # heights[k,l] = [6, 9, 8, 7] then the while above remove 7, then we still have 9, 8 but we can only see 9
                res[i] += 1
            stack.append(heights[i]) # we removed all the smaller person (from the left of the stack), so the next smallest is the current heights[i]
        return res


