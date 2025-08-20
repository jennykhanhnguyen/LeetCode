class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums.sort()
        missing_numbers = []

        for i in range(1, len(nums) + 1):
            index = bisect_left(nums, i)

            if index >= len(nums) or nums[index] != i:
                missing_numbers.append(i)
        
        return missing_numbers