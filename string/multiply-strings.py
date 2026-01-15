class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Handle edge case where either number is zero
        if num1 == "0" or num2 == "0":
            return "0"
      
        # Get lengths of both numbers
        len1, len2 = len(num1), len(num2)
      
        # Initialize result array with zeros
        # Maximum possible length of product is len1 + len2
        result = [0] * (len1 + len2)
      
        # Multiply each digit of num1 with each digit of num2
        # Starting from the rightmost digits (least significant)
        for i in range(len1 - 1, -1, -1):
            digit1 = int(num1[i])
          
            for j in range(len2 - 1, -1, -1):
                digit2 = int(num2[j])
              
                # Multiply current digits and add to corresponding position
                # Position i + j + 1 corresponds to the current digit position
                result[i + j + 1] += digit1 * digit2
      
        # Handle carries from right to left
        for i in range(len1 + len2 - 1, 0, -1):
            # Add carry to the previous position
            result[i - 1] += result[i] // 10
            # Keep only the single digit at current position
            result[i] %= 10
      
        # Find the starting index (skip leading zero if present)
        start_index = 0 if result[0] != 0 else 1
      
        # Convert result array to string and return
        return "".join(str(digit) for digit in result[start_index:])