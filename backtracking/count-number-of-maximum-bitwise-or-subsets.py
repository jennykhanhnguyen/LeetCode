class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        cnt = 0
        maxval = 0

        for i in range(len(nums)):
            maxval = maxval|nums[i]
        for mask in range(1, 2**len(nums)):
            orval = 0
            for i in range (len(nums)):
                if (mask >> i) & 1:
                    orval|= nums[i]
            if orval == maxval:
                cnt += 1
            

        return cnt