import bisect

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + nums[i]

        ans = float('inf')

        for j in range(1, n + 1):
            needed = prefix[j] - target

            i = bisect.bisect_right(prefix, needed, 0, j) - 1

            if i >= 0:
                ans = min(ans, j - i)

        return ans if ans != float('inf') else 0