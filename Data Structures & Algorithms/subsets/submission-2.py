class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])      # choose
                backtrack(i+1, path)     # explore deeper
                path.pop()               # un-choose (undo)

        backtrack(0, [])
        return result

        # def backtrack(choices_left, current_path):
        #     save current_path if it's valid

        #     for each choice in choices_left:
        #         make the choice
        #         backtrack(updated_choices_left, current_path)
        #         undo the choice
