class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxval = 0
        left = 0
        right = len(height) -1
        while left < right:
            maxx = min(height[left], height[right])*(right-left)
            # print(left, right, maxx, maxval)
            maxval = max(maxx, maxval)
            if left >= right:
                right -= 1
            else:
                left += 1
        return maxval
