class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        dp = [[ -1 ] * (n + 1) for _ in range(n + 1)]
        
        def f(summ, tmp):
            nonlocal x, n
            if dp[summ][tmp] != -1:
                return dp[summ][tmp]
            if summ == 0:
                return 1
            if tmp < 0 :
                return 0
            
            cnt = 0
            if pow(tmp, x) <= summ:
                cnt =  (f(summ - pow(tmp, x), tmp - 1) + f(summ, tmp - 1)) % MOD
            else:
                cnt = f(summ, tmp - 1) 
            dp[summ][tmp] = cnt
            return cnt
                
            
        return f(n, n)