class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        f = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            for j in range(i): 
                if nums[j] < nums[i]:
                    f[i] = max(f[i], f[j] + 1)

        return max(f)