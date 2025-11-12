class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        n = len(nums)
        dic = {0: 1}
        for j in range(0, n):
            summ += nums[j]
            if summ % k not in dic:
                dic[summ % k] = 0
            if summ % k in dic:
                res += dic[summ % k]
            dic[summ % k] += 1
        return res