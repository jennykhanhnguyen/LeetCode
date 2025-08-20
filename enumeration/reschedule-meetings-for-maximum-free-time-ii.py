class Solution(object):
    def maxFreeTime(self, eventTime, startTime, endTime):
        """
        :type eventTime: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """

        gaps = []
        for i in range(len(startTime)):
            if i == 0:
                gaps.append(startTime[i])
            else:
                gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])
        #    0     1     2
        # 0     1      2       3
        #xxxx--xxxx---xxx----xxxxx--
        pref = [gaps[i] for i in range(len(gaps))]
        suff = [gaps[i] for i in range(len(gaps))]

        for i in range(1, len(pref)):
            pref[i] = max(pref[i - 1], pref[i])

        for i in range(2, len(pref)):
            suff[-i] = max(suff[-i + 1], suff[-i])
        ans = 0
        for j in range(1, len(gaps)):
            # merge j, j - 1
            ans = max(ans, gaps[j] + gaps[j - 1])
            meeting_duration = endTime[j - 1] - startTime[j - 1]

            Left_gaps_max = pref[j - 2] if j >= 2 else 0
            Right_gaps_max = suff[j + 1] if j + 1 < len(gaps) else 0

            if max(Left_gaps_max, Right_gaps_max) >= meeting_duration:
                ans = max(ans, gaps[j] + gaps[j - 1] + meeting_duration)

        return ans