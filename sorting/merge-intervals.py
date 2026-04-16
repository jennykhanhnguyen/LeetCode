class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()
        current_start = intervals[0][0]
        current_end = intervals[0][1]
        for index, item in enumerate(intervals):
            if index == 0:
                continue
            start = item[0]
            end = item[1]
            if start >= current_start and start <= current_end:
                current_end = max(end, current_end)
            else:
                ans.append([current_start, current_end])
                current_start = start
                current_end = end
        if len(ans) == 0 or ans[-1][0] != current_start:
            ans.append([current_start, current_end])
        return ans