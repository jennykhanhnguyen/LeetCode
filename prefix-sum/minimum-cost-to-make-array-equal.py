class Solution(object):
    def minCost(self, nums, cost):
        """
        :type nums: List[int]
        :type cost: List[int]
        :rtype: int
        """
        lst = []
        for i in range(len(nums)):
            lst.append((nums[i], cost[i]))
        lst = sorted(lst)

        cnt = 0
        med = (sum(cost)+1)//2
        medval = 0
        for i in range(len(nums)):
            cnt += lst[i][1]
            if cnt >= med:
                medval = lst[i][0]
                break

        ans = 0
        for i in range(len(nums)):
            ans += abs(medval - nums[i])*cost[i]
        return ans

