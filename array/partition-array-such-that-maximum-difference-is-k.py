class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        ans = 0
        nums.sort()
        minval = nums[0]
        for i in range (len(nums)):
            if nums[i] - minval > k:
                minval = nums[i] 
                ans += 1
        return ans+1
