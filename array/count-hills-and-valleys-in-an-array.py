class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        up = 3
        cnt = 0
        for i in range (len(nums)-1):
            if nums[i] < nums[i+1]:
                if up != 3 and up == False:
                    cnt += 1
                up = True
            elif nums[i] > nums[i+1]:
                if up != 3 and up == True:
                    cnt += 1
                up = False
        return cnt