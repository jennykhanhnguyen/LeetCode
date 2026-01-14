class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
      
        # Iterate through digits from right to left (least significant to most significant)
        for i in range(n - 1, -1, -1):
            # Add 1 to the current digit
            digits[i] += 1
          
            # Handle carry by taking modulo 10
            digits[i] %= 10
          
            # If the digit is not 0, there's no carry, so we can return
            if digits[i] != 0:
                return digits
      
        # If we reach here, all digits were 9 (e.g., 999 -> 1000)
        # Need to add a leading 1
        return [1] + digits