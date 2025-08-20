class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        left = 0
        ans = 0
        right = len(nums) -1
        abc = 10**9 + 7
        for left in range(len(nums)):
            while right >= left and nums[right] + nums[left] > target:
                right -= 1
            if right < left:
                break
            ans += pow(2, right-left, abc)
        return ans%abc
            

