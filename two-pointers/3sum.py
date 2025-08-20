class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = set()
        nums.sort()
        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            rangej = set()
            for k in range (i+2, len(nums)):
                diff = 0 - nums[i] - nums[k]
                rangej.add(nums[k-1])
                if diff < nums[i+1]:
                    break
                if diff in rangej:
                    ans.add((nums[i], diff, nums[k]))
        ans = list(ans)
        newans = []
        for tup in ans:
            newans.append([x for x in tup])
        return newans
