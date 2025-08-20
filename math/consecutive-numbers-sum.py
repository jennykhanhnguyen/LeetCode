class Solution(object):
    def consecutiveNumbersSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        # b*(b+1) - (a-1)*(a) = 2n
        # b**2 + b - a**2 + a = 2n
        # (b-a) * (b+a) + (b+a) = 2n
        # (b+a) (b-a+1) = 2n
        cnt = 0
        for u in range (1, int(sqrt(2*n))+1):
            if (2*n)%u == 0 and ((2*n)//u+u-1)%2== 0 and ((2*n)//u-u+1)%2==0:
                cnt+= 1
        return cnt

