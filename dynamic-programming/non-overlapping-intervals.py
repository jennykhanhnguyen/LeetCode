class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 1
        intervals.sort(key=lambda x: x[1])
        # print(intervals)
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        for index, item in enumerate(intervals):
            if index == 0:
                continue
            start = item[0]
            end = item[1]
            if current_end == end:
                current_start = min(current_start, start)
                continue
            if start >= current_start and start < current_end:
                continue
            # print(current_start, current_end, start, end)
            current_end = end
            ans += 1
        return len(intervals) - ans
