class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        left, right = 0, n - 1
        first_true_index = -1

        def feasible(mid):
            """
            Returns True if target is at mid or should be to its left.
            """
            if nums[0] <= nums[mid]:
                # Left half is sorted
                return nums[0] <= target <= nums[mid]
            else:
                # Right half is sorted
                # Feasible if target is NOT in the sorted right half
                return not (nums[mid] < target <= nums[n - 1])

        while left <= right:
            mid = (left + right) // 2
            if feasible(mid):
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        # Check if the element at first_true_index is the target
        if first_true_index == -1:
            return -1
        return first_true_index if nums[first_true_index] == target else -1
