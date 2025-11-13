class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        res = 0
        dic = {0:1}
        n = len(nums)
        summ = 0
        for j in range(0,n):
            summ += nums[j]
            if summ%k not in dic:
                dic[summ%k] = 0
            if summ%k in dic:
                res += dic[summ%k]
            dic[summ%k]+=1
            print(summ)
            print(summ//k)
            print(dic)
            print(res)
        print(dic)
        return res>0