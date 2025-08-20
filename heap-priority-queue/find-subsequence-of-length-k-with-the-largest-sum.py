class Solution(object):
    def maxSubsequence(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        newnums = []
        for i in range (len(nums)):
            newnums.append((i, nums[i]))
        newnums = sorted(newnums, key = lambda x: -x[1])
        newnums = newnums[:k]
        newnums = sorted(newnums, key = lambda x: x[0])
        return [x[1] for x in newnums]
