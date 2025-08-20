class Solution(object):
    def isZeroArray(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: bool
        """
        newarr = [0] * (len(nums) + 1)
        for l, r in queries:
            newarr[l] += 1
            if newarr[r+1] < len(nums):
                newarr[r+1] -= 1
        count = 0
        for i in range(len(nums)):
            count += newarr[i]
            if nums[i] > count:
                return False
        return True




