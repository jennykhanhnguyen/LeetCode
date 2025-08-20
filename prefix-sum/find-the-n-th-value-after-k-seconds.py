class Solution(object):
    def valueAfterKSeconds(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        nums = [1]*n
        for sec in range (1, k+1):
            for i in range (1,n):
                nums[i] += nums[i-1]
        return nums[n-1]%((10**9)+ 7)