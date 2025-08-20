class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if i != 0:
                nums[i] += nums[i-1]
        count = 0
        for i in range(len(nums)-1):
            if nums[i] >= (nums[-1] - nums[i]):
                count +=1

        return count