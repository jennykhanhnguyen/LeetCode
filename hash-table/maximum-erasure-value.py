class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ans = 0
        max_val = 0
        set_nums = set()
        left = 0
        for i in range(len(nums)):
            while nums[i] in set_nums:
                set_nums.remove(nums[left])
                max_val -= nums[left]
                left += 1
            max_val += nums[i]
            ans = max(ans, max_val)
            set_nums.add(nums[i])
        return ans