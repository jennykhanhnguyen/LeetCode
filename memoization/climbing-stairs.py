class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0]*(n+1)
        for i in range(1,n+1):
            if i == 1:
                mem[i] = 1
            elif i == 2:
                mem[i] = 2
            else:
                mem[i] = mem[i-1]+mem[i-2]
        return mem[n]