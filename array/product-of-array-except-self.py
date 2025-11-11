class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        pref = [0]* n
        suff = [0]* n
        pref[0] = nums[0]
        suff[0] = nums[-1]
        for i in range(1, n):
            pref[i] = pref[i-1] * nums[i]
            suff[i] = suff[i-1] * nums[n-i-1]
        for i in range(n):
            if i == 0:
                res.append(suff[n-2])
            elif i == n-1: 
                res.append(pref[n-2])
            else:
                res.append(pref[i-1]*suff[n-2-i])
        return res