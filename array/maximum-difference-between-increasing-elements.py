class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        curmin = nums[0]
        ans = -1
        for i in range(1, len(nums)):
            if nums[i] > curmin:
                ans = max(ans, nums[i] - curmin)
            else:
                curmin = nums[i]
        return ans
