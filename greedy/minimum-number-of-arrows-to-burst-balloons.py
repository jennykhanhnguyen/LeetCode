class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        current = points[0][1]
        ans = 1
        points = points[1:]
        for start, end in points:
            if start > current:
                ans += 1
                current = max(end, current)
        return ans