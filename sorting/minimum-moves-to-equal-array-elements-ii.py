class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        med = nums[len(nums)//2]
        ans = 0
        for i in range(len(nums)):
            ans += abs(med - nums[i])
        return ans
