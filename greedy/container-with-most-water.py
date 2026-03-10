class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxval = 0
        left = 0
        right = len(height) -1
        while left < right:
            maxx = min(height[left], height[right])*(right-left)
            maxval = max(maxx, maxval)
            # print(left, right, maxx, maxval)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxval
