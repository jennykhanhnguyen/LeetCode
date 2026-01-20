class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(index: int) -> None:
            if index == len(nums):
                result.append(current_subset[:])
                return
          
            backtrack(index + 1)
            current_subset.append(nums[index])
            backtrack(index + 1)
            current_subset.pop()
            
        result = []
        current_subset = []
        backtrack(0)
      
        return result
