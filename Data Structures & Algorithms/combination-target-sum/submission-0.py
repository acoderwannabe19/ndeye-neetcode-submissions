class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
    
        def backtrack(start, path, current_sum):
            # exact match
            if current_sum == target:
                result.append(path[:])
                return

            # if sum exceeds target
            if current_sum > target:
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])

                # explore
                backtrack(i, path, current_sum + nums[i])

                # undo explore
                path.pop()

        backtrack(0, [], 0)
        return result