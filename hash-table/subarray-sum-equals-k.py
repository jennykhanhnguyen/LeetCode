class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pref = [0]*len(nums)
        pref[0] = nums[0]
        for i in range(1, len(nums)):
            pref[i] = pref[i-1] + nums[i]
        # for i in range(0, len(nums)):
        #     for j in range(i, len(nums)):
        #         if i == 0:
        #             print(pref[j])
        #             if pref[j] == k:
        #                 res += 1
        #         else:
        #             print(pref[j] - pref[i-1])
        #             if pref[j] - pref[i-1] == k:
        #                 res += 1
        dic = {0:1}
        for j in range(0, len(nums)):
            if pref[j] not in dic:
                dic[pref[j]] = 0
            
            if pref[j] - k in dic:
                res += dic[pref[j] - k]
            dic[pref[j]] += 1
        return res
        
