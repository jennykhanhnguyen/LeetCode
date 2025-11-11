class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        gres = 1
        lres = 1
        if len(nums) == 0:
            return 0
        else: 
            prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == prev + 1:
                prev += 1
                lres += 1
                gres = max(gres, lres)
            elif nums[i] == prev:
                continue
            else:
                prev = nums[i]
                lres = 1
                gres = max(gres, lres)
        return gres
            