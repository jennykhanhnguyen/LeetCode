class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = overal = nums[0]
        for i in range(1, len(nums)):
            cur = max(nums[i], cur + nums[i])
            overal = max(overal, cur)
        return overal


            