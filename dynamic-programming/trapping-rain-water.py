class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        left_max = height[i]
        right_max = height[j]
        ans = 0
        while i < j:
            if height[i] < height[j]:
                left_max = max(height[i], left_max)
                ans += left_max - height[i]
                i += 1
            else:
                right_max = max(height[j], right_max)
                ans += right_max - height[j]
                j -= 1
        return ans