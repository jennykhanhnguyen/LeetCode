class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        res = 0
        dic = {0:-1}
        n = len(nums)
        if n <2:
            return False
        mod = 0
        for j in range(n):
            mod = (mod + nums[j])%k
            if mod in dic:
                if j - dic[mod] > 1:
                    return True
            else:
                dic[mod] = j
        return False