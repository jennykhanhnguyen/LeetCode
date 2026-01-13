class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
      
        def quick_power(base: float, exponent: int) -> float:
            """
            Helper function to calculate base^exponent using binary exponentiation.
            Only handles non-negative exponents.
            """
            result = 1.0
          
            # Process each bit of the exponent
            while exponent > 0:
                # If current bit is 1, multiply result by current base
                if exponent & 1:  # Check if least significant bit is 1
                    result *= base
              
                # Square the base for the next bit position
                base *= base
              
                # Right shift to process the next bit
                exponent >>= 1
          
            return result
      
        # Handle negative exponents by computing 1 / (x^(-n))
        if n >= 0:
            return quick_power(x, n)
        else:
            return 1.0 / quick_power(x, -n)     