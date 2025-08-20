class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        cnteven = sum(1 for x in nums if x % 2 == 0)
        cntodd = sum(1 for x in nums if x % 2 == 1)

        even = odd = 0
        for num in nums:
            if num % 2 == 0:
                even = max(even, odd + 1)
            else:
                odd = max(odd, even + 1)

        return max(cnteven, cntodd, even, odd)