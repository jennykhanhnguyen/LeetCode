class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            # Clear the least significant set bit
            # Example: n = 1100, n-1 = 1011, n & (n-1) = 1000
            n &= n - 1
          
            # Increment the count as we've removed one 1 bit
            count += 1
      
        return count
