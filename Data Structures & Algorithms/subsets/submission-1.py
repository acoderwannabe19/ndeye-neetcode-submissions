class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                # explore
                path.append(nums[i])

                backtrack(i+1, path)

                #undo explore
                path.pop()

        backtrack(0, [])
        return result