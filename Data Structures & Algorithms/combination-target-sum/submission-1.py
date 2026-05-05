class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, current_sum):
            if current_sum == target:
                result.append(path[:])
                return 
            if current_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])      # choose

                backtrack(i, path, current_sum + nums[i])     # explore deeper
                
                path.pop()               # un-choose (undo)

        backtrack(0, [], 0)
        return result