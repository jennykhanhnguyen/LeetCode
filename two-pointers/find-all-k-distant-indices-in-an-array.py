class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        index = []
        ans = []
        for i in range (len(nums)):
            if nums[i] == key:
                index.append(i)
                
        for i in range (len(nums)):
            for j in index:
                if abs(i-j) <=k:
                    ans.append(i)
                    break
        ans.sort()
        return ans