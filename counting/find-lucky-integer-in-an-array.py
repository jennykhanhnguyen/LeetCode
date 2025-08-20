class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        ans = 0
        dic = Counter(arr)
        for key in dic:
            if key == dic[key]:
                ans = key
        if ans == 0:
            ans = -1
        return ans