class Solution(object):
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        """
        :type eventTime: int
        :type k: int
        :type startTime: List[int]
        :type endTime: List[int]
        :rtype: int
        """
        arr = []
        best = 0
        s = 0
        for i in range (len(startTime)):
            if i == 0:
                arr.append(startTime[i] - 0)
            else:
                arr.append(startTime[i] - endTime[i-1])
        arr.append(eventTime - endTime[i])

        k+=1
        
        for i in range (len(arr)):
            s += arr[i]
            if i >= k:
                s -= arr[i-k]
            best = max(best, s)

        return best